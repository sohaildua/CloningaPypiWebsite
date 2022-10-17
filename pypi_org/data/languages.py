import sqlalchemy
import datetime

from pypi_org.data.modelbase import sqlAlchemyBase


class ProgrammingLanguage(sqlAlchemyBase):
    __tablename__ = 'languages'

    id = sqlalchemy.Column(sqlalchemy.BigInteger,primary_key=True,autoincrement=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    description = sqlalchemy.Column(sqlalchemy.String)
