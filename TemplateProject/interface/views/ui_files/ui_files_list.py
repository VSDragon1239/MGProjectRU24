from MGProjectRU25.Project.project_settings import UI_DIR, UIS_DIRS, PY_UIS_DIRS


UITypes = []
PYUITypes = []

for ui_dir in UIS_DIRS:
    UITypes.append(UI_DIR+ui_dir+'.ui')
    print("===================  ", UITypes)

for py_ui_dir in PY_UIS_DIRS:
    PYUITypes.append(UI_DIR+py_ui_dir+'.py')
