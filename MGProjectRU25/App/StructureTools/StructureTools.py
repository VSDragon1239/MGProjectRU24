import re
import socket
import subprocess

import psutil
import string
import os

# from TemplateProject.core.services.directory_service import DirectoryService
# from TemplateProject.core.services.file_service import FileService
from TemplateProject.data.data_directories import DataDirectories
from TemplateProject.core.ss_utils.structure_utils import StructureUtils
from TemplateProject.core.ss_utils.metadata_utils import MetadataUtils


class StructureTools:
    structure_utils = StructureUtils
    metadata_utils = MetadataUtils
    data_directories = DataDirectories

    subdata_drives = []

    def __init__(self):
        self.drive_map = {}       # letter -> physical drive
        self.drives_name = []     # list of {"device_id", "model"}

        self.drives = []
        self.drives_name = []
        self.registrate_drives = []
        self.device = []
        self.registrate_devices = []
        self.GMSStructureCreateData = None
        self.main_template_modules = ["GMSStorageFilesModule", "GMSControlDataModule", "GMSServerFilesModule"]
        self.global_project_ids = ["1", "2", "3"]

        self.global_project_data = {"1": {"GProjectName": "Глобальная Виртуализация", "Description": "Описание интересное - 1"},
                                    "2": {"GProjectName": "Реверсия Реальности", "Description": "Описание интересное - 2"},
                                    "3": {"GProjectName": "Глобальное Программирование", "Description": "Описание интересное - 3"}}

        self.global_project_projects = {"1": {"Project11": "DataP11", "Project12": "DataP12", "Project13": "DataP13"},
                                        "2": {"Project21": "DataP21", "Project22": "DataP22", "Project23": "DataP23"},
                                        "3": {"Project31": "DataP31", "Project32": "DataP32", "Project33": "DataP33"}}

    def get_device(self):
        hostname = socket.gethostname()
        self.device = [hostname]
        return self.device

    def get_drive_name(self, drive=None):
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
                letter   = m2.group('letter')
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
                    "device_id": parts[0],       # "\\.\PHYSICALDRIVE0"
                    "model":     parts[1].strip()
                })

    def get_drives(self):
        # self.drives = [disk.device for disk in psutil.disk_partitions(all=False)]
        self.drives = [f"{d}:/" for d in string.ascii_uppercase if os.path.exists(f"{d}:/")]
        return self.drives

    def get_drive_size(self, drive):
        usage = psutil.disk_usage(drive)
        self.subdata_drives.append({
            'total': usage.total,
            'used': usage.used,
            'free': usage.free,
            'percent': usage.percent
        })
        return self.subdata_drives

    def get_path_template_modules(self, drive):
        path_template_modules = []
        for module in self.main_template_modules:
            path_template_modules.append(drive + module + '/')
        return path_template_modules

    def get_path_template_projects_data(self, drive):
        return self.get_path_template_modules(drive)[0] + "ProjectsData" + '/'

    def get_path_template_memory_data(self, drive):
        return self.get_path_template_modules(drive)[0] + "MemoryData" + '/'

    def get_path_template_app_data(self, drive):
        return self.get_path_template_modules(drive)[0] + "AppData" + '/'

    def get_path_template_applications(self, drive):
        return self.get_path_template_modules(drive)[0] + "Applications" + '/'

    def get_path_template_control_projects_data(self, drive):
        return self.get_path_template_modules(drive)[1] + "ProjectsData" + '/'

    def get_path_template_global_projects(self, drive):
        path_template_global_projects_data = []
        for global_projects_id in self.global_project_ids:
            path_template_global_projects_data.append(self.get_path_template_projects_data(drive) + f"{global_projects_id}" + '/')
        return path_template_global_projects_data

    def get_path_template_control_global_projects(self, drive):
        path_template_control_global_projects_data = []
        for global_projects_id in self.global_project_ids:
            path_template_control_global_projects_data.append(self.get_path_template_control_projects_data(drive) + f"{global_projects_id}" + '/')
        return path_template_control_global_projects_data

    def get_path_template_global_project_projects(self, global_project_id, drive):
        global_project_projects = []
        path = self.get_path_template_global_projects(drive)[int(global_project_id)-1]
        for project in self.global_project_projects[str(global_project_id)]:
            global_project_projects.append(path + project + '/')
        return global_project_projects

    def exist_drive_path(self, module, drive):
        modules = self.get_path_template_modules(drive)
        for module_i in modules:
            if drive+module+'/' == module_i:
                return os.path.exists(module_i)
            else:
                raise ValueError("Такого модуля нету!")

    def __init_gms_structure_utils(self, drive):
        self.GMSStructureUtils = self.structure_utils("CreateGMS-Structure", drive)

    def init_gms_structure_create(self, drive):
        content = self.__init_gms_structure_set_data(drive)
        self.__init_gms_structure_utils(drive)
        self.GMSStructureUtils.createStructure(onFSDocFile=True)
        self.__init_gms_structure_file(content)

    def __init_gms_structure_file(self, content):
        self.gmsStructureFile = self.GMSStructureUtils.new_json_file(file_id="1", file_name="GMSStructure", content=content)

    def __init_gms_structure_set_data(self, drive):
        device = self.get_device()[0]
        drive_name = self.get_drive_name(drive)
        return {
            "devices": [{
                "device": device,
                "type": None,
                "drives": [{
                    "drive": drive,
                    "name": drive_name
                }]
            }]
        }

    def set_type_gms_structure(self, drive, gms_type: str):
        self.__init_gms_structure_utils(drive)

        file_data = self.GMSStructureUtils.get_file_data(file_name="GMSStructure", file_extension="json")
        if type(file_data) is list:
            file = file_data[1]
        else:
            return False

        gms_data = file
        gms_data["devices"][0]["type"] = gms_type

        self.GMSStructureUtils.update_json_file("GMSStructure", "json", gms_data)

    def __check_gms_structure(self, drive):
        """
        """
        this_device = self.get_device()[0]
        this_drive_name = self.get_drive_name(drive)
        print("this_data:   ", this_device, this_drive_name)

        try:
            self.__init_gms_structure_utils(drive)
            file_data = self.GMSStructureUtils.get_file_data(file_name="GMSStructure", file_extension="json")
            if type(file_data) is list:
                file = file_data[1]
            else:
                return False
        except Exception as e:
            print(e)
            return False

        print("file:    ", file)

        device = file["devices"][0]["device"]
        drive_dir = file["devices"][0]["drives"][0]["drive"]
        drive_name = file["devices"][0]["drives"][0]["name"]
        print("get: ", device, drive_dir)
        if drive == drive_dir and this_drive_name == drive_name and this_device == device:
            return True
        else:
            return False

    def get_type_gms_structure(self, drive):
        if self.__check_gms_structure(drive):
            file_data = self.GMSStructureUtils.get_file_data(file_name="GMSStructure", file_extension="json")
            return file_data[1]["devices"][0]["type"]
        return False
