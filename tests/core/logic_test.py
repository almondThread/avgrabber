import unittest
from unittest.mock import patch, Mock, MagicMock, call
from avgrabber.core import new_project, list_projects, list_updates, update_project
from avgrabber.persistence.model import Ad, Update, Project
from avgrabber.persistence.model import DBSession, Base
from datetime import datetime

class TestCoreLogic(unittest.TestCase):

    def setUp(self):
        Base.metadata.create_all()

    def tearDown(self):
        Base.metadata.drop_all()


    def test_new_project(self):
        name = 'test'
        query = 'PS4'.split(',')

        # Object creation
        p = new_project(name, query)
        self.assertIsInstance(p, Project)

        # Correct db representation
        stored_project = DBSession().query(Project).first()
        self.assertEqual(p, stored_project)

        # Correct fields filling
        self.assertEqual(stored_project.name, name)
        self.assertEqual(stored_project.query, query)
        self.assertIsNotNone(stored_project.at)

    def test_list_projects(self):
        name1 = 'test1'
        query1 = 'PS4_1'.split(',')
        DBSession().add(Project(name=name1, query=query1))

        name2 = 'test2'
        query2 = 'PS4_2'.split(',')
        DBSession().add(Project(name=name2, query=query2))
        DBSession().commit()

        projects = list_projects()
        self.assertEqual(len(projects), 2)

    def test_list_updates(self):
        # First project
        name1 = 'test1'
        query1 = 'PS4_1'.split(',')
        p1 = Project(name=name1, query=query1)
        DBSession().add(p1)
        update1 = Update(project=p1, at=datetime.now())
        DBSession().add(update1)
        update2 = Update(project=p1, at=datetime.now())
        DBSession().add(update2)

        # Second project
        name2 = 'test2'
        query2 = 'PS4_2'.split(',')
        DBSession().add(Project(name=name2, query=query2))

        DBSession().commit()

        # Correct update listing
        stored_updates1 = list_updates(name1)
        stored_updates2 = list_updates(name2)
        self.assertEqual(len(stored_updates1), 2)
        self.assertEqual(len(stored_updates2), 0)  # Project has never been updated

        #@patch('avgrabber.core.logic.grabber.search')
        #def test_update_project(search):
        #    search.return_value = {}

       #@patch('avgrabber.core.logic.grabber.search')
       #def test_resolve_state():



if __name__ == '__main__':
    unittest.main()