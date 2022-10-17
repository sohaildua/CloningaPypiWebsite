import sqlalchemy as sa
import sqlalchemy.orm as orm

from typing import List
import datetime
from pypi_org.data.modelbase import sqlAlchemyBase
from pypi_org.data.releases import Release


class Package(sqlAlchemyBase):
    __tablename__ = 'packages'

    id = sa.Column(sa.String, primary_key=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now)
    updated_date = sa.Column(sa.DateTime, default=datetime.datetime.now)
    summary = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String, nullable=True)

    homepage = sa.Column(sa.String)
    docs_url = sa.Column(sa.String)
    package_url = sa.Column(sa.String)

    author_name = sa.Column(sa.String)
    author_email = sa.Column(sa.String, index=True)

    license = sa.Column(sa.String, index=True)

    releases:List[Release] = orm.relationship("Release", order_by=[
        Release.minor_ver.desc(),
        Release.major_ver.desc(),
        Release.build_ver.desc()], back_populates="package")

    def __repr__(self) -> str:
        return '<Package {}>'.format(self.id)
