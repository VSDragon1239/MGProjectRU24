from distutils.command.build_ext import extension_name_re

from TemplateProject.core.services.directory_service import DirectoryService
from TemplateProject.core.services.file_service import FileService
from TemplateProject.core.ss_utils.metadata_utils import MetadataUtils


class StructureUtils:
    def __init__(self, dir_name, directory):
        self.dir_name = dir_name
        self.directory = directory.replace('\\', '/')
        self.DSMainDir = None
        self.__dirExist()
        self.MDDocData = MetadataUtils(self.directory)

    def __dirExist(self):
        try:
            self.DSMainDir = DirectoryService(self.directory + '/' + self.dir_name)
            self.directory = self.directory + '/' + self.dir_name
        except FileNotFoundError:
            self.DSMainDir = DirectoryService(self.directory)
            self.DSMainDir.create_directory(self.directory + '/' + self.dir_name)
            self.directory = self.directory + '/' + self.dir_name

    def __set_base_metadata_file(self):
        self.MDDocData.writeMetadataDSDocFile('Directory', 'Dirname', self.dir_name)
        self.MDDocData.writeMetadataDSDocFile('Details', 'DirectoryPath', self.directory)

    def createStructure(self, onFSDocFile=False):
        self.MDDocData.createDSDocFile()
        if onFSDocFile:
            self.MDDocData.createFSDocFile()
        self.__set_base_metadata_file()

    def removeStructure(self):
        try:
            self.MDDocData.deleteDSDocFile()
            self.MDDocData.deleteFSDocFile()
        except FileNotFoundError:
            print('1')
        finally:
            self.DSMainDir.delete_directory(self.directory)

    def setDirectoryDescription(self, content):
        self.MDDocData.writeMetadataDSDocFile('Directory', 'Description', content)

    def setDirectoryDetailName(self, content):
        self.MDDocData.writeMetadataDSDocFile('Details', 'DetailName', content)

    def setDirectoryPriority(self, content):
        self.MDDocData.writeMetadataDSDocFile('Details', 'Priority', content)

    def setDirectoryDirLinks(self, content):
        """
        У этого тега если ещё метод удаления Get и Remove
        :param content: [str, str, ..., str] or 'str'
        :return: 131, 132, None
        """
        return self.MDDocData.writeMetadataDSDocFile('Details', 'DirLinks', content)

    def setDirectoryTotalSize(self, content):
        self.MDDocData.writeMetadataDSDocFile('Details', 'TotalSize', content)

    def setDirectoryFileCount(self, content):
        self.MDDocData.writeMetadataDSDocFile('Details', 'FileCount', content)

    def setDirectoryCreatedAt(self, content):
        self.MDDocData.writeMetadataDSDocFile('Details', 'CreatedAt', content)

    def setDirectoryModifiedAt(self, content):
        self.MDDocData.writeMetadataDSDocFile('Details', 'ModifiedAt', content)

    def setDirectoryNewSdN(self, content: list):
        """
        :param content: ["Dirname", "DetailName", "DocFile.json"]
        :return: None
        """
        self.MDDocData.writeMetadataDSDocFile('SubdirectoryInfo', '', content)

    def setDirectorySdN(self, content: list, SdN: str):
        """
        :param content: ["Dirname", "DetailName", "DocFile.json"]
        :param SdN: "1", "2"... "n". But`n "0"
        :return: None
        """
        if SdN == "0":
            raise ValueError("SdN cannot be 0, use method 'setDirectoryNewSdN'")
        self.MDDocData.writeMetadataDSDocFile('SubdirectoryInfo', '', content, SdN=SdN)

    def setDirectoryNewSdNonIndex(self, content):
        self.MDDocData.writeMetadataDSDocFile('SubdirectoryNonIndex', '', content)

    def setDirectorySdNonIndex(self, SdNonIndexName, SdNonIndexNewName):
        content = [SdNonIndexName, SdNonIndexNewName]
        self.MDDocData.writeMetadataDSDocFile('SubdirectoryNonIndex', '', content)

    def setDirectory(self):
        pass

    # Getters
    def getDirectoryDescription(self):
        return self.MDDocData.readMetadataSDocFile('Directory', '1', 'Description')

    def getDirectoryDetailName(self):
        return self.MDDocData.readMetadataSDocFile('Directory', '1', 'DetailName')

    def getDirectoryPriority(self):
        return self.MDDocData.readMetadataSDocFile('Directory', '21', 'Priority')

    def getDirectoryDirLinks(self):
        return self.MDDocData.readMetadataSDocFile('Directory', '21', 'DirLinks')

    def getDirectoryTotalSize(self):
        return self.MDDocData.readMetadataSDocFile('Directory', '21', 'TotalSize')

    def getDirectoryFileCount(self):
        self.MDDocData.readMetadataSDocFile('Directory', '21', 'FileCount')

    def getDirectoryCreatedAt(self):
        self.MDDocData.readMetadataSDocFile('Directory', '21', 'CreatedAt')

    def getDirectoryModifiedAt(self):
        self.MDDocData.readMetadataSDocFile('Directory', '21', 'ModifiedAt')

    def getDirectorySdN_by_dirname_or_detail_name(self, dirname_or_detail_name):
        for keys, values in self.MDDocData.readMetadataSDocFile('Directory', '22', '-1', '0').items():
            print("getDirectorySdN_by_dirname_or_detail_name    ", keys, values, values["Dirname"], values["DetailName"])
            if values["Dirname"] == dirname_or_detail_name:
                return values["Dirname"], keys
            elif values["DetailName"] == dirname_or_detail_name:
                return values['DetailName'], keys
        return None, None

    def getDirectorySdN_byId(self, SdN):
        self.MDDocData.readMetadataSDocFile('Directory', '22', 'Description')

    def getDirectorySdN_all(self):
        self.MDDocData.readMetadataSDocFile('Directory', '22', 'Description')

    def getDirectorySdNonIndex(self, SdNonIndexName):
        self.MDDocData.readMetadataSDocFile('Directory', '23', 'Description')

    def getDirectory(self):
        pass

    def removeDirectoryDescription(self):
        self.MDDocData.writeMetadataDSDocFile('Directory', 'Description', "")

    def removeDirectoryDetailName(self):
        self.MDDocData.writeMetadataDSDocFile('Details', 'DetailName', "")

    def removeDirectoryPriority(self):
        self.MDDocData.writeMetadataDSDocFile('Details', 'Priority', "")

    def removeDirectoryDirLinks(self, dirLink_name):
        """
        У этого тега если ещё метод удаления Get и Remove
        :param dirLink_name: [str, str, ..., str] or 'str'
        :return: None
        """
        if type(dirLink_name) == str:
            return self.MDDocData.writeMetadataDSDocFile('Details', 'DirLinks', [dirLink_name, ""])
        elif type(dirLink_name) == list:
            while dirLink_name.__len__() > 0:
                print(dirLink_name[0])
                self.MDDocData.writeMetadataDSDocFile('Details', 'DirLinks', [dirLink_name[0], ""])
                del dirLink_name[0]
            return 1

    def removeDirectoryTotalSize(self):
        self.MDDocData.writeMetadataDSDocFile('Details', 'TotalSize', "")

    def removeDirectoryFileCount(self):
        self.MDDocData.writeMetadataDSDocFile('Details', 'FileCount', "")

    def removeDirectoryCreatedAt(self):
        self.MDDocData.writeMetadataDSDocFile('Details', 'CreatedAt', "")

    def removeDirectoryModifiedAt(self):
        self.MDDocData.writeMetadataDSDocFile('Details', 'ModifiedAt', "")

    def removeDirectorySdN(self, content):
        """
        :param content: "SdN" or DirName
        :return: None
        """
        self.MDDocData.removeSubdirMetadataDSDocFile('SubdirectoryInfo', content)

    def removeDirectorySdNonIndex(self, content):
        """
        :param content:  Used is select to remove -> "name"
        :return: The More I Try... Shy KNOW!11!!1!
        """
        if type(content) == str:
            if content != "":
                return self.MDDocData.writeMetadataDSDocFile('SubdirectoryNonIndex', '', [content, ""])
            else:
                return self.MDDocData.writeMetadataDSDocFile('SubdirectoryNonIndex', '', "")
        elif type(content) == list:
            while content.__len__() > 0:
                print(content[0])
                self.MDDocData.writeMetadataDSDocFile('SubdirectoryNonIndex', '', [content[0], ""])
                del content[0]
            return 1

    def __create_file(self, file_name, file_extension, content):
        print("create_file", self.directory)
        file = FileService(self.directory, file_name,  file_extension)
        file.create_file(content)
        return file

    def new_json_file(self, file_id: str, file_name: str, content: dict):
        extension = "json"
        self.new_file_metadata(file_id)
        self.set_file_metadata_name(file_id, file_name, extension)
        return self.__create_file(file_name, extension, content)

    def new_file_metadata(self, file_id):
        self.MDDocData.writeMetadataFSDocFile("AddFile", "Files", "SystemFiles", "", file_id=file_id)

    def set_file_metadata_name(self, file_id, file_name, extension):
        print('set_file_metadata_name', file_id, file_name)
        self.MDDocData.writeMetadataFSDocFile("UpdateFile", "File", "SystemFiles", ["DirName", f"{file_name}.{extension}"], file_id=file_id)

    def get_file_data(self, file_name, file_extension):
        file = FileService(self.directory, file_name, file_extension)
        if file.file_exists():
            return file.read_file()
        else:
            return False

    def get_file_metadata(self, dirname):
        pass

    def update_json_file(self, file_name, file_extension, content: dict):
        file = FileService(self.directory, file_name,  file_extension)
        file.write_file(content, safeMode=True)
