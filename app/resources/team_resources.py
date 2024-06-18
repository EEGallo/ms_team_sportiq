from flask import jsonify, Blueprint, request
from app.services.team_services import TeamService
from app.models.response_message import ResponseBuilder
from app.mapping import ResponseSchema, TeamSchema
import random


team = Blueprint('team', __name__)
team_schema = TeamSchema()
response_schema = ResponseSchema()

"""
id: int ingresado por el team
return: json con los datos del team
"""

@team.route('/', methods=['GET'])
def index():
    resp = jsonify({"microservicio": "2", "status": "ok"})
    resp.status_code = random.choice([200, 404])
    return resp

@team.route('/compensation', methods=['GET'])
def compensation():
    resp = jsonify({"microservicio": "Compensation 2", "status": "ok"})
    resp.status_code = 200
    return resp


@team.route('/add', methods=['POST'])
def post_user():
    try:
        service = TeamService()
        team = team_schema.load(request.json)
        created_team = service.create(team)
        response = {"team": team_schema.dump(created_team)}
        return jsonify(response), 201
    except Exception as e:
        error_message = f"Error al agregar equipo: {str(e)}"
        return jsonify({"error": error_message}), 400


@team.route('/<int:id>', methods=['GET'])
def find(id):
    service = TeamService()
    team = service.find_by_id(id)

    if team:
        response_builder = ResponseBuilder()
        response_builder.add_message("Equipo encontrado").add_status_code(100).add_data(team_schema.dump(team))
        return jsonify(response_schema.dump(response_builder.build()))
    else:
        return jsonify({"error": "Equipo no encontrado"}), 404


@team.route('/all', methods=['GET'])
def find_all():
    service = TeamService()
    response_builder = ResponseBuilder()
    teams = service.find_all()
    teams_json = [team_schema.dump(team) for team in teams]
    response_builder.add_message("Equipos encontrados").add_status_code(100).add_data({'teams': teams_json})
    return response_schema.dump(response_builder.build())
  

@team.route('/update/<int:team_id>', methods=['PUT'])
def update_team(team_id):
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Datos de equipo no proporcionados"}), 400

        service = TeamService()
        updated_team = service.update(team_id, data)

        if updated_team:
            response_builder = ResponseBuilder()
            response_builder.add_message("Equipo actualizado con éxito").add_status_code(200).add_data(team_schema.dump(updated_team))
            return response_schema.dump(response_builder.build())

        return jsonify({"error": "El equipo no se pudo actualizar"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@team.route('/delete/<int:team_id>', methods=['DELETE'])
def delete_team(team_id):
    try:
        service = TeamService()
        deleted = service.delete(team_id)

        if deleted:
            return jsonify({"message": "Equipo eliminado con éxito", "status_code": 200}), 200

        return jsonify({"error": "Equipo no encontrado", "status_code": 404}), 404
    except Exception as e:
        return jsonify({"error": str(e), "status_code": 500}), 500