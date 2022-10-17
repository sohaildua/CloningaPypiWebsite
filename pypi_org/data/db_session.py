import sqlalchemy as sa
import sqlalchemy.orm as orm

from sqlalchemy.orm import Session

from pypi_org.data.modelbase import sqlAlchemyBase

__factory = None


def global_init(db_file: str):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("you must specify the db file or missing db_file")

    conn_str = "sqlite:///" + db_file.strip()
    engine = sa.create_engine(conn_str, echo=True, connect_args={"check_same_thread": False})

    __factory = orm.sessionmaker(bind=engine)

    import pypi_org.data.__all_models
    sqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    session: Session = __factory()

    session.expire_on_commit = False

    return __factory()
