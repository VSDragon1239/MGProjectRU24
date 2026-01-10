import unittest

from TemplateProject.core.ss_utils.structure_utils import StructureUtils
from TemplateProject.data.test_data_constants import PROJECT_PATH, TEST_MAIN_DIR
from TemplateProject.data.test_data_variables import PyCharmProjectPath


class TestStructureUtils(unittest.TestCase):
    def setUp(self):
        self.testDir = PyCharmProjectPath + '/' + PROJECT_PATH + '/' + TEST_MAIN_DIR + '/' + 'TestStructureUtils'
        self.SUMainDir = StructureUtils('SUMainDir', self.testDir)

    def test_create_structure(self):
        """
        В самом приложении (интерфейсе) уже определяется глубина и связи между директориями (кто в какой и какая глубина)
        :return:
        """
        self.SUMainDir.createStructure(onFSDocFile=True)
        self.assertEqual(True, True)  # add assertion here

    def test_remove_structure(self):
        self.SUMainDir.removeStructure()

    def test_setDirectoryData(self):
        self.assertEqual(self.SUMainDir.setDirectoryDescription("Установка тестового описания для тестовой директории '1'"), None)
        self.assertEqual(self.SUMainDir.setDirectoryDetailName("Тестовая директория '1'"), None)
        self.assertEqual(self.SUMainDir.setDirectoryPriority("0"), None)    # Выше определённого значения, невозможно будет удалить данную структуру

        self.assertEqual(self.SUMainDir.setDirectoryDirLinks(["C:/(0)MGProjectData/4/1/1/3/2/2/3/MGSD25/MGSD/TestDir/2", "C:/(0)MGProjectData/4/1/1/3/2/2/3/MGSD25/MGSD/TestDir/3", "C:/(0)MGProjectData/4/1/1/3/2/2/3/MGSD25/MGSD/TestDir/4"]), 1)
        self.assertEqual(self.SUMainDir.setDirectoryDirLinks("C:/(0)MGProjectData/4/1/1/3/2/2/3/MGSD25/MGSD/TestDir/4"), -2)
        self.assertEqual(self.SUMainDir.setDirectoryDirLinks("C:/(0)MGProjectData/4/1/1/3/2/2/3/MGSD25/MGSD/TestDir/5"), 2)

        self.assertEqual(self.SUMainDir.setDirectoryTotalSize("0"), None)
        self.assertEqual(self.SUMainDir.setDirectoryFileCount("2"), None)
        self.assertEqual(self.SUMainDir.setDirectoryCreatedAt("12-01-2025 09:36:41"), None)
        self.assertEqual(self.SUMainDir.setDirectoryModifiedAt("12-03-2025 13:46:41"), None)

        self.assertEqual(self.SUMainDir.setDirectoryNewSdN(["1", "Тестовая поддиректория '1' в тестовой директории '1'", 'DSDocFile.json']), None)
        self.assertEqual(self.SUMainDir.setDirectoryNewSdN(["2", "Тестовая поддиректория '2' в тестовой директории '1' c ошибочной информацией", 'DSDocFile.json']), None)
        self.assertEqual(self.SUMainDir.setDirectorySdN(["2", "Тестовая поддиректория '2' в тестовой директории '2' с изменением", 'DSDocFile.json'], "1"), None)

        self.assertEqual(self.SUMainDir.setDirectoryNewSdNonIndex('NameNonIndexFolder'), None)
        self.assertEqual(self.SUMainDir.setDirectorySdNonIndex('NameNonIndexFolder', 'newNameNonIndexFolder'), None)

    def test_removeDirectoryData(self):
        self.assertEqual(self.SUMainDir.removeDirectoryDescription(), None)

        self.assertEqual(self.SUMainDir.removeDirectoryDetailName(), None)
        self.assertEqual(self.SUMainDir.removeDirectoryPriority(), None)
        self.assertEqual(self.SUMainDir.removeDirectoryTotalSize(), None)
        self.assertEqual(self.SUMainDir.removeDirectoryFileCount(), None)
        self.assertEqual(self.SUMainDir.removeDirectoryCreatedAt(), None)
        self.assertEqual(self.SUMainDir.removeDirectoryModifiedAt(), None)

        self.assertEqual(self.SUMainDir.removeDirectorySdN("1"), None)
        self.assertEqual(self.SUMainDir.removeDirectorySdN("2"), None)

        self.assertEqual(self.SUMainDir.removeDirectoryDirLinks("C:/(0)MGProjectData/4/1/1/3/2/2/3/MGSD25/MGSD/TestDir/2"), 32)
        self.assertEqual(self.SUMainDir.removeDirectoryDirLinks("C:/(0)MGProjectData/4/1/1/3/2/2/3/MGSD25/MGSD/TestDir/2"), -312)
        self.assertEqual(self.SUMainDir.removeDirectoryDirLinks(["C:/(0)MGProjectData/4/1/1/3/2/2/3/MGSD25/MGSD/TestDir/3", "C:/(0)MGProjectData/4/1/1/3/2/2/3/MGSD25/MGSD/TestDir/4", "C:/(0)MGProjectData/4/1/1/3/2/2/3/MGSD25/MGSD/TestDir/5"]), 1)

        self.assertEqual(self.SUMainDir.removeDirectorySdNonIndex("newNameNonIndexFolder"), 31)

    def test_getDirectoryData(self):
        self.assertEqual(self.SUMainDir.getDirectoryDescription(), "Установка тестового описания для тестовой директории '1'")

    def test_setDirectoryDirLink(self):
        pass

    def test_setDirectoryTotalSize(self):
        pass

    def test_setDirectoryFileCount(self):
        pass

    def test_setDirectoryCreatedAt(self):
        pass

    def test_setDirectoryModifiedAt(self):
        pass

    def test_setDirectoryNewSdN(self):
        pass

    def test_setDirectoryNewSdNonIndex(self):
        pass

    def test_setDirectory(self):
        pass

    def test_setDirectory(self):
        pass

    def test_setDirectory(self):
        pass

    def test_setDirectory(self):
        pass

    def test_setDirectory(self):
        pass

    def test_setDirectory(self):
        pass

    def test_setDirectory(self):
        pass

    def test_setDirectory(self):
        pass

    def test_setDirectory(self):
        pass

    def test_setDirectory(self):
        pass

    def test_new_json_file(self):
        print(self.SUMainDir.new_json_file("1", "Name", {}))


if __name__ == '__main__':
    unittest.main()
