import sqlalchemy
import datetime
import sqlalchemy.orm as orm
from pypi_org.data.modelbase import sqlAlchemyBase


class Release(sqlAlchemyBase):
    __tablename__ = 'releases'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    major_ver = sqlalchemy.Column(sqlalchemy.BigInteger, index=True)
    minor_ver = sqlalchemy.Column(sqlalchemy.BigInteger, index=True)
    build_ver = sqlalchemy.Column(sqlalchemy.BigInteger, index=True)

    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    comment = sqlalchemy.Column(sqlalchemy.String)
    url = sqlalchemy.Column(sqlalchemy.String)
    size = sqlalchemy.Column(sqlalchemy.BigInteger)
    # table name in packages.id rest all are class name
    package_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("packages.id"))
    package = orm.relationship("Package")

    @property
    def version_text(self):
        return '{}.{}.{}'.format(self.major_ver, self.minor_ver, self.build_ver)
