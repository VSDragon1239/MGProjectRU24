from RecognizingRU24.Project.settings import PROJECT_ROOT
from TemplateProject.core.services.file_service import FileService


class Manager:
    data = None

    def __init__(self, name: str, fe='json'):
        self.FSFile = FileService(str(PROJECT_ROOT), name, fe)
        self.init_FSFile()

    def create_FSFile(self, i=0):
        if not self.FSFile.file_exists():
            self.FSFile.create_file(self.data)
        if i == 0:
            self.init_FSFile()

    def init_FSFile(self):
        try:
            data = self.FSFile.read_file()
            if data:
                self.load_data(data[1])
            else:
                self.FSFile.write_file(self.data)
        except FileNotFoundError:
            self.create_FSFile(1)

    def safe_file(self):
        self.FSFile.write_file(self.data)

    def load_data(self, data):
        self.data = data
