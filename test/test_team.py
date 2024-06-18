import unittest
from flask import current_app
from app import create_app, db
from app.models.team import Team
from app.services.team_services import TeamService

service = TeamService()

class TeamTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)

    def test_user(self):
        team = Team()  
        team.name = "Los Pumitas" 
        self.assertEqual(team.name, "Los Pumitas")

    def test_create_team(self):
        team = self.__create_team()
        self.assertGreaterEqual(team.id, 1)

    def __create_team(self):
        team = Team()
        team.name="Los Pumitas"
        team.sport="Rugby"
        team.league="Unión Argentina de Rugby"
        service.create(team)
        return team

    def test_find_by_id(self):
        _ = self.__createteam()
        team = service.find_by_id(1)
        self.assertIsNotNone(team) 
        self.assertEqual(team.name, "nameExampleTest")
        self.assertEqual(team.surname, "surnameExampleTest")
        self.assertEqual(team.email, "emailexample@test.com")
        

    def test_find_all(self):
        _ = self.__createteam()
        teams = service.find_all()
        self.assertGreaterEqual(len(teams), 1)

    def test_update(self):
        team=self.__createteam()
        team.name = "nameUpdateTest"
        team.surname = "surnameUpdateTest"
        team.email = "emailupdate@test.com"
        team.password = "passwordUpdateTest"
        service.update(team, 1)
        result = service.find_by_id(1)
        self.assertEqual(result.name, team.name)
        self.assertEqual(result.surname, team.surname)
        self.assertEqual(result.email, team.email)
        self.assertEqual(result.password, team.password)

    def test_delete(self):
        _ = self.__createteam()
        service.delete(1)
        teams = service.find_all()
        self.assertEqual(len(teams), 0)

if __name__ == '_main_':
    unittest.main()