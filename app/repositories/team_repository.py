from app import db
from app.models import Team
from .repository_base import Create, Read, Update, Delete


class TeamRepository(Create, Read, Update, Delete):
        
    def __init__(self):
            self.__model = Team

    def create(self, model: Team):
        db.session.add(model)
        db.session.commit()
        return model


    def find_all(self):
        try:
            teams = db.session.query(self.__model).all()
            return teams
        except Exception as e:
            raise Exception('Error a obtener la lista de equipos'  + str(e))
    

    def find_by_id(self, id):
        try:
            entity = db.session.query(self.__model).filter(self.__model.id == id).one()
            return entity
        except Exception as e:
            raise Exception('Error a obtener equipo por id' + str(e))


    def update(self, entity: Team):
            db.session.merge(entity)
            db.session.commit()
            return entity


    def delete(self, team_id) -> bool:
        team = Team.query.get(team_id)
        if team:
            db.session.delete(team)
            db.session.commit()
            return True
        return False

    def search(self, lease_min, lease_max):
        return db.session.query(self.__model).filter(self.__model.lease.between(lease_min, lease_max)).all()
    
        