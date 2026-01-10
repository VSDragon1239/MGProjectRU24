from random import randint

from MGProjectRU25.App.StructureTools.Managers import Manager
from RecognizingRU24.App.router import CommandRouter
from RecognizingRU24.Project.settings import COMMAND_CONFIGURATION


class CommandManager(Manager):
    data = COMMAND_CONFIGURATION
    router = None

    def __init__(self):
        super().__init__("CommandsConfigurationFile")
        self.init_router()

    def init_router(self):
        print(self.data, type(self.data))
        self.router = CommandRouter(self.data, fuzzy_threshold=60)

    def exec_command(self, voice):
        try:
            result = self.router.handle(voice)
            print("OK:", result)
        except Exception as e:
            print("Ошибка:", e)
