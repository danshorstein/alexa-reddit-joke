import sqlalchemy
from joke_fairy.data.modelbase import SqlAlchemyBase

class DbSessionFactory:

    @staticmethod
    def global_init(db_file):
        if not db_file:
            raise Exception('Specify a valid data file!')

        conn_str = 'sqlite:///' + db_file
        engine = sqlalchemy.create_engine(conn_str)
        SqlAlchemyBase.metadata.create_all(engine)
