
class MetadataService:
    meta_tags = {
        "Type": [
            {
                "Directory": {"level_1": ["Dirname", "Description", "Details", "SubdirectoryInfo", "SubdirectoryNonIndex"],
                              "level_2": [["DirectoryPath", "DetailName", "Priority", "DirLinks", "TotalSize", "FileCount", "CreatedAt", "ModifiedAt"], ["SdN"]],
                              "level_3": ["Dirname", "DetailName", "DocFile"]}
            },
            {
                "Files": {"level_1": ["SystemFiles", "UserFiles", "NonIndexedFiles"],
                          "level_2": ["FileIDs"],
                          "level_3": ["DirName", "DetailName", "FileDetails"],
                          "level_4": ["Description", "Priority", "FilesLinks", "FileSize", "CreatedAt", "ModifiedAt"]},
            }
        ]
    }

    def get_tag(self, tag_type: str, tag_level: str):
        tag = self.meta_tags["Type"]
        if tag_type == "Directory":
            return tag[0][tag_type]["level_"+tag_level]
        elif tag_type == "Files":
            return tag[1][tag_type]["level_" + tag_level]
