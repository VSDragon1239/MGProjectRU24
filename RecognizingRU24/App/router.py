# core/router.py
import re
from typing import Any, Dict, Tuple, Optional
from RecognizingRU24.App.loader import resolve_action
from RecognizingRU24.App.registry import get_registered

try:
    from rapidfuzz import process, fuzz

    _FUZZ = True
except Exception:
    _FUZZ = False


class CommandRouter:
    def __init__(self, config: Dict[str, Any], fuzzy_threshold: int = 82):
        self.config = config
        self.fuzzy_threshold = fuzzy_threshold

        # плоский список правил: [(pattern, action, args_template, type_key)]
        self.rules = []
        for type_key, type_section in config["types"].items():
            for group_key, items in type_section.items():
                if group_key in ("ApplicableWords",):  # служебное
                    continue
                for item in items:
                    self.rules.append((
                        item["phrases"],  # список фраз/шаблонов
                        item["action"],  # dotted-path
                        item.get("args", {}),  # шаблон аргументов
                        type_key
                    ))
        # подготовка для fuzzy
        self._all_phrases = []
        for phrases, _, _, _ in self.rules:
            self._all_phrases.extend(phrases)

    def _match_phrase(self, text: str) -> Optional[Tuple[int, Dict[str, str]]]:
        """
        Возвращает индекс правила и словарь заполненных плейсхолдеров {name: value}.
        Поддерживает шаблоны вида 'запусти проект {name}'.
        """
        text_norm = text.strip().lower()

        # 1) точное/шаблонное совпадение
        for idx, (phrases, _, _, _) in enumerate(self.rules):
            for p in phrases:
                # шаблон -> regex
                patt = re.escape(p.lower())
                patt = patt.replace(r"\{name\}", r"(?P<name>.+)")
                m = re.fullmatch(patt, text_norm)
                if m:
                    return idx, m.groupdict()

        # 2) fuzzy (без плейсхолдеров)
        if _FUZZ:
            phrase, score, _ = process.extractOne(text_norm, self._all_phrases, scorer=fuzz.WRatio)
            if score >= self.fuzzy_threshold:
                # найти правило, где эта фраза
                for idx, (phrases, _, _, _) in enumerate(self.rules):
                    if phrase in phrases:
                        return idx, {}
        return None

    def handle(self, text: str) -> Any:
        m = self._match_phrase(text)
        if not m:
            raise LookupError(f"Команда не найдена: '{text}'")
        idx, slots = m

        raw_text = text.strip()

        def _parse_percent_from_text(t: str) -> int | None:
            import re
            t = t.lower()
            # 1) цифры
            m = re.search(r'(\d{1,3})\s*%?', t)
            if m:
                v = int(m.group(1))
                return max(0, min(100, v))
            # 2) слова (простая русская грамматика)
            units = {
                "ноль": 0, "один": 1, "одну": 1, "два": 2, "две": 2, "три": 3, "четыре": 4, "пять": 5,
                "шесть": 6, "семь": 7, "восемь": 8, "девять": 9, "десять": 10, "одиннадцать": 11,
                "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14, "пятнадцать": 15,
                "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19
            }
            tens = {
                "двадцать": 20, "тридцать": 30, "сорок": 40, "пятьдесят": 50, "шестьдесят": 60,
                "семьдесят": 70, "восемьдесят": 80, "девяносто": 90, "сто": 100
            }
            tokens = re.findall(r"[а-яё]+", t)
            val = 0;
            used = False
            for w in tokens:
                if w in tens:
                    val += tens[w];
                    used = True
                elif w in units:
                    val += units[w];
                    used = True
            if used:
                return max(0, min(100, val))
            return None

        phrases, action, args_tmpl, _type = self.rules[idx]

        # Подстановка плейсхолдеров с умными фоллбэками
        args = {}
        for k, v in args_tmpl.items():
            if isinstance(v, str) and v.startswith("{") and v.endswith("}"):
                key = v.strip("{}")
                filled = slots.get(key)
                if filled in (None, ""):
                    # умные подстановки:
                    if key == "percent":
                        filled = _parse_percent_from_text(raw_text)
                    elif key == "query":
                        filled = raw_text  # отдаём весь текст — плагин сам очистит
                    elif key == "name":
                        filled = raw_text
                args[k] = filled
            else:
                args[k] = v

        # всегда передаём сырой текст
        args["raw_text"] = raw_text

        # 1) пробуем статически зарегистрированный обработчик
        fn = get_registered(action)
        if fn is None:
            # 2) иначе динамически импортируем
            fn = resolve_action(action)

        return fn(**args)
