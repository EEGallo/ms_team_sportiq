from app.models.team import Team
from marshmallow import fields, Schema, post_load

class TeamSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    sport = fields.String(required=True)
    league = fields.String(required=True)

    @post_load
    def make_team(self, data, **kwargs):
        return Team(**data)