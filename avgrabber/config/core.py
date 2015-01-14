from os.path import dirname, join, normpath
import os



class Config:

    ENV_VAR = 'AVG_CONFIG'
    DEFAULT_CONFIG = 'development'

    def load_settings(self, settings_name):
        klass = globals()[settings_name.capitalize()]
        self.settings = klass()

    def get(self, name):
        return getattr(self._get_settings(), name)

    def set(self, name, value):
        setattr(self._get_settings(), name, value)

    def _get_settings(self):
        if not hasattr(self, 'settings') or not self.settings:

            if Config.ENV_VAR in os.environ:
                self.load_settings(os.environ[Config.ENV_VAR])
            else:
                self.load_settings(Config.DEFAULT_CONFIG)

        return self.settings


config = Config()


def get_project_dir():
    import avgrabber
    return normpath(join(dirname(avgrabber.__file__), '..'))

class Settings:
    DEBUG = False

    # RESOURCES
    PROJECT_DIR = get_project_dir()
    # PERSISTENCE
    PERSISTENCE_SCHEMA = 'sqlite:///' + join(PROJECT_DIR, 'db.sqlite')


class Production(Settings):
    pass


class Development(Settings):
    pass


class Test(Settings):
    # PERSISTENCE
    PERSISTENCE_SCHEMA = 'sqlite:///:memory:'

#test
#print(config.get('PERSISTENCE_SCHEMA'))

