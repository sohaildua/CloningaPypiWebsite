import sqlalchemy
import datetime

from pypi_org.data.modelbase import sqlAlchemyBase


class License(sqlAlchemyBase):
    __tablename__ = 'licenses'

    id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    description = sqlalchemy.Column(sqlalchemy.String)
