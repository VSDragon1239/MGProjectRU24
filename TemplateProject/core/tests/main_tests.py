import unittest

from TemplateProject.core.tests.test_directory_service import TestDirectoryService
from TemplateProject.core.tests.test_file_service import TestFileService
from TemplateProject.core.tests.test_metadata_service import TestMetadataService
from TemplateProject.core.tests.test_metadata_utils import TestMetadataUtils

# Только один тест
suite = unittest.TestSuite()
# test_func_1 = lambda: TestDirectoryService("test_exists_folder")
suite.addTest(TestDirectoryService("test_exists_folder"))
suite.addTest(TestDirectoryService("test_create_folder"))
suite.addTest(TestDirectoryService("test_delete_empty_folder"))

print("\n")

suite.addTest(TestFileService("test_create_empty_files"))
suite.addTest(TestFileService("test_check_exists_and_create_empty_file"))
suite.addTest(TestFileService("test_json_read_empty_file"))

suite.addTest(TestFileService("test_json_read_write_file"))
suite.addTest(TestFileService("test_json_write_read_file_value_error"))
suite.addTest(TestFileService("test_json_write_file"))
suite.addTest(TestFileService("test_delete_files"))

print("\n")

suite.addTest(TestMetadataService("test_get_tag"))

print("\n")

suite.addTest(TestMetadataUtils("test_dir_service_file_path"))
suite.addTest(TestMetadataUtils("test_delete_file_service_file"))
suite.addTest(TestMetadataUtils("test_delete_dir_service_file"))

suite.addTest(TestMetadataUtils("test_exists_and_create_dir_service_file"))
suite.addTest(TestMetadataUtils("test_exists_and_create_file_service_file"))


suite.addTest(TestMetadataUtils("test_write_main_data_dir_service_file"))
suite.addTest(TestMetadataUtils("test_write_priority_data_dir_service_file"))
suite.addTest(TestMetadataUtils("test_write_links_data_dir_service_file"))

suite.addTest(TestMetadataUtils("test_write_subdir_data_dir_service_file"))
suite.addTest(TestMetadataUtils("test_write_non_index_subdir_data_dir_service_file"))

suite.addTest(TestMetadataUtils("test_read_dir_service_file"))

suite.addTest(TestMetadataUtils("test_rewrite_dir_service_file"))

# suite.addTest(TestMetadataUtils("test_delete_file_service_file"))
# suite.addTest(TestMetadataUtils("test_delete_dir_service_file"))

# Или несколько
# suite.addTests([
#     TestDirectoryService("test_create_folder"),
#     TestDirectoryService("test_delete_empty_folder"),
# ])

runner = unittest.TextTestRunner()
runner.run(suite)
