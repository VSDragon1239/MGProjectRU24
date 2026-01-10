import unittest

from TemplateProject.core.services.metadata_service import MetadataService


class TestMetadataService(unittest.TestCase):
    def setUp(self):
        self.MS = MetadataService()

    def test_get_tag(self):
        test_data_11 = self.MS.get_tag("Directory", "1")
        test_data_12 = self.MS.get_tag("Directory", "2")
        test_data_13 = self.MS.get_tag("Directory", "3")
        test_data_21 = self.MS.get_tag("Files", "1")
        test_data_22 = self.MS.get_tag("Files", "2")
        test_data_23 = self.MS.get_tag("Files", "3")
        test_data_24 = self.MS.get_tag("Files", "4")
        self.assertEqual(test_data_11, ["Dirname", "Description", "Details", "SubdirectoryInfo", "SubdirectoryNonIndex"])  # add assertion here
        self.assertEqual(test_data_12, [['DirectoryPath', 'DetailName', 'Priority', 'DirLinks', 'TotalSize', 'FileCount', 'CreatedAt', 'ModifiedAt'], ['SdN']])  # add assertion here
        self.assertEqual(test_data_13, ['Dirname', 'DetailName', 'DocFile'])  # add assertion here
        self.assertEqual(test_data_21, ['SystemFiles', 'UserFiles', 'NonIndexedFiles'])  # add assertion here
        self.assertEqual(test_data_22, ['FileIDs'])  # add assertion here
        self.assertEqual(test_data_23, ['DirName', 'DetailName', 'FileDetails'])  # add assertion here
        self.assertEqual(test_data_24, ['Description', 'Priority', 'FilesLinks', 'FileSize', 'CreatedAt', 'ModifiedAt'])  # add assertion here
        with self.assertRaises(KeyError):
            test_data_25 = self.MS.get_tag("Files", "5")
            self.assertEqual(test_data_25, ["Dirname", "Description", "Details", "SubdirectoryInfo"])


if __name__ == '__main__':
    unittest.main()
