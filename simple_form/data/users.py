import datetime
import sqlalchemy
from simple_form.data.base_model import SqlAlchemyBase

class User(SqlAlchemyBase):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True,autoincrement=True)
    username = sqlalchemy.Column(sqlalchemy.String,nullable=False)
    password = sqlalchemy.Column(sqlalchemy.String,nullable=False)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
