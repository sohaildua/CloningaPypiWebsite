import sqlalchemy
import datetime

from pypi_org.data.modelbase import sqlAlchemyBase


class Maintainer(sqlAlchemyBase):
    __tablename__ = 'maintainers'

    user_id = sqlalchemy.Column(sqlalchemy.BigInteger,primary_key=True)
    package_id = sqlalchemy.Column(sqlalchemy.String,primary_key=True)
