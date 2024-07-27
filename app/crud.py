import uuid
from app.database.schema import UserData_tbl
from app.database.session import db_dependency
from sqlalchemy import select


class UserData:
    @classmethod
    def create_user(
        cls, *, name: str, age: int, address: str, db_conn: db_dependency
    ) -> uuid.UUID:
        model = UserData_tbl(id=uuid.uuid4(), name=name, age=age, address=address)
        db_conn.add(model)
        db_conn.commit()

        return model.id

    @classmethod
    def get_all_users(cls, db_conn: db_dependency):
        query = select(UserData_tbl)
        return db_conn.execute(query).scalars().all()


class TableData:
    @classmethod
    def create_table(cls, *, mongodb_conn):
        election_data = mongodb_conn.list_database_names()
        return election_data
