# Работа с мета-данными.
import ast

from TemplateProject.core.services.file_service import FileService
from TemplateProject.core.services.metadata_service import MetadataService


class MetadataUtils:
    Tags = {}

    def __init__(self, directory):
        self.directory = directory
        self.MSTagsData = MetadataService()
        self.DSDocFile = FileService(self.directory, file_name='DSDocFile', file_extension='json')
        self.FSDocFile = FileService(self.directory, file_name='FSDocFile', file_extension='json')

    # def _check_tag(self, level, tag):
    #     if level == "1":
    #         if tag not in self.MSTagsData.meta_tags_directory:
    #             return False
    #         else:
    #             return True

    def createDSDocFile(self, rewrite=False):
        filedata = self.__create_doc_file_meta_tags("DSDocFile")
        if rewrite:
            self.DSDocFile.write_file(content=filedata)
            return True
        else:
            try:
                self.DSDocFile.create_file(content=filedata)
                return self.DSDocFile.get_file_path()
            except FileExistsError:
                return [self.DSDocFile.get_file_path(), self.DSDocFile.read_file()]

    def createFSDocFile(self, rewrite=False):
        filedata = self.__create_doc_file_meta_tags("FSDocFile")
        if rewrite:
            self.FSDocFile.write_file(content=filedata)
        else:
            try:
                self.FSDocFile.create_file(content=filedata)
                return self.FSDocFile.get_file_path()
            except FileExistsError:
                return [self.FSDocFile.get_file_path(), self.FSDocFile.read_file()]

    def __create_doc_file_meta_tags(self, filename):
        if filename == 'DSDocFile':
            type_tag = "Directory"
            tags_level_1 = self.MSTagsData.get_tag(type_tag,
                                                   "1")  # "Dirname", "Description", "Details", "SubdirectoryInfo", "SubdirectoryNonIndex"
            tags_level_2 = self.MSTagsData.get_tag(type_tag,
                                                   "2")  # ['DirectoryPath', 'DetailName', 'Priority', 'DirLinks', 'TotalSize', 'FileCount', 'CreatedAt', 'ModifiedAt'], ['SdN']]
            ts_lvl_2_details = tags_level_2[
                0]  # 'DirectoryPath', 'DetailName', 'Priority', 'DirLinks', 'TotalSize', 'FileCount', 'CreatedAt', 'ModifiedAt'
            ts_lvl_2_SdNs = tags_level_2[1]  # 'SdN' - no used == "0"
            tags_level_3 = self.MSTagsData.get_tag(type_tag, "3")  # 'Dirname', 'DetailName', 'DocFile'

            filedata = {
                type_tag: {
                    tags_level_1[0]: "",
                    tags_level_1[1]: "",
                    tags_level_1[2]: {ts_lvl_2_details[0]: "", ts_lvl_2_details[1]: "",
                                      ts_lvl_2_details[2]: "", ts_lvl_2_details[3]: "",
                                      ts_lvl_2_details[4]: "", ts_lvl_2_details[5]: "",
                                      ts_lvl_2_details[6]: "", ts_lvl_2_details[7]: ""},
                    tags_level_1[3]: {"0": {tags_level_3[0]: "", tags_level_3[1]: "",
                                            tags_level_3[2]: ""}},
                    tags_level_1[4]: "",
                }
            }
            return filedata
        elif filename == 'FSDocFile':
            type_tag = "Files"
            tags_level_1 = self.MSTagsData.get_tag(type_tag, "1")  # 'SystemFiles', 'UserFiles', 'NonIndexedFiles'
            tags_level_2 = self.MSTagsData.get_tag(type_tag, "2")  # 'FileIDs' - no used == "0"
            tags_level_3 = self.MSTagsData.get_tag(type_tag, "3")  # 'DirName', 'DetailName', 'FileDetails'
            tags_level_4 = self.MSTagsData.get_tag(type_tag,
                                                   "4")  # 'Description', 'Priority', 'FilesLinks', 'FileSize', 'CreatedAt', 'ModifiedAt'

            detailTagFile = {tags_level_4[0]: "", tags_level_4[1]: "", tags_level_4[2]: [], tags_level_4[3]: "",
                             tags_level_4[4]: "", tags_level_4[5]: ""}
            tagfile = {"0": {tags_level_3[0]: "", tags_level_3[1]: "", tags_level_3[2]: detailTagFile}}
            tagfileNonIndexed = {"0": {tags_level_3[0]: "", tags_level_3[1]: ""}}

            filedata = {
                type_tag: {
                    tags_level_1[0]: tagfile,
                    tags_level_1[1]: tagfile,
                    tags_level_1[2]: tagfileNonIndexed
                }
            }
            return filedata

    @staticmethod
    def __checkTargFileLvl(level_name_tag):
        if level_name_tag == "21" or level_name_tag == "31":
            level_name_tag = "SystemFiles"
        elif level_name_tag == "22" or level_name_tag == "32":
            level_name_tag = "UserFiles"
        elif level_name_tag == "23" or level_name_tag == "33":
            level_name_tag = "NonIndexedFiles"
        else:
            if level_name_tag[:5] == "System":
                level_name_tag = "SystemFiles"
            elif level_name_tag[:4] == "User":
                level_name_tag = "UserFiles"
            elif level_name_tag[:9] == "NonIndexed":
                level_name_tag = "NonIndexedFiles"
        return level_name_tag

    def __targFileLvlTwoReadMetadataSDocFile(self, datafile, level_name_tag, target_name_tag, file_id):
        """Выделение дублирующего функционала во втором уровне"""
        level_name_tag = self.__checkTargFileLvl(level_name_tag)
        try:
            if file_id != "0":
                return datafile["Files"][level_name_tag][file_id]
            else:
                return datafile["Files"][level_name_tag][target_name_tag]
        except KeyError:
            raise KeyError(f"Допустимые теги (файлы): {datafile['Files'][level_name_tag].keys()}")

    def __targFileLvlThreeReadMetadataSDocFile(self, datafile, level_name_tag, target_name_tag, file_id):
        """Выделение дублирующего функционала на третьем уровне вложенности"""
        level_name_tag = self.__checkTargFileLvl(level_name_tag)
        try:
            if file_id != "0":
                return datafile["Files"][level_name_tag][file_id]["FileDetails"][target_name_tag]
            else:
                return datafile["Files"][level_name_tag]["0"]["FileDetails"][target_name_tag]
        except KeyError:
            try:
                raise KeyError(f"Допустимые теги: {datafile['Files'][level_name_tag][file_id]['FileDetails'].keys()}")
            except KeyError as e:
                if e != "Допустимые теги: dict_keys(['Description', 'Priority', 'FilesLinks', 'FileSize', 'CreatedAt', 'ModifiedAt'])":
                    print(e)
                    if e == "FileDetails":
                        # try:
                        raise KeyError(
                            f"Не индексированные опознанные файлы не имеют уровня деталей: {datafile['Files'][datafile['Files'][level_name_tag].keys()]}")
                        # except KeyError as e:
                        #     if e == "FileDetails":
                    else:
                        raise KeyError(f"Допустимые теги (файлы): {datafile['Files'][level_name_tag].keys()}")
                else:
                    raise KeyError(
                        f"Допустимые теги: {datafile['Files'][level_name_tag][file_id]['FileDetails'].keys()}")

    def readMetadataSDocFile(self, type_tag, level_name_tag, target_name_tag, SdN="0", file_id="0"):
        """
        :param type_tag: Тип FSDocFile == "Files" или DSDocFile == "Directory"
        :param level_name_tag: Уровень, "Directory" == "1", "Details" == "21", "SubdirectoryInfo" == "22", "SubdirectoryNonIndex" == "23".
        :param target_name_tag: Целевой тег в json файле
        :param SdN: if 0 and :param target_name_tag: == -1: Возвращает все поддиректории,
                иначе if :param SdN: == 0 вместо этого параметра берётся вот этот :param target_name_tag:
        :param file_id:
        :return: {json}
        :raise: KeyError, ValueError
        """
        # ---------------------------------------Directory---------------------------------------
        if type_tag == "Directory":
            datafile = self.DSDocFile.read_file()[1]
            if level_name_tag == "Directory" or level_name_tag == "1":
                try:
                    return datafile["Directory"][target_name_tag]
                except KeyError:
                    raise KeyError(f"Допустимые теги: {datafile['Directory'].keys()}")
            elif level_name_tag == "Details" or level_name_tag == "21":
                try:
                    return datafile["Directory"]["Details"][target_name_tag]
                except KeyError:
                    raise KeyError(f"Допустимые теги: {datafile['Directory']['Details'].keys()}")
            elif level_name_tag == "SubdirectoryInfo" or level_name_tag == "22":
                try:
                    if SdN == "0":
                        if target_name_tag == "-1":
                            return datafile["Directory"]["SubdirectoryInfo"]
                        else:
                            try:
                                type(int(target_name_tag))
                                return datafile["Directory"]["SubdirectoryInfo"][target_name_tag]
                            except ValueError:
                                raise ValueError(
                                    f"Допустимые значения на этом уровне: target_name_tag == '-1' and SdN != '0' or target_name_tag in {datafile['Directory']['SubdirectoryInfo'].keys()}")
                    else:
                        return datafile["Directory"]["SubdirectoryInfo"][SdN]
                except KeyError:
                    raise KeyError(
                        f"Допустимые теги (target): {datafile['Directory']['SubdirectoryInfo'].keys()} or '-1' (SdN): {datafile['Directory']['SubdirectoryInfo'].keys()}")
            elif level_name_tag == 'SubdirectoryNonIndex' or level_name_tag == "23":
                try:
                    if SdN == "0":
                        return datafile["Directory"]["SubdirectoryNonIndex"]
                    else:
                        return datafile["Directory"]["SubdirectoryNonIndex"][SdN]
                except KeyError:
                    raise KeyError(f"Допустимые значения (файлы):    {datafile['Directory']['SubdirectoryNonIndex']}")
            else:
                raise KeyError("Уровень не существует")
        # ---------------------------------------Files---------------------------------------
        elif type_tag == "Files":
            datafile = self.FSDocFile.read_file()[1]
            if level_name_tag == "Files" or level_name_tag == "1":
                try:
                    return datafile["Files"][target_name_tag]
                except KeyError:
                    raise KeyError(f"Допустимые теги: {datafile['Files'].keys()}")
            elif level_name_tag == "SystemFiles" or level_name_tag == "UserFiles" or level_name_tag == "NonIndexedFiles" or level_name_tag == "21" or level_name_tag == "22" or level_name_tag == "23":
                return self.__targFileLvlTwoReadMetadataSDocFile(datafile, level_name_tag, target_name_tag, file_id)
            elif level_name_tag == "SystemDetailsFile" or level_name_tag == "31" or level_name_tag == "UserDetailsFile" or level_name_tag == "32" or level_name_tag == "NonIndexedDetailsFile" or level_name_tag == "33":
                return self.__targFileLvlThreeReadMetadataSDocFile(datafile, level_name_tag, target_name_tag, file_id)

    def writeMetadataDSDocFile(self, tag_level_name, nametag, content, SdN="0"):
        """
        :param tag_level_name: Уровни тегов - 1=('Directory'),
                                              2=('Details', 'SubdirectoryInfo', 'SubdirectoryNonIndex')
        :param nametag: 'Dirname', 'Description',
                        if tag_level_name == 'Details':
                           'DirectoryPath', DetailName, TotalSize, FileCount, CreatedAt, ModifiedAt;
                        if tag_level_name == 'SubdirectoryInfo' and :param SdN: !=0:
                           'Dirname', 'DetailName', 'DocFile' or ['1', '2', '3']
        :param content: Данные для заполнения, для поддиректорий используется уровень SubdirectoryInfo и данные в виде списка [1,2,3]
        :param SdN: Номер поддиректории, а так как папки (директории) будут названы цифрами, то сюда вписывается номер в виде строки
        :return: Возвращает цифру, соответствующего уровня вложенности тега, отрицательная если запись не удалась
        """
        if tag_level_name == "Directory":
            if nametag not in ["Details", "SubdirectoryInfo", "SubdirectoryNonIndex"]:
                self.DSDocFile.write_file({tag_level_name: {nametag: content}}, safeMode=True)
                return 1
            return -1
        elif tag_level_name == "Details":
            if nametag == "DirLinks":
                dir_links = self.readMetadataSDocFile('Directory', '21', 'DirLinks')
                if type(content) == list:
                    if len(content) == 2:
                        print("writeMetadataDSDocFile", tag_level_name, nametag, content, dir_links)
                        return self.replace_data_wMDSDF(tag_level_name, content, dir_links, tag=nametag)
                    else:
                        for d_link in content:
                            if type(d_link) is not str:
                                raise ValueError('use a only string in list!')
                            if d_link in dir_links:
                                return -2
                            if dir_links == "":
                                dir_links = []
                            dir_links.append(d_link)
                        self.DSDocFile.write_file({"Directory": {tag_level_name: {nametag: dir_links}}}, safeMode=True)
                        return 2
                elif type(content) is str:
                    if content in dir_links:
                        return -2
                    else:
                        if dir_links == "":
                            dir_links = []
                        dir_links.append(content)
                        self.DSDocFile.write_file({"Directory": {tag_level_name: {nametag: dir_links}}}, safeMode=True)
                        return 2
            else:
                self.DSDocFile.write_file({"Directory": {tag_level_name: {nametag: content}}}, safeMode=True)
                return 2
        elif tag_level_name == "SubdirectoryInfo":

            fileData = self.DSDocFile.read_file()[1]["Directory"]["SubdirectoryInfo"]
            SdN_New = str(int((max(fileData, key=lambda x: int(x)))) + 1)
            if SdN == "0" or SdN == "New":
                SdN = SdN_New
            else:
                if SdN >= SdN_New:
                    raise KeyError("Данный SdN не является действительным - SdN is not correct and not keys and values")

            if type(content) == str:
                if nametag == "Dirname" or nametag == "DetailName" or nametag == "DocFile":
                    if nametag == "Dirname":
                        for i in fileData.keys():
                            if fileData[i]['Dirname'] == content:
                                return -2
                    self.DSDocFile.write_file({"Directory": {tag_level_name: {SdN: {nametag: content}}}}, safeMode=True)
                    return 2
                else:
                    return -2
            elif type(content) == list:
                if len(content) == 3:
                    for i in fileData.keys():
                        if fileData[i]['Dirname'] == content[0]:
                            return -2
                    self.DSDocFile.write_file({"Directory": {tag_level_name: {
                        SdN: {"Dirname": content[0], "DetailName": content[1], "DocFile": content[2]}}}}, safeMode=True)
                    return 2
                else:
                    return -2
        elif tag_level_name == "SubdirectoryNonIndex":
            content_list = self.readMetadataSDocFile('Directory', tag_level_name, target_name_tag=nametag)
            if type(content) == str:
                if type(content_list) == list:
                    if not content in content_list:
                        content_list.append(content)
                        self.DSDocFile.write_file({"Directory": {tag_level_name: content_list}}, safeMode=True)
                        return 2
                    else:
                        return -2
                elif content_list == "":
                    self.DSDocFile.write_file({"Directory": {tag_level_name: [content]}}, safeMode=True)
                    return 2
                else:
                    return -2
            elif type(content) == list:
                if len(content) == 2:
                    return self.replace_data_wMDSDF(tag_level_name, content, content_list)
                else:
                    content.extend(content_list)
                    content = list(set(content))
                    content.sort()
                    self.DSDocFile.write_file({"Directory": {tag_level_name: content}}, safeMode=True)
                    return 2
            else:
                return -2

    def replace_data_wMDSDF(self, tag_level_name, content, content_list, tag=""):
        """
        :param tag_level_name:
        :param content:
        :param content_list:
        :param tag:
        :return: Возвращает -311 = уже есть такой элемент. -312 = не существует. 31 и 32 - если успех
        """
        # print(content_list) --> ['path/to/directory/link1', 'path/to/directory/link2', 'path/to/directory/link3', 'path/to/directory/link4']
        if content[0] in content_list:
            new_content = []
            for cont_i in content_list:
                if cont_i != content[0]:
                    if cont_i == content[1]:
                        return -311     # Элемент уже существует с таким названием
                    else:
                        new_content.append(cont_i)
                else:
                    if cont_i == content[1]:
                        return -311     # Элемент уже существует с таким названием
                    else:
                        if content[1] != "":
                            new_content.append(content[1])  # Добавляет элемент, вместо того, который был

            print("replace_data_wMDSDF (new_content)", new_content)
            if tag == "":
                self.DSDocFile.write_file({"Directory": {tag_level_name: new_content}}, safeMode=True)
                return 31
            else:
                self.DSDocFile.write_file({"Directory": {tag_level_name: {tag: new_content}}}, safeMode=True)
                return 32   # Записан в файл под tag
        else:
            return -312     # Элемент не найден

    def writeMetadataFSDocFile(self, operation_name, level_name_tag, target_name_tag, content, file_id="0"):
        """
        :param operation_name: "AddType" (content useless), "RemoveType", "AddFile", "RemoveFile", "UpdateFile", "UpdateFileDetails"
        :param level_name_tag: "Files", "File", "FileDetails"
        :param target_name_tag: "SystemFiles", "UserFiles", "NonIndexedFiles"
        :param content:
        :param file_id:
        :return:
        """
        self.content = {"DirName": "", "DetailName": "",
                        "FileDetails": {"Description": "", "Priority": "", "FilesLinks": [], "FileSize": "",
                                        "CreatedAt": "", "ModifiedAt": ""}}
        self.content_non_indexed_file = {"DirName": "", "DetailName": ""}

        if operation_name == "AddType":
            try:
                if level_name_tag == "Files" and target_name_tag[-5:] == "Files":
                    self.FSDocFile.write_file({level_name_tag: {target_name_tag: {file_id: self.content}}},
                                              safeMode=True)
                    return 0
                else:
                    return -1
            except IndexError:
                return -2

        elif operation_name == "RemoveType":
            if level_name_tag == "Files":
                try:
                    for file_type in self.readMetadataSDocFile("Files", "Files", ""):
                        print(file_type)
                except KeyError as e:
                    e = str(e)
                    files_types = ast.literal_eval(e[28:-2])
                    for type_file in files_types:
                        if type_file == target_name_tag:
                            datafile = self.FSDocFile.read_file()[1]
                            del datafile["Files"][type_file]
                            self.FSDocFile.write_file(datafile)
                            return 0
                    return -1
            else:
                return -1
        elif operation_name == "AddFile":
            if level_name_tag == "Files":
                print('Надо сделать приём без file_id != 0, и возвращать id созданного файла')
                if file_id != "0":
                    def files_test(d_file_id, d_files):
                        for d_file in d_files:
                            if d_file == d_file_id:
                                return -1
                            return 0

                    if target_name_tag != "NonIndexedFiles":
                        try:
                            files = list(self.readMetadataSDocFile("Files", "Files", target_name_tag).keys())
                            if files_test(file_id, files) == 0:
                                self.FSDocFile.write_file({level_name_tag: {target_name_tag: {file_id: self.content}}},
                                                          safeMode=True)
                                return 0
                            else:
                                return -1
                        except KeyError:
                            return -2
                    elif target_name_tag == "NonIndexedFiles":
                        files = list(self.readMetadataSDocFile("Files", "Files", "NonIndexedFiles").keys())
                        files_test(file_id, files)
                        self.FSDocFile.write_file(
                            {level_name_tag: {target_name_tag: {file_id: self.content_non_indexed_file}}},
                            safeMode=True)
                        return 0
                    else:
                        return -1
                else:
                    return -1
            else:
                return -1
        elif operation_name == "RemoveFile":
            def check_and_del_file(d_file_id, d_filedata, d_target_name_tag):
                try:
                    del d_filedata["Files"][d_target_name_tag][d_file_id]
                    self.FSDocFile.write_file(d_filedata)
                    return 0
                except KeyError:
                    return -2

            if level_name_tag == "Files":
                filedata = self.FSDocFile.read_file()[1]
                if file_id != "0":
                    return check_and_del_file(file_id, filedata, target_name_tag)
                else:
                    return -1
            else:
                return -1
        elif operation_name == "UpdateFile":
            if type(content) is list:
                if file_id != 0:
                    if level_name_tag != "FileDetails":
                        try:
                            filedata = self.FSDocFile.read_file()[1]
                            check_data = filedata["Files"][target_name_tag][file_id]
                            print(check_data)
                            self.FSDocFile.write_file({"Files": {target_name_tag: {file_id: {content[0]: content[1]}}}}, safeMode=True)
                            return 0
                        except KeyError:
                            return -2
                    else:
                        return -1
                else:
                    return -1
            else:
                raise ValueError("Ожидался list-список, с двумя значениями [target_tag: content]")
        elif operation_name == "UpdateFileDetails":
            if file_id != 0:
                try:
                    filedata = self.FSDocFile.read_file()[1]
                    check_data = filedata["Files"][level_name_tag][file_id]["FileDetails"][target_name_tag]
                    filedata = None
                    self.FSDocFile.write_file(
                        {"Files": {level_name_tag: {file_id: {"FileDetails": {target_name_tag: content}}}}},
                        safeMode=True)
                    return 0
                except KeyError as e:
                    if e == "FileDetails":
                        raise KeyError("Файлы не индексированы")
                    return -2
        else:
            return -1

    def removeSubdirMetadataDSDocFile(self, tag_level_name, SdN="0"):
        """
        :param tag_level_name:
        :param SdN: int or str (SdN or DetailName)
        :return: -1 = Элемент не найден. 1 = найден и удалён.
        """
        file_data = self.DSDocFile.read_file()[1]
        SdNs = file_data["Directory"][tag_level_name]

        try:
            int(SdN)
        except ValueError:
            for SdNi in SdNs:
                if SdNs[SdNi]["DetailName"] == SdN:
                    del file_data["Directory"][tag_level_name][SdNi]
                    self.DSDocFile.write_file(file_data)
                    return 1
            return -1
        if tag_level_name == "SubdirectoryInfo" and SdN != "0":
            for key in SdNs.keys():
                if key == SdN:
                    del file_data["Directory"][tag_level_name][key]
                    self.DSDocFile.write_file(file_data)
                    return 1
            return -1
        elif tag_level_name == "SubdirectoryNonIndex" and SdN != "0":
            SdNi = file_data["Directory"][tag_level_name]
            data_list = []
            check_element = 0
            for i in SdNi:
                if i == SdN:
                    check_element = 1
                else:
                    data_list.append(i)
            if check_element == 0:
                return -1
            else:
                self.DSDocFile.write_file({"Directory": {tag_level_name: data_list}}, safeMode=True)
                return 2
        else:
            return -2

    def deleteDSDocFile(self):
        self.DSDocFile.delete_file()

    def deleteFSDocFile(self):
        self.FSDocFile.delete_file()
