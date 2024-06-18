from app.repositories import TeamRepository
from app import db
from sqlalchemy.orm.exc import NoResultFound

class TeamService():
    def __init__(self):
        self.__repository = TeamRepository()


    def create(self, entity):
        return self.__repository.create(entity)
    

    def find_all(self):
        try:
            teams = self.__repository.find_all()
            if teams:
                return teams
            else:
                return []
            
        except Exception as e:
            raise Exception('Error al obtener la lista de equipos' + str(e))

    
    def find_by_id(self, entity_id):
        try:
            entity = self.__repository.find_by_id(entity_id)
            if entity:
                return entity
            else:
                return None 
        except NoResultFound:
            return None
        except Exception as e:
            raise Exception('Error al obtener equipo por id: ' + str(e))


    
    def update(self, entity_id, updated_fields):
        try:
            team = self.__repository.find_by_id(entity_id)

            if team:
                for field, value in updated_fields.items():
                    setattr(team, field, value)

                db.session.commit()

            return team
        except Exception as e:
            raise Exception('Error al actualizar el equipo: ' + str(e))
    
    def delete(self, entity_id):
        return self.__repository.delete(entity_id) 