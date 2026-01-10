from PySide6.QtWidgets import QPushButton




class QtViewerObjects:
    view = None
    viewModel = None
    object = None
    objects = None
    lastObject = None
    objectsArray = None

    def __init__(self, View, ViewModel):
        self.initViewViewModel(View, ViewModel)

    def initViewViewModel(self, View, ViewModel):
        self.view = View
        self.viewModel = ViewModel

    def initObject(self, objectName, objectNameStr):
        self.object = objectNameStr
        self.objects = self.findObject(objectName)
        self.objectsArray = {}

    def findObject(self, objectName):
        return self.view.findChildren(objectName)

    def setObjectArray(self, className, startIndex=1):
        for index, object in enumerate(self.objects, start=startIndex):
            var_name = f"{self.object}{index}"  # Генерируем имя переменной, например, pushButton или stackedWidget
            self.objectsArray[var_name] = object  # Сохраняем объект в словарь
            self.lastObject = index
            print(f"{className}:   ", self.object + str(index), self.getObjectNameByIndex(index))

    def getObjectNameByIndex(self, index: int):
        ObjectName = self.objectsArray[f'{self.object}{index}'].objectName()
        return ObjectName

    def getObjectByIndex(self, index: int):
        return self.objectsArray[f'{self.object}{index}']

    def newObjectToArray(self, className, object):
        self.lastObject = self.lastObject + 1
        var_name = f"{self.object}{self.lastObject}"
        self.objectsArray[var_name] = object
        print(f"{className}:   ", self.object + str(self.lastObject), self.getObjectNameByIndex(self.lastObject))
        return self.lastObject

