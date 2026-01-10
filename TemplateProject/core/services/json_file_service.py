import json


def write_json_file_service(file, _file_path, content, safeMode, ignore_value_type):
    def deep_merge_dicts(original, new):
        """
        Рекурсивное объединение вложенных словарей. Значения из new перезаписывают значения из original.
        """
        for key, value in new.items():
            if key in original and isinstance(original[key], dict) and isinstance(value, dict):
                deep_merge_dicts(original[key], value)
            else:
                original[key] = value

    if safeMode:
        # Читаем существующее содержимое файла
        try:
            with open(_file_path, 'r', encoding='utf-8') as existing_file:
                existing_content = json.load(existing_file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_content = {}

        if not isinstance(content, dict):
            raise ValueError("Content for JSON files must be a dictionary.")

        # Объединяем существующее содержимое с новым
        deep_merge_dicts(existing_content, content)

        # Сохраняем объединенный результат
        with open(_file_path, 'w', encoding='utf-8') as merge_file:
            json.dump(existing_content, merge_file, indent=4)
            # print('write_json_file_service - SafeMode, WriteToFile')

        return existing_content
    else:
        if not isinstance(content, dict):
            raise ValueError("Content for JSON files must be a dictionary.")
        json.dump(content, file, indent=4)
        # print('write_json_file_service - NoSafeMode, json.dump')
        return content
