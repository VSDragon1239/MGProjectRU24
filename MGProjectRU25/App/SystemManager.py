import socket
import subprocess
import re

from MGProjectRU25.App.Data import STRUCTURE, get_main_modules
from MGProjectRU25.Project.project_settings import PROJECT_ROOT
from TemplateProject.core.services.file_service import FileService


class DeviceManager:
    def __init__(self):
        self.drive_map = {}  # letter -> physical drive
        self.drives_name = []  # list of {"device_id", "model"}

    def _get_drive_id(self, device_id: str) -> str | None:
        """
        Возвращает букву диска (например, "C:") по физическому device_id (например, "\\\\.\\PHYSICALDRIVE0").
        """
        norm_id = device_id.strip().lower()
        for letter, phys_id in self.drive_map.items():
            if phys_id.lower() == norm_id:
                return letter
        return None

    def _get_drive_name(self, drive=None):
        if not self.drive_map:
            # 1) соберём маппинг букв в физические диски
            self._build_letter_to_physical_map()
            # 2) получим список всех физ. Дисков и их моделей
            self._fetch_drive_models()

        # Если drive не указан — вернём список всех
        if drive is None:
            return self.drives_name

        # Нормализуем вход: "C:/", "c:\" → "C:"
        drive_letter = drive.strip().upper().rstrip('\/')
        if not drive_letter.endswith(':'):
            drive_letter += ':'

        # Ищем физ. диск по букве
        phys = self.drive_map.get(drive_letter)
        if not phys:
            return None

        # Ищем в списке моделей
        for item in self.drives_name:
            if item["device_id"].lower() == phys.lower():
                return item

        return None

    def _build_letter_to_physical_map(self):
        self.drive_map.clear()
        # выводит строки вида:
        # Antecedent                                           Dependent
        # \\.\ROOT\cimv2:Win32_DiskPartition.DeviceID="Disk #0, Partition #0"    \\.\ROOT\cimv2:Win32_LogicalDisk.DeviceID="C:"
        result = subprocess.run(
            ['wmic', 'path', 'Win32_LogicalDiskToPartition', 'get', 'Antecedent,Dependent'],
            capture_output=True, text=True
        )
        for line in result.stdout.splitlines()[1:]:
            if not line.strip():
                continue
            # Извлекаем номер диска из Antecedent
            m1 = re.search(r'Disk #(?P<disk>\d+), Partition #\d+', line)
            # Извлекаем букву из Dependent
            m2 = re.search(r'DeviceID="(?P<letter>[A-Z]:)"', line)
            if m1 and m2:
                disk_num = m1.group('disk')
                letter = m2.group('letter')
                self.drive_map[letter] = f"\\\\.\\PHYSICALDRIVE{disk_num}"

    def _fetch_drive_models(self):
        self.drives_name.clear()
        result = subprocess.run(
            ['wmic', 'diskdrive', 'get', 'DeviceID,Model'],
            capture_output=True, text=True
        )
        for line in result.stdout.splitlines()[1:]:
            parts = line.strip().split(None, 1)
            if len(parts) == 2:
                self.drives_name.append({
                    "device_id": parts[0],  # "\\.\PHYSICALDRIVE0"
                    "model": parts[1].strip(),
                    "type": "Unknown",
                    "paths": []
                })


class SystemManager(DeviceManager):
    structure = STRUCTURE
    SYSTEM_NAME = socket.gethostname()
    structure_file = FileService(str(PROJECT_ROOT), "StructureFile", "json")

    def __init__(self):
        super().__init__()
        # print(type(self.structure))
        self.__read_data()
        self.safe_structure_data()

    def __read_data(self):
        if self.structure_file.file_exists():
            self.structure = self.structure_file.read_file()[1]
            print('__read_data')
            self.reload_system_data()
        else:
            self.__first_init_main_data()
        self.init_drive_map()

    def reload_system_data(self):
        print('reload_system_data')
        print(self.structure["MGProjectRU25"]["SystemData"])
        if self.structure["MGProjectRU25"]["SystemData"]:
            print('reload_system_data if')
            data = self.__get_system_data()
            print(data)
            if not data:
                self.set_system_data()
                self.safe_structure_data()
            return None

        self.set_system_data()
        self.safe_structure_data()

    def __get_system_data(self):
        for sys_data in self.structure["MGProjectRU25"]["SystemData"]:
            if sys_data["SystemName"] == self.SYSTEM_NAME:
                return sys_data

    def set_system_data(self):
        sys_data = STRUCTURE["MGProjectRU25"]["SystemData"][0]
        sys_data["SystemName"] = self.SYSTEM_NAME
        sys_data["Drives"] = self.__get_drives()
        self.structure["MGProjectRU25"]["SystemData"].append(sys_data)


    def safe_structure_data(self):
        if not self.structure_file.file_exists():
            self.structure_file.create_file(self.structure)
        self.structure_file.write_file(self.structure)

    def __first_init_main_data(self):
        self.structure["MGProjectRU25"]["SystemData"][0]["SystemName"] = self.SYSTEM_NAME
        self.structure["MGProjectRU25"]["SystemData"][0]["Drives"] = self.__get_drives()
        self._build_letter_to_physical_map()

    def __get_drives(self):
        return self._get_drive_name()

    def __get_drive(self, name: str):
        return self._get_drive_name(name)

    def set_type_drive(self, name: str, type_drive_id: int):
        """
        :param name: " C:/ "

        :param type_drive_id:
            "1" -> "Mirror",
            "2" -> "Main",
            "3" -> "Portable",
            "4" -> "Unknown"

        :return: 1
        """
        drive: dict = self.__get_drive(name)
        drive = drive.copy()

        try:
            drive["type"] = self.get_all_types_drive()[str(type_drive_id)]
        except TypeError:
            raise ValueError("Указанный диск не подключен")

        for i in range(0, len(self.__get_system_data()["Drives"])):
            drive_i = self.__get_system_data()["Drives"][i]
            if drive_i["model"] == drive["model"] and drive_i["device_id"] == drive["device_id"]:
                if drive_i["type"] == "Unknown":
                    if not drive_i["paths"]:
                        drive["paths"] = get_main_modules()
                    self.__get_system_data()["Drives"][i] = drive
                    self.safe_structure_data()
                    return 1
                else:
                    raise ValueError("Диск уже инициализирован")

    @staticmethod
    def get_all_types_drive():
        return {
            "1": "Mirror",
            "2": "Main",
            "3": "Portable",
            "4": "Unknown"
        }

    def __get_data_current_system_name(self):
        for sys_data in self.structure["MGProjectRU25"]["SystemData"]:
            if str(sys_data["SystemName"]) == str(self.SYSTEM_NAME):
                return sys_data
            print(sys_data)

    def get_drives(self):
        return self.__get_data_current_system_name()["Drives"]

    def get_main_drive(self):
        if self.__get_data_current_system_name() is not None:
            for drive in self.__get_data_current_system_name()["Drives"]:
                if drive["type"] == self.get_all_types_drive()["2"]:
                    return self._get_drive_id(drive["device_id"]) + '//'
            return None
        else:
            pass
            # self.reload_system_data()
            # if self.__get_data_current_system_name is not None:
            #     self.get_main_drive()
            # else:
            #     raise TypeError("Диски не инициализируются")

    def set_main_drive(self):
        self.set_type_drive(str(PROJECT_ROOT)[:3].replace("\\", "/"), 2)
        return self.get_main_drive()

    def init_drive_map(self):
        self._build_letter_to_physical_map()
        self._fetch_drive_models()


# if __name__ == "__main__":
#     SystemManager = SystemManager()
#
#     print(SystemManager.get_main_drive())

    # SystemManager.set_type_drive("C:/", 2)
    # drives = SystemManager.get_drives()
    # print()
