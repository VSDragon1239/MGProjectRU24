import re

# 2. Простая функция транслитерации (можно расширить по своему алфавиту)
_translit_map = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e", "ж": "zh", "з": "z",
    "и": "i", "й": "i", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r",
    "с": "s", "т": "t", "у": "u", "ф": "f", "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh",
    "щ": "shch", "ы": "y", "э": "e", "ю": "yu", "я": "ya", "ь": "", "ъ": ""
}


def transliterate(text: str) -> str:
    result = []
    for ch in text.lower():
        if ch in _translit_map:
            result.append(_translit_map[ch])
        elif re.match(r"[a-z0-9]", ch):
            result.append(ch)
        else:
            result.append(" ")
    # объединяем и удаляем лишние пробелы
    return re.sub(r"\s+", " ", "".join(result)).strip().title()


# 3. Функция для формирования слага
def slugify(text: str) -> str:
    # по нижнему регистру, пробелы → дефис, убрать всё лишнее
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)  # оставить буквы, цифры, подчёрки и пробелы
    text = re.sub(r"\s+", "-", text)  # пробелы → дефисы
    text = re.sub(r"-{2,}", "-", text)  # убрать двойные дефисы
    return text.strip("-")

