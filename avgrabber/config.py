import avgrabber
from os.path import dirname, join, normpath


# RESOURCES
PROJECT_DIR = normpath(dirname(avgrabber.__file__))

# PERSISTENCE
PERSISTENCE_SCHEMA = 'sqlite:///' + join(PROJECT_DIR, 'db.sqlite')
PERSISTENCE_SCHEMA_INMEMORY = 'sqlite:///:memory:'