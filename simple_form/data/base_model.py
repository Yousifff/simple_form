import sqlalchemy
import sqlalchemy.orm
from sqlalchemy.ext.declarative import declarative_base

SqlAlchemyBase = declarative_base()
from simple_form.data.users import  User


class DBsession:
    factory = None
    engine = None

    @staticmethod
    def db_init(db_file):
        if DBsession.factory:
            return

        if not db_file or not db_file.strip():
            raise Exception("db_file has to be provided")

        con_str = "sqlite:///" + db_file
        engine = sqlalchemy.create_engine(con_str,echo=False)
        DBsession.engine = engine
        DBsession.factory = sqlalchemy.orm.sessionmaker(bind=engine)
        SqlAlchemyBase.metadata.create_all(engine)