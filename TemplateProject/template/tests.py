import unittest
from TemplateProject.data.test_data_constants import TEST_MAIN_DIR, PROJECT_PATH
from TemplateProject.data.test_data_variables import PyCharmProjectPath
from TemplateProject.template.template_structure import TemplateStructure


class TestTemplateStructure(unittest.TestCase):

    def setUp(self):
        self.MAIN_DIR = PyCharmProjectPath + '/' + PROJECT_PATH + '/' + TEST_MAIN_DIR + '/' + 'TestTemplateStructure'
        self.Structure = TemplateStructure()

    def test_get_drive_name(self):
        print(self.Structure.get_drive_name())
        self.assertEqual(self.Structure.get_drive_name(), [{'device_id': '\\\\.\\PHYSICALDRIVE1', 'model': 'Apacer AS350 128GB'}, {'device_id': '\\\\.\\PHYSICALDRIVE7', 'model': 'Kingston DataTraveler 3.0 USB Device'}, {'device_id': '\\\\.\\PHYSICALDRIVE5', 'model': 'Kingston DataTraveler 3.0 USB Device'}, {'device_id': '\\\\.\\PHYSICALDRIVE4', 'model': 'WDC WD10SPZX-00Z10T0'}, {'device_id': '\\\\.\\PHYSICALDRIVE2', 'model': 'Apacer AS350 128GB'}, {'device_id': '\\\\.\\PHYSICALDRIVE6', 'model': 'Kingston DataTraveler 3.0 USB Device'}, {'device_id': '\\\\.\\PHYSICALDRIVE0', 'model': 'WDC WD2003FYYS-02W0B0'}, {'device_id': '\\\\.\\PHYSICALDRIVE3', 'model': 'Apacer AS350 1TB'}, {'device_id': '\\\\.\\PHYSICALDRIVE8', 'model': 'Kingston DataTraveler 3.0 USB Device'}])

    def test_get_device(self):
        print(self.Structure.get_device())
        self.assertEqual(self.Structure.get_device(), ['DESKTOP-DPHB0R8'])

    def test_get_drives(self):
        self.assertEqual(self.Structure.get_drives(), ['C:/', 'D:/', 'E:/', 'F:/', 'G:/', 'H:/', 'I:/', 'J:/', 'K:/', 'L:/'])
        print(self.Structure.get_drives())

    def test_get_drive_size(self):
        print(self.Structure.get_drive_size(self.Structure.get_drives()[0]))
        self.assertEqual(self.Structure.get_drive_size(self.Structure.get_drives()[0]), [{'total': 1023289724928, 'used': 952719007744, 'free': 70570717184, 'percent': 93.1}])

    def test_get_path_template_modules(self):
        result_gptm = self.Structure.get_path_template_modules(self.Structure.get_drives()[0])
        print(result_gptm)
        self.assertEqual(result_gptm, ['C:/GMSStorageFilesModule/', 'C:/GMSControlDataModule/', 'C:/GMSServerFilesModule/'])

    def test_get_path_template_data(self):
        result = self.Structure.get_path_template_projects_data(self.Structure.get_drives()[0])
        print(result)
        self.assertEqual(result, "C:/GMSStorageFilesModule/ProjectsData/")

    def test_get_path_control_template_data(self):
        result = self.Structure.get_path_template_control_projects_data(self.Structure.get_drives()[0])
        print(result)
        self.assertEqual(result, "C:/GMSControlDataModule/ProjectsData/")

    def test_get_path_template_global_projects(self):
        result = self.Structure.get_path_template_global_projects(self.Structure.get_drives()[0])
        print(result)
        self.assertEqual(result, ['C:/GMSStorageFilesModule/ProjectsData/1/', 'C:/GMSStorageFilesModule/ProjectsData/2/', 'C:/GMSStorageFilesModule/ProjectsData/3/'])

    def test_get_path_template_control_global_projects(self):
        result = self.Structure.get_path_template_control_global_projects(self.Structure.get_drives()[0])
        print(result)
        self.assertEqual(result, ['C:/GMSControlDataModule/ProjectsData/1/', 'C:/GMSControlDataModule/ProjectsData/2/', 'C:/GMSControlDataModule/ProjectsData/3/'])

    def test_get_path_template_global_project_projects(self):
        result1 = self.Structure.get_path_template_global_project_projects(1, self.Structure.get_drives()[0])
        result2 = self.Structure.get_path_template_global_project_projects(2, self.Structure.get_drives()[1])
        result3 = self.Structure.get_path_template_global_project_projects(3, self.Structure.get_drives()[2])
        print(result1, '\n', result2, '\n', result3)
        self.assertEqual(result1, [
                                    'C:/GMSStorageFilesModule/ProjectsData/1/Project11/',
                                    'C:/GMSStorageFilesModule/ProjectsData/1/Project12/',
                                    'C:/GMSStorageFilesModule/ProjectsData/1/Project13/'])
        self.assertEqual(result2, [
                                    'D:/GMSStorageFilesModule/ProjectsData/2/Project21/',
                                    'D:/GMSStorageFilesModule/ProjectsData/2/Project22/',
                                    'D:/GMSStorageFilesModule/ProjectsData/2/Project23/'])
        self.assertEqual(result3, [
                                    'E:/GMSStorageFilesModule/ProjectsData/3/Project31/',
                                    'E:/GMSStorageFilesModule/ProjectsData/3/Project32/',
                                    'E:/GMSStorageFilesModule/ProjectsData/3/Project33/'])
        with self.assertRaises(IndexError):
            self.Structure.get_path_template_global_project_projects(4, self.Structure.get_drives()[0])

    def test_exist_drive_path(self):
        result1 = self.Structure.exist_drive_path(self.Structure.main_template_modules[0], self.Structure.get_drives()[4])
        print(result1)

    def test_init_gms_structure_create_data(self):
        self.Structure.init_gms_structure_create(self.Structure.get_drives()[4])

    def test_set_type_gms_structure(self):
        print(self.Structure.set_type_gms_structure(self.Structure.get_drives()[4], "main"))
        print(self.Structure.set_type_gms_structure(self.Structure.get_drives()[4], "mirror"))
        print(self.Structure.set_type_gms_structure(self.Structure.get_drives()[4], "portable"))

    def test_get_type_gms_structure(self):
        print(self.Structure.get_type_gms_structure(self.Structure.get_drives()[4]))



if __name__ == '__main__':
    unittest.main()
