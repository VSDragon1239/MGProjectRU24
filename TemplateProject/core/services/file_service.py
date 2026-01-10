# Основные операции над файлами.
import csv
import json
import os
from json import JSONDecodeError

from TemplateProject.core.services.json_file_service import write_json_file_service


class FileService:
    """
    json
    """

    def __init__(self, full_directory: str, file_name: str, file_extension: str):
        self.directory = full_directory.replace("\\", "/")
        self.file_name1 = file_name.replace("\\", "/")
        self.file_name = file_name
        self.file_extension = file_extension
        self._file_path = os.path.join(self.directory, f"{self.file_name}.{self.file_extension}").replace("\\", "/")

        # if not os.path.exists(self._file_path):
        #     raise FileNotFoundError(f"File not found: {self._file_path}")

    def file_exists(self):
        """
        :return: True if file существует, иначе False
        """
        if os.path.exists(self._file_path):
            return True
        return False

    def get_file_name(self):
        return f"{self.file_name}"

    def get_file_extension(self):
        return f"{self.file_extension}"

    def get_file_path(self):
        return self._file_path

    def get_path_to_file(self):
        return self.directory

    def append_file(self, content):
        """
        Appends content to an existing file.
        """
        self.write_file(content, safeMode=True)

    def read_file(self, mode='r', encoding='utf-8'):
        if not self.file_exists():
            self.create_file()
        with open(self._file_path, mode, encoding=encoding) as file:
            if self.file_extension == "json":
                try:
                    value_json_file = json.load(file)
                    file.close()
                    return ['json', value_json_file]
                except JSONDecodeError as e:
                    print("В файле не верные данные:", e)
                    return ['json', file]

            elif self.file_extension == "zip":
                pass

            elif self.file_extension == "csv":
                value_csv_file = csv.reader(file)
                file.close()
                return ['csv', value_csv_file]
            elif self.file_extension == "xlsx":
                pass

            elif self.file_extension == "md":
                value_file = file.read()
                file.close()
                return ['markdown', value_file]
            else:
                file.close()
                return 'NOT_SUPPORTED'

    def create_file(self, content=None):
        """
        Creates a new file with the specified content. Content handling depends on the file type.
        """
        if os.path.exists(self._file_path):
            # Путь не найден куда вставлять файл
            raise FileExistsError(f"File already exists: {self._file_path}")
            # raise FileExistsError()
        if content is None:
            content = {}
        with open(self._file_path, 'w', encoding='utf-8') as file:
            if self.file_extension == "json":
                if isinstance(content, dict):
                    json.dump(content, file, indent=4)
                else:
                    raise ValueError("Content for JSON files must be a dictionary.")
            elif self.file_extension == "csv":
                if isinstance(content, list):
                    writer = csv.writer(file)
                    writer.writerows(content)
                else:
                    raise ValueError("Content for CSV files must be a list of lists.")
            elif self.file_extension in ["txt", "md"]:
                if isinstance(content, str):
                    file.write(content)
                else:
                    raise ValueError("Content for text files must be a string.")
            else:
                raise ValueError(f"File type '{self.file_extension}' is not supported.")

    def write_file(self, content, safeMode=False, ignore_value_type=False):
        """
        Writes new content to an existing file. Supports two modes:
        - Safe mode (safeMode=True): Appends new content to the existing content.
        - Default mode (safeMode=False): Completely overwrites the existing content.

        :param content: New content to write into the file.
        :param safeMode: If True, appends new content to the old one.
        :param ignore_value_type: If True, overwrites existing keys even if their types differ.
        """
        if self.file_extension == "json":
            if not isinstance(content, dict):
                # print('write_json_file_service - NoSafeMode, ValueError')
                raise ValueError("Content for JSON files must be a dictionary.")
        mode = 'a' if safeMode else 'w'
        with open(self._file_path, mode, encoding='utf-8') as file:
            if self.file_extension == "json":
                return write_json_file_service(file, self._file_path, content, safeMode, ignore_value_type)

            elif self.file_extension == "csv":
                if not isinstance(content, list):
                    raise ValueError("Content for CSV files must be a list of lists.")
                writer = csv.writer(file)
                if not safeMode:  # Full overwrite
                    writer.writerows(content)
                else:  # Append to existing content
                    for row in content:
                        writer.writerow(row)

            elif self.file_extension in ["txt", "md"]:
                if not isinstance(content, str):
                    raise ValueError("Content for text files must be a string.")
                if safeMode:
                    file.write(content)
                else:
                    file.write(content)  # Default behavior for 'w' mode
            else:
                raise ValueError(f"File type '{self.file_extension}' is not supported.")

    def delete_file(self):
        """
        Deletes the file at the specified path.
        """
        if os.path.exists(self._file_path):
            os.remove(self._file_path)
            return 1
        else:
            raise FileNotFoundError(f"File not found: {self._file_path}")
