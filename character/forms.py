from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired


class CharacterForm(FlaskForm):
    id = IntegerField("Identificador", validators=[DataRequired()])
    name = StringField("Nome do Personagem", validators=[DataRequired()])
    gender = StringField("Gênero")
    status = StringField("Status")
    species = StringField("Especie")
