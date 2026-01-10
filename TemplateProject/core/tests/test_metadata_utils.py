import time
import unittest

from TemplateProject.core.ss_utils.metadata_utils import MetadataUtils
from TemplateProject.data.test_data_constants import PROJECT_PATH, TEST_MAIN_DIR
from TemplateProject.data.test_data_variables import PyCharmProjectPath


class TestMetadataUtils(unittest.TestCase):

    def setUp(self):
        self.testDir = PyCharmProjectPath + '/' + PROJECT_PATH + '/' + TEST_MAIN_DIR + '/' + 'TestMetaDataSSUtils'
        self.MetadataUtils = MetadataUtils(self.testDir)

    def test_dir_service_file_path(self):
        # self.assertEqual(self.MetadataUtils.DSDocFile, None)
        self.assertEqual(self.MetadataUtils.DSDocFile.get_file_path(), self.testDir + '/' + 'DSDocFile.json')
        result = self.MetadataUtils.DSDocFile.get_file_path()
        print('test_dir_file_path     =   ', result)

    def test_exists_and_create_dir_service_file(self):
        """
        Если файл существует, возвращает
        [путь к файлу, его содержимое] -> [self.DSDocFile.get_file_path(), self.DSDocFile.read_file()]
        иначе только путь к нему
        """
        try:
            file = self.MetadataUtils.createDSDocFile()
            if type(file) is not list:
                result = "ФайлДоЭтогоНеБылСоздан - ТеперьСоздан(DSDocFile)"
                self.assertEqual(file, self.MetadataUtils.DSDocFile.get_file_path())
            else:
                self.assertEqual(self.MetadataUtils.createDSDocFile(), [self.MetadataUtils.DSDocFile.get_file_path(),
                                                                        self.MetadataUtils.DSDocFile.read_file()])
                result = "ФайлУжеСоздан(DSDocFile) - ПроверкаЧтениемПути(get_file_path) - ПроверкаЧтениемСодержимогоФайла(read_file)"
            print('test_exists_and_create_dir_service_file     =   ', result)

        except FileNotFoundError:
            result = 'ФайлНеНайден(DSDocFile)'
            print('test_exists_and_create_dir_service_file     =   ', result)

    def test_exists_and_create_file_service_file(self):
        """
        Если файл существует, возвращает
        [путь к файлу, его содержимое] -> [self.DSDocFile.get_file_path(), self.DSDocFile.read_file()]
        иначе только путь к нему
        """
        try:
            file = self.MetadataUtils.createFSDocFile()
            if type(file) is not list:
                result = "ФайлДоЭтогоНеБылСоздан - ТеперьСоздан(FSDocFile)"
                self.assertEqual(file, self.MetadataUtils.FSDocFile.get_file_path())
            else:
                self.assertEqual(self.MetadataUtils.createFSDocFile(), [self.MetadataUtils.FSDocFile.get_file_path(),
                                                                        self.MetadataUtils.FSDocFile.read_file()])
                result = "ФайлУжеСоздан(FSDocFile) - ПроверкаЧтениемПути(get_file_path) - ПроверкаЧтениемСодержимогоФайла(read_file)"
            print('test_exists_and_create_file_service_file     =   ', result)

        except FileNotFoundError:
            result = 'ФайлНеНайден(FSDocFile)'
            print('test_exists_and_create_file_service_file     =   ', result)

    def test_delete_dir_service_file(self):
        """
        Хы-ы-ы
        :return: None
        """
        try:
            self.assertEqual(self.MetadataUtils.deleteDSDocFile(), None)
            with self.assertRaises(FileNotFoundError):
                self.MetadataUtils.deleteDSDocFile()
            result = 'ФайлУдалён(DSDocFile) ,   ПовторнаяПопыткаУдаления(FileNotFoundError)'
            print('test_delete_file_service_file     =   ', result)

        except FileNotFoundError:
            result = 'ФайлНеНайден(DSDocFile)(FileNotFoundError)'
            print('test_delete_file_service_file     =   ', result)

    def test_delete_file_service_file(self):
        try:
            self.assertEqual(self.MetadataUtils.deleteFSDocFile(), None)
            with self.assertRaises(FileNotFoundError):
                self.MetadataUtils.deleteFSDocFile()
            result = 'ФайлУдалён(FSDocFile) ,   ПовторнаяПопыткаУдаления(FileNotFoundError)'
            print('test_delete_file_service_file     =   ', result)

        except FileNotFoundError:
            result = 'ФайлНеНайден(FSDocFile)(FileNotFoundError)'
            print('test_delete_file_service_file     =   ', result)

    # def test_delete_DSDocFile(self):
    #     with self.assertRaises(FileNotFoundError):
    #         self.assertEqual(self.MetadataUtils.DSDocFile.delete_file(), 1)
    #         self.MetadataUtils.DSDocFile.delete_file()
    #
    # def test_delete_FSDocFile(self):
    #     with self.assertRaises(FileNotFoundError):
    #         self.assertEqual(self.MetadataUtils.FSDocFile.delete_file(), 1)
    #         self.MetadataUtils.FSDocFile.delete_file()

    def test_write_main_data_dir_service_file(self):
        """
        """
        set_data_1 = self.MetadataUtils.writeMetadataDSDocFile("Directory", "Dirname", "1")
        set_data_11 = self.MetadataUtils.writeMetadataDSDocFile("Directory", "Description",
                                                                "Desc - Описательное Описание")
        set_data_121 = self.MetadataUtils.writeMetadataDSDocFile("Directory", "Details",
                                                                 "Rewrite - Затираем влажные данные 1...")
        set_data_122 = self.MetadataUtils.writeMetadataDSDocFile("Directory", "SubdirectoryInfo",
                                                                 "Rewrite - Затираем влажные данные 2...")
        set_data_123 = self.MetadataUtils.writeMetadataDSDocFile("Directory", "SubdirectoryNonIndex",
                                                                 "Rewrite - Затираем влажные данные 3...")

        set_data_21 = self.MetadataUtils.writeMetadataDSDocFile("Details", "DirectoryPath",
                                                                self.MetadataUtils.DSDocFile.get_path_to_file())
        set_data_22 = self.MetadataUtils.writeMetadataDSDocFile("Details", "DetailName",
                                                                "DetailName - ДетальноеНазвание")
        set_data_24 = self.MetadataUtils.writeMetadataDSDocFile("Details", "TotalSize", "TotalSize - Размер")
        set_data_25 = self.MetadataUtils.writeMetadataDSDocFile("Details", "FileCount", "FilesCount - Количество")
        set_data_26 = self.MetadataUtils.writeMetadataDSDocFile("Details", "CreatedAt", "CreateDate - ДатаСоздания")
        set_data_27 = self.MetadataUtils.writeMetadataDSDocFile("Details", "ModifiedAt", "ModifyDate - ДатаИзменения")

        self.assertEqual(set_data_1, 1)
        self.assertEqual(set_data_11, 1)
        self.assertEqual(set_data_121, -1)  # Не получилось затереть влажные данные
        self.assertEqual(set_data_122, -1)  # Не получилось затереть влажные данные
        self.assertEqual(set_data_123, -1)  # Не получилось затереть влажные данные
        self.assertEqual(set_data_21, 2)
        self.assertEqual(set_data_22, 2)
        self.assertEqual(set_data_24, 2)
        self.assertEqual(set_data_25, 2)
        self.assertEqual(set_data_26, 2)
        self.assertEqual(set_data_27, 2)
        result = 'ОсновныеДанныеБылиЗаписаныВерно'
        print('test_write_main_data_dir_service_file     =   ', result)

    def test_write_priority_data_dir_service_file(self):
        set_data_23 = self.MetadataUtils.writeMetadataDSDocFile("Details", "Priority", "[To be - Когда-нибудь...]")
        self.assertEqual(set_data_23, 2)
        result = 'ПриоритетБылЗаписанВерно'
        print('test_write_priority_data_dir_service_file     =   ', result)

    def test_write_links_data_dir_service_file(self):
        """
        Content: ['1', '2'] -> Замена первого элемента на второй.
        Content: ['1', '2', '3', ..., 'n'] -> Запись списка элементов.
        Content: '1' -> Запись одного элемента в список

        Code __2 - Запись прошла успешно
        Code _-2 - Отказ в записи...
        Code _32 - Замена прошла успешно
        Code 311 - элемент уже существует (элемент заменяется на уже существующий)
        Code 312 - элемент не найден (заменяемый элемент не найден)
        """
        print('Обычная запись списка из 3-х связанных директорий')
        self.assertEqual(self.MetadataUtils.writeMetadataDSDocFile("Details", "DirLinks", ["path/to/directory/link1",
                                                                                           "path/to/directory/link2",
                                                                                           "path/to/directory/link3"]),
                         2)
        self.assertEqual(self.MetadataUtils.writeMetadataDSDocFile("Details", "DirLinks", ["path/to/directory/link4",
                                                                                           "path/to/directory/link5",
                                                                                           "path/to/directory/link6",
                                                                                           "path/to/directory/link7"]),
                         2)

        print('Добавление к уже записанным, ещё одной директории')
        self.assertEqual(self.MetadataUtils.writeMetadataDSDocFile("Details", "DirLinks", "path/to/directory/link8"), 2)

        print('(Не)Добавление уже существующей записи')
        self.assertEqual(self.MetadataUtils.writeMetadataDSDocFile("Details", "DirLinks", "path/to/directory/link1"),
                         -2)
        self.assertEqual(self.MetadataUtils.writeMetadataDSDocFile("Details", "DirLinks", "path/to/directory/link2"),
                         -2)
        self.assertEqual(self.MetadataUtils.writeMetadataDSDocFile("Details", "DirLinks", "path/to/directory/link3"),
                         -2)
        self.assertEqual(self.MetadataUtils.writeMetadataDSDocFile("Details", "DirLinks", ["path/to/directory/link4",
                                                                                           "path/to/directory/link5",
                                                                                           "path/to/directory/link6",
                                                                                           "path/to/directory/link7"]),
                         -2)

        print('Замена существующей директории...')
        self.assertEqual(self.MetadataUtils.writeMetadataDSDocFile("Details", "DirLinks", ["path/to/directory/link4",
                                                                                           "new_path/to/directory/link4"]),
                         32)
        self.assertEqual(self.MetadataUtils.writeMetadataDSDocFile("Details", "DirLinks", ["path/to/directory/link4",
                                                                                           "new_path/to/directory/link401"]),
                         -312)
        self.assertEqual(self.MetadataUtils.writeMetadataDSDocFile("Details", "DirLinks",
                                                                   ["new_path/to/directory/link4",
                                                                    "path/to/directory/link1"]), -311)

    def test_write_subdir_data_dir_service_file(self):
        print('Добавляем по списку ниже все 3 данные')
        self.assertEqual(
            self.MetadataUtils.writeMetadataDSDocFile("SubdirectoryInfo", "", ["1", "Main Folder", "DSDocFile.json"]),
            2)

        print('Добавление id и названия поддиректории в список, нужно добавить возврат id')
        self.assertEqual(self.MetadataUtils.writeMetadataDSDocFile("SubdirectoryInfo", "Dirname", "Dirname1", "New"), 2)
        self.assertEqual(self.MetadataUtils.writeMetadataDSDocFile("SubdirectoryInfo", "Dirname", "Dirname1", "New"),
                         -2)

        print('Перезаписывает id="1", но если Dirname уже есть в списке, не записываем')
        self.assertEqual(
            self.MetadataUtils.writeMetadataDSDocFile("SubdirectoryInfo", "", ["2", "Main Folder", "DSDocFile.json"],
                                                      "1"), 2)
        self.assertEqual(
            self.MetadataUtils.writeMetadataDSDocFile("SubdirectoryInfo", "", ["1", "Main Folder", "DSDocFile.json"],
                                                      "2"), 2)
        self.assertEqual(
            self.MetadataUtils.writeMetadataDSDocFile("SubdirectoryInfo", "", ["2", "Main Folder", "DSDocFile.json"],
                                                      "2"), -2)

    def test_write_non_index_subdir_data_dir_service_file(self):
        """
        Code -311 - элемент уже существует (элемент заменяется на уже существующий)
        Code -312 - элемент не найден (заменяемый элемент не найден)
        """
        print('Добавление неизвестной директории...')
        self.assertEqual(self.MetadataUtils.writeMetadataDSDocFile("SubdirectoryNonIndex", "", "1"), 2)
        self.assertEqual(self.MetadataUtils.writeMetadataDSDocFile("SubdirectoryNonIndex", "", "2"), 2)
        self.assertEqual(self.MetadataUtils.writeMetadataDSDocFile("SubdirectoryNonIndex", "", "3"), 2)

        print('Не верная замена неизвестной директории...')
        self.assertEqual(self.MetadataUtils.writeMetadataDSDocFile("SubdirectoryNonIndex", "", ["2", "3"]), -311)
        self.assertEqual(self.MetadataUtils.writeMetadataDSDocFile("SubdirectoryNonIndex", "", ["3", "2"]), -311)
        self.assertEqual(self.MetadataUtils.writeMetadataDSDocFile("SubdirectoryNonIndex", "", ["3", "2"]), -311)
        self.assertEqual(self.MetadataUtils.writeMetadataDSDocFile("SubdirectoryNonIndex", "", ["3", "3"]), -311)
        self.assertEqual(self.MetadataUtils.writeMetadataDSDocFile("SubdirectoryNonIndex", "", ["4", "5"]), -312)

        print('Верная замена неизвестной директории')
        self.assertEqual(self.MetadataUtils.writeMetadataDSDocFile("SubdirectoryNonIndex", "", ["3", "4"]), 31)

    def test_rewrite_dir_service_file(self):
        print('Перезапись в случае чего...')
        self.assertEqual(self.MetadataUtils.createDSDocFile(rewrite=True), True)

    def test_read_dir_service_file(self):
        # DSDocFile
        data_dirname_test = "1"
        data_details_test = {
            'DirectoryPath': 'C:/(0)MGProjectData/4/1/1/3/2/2/2/MGPPythonLibQtMVVM/TemplateProject/unittestdir/TestMetaDataSSUtils',
            'DetailName': 'DetailName - ДетальноеНазвание',
            'Priority': '[To be - Когда-нибудь...]',
            'DirLinks': ['path/to/directory/link1',
                         'path/to/directory/link2',
                         'path/to/directory/link3',
                         'new_path/to/directory/link4',
                         'path/to/directory/link5',
                         'path/to/directory/link6',
                         'path/to/directory/link7',
                         'path/to/directory/link8'],
            'TotalSize': 'TotalSize - Размер',
            'FileCount': 'FilesCount - Количество',
            'CreatedAt': 'CreateDate - ДатаСоздания',
            'ModifiedAt': 'ModifyDate - ДатаИзменения'
        }
        data_details_dirpath_test = "C:/(0)MGProjectData/4/1/1/3/2/2/2/MGPPythonLibQtMVVM/TemplateProject/unittestdir/TestMetaDataSSUtils"
        data_details_detail_name = "DetailName - ДетальноеНазвание"
        data_details_priority = "[To be - Когда-нибудь...]"
        data_details_dir_links = [
            'path/to/directory/link1',
            'path/to/directory/link2',
            'path/to/directory/link3',
            'new_path/to/directory/link4',
            'path/to/directory/link5',
            'path/to/directory/link6',
            'path/to/directory/link7',
            'path/to/directory/link8'
        ]
        data_details_total_size = "TotalSize - Размер"
        data_details_file_count = "FilesCount - Количество"
        data_details_created_at = "CreateDate - ДатаСоздания"
        data_details_modified_at = "ModifyDate - ДатаИзменения"

        data_details_subdir = {'0': {'DetailName': '', 'Dirname': '', 'DocFile': ''},
                               '1': {'DetailName': 'Main Folder',
                                     'Dirname': '2',
                                     'DocFile': 'DSDocFile.json'},
                               '2': {'DetailName': 'Main Folder',
                                     'Dirname': '1',
                                     'DocFile': 'DSDocFile.json'}}

        file_data_dirname = self.MetadataUtils.readMetadataSDocFile("Directory", "1", "Dirname")
        file_data_details = self.MetadataUtils.readMetadataSDocFile("Directory", "1", "Details")
        file_data_details_dirpath = self.MetadataUtils.readMetadataSDocFile("Directory", "21", "DirectoryPath")
        file_data_details_detail_name = self.MetadataUtils.readMetadataSDocFile("Directory", "21", "DetailName")
        file_data_details_priority = self.MetadataUtils.readMetadataSDocFile("Directory", "21", "Priority")
        file_data_details_dir_links = self.MetadataUtils.readMetadataSDocFile("Directory", "21", "DirLinks")
        file_data_details_total_size = self.MetadataUtils.readMetadataSDocFile("Directory", "21", "TotalSize")
        file_data_details_file_count = self.MetadataUtils.readMetadataSDocFile("Directory", "21", "FileCount")
        file_data_details_created_at = self.MetadataUtils.readMetadataSDocFile("Directory", "21", "CreatedAt")
        file_data_details_modified_at = self.MetadataUtils.readMetadataSDocFile("Directory", "21", "ModifiedAt")
        file_data_details_subdir = self.MetadataUtils.readMetadataSDocFile("Directory", "22", "-1")

        result = 'НачинаемПроверкуОсновныхДанных...'
        print('test_read_dir_service_file     =   ', result)
        self.assertEqual(file_data_dirname, data_dirname_test)
        self.assertEqual(file_data_details, data_details_test)
        self.assertEqual(file_data_details_dirpath, data_details_dirpath_test)

        self.assertEqual(file_data_details_detail_name, data_details_detail_name)
        self.assertEqual(file_data_details_priority, data_details_priority)
        self.assertEqual(file_data_details_dir_links, data_details_dir_links)
        self.assertEqual(file_data_details_total_size, data_details_total_size)
        self.assertEqual(file_data_details_file_count, data_details_file_count)
        self.assertEqual(file_data_details_created_at, data_details_created_at)
        self.assertEqual(file_data_details_modified_at, data_details_modified_at)
        result = 'Проверка1Завершена!'
        print('test_read_dir_service_file     =   ', result)

        result = 'НачалоПроверкиПоддиректорий...'
        print('test_read_dir_service_file     =   ', result)
        self.assertEqual(data_details_subdir, file_data_details_subdir)
        result = 'Проверка2Завершена!'
        print('test_read_dir_service_file     =   ', result)

    def test_read_file_service_file(self):
        # FSDocFile data
        filesData = {'0': {'DetailName': '', 'DirName': '',
                           'FileDetails': {'CreatedAt': '', 'Description': '', 'FileSize': '', 'FilesLinks': [],
                                           'ModifiedAt': '', 'Priority': ''}}}
        fileData = {'DetailName': '', 'DirName': '',
                    'FileDetails': {'CreatedAt': '', 'Description': '', 'FileSize': '', 'FilesLinks': [],
                                    'ModifiedAt': '', 'Priority': ''}}

        # FSDocFile tests
        self.assertEqual(self.MetadataUtils.readMetadataSDocFile("Files", "1", "SystemFiles"), filesData)
        self.assertEqual(self.MetadataUtils.readMetadataSDocFile("Files", "Files", "UserFiles"), filesData)

        self.assertEqual(self.MetadataUtils.readMetadataSDocFile("Files", "21", "0"), fileData)
        self.assertEqual(self.MetadataUtils.readMetadataSDocFile("Files", "22", "0"), fileData)
        self.assertEqual(self.MetadataUtils.readMetadataSDocFile("Files", "23", "0"), {'DetailName': '', 'DirName': ''})

        self.assertEqual(self.MetadataUtils.readMetadataSDocFile("Files", "31", "Description", file_id="0"), "")
        self.assertEqual(self.MetadataUtils.readMetadataSDocFile("Files", "32", "Description", file_id="0"), "")
        self.assertEqual(self.MetadataUtils.readMetadataSDocFile("Files", "33", "Description", file_id="0"), "")

    def test_complex_removeSubDirMetadataDSDocFile(self):
        self.assertEqual(self.MetadataUtils.removeSubdirMetadataDSDocFile("SubdirectoryInfo", "1"), 1)
        self.assertEqual(self.MetadataUtils.removeSubdirMetadataDSDocFile("SubdirectoryInfo", "1"), -1)
        self.assertEqual(self.MetadataUtils.removeSubdirMetadataDSDocFile("SubdirectoryInfo", "0"), -2)
        self.assertEqual(self.MetadataUtils.removeSubdirMetadataDSDocFile("SubdirectoryNonIndex", "1"), 2)
        self.assertEqual(self.MetadataUtils.removeSubdirMetadataDSDocFile("SubdirectoryNonIndex", "1"), -1)

    def test_removeSubDirMetadataDSDocFile(self):
        self.assertEqual(self.MetadataUtils.removeSubdirMetadataDSDocFile("SubdirectoryInfo", "0"), -2)
        self.assertEqual(self.MetadataUtils.removeSubdirMetadataDSDocFile("SubdirectoryInfo", "Main Folder"), -2)
        # self.assertEqual(self.MetadataUtils.removeSubdirMetadataDSDocFile("SubdirectoryInfo", "1"), 1)

    def test_writeMetadataFSDocFile_AddType(self):
        self.assertEqual(self.MetadataUtils.writeMetadataFSDocFile("AddType", "Files", "", "", file_id="0"), -1)
        self.assertEqual(self.MetadataUtils.writeMetadataFSDocFile(
            "AddType", "Files", "CacheFiles", "", file_id="0"),
            0)

    def test_writeMetadataFSDocFile_RemoveType(self):
        self.assertEqual(
            self.MetadataUtils.writeMetadataFSDocFile("RemoveType", "Files", "RadianыFiles", "", file_id="0"), -1)
        self.assertEqual(
            self.MetadataUtils.writeMetadataFSDocFile("RemoveType", "Files", "CacheFiles", "", file_id="0"), 0)
        self.assertEqual(
            self.MetadataUtils.writeMetadataFSDocFile("RemoveType", "Files", "CacheFiles", "", file_id="0"), -1)

    def test_writeMetadataFSDocFile_AddFile(self):
        self.assertEqual(self.MetadataUtils.writeMetadataFSDocFile("AddFile", "Files", "SystemFiles", "", file_id="0"),
                         -1)
        self.assertEqual(self.MetadataUtils.writeMetadataFSDocFile("AddFile", "Files", "SystemFiles", "", file_id="1"),
                         0)

        self.assertEqual(self.MetadataUtils.writeMetadataFSDocFile("AddFile", "Files", "UserFiles", "", file_id="0"),
                         -1)
        self.assertEqual(self.MetadataUtils.writeMetadataFSDocFile("AddFile", "Files", "UserFiles", "", file_id="1"), 0)

        self.assertEqual(
            self.MetadataUtils.writeMetadataFSDocFile("AddFile", "Files", "NonIndexedFiles", "", file_id="0"), -1)
        self.assertEqual(
            self.MetadataUtils.writeMetadataFSDocFile("AddFile", "Files", "NonIndexedFiles", "", file_id="1"), 0)

        self.assertEqual(self.MetadataUtils.writeMetadataFSDocFile("AddFile", "Files", "CacheFiles", "", file_id="0"),
                         -1)
        self.assertEqual(self.MetadataUtils.writeMetadataFSDocFile("AddFile", "Files", "CacheFiles", "", file_id="1"),
                         0)

    def test_writeMetadataFSDocFile_RemoveFile(self):
        self.assertEqual(
            self.MetadataUtils.writeMetadataFSDocFile("RemoveFile", "Files", "SystemFiles", "", file_id="1"), 0)
        self.assertEqual(self.MetadataUtils.writeMetadataFSDocFile("RemoveFile", "Files", "UserFiles", "", file_id="1"),
                         0)
        self.assertEqual(self.MetadataUtils.writeMetadataFSDocFile("RemoveFile", "Files", "UserFiles", "", file_id="1"),
                         -2)
        self.assertEqual(
            self.MetadataUtils.writeMetadataFSDocFile("RemoveFile", "Files", "NonIndexedFiles", "", file_id="1"), 0)
        self.assertEqual(
            self.MetadataUtils.writeMetadataFSDocFile("RemoveFile", "Files", "NonIndexedFiles", "", file_id="1"), -2)
        self.assertEqual(
            self.MetadataUtils.writeMetadataFSDocFile("RemoveFile", "Files", "CacheFiles", "", file_id="1"), 0)

    def test_writeMetadataFSDocFile_UpdateFile(self):
        self.assertEqual(
            self.MetadataUtils.writeMetadataFSDocFile("UpdateFile", "SystemFiles", "DirName", "dr1", file_id="1"), 0)
        self.assertEqual(
            self.MetadataUtils.writeMetadataFSDocFile("UpdateFile", "SystemFiles", "FileDetails", "Fd", file_id="1"),
            -1)
        self.assertEqual(
            self.MetadataUtils.writeMetadataFSDocFile("UpdateFile", "SystemFiles", "DetailName", "Dn", file_id="-1"),
            -2)
        self.assertEqual(
            self.MetadataUtils.writeMetadataFSDocFile("UpdateFile", "CacheFiles", "DirName", "CacheContent",
                                                      file_id="1"), 0)
        self.assertEqual(self.MetadataUtils.writeMetadataFSDocFile("UpdateFile", "CacheFiles", "Sedjun", "CacheContent",
                                                                   file_id="1"), -2)

    def test_writeMetadataFSDocFile_UpdateFileDetails(self):
        self.assertEqual(
            self.MetadataUtils.writeMetadataFSDocFile("UpdateFileDetails", "CacheFiles", "Description", "CacheDesc",
                                                      file_id="1"), 0)
        self.assertEqual(
            self.MetadataUtils.writeMetadataFSDocFile("UpdateFileDetails", "CacheFile", "Description", "CacheDesc",
                                                      file_id="1"), -2)
        self.assertEqual(
            self.MetadataUtils.writeMetadataFSDocFile("UpdateFileDetails", "CacheFiles", "Description", "CacheDesc",
                                                      file_id="-1"), -2)
        self.assertEqual(
            self.MetadataUtils.writeMetadataFSDocFile("UpdateFileDetails", "CacheFiles", "Descriptions", "CacheDesc",
                                                      file_id="1"), -2)

    # def test__check_tag(self):
    #     for tag in self.MetadataUtils.MSTagsData.meta_tags_directory:
    #         self.assertEqual(self.MetadataUtils._check_tag("1", tag), True)
    #     self.assertEqual(self.MetadataUtils._check_tag("1", "Не тег"), False)


if __name__ == '__main__':
    unittest.main()
