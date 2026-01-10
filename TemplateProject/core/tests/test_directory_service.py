import unittest

from TemplateProject.core.services.directory_service import DirectoryService

from TemplateProject.data.test_data_constants import TEST_MAIN_DIR, PROJECT_PATH
from TemplateProject.data.test_data_variables import PyCharmProjectPath


class TestDirectoryService(unittest.TestCase):
    testDir = PyCharmProjectPath + '/' + PROJECT_PATH + '/' + TEST_MAIN_DIR + '/' + 'TestDirectoryService'
    DSFolder = DirectoryService(testDir)

    def test_exists_folder(self):
        result = self.DSFolder.directory_exists("test_create_folder")
        print('test_exists_folder     =   ', result)
        self.assertEqual(result, False)

    def test_create_folder(self):
        result = self.DSFolder.create_directory("test_create_folder")
        print('test_create_folder     =   ', result)
        self.assertEqual(result, self.testDir + "/test_create_folder")

    def test_get_directories(self):
        self.assertEqual(self.DSFolder.get_directories(), ['1', 'TestDir1', 'test_create_folder'])

    def test_list_files(self):
        result = self.DSFolder.list_files()
        print('test_list_files     =   ', result)
        self.maxDiff = None
        # self.assertEqual(result)

    def test_not_found_folder_copy_file(self):
        with self.assertRaises(FileNotFoundError):
            self.DSFolder.copy_file("test_files.json", 'test_create_folder')

    def test_copy_file(self):
        self.assertEqual(self.DSFolder.create_directory("test_create_folder"), self.testDir + "/test_create_folder")
        self.assertEqual(self.DSFolder.copy_file("test_files.json", 'test_create_folder'),
                         'C:/(0)MGProjectData/4/1/1/3/2/2/3/MGSD25/MGSD/TestDir/test_create_folder')

    def test_delete_empty_folder(self):
        result = self.DSFolder.delete_directory("test_create_folder")
        print('test_delete_empty_folder     =   ', result)
        self.assertEqual(result, True)

    def test_delete_folder(self):
        result = self.DSFolder.delete_directory("test_create_folder")
        print('test_delete_folder     =   ', result)
        self.assertEqual(result, [False, 'Confirmation Required', [['C:/(0)MGProjectData/4/1/1/3/2/2/3/MGSD25/MGSD/TestDir/test_create_folder/test_files.json']]])



if __name__ == '__main__':
    unittest.main()
