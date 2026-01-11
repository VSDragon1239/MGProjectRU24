# def get_template_main_data():
#     return {
#         "MGProjectRU25": {
#             "SystemData": {
#                 "SystemName": "Название системы",
#                 "Drives": [
#                     {
#                         "Drive": "C:/",
#                         "DriveID": "Ид диска",
#                         "DrivePhysicName": "Физическое название диска",
#                         "UseType": "main"
#                     }
#                 ]
#             },
#             "StructureData": {
#                 "GlobalProjectsData": [
#                     {
#                         "id_GlobalProject": 1,
#                         "GlobalProjectEnName": "GlobalReversionVirtualization",
#                         "GlobalProjectSlugName": "GRV",
#                         "GlobalProjectRuName": "Глобальная Реверсия Виртуализации",
#
#                         "Projects": [
#                             {
#                                 "id_Project": 1,
#                                 "ProjectEnName": "",
#                                 "ProjectSlugName": "",
#                                 "ProjectRuName": "",
#                             },
#                         ]
#                     },
#                     {
#                         "id_GlobalProject": 2,
#                         "GlobalProjectEnName": "GlobalReversionReality",
#                         "GlobalProjectSlugName": "GRR",
#                         "GlobalProjectRuName": "Глобальная Реверсия Реальности",
#
#                         "Projects": [
#                             {
#                                 "id_Project": 1,
#                                 "ProjectEnName": "",
#                                 "ProjectSlugName": "",
#                                 "ProjectRuName": "",
#                             },
#                         ]
#                     },
#                     {
#                         "id_GlobalProject": 3,
#                         "GlobalProjectEnName": "GlobalReversionProgram",
#                         "GlobalProjectSlugName": "GRP",
#                         "GlobalProjectRuName": "Глобальная Реверсия Программ",
#
#                         "Projects": [
#                             {
#                                 "id_Project": 1,
#                                 "ProjectEnName": "",
#                                 "ProjectSlugName": "",
#                                 "ProjectRuName": "",
#                             },
#                         ]
#                     },
#                     {
#                         "id_GlobalProject": 4,
#                         "GlobalProjectEnName": "GlobalReversionScience",
#                         "GlobalProjectSlugName": "GRS",
#                         "GlobalProjectRuName": "Глобальная Реверсия Науки",
#
#                         "Projects": [
#                             {
#                                 "id_Project": 1,
#                                 "ProjectEnName": "",
#                                 "ProjectSlugName": "",
#                                 "ProjectRuName": "",
#                             },
#                         ]
#                     }
#                 ],
#             }
#         }
#     }



STRUCTURE = {
    "MGProjectRU25": {
        "SystemData": [
            {
                "SystemName": str,
                "Drives": []
            }
        ],
        "StructureData": {
            "GlobalProjectsData": []
        }
    }
}

PROJECTS = {
    "StructureData": {
        "GlobalProjectsData": []
    }
}

# PROJECTS_VISUAL: list = PROJECTS["StructureData"]["GlobalProjectsData"]
PROJECTS_VISUAL = {
    "GlobalProjectsData": []
}


def get_main_modules():
    return {
        "Modules": [
            {
                "Name": "GMSStorageFilesModule",
                "Directory": "1",
                "SubDirectories": [
                    {
                        "Name": "ProjectsData",
                        "Directory": "1",
                    },
                    {
                        "Name": "MemoryData",
                        "Directory": "2",
                    },
                    {
                        "Name": "AppData",
                        "Directory": "3",
                    },
                    {
                        "Name": "Applications",
                        "Directory": "4",
                    },
                ],
            },
            {
                "Name": "GMSControlDataModule",
                "Directory": "2",
                "SubDirectories": [
                    {
                        "Name": "ProjectsData",
                        "Directory": "1",
                    },
                    {
                        "Name": "MemoryData",
                        "Directory": "2",
                    },
                    {
                        "Name": "AppData",
                        "Directory": "3",
                    },
                    {
                        "Name": "Applications",
                        "Directory": "4",
                    },
                ],
            },
            {
                "Name": "GMSServerFilesModule",
                "Directory": "3",
                "SubDirectories": [
                    {
                        "Name": "ServerData",
                        "Directory": "1",
                    },
                ],
            },
        ]
    }


def get_mirror_module():
    return {
        "Name": "GMSControlDataModule",
        "Directory": "2",
        "SubDirectories": [
            {
                "Name": "ProjectsData",
                "Directory": "1",
            },
            {
                "Name": "MemoryData",
                "Directory": "2",
            },
            {
                "Name": "AppData",
                "Directory": "3",
            },
            {
                "Name": "Applications",
                "Directory": "4",
            },
        ],
    },

# def _create_data_global_project(global_project_data: list):
#     global_project_id = len(get_template_main_data()["MGProjectRU25"]["StructureData"]["GlobalProjectsData"]) + 1
#     return {
#         "id_GlobalProject": global_project_id,
#         "GlobalProjectEnName": global_project_data[0],
#         "GlobalProjectSlugName": global_project_data[1],
#         "GlobalProjectRuName": global_project_data[2],
#         "Projects": []
#     }
#
#
# def _append_new_global_project(global_project_data: dict):
#     fullData = get_template_main_data()
#     fullData["MGProjectRU25"]["StructureData"]["GlobalProjectsData"].append(global_project_data)
#     return fullData
#
#
# def create_new_global_project(global_project_data: list):
#     data = _create_data_global_project(global_project_data)
#     return _append_new_global_project(data)


# def _create_data_project(global_project_name, project_name, project_data: list):
#     for global_project in get_template_main_data()["MGProjectRU25"]["StructureData"]["GlobalProjectsData"]:
#         if global_project["GlobalProjectEnName"] == global_project_name:
#             global_project_id = global_project["id_GlobalProject"]
#             last_project_id = global_project["Projects"][-1]["id_Project"] + 1
#             for project in global_project["Projects"]:
#                 if project["ProjectEnName"] == project_name:
#                     return -1
#             new_project = {
#                 "id_Project": last_project_id,
#                 "ProjectEnName": project_data[0],
#                 "ProjectSlugName": project_data[1],
#                 "ProjectRuName": project_data[2],
#             }
#             return global_project_id, new_project


# def _append_new_project(global_project_id, project_data: dict):
#     fullData = get_template_main_data()
#     fullData["MGProjectRU25"]["StructureData"]["GlobalProjectsData"][global_project_id]["Projects"].append(project_data)
#     return fullData


# def create_project(global_project_name, project_name, project_data: list):
#     data = _create_data_project(global_project_name, project_name, project_data)
#     select_global_project_id = data[0]
#     project = data[1]
#     return _append_new_project(select_global_project_id, project)
#
#
# def get_global_project_data(global_project_name):
#     for global_project in get_template_main_data()["MGProjectRU25"]["StructureData"]["GlobalProjectsData"]:
#         if global_project["GlobalProjectEnName"] == global_project_name:
#             return global_project
#
#
# def get_project_data(global_project_name, project_name):
#     for global_project in get_template_main_data()["MGProjectRU25"]["StructureData"]["GlobalProjectsData"]:
#         if global_project["GlobalProjectEnName"] == global_project_name:
#             for project in global_project["Projects"]:
#                 if project["ProjectEnName"] == project_name:
#                     return project
