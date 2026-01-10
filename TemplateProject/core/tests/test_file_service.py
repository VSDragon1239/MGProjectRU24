import unittest
from unittest import result

from TemplateProject.core.services.file_service import FileService
from TemplateProject.data.test_data_constants import TEST_MAIN_DIR, PROJECT_PATH
from TemplateProject.data.test_data_variables import PyCharmProjectPath


class TestFileService(unittest.TestCase):

    def setUp(self):
        self.MAIN_DIR = PyCharmProjectPath + '/' + PROJECT_PATH + '/' + TEST_MAIN_DIR + '/' + 'TestFileService'
        self.FSDocFile = FileService(self.MAIN_DIR, "File Name - FSDocFile", "json")

        self.test_json_read_data = {
            "Test_Data_4": {"TD_2": {"TD_2.1": {"TD_2.1.1": {"TD_2.1.1.1": {"TD_2.1.1.1.2": "READING_TEST"}}}}}}

    def test_create_empty_files(self):
        with self.assertRaises(ValueError):
            self.FSDocFile.create_file()
        result_tcef = "СозданПустойФайл(ValueError)"
        print("test_create_empty_files     =   '", result_tcef)

    def test_check_exists_and_create_empty_file(self):
        if self.FSDocFile.file_exists():
            with self.assertRaises(FileExistsError):
                self.FSDocFile.create_file()
            result_tceacef = "ФайлЕсть(file_exists) - And - НельзяСоздатьТакойЖеФайл(FileExistsError)"
        else:
            with self.assertRaises(ValueError):
                self.FSDocFile.create_file()
            result_tceacef = "ФайлаНет(file_not_exists) - And - СозданПустойФайл(ValueError)"
        print('test_check_exists_and_create_empty_file     =   ', result_tceacef)

    def test_json_read_empty_file(self):

        try:
            data = self.FSDocFile.read_file()
            if data is dict:
                self.assertEqual(data, ['json', data[0]])
                result_tjref = f'ФайлНеПустой(["json", {data[0]}])'
            else:
                self.assertEqual(data, ['json', ""])
                result_tjref = 'ФайлНеПустой(Строка???)'
            print('test_json_read_empty_file (NoEmptyError)     =   ', result_tjref)
        except AssertionError:
            result_tjref = 'ФайлПустой(JSONDecodeError)'
            print('test_json_read_empty_file     =   ', result_tjref)

    def test_json_read_write_file(self):
        self.FSDocFile.write_file(self.test_json_read_data, safeMode=False)
        try:
            self.assertEqual(self.FSDocFile.read_file()[0], "json")
            self.assertEqual(self.FSDocFile.read_file()[1], self.test_json_read_data)
            result_trf = "ФайлПрочитанВерно"
            print('test_json_read_write_file     =   ', result_trf)
        except FileNotFoundError:
            result_trf = "ФайлНеНайден(FileNotFoundError)"
            print('test_json_read_write_file     =   ', result_trf)

    def test_json_write_read_file_value_error(self):
        """
        Попытка записать неверный формат в json, что должно выдать ValueError, и не изменить в нём существующие данные
        """
        result_tjwfve_1 = self.FSDocFile.read_file()
        try:
            self.FSDocFile.write_file({1})
        except ValueError:
            result_tjwfve_2 = self.FSDocFile.read_file()
            self.assertEqual(result_tjwfve_1, result_tjwfve_2)
            print('test_json_write_read_file_value_error     =   ', result_tjwfve_2, "- Тест того, что попытка записать неправильные данные, не затирает то, что уже есть")

    def test_json_write_file(self):
        test_data_1 = {"TestData_1": {"TD_1": 1.0}}
        check_test_data_1 = {"TestData_1": {"TD_1": 1.0}}
        self.FSDocFile.write_file(test_data_1)
        self.assertEqual(self.FSDocFile.read_file()[1], check_test_data_1)
        print('test_json_write_file_1     =   ', "ТестЗаписи(NotSafeMode)ЧтенияПрошёлУспешно")

        test_data_2 = {"TestData_1": {"TD_2": {"TD_2.1": 2.1}}}
        check_test_data_2 = {"TestData_1": {"TD_1": 1.0, "TD_2": {"TD_2.1": 2.1}}}
        self.FSDocFile.write_file(test_data_2, safeMode=True)
        self.assertEqual(self.FSDocFile.read_file()[1], check_test_data_2)
        print('test_json_write_file_2     =   ', "ТестЗаписиЧтения(SafeMode)ПрошёлУспешно")

        test_data_3 = {"TestData_1": {"TD_2": {"TD_2.2": {"TD_2.2.1": {"TD_2.2.1.1": 2.211}}}}}
        check_test_data_3 = {'TestData_1': {"TD_1": 1.0, "TD_2": {"TD_2.1": 2.1, "TD_2.2": {"TD_2.2.1": {"TD_2.2.1.1": 2.211}}}}}
        self.FSDocFile.write_file(test_data_3, safeMode=True)
        self.assertEqual(self.FSDocFile.read_file()[1], check_test_data_3)
        print('test_json_write_file_3     =   ', "ТестЗаписиЧтения(SafeMode)ПрошёлУспешно")

        test_data_4 = {"TestData_2": {"TD_2": {"TD_2.2": {"TD_2.2.1": {"TD_2.2.1.1": 2.211}}}}}
        check_test_data_4 = {"TestData_1": {"TD_1": 1.0, "TD_2": {"TD_2.1": 2.1, "TD_2.2": {"TD_2.2.1": {"TD_2.2.1.1": 2.211}}}},
                             "TestData_2": {"TD_2": {"TD_2.2": {"TD_2.2.1": {"TD_2.2.1.1": 2.211}}}}}
        self.FSDocFile.write_file(test_data_4, safeMode=True)
        self.assertEqual(self.FSDocFile.read_file()[1], check_test_data_4)
        print('test_json_write_file_4     =   ', "ТестЗаписиЧтения(SafeMode)ПрошёлУспешно")

        test_data_5 = {"Test_Data_3": {"TD_3": 3.0}}
        test_data_6 = {"Test_Data_3": 3.0}
        test_data_7 = {"Test_Data_3": {"TD_3": 3.0}}
        test_data_8 = {"Test_Data_3": {"TD_2": 3.0}}
        test_data_9 = {"Test_Data_3": {"TD_2": {"TD_2.1": {"TD_2.1.1": {"TD_2.1.1.1": {"TD_2.1.1.1.1": 2.1111}}}}}}
        test_data_10 = {"Test_Data_3": {"TD_2": {"TD_2.1": {"TD_2.1.1": {"TD_2.1.1.1": {"TD_2.1.1.1.2": 2.1111}}}}}}
        test_data_11 = {"Test_Data_3": {"TD_2": {"TD_2.1": {"TD_2.1.1": {"TD_2.1.1.1": {"TD_2.1.1.1.2": 2.1112}}}}}}
        self.FSDocFile.write_file(test_data_5, safeMode=True)
        self.FSDocFile.write_file(test_data_6, safeMode=True)
        self.FSDocFile.write_file(test_data_7, safeMode=True)
        self.FSDocFile.write_file(test_data_8, safeMode=True)
        # self.FSDocFile.write_file(test_data_9, safeMode=False)
        self.FSDocFile.write_file(test_data_10, safeMode=True)
        self.FSDocFile.write_file(test_data_11, safeMode=True)
        print('test_json_write_file_5-11     =   ', "ТестРазличныхЗаписей...")

    def test_delete_files(self):
        with self.assertRaises(FileNotFoundError):
            result_tdf_1 = "ФайлНеНайден"
            self.assertEqual(self.FSDocFile.delete_file(), 1)
            result_tdf_1 = "ФайлУдалён"
            self.FSDocFile.delete_file()
        result_tdf_2 = "ПовторнаяПопыткаУдаления(FileNotFoundError)"
        print('test_delete_files       =   ', result_tdf_1, ",  ", result_tdf_2)



if __name__ == '__main__':
    unittest.main()
