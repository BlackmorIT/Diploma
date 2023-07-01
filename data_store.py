# импорты
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session

from config import db_url_object


# схема БД
metadata = MetaData()
Base = declarative_base()
engine = create_engine(db_url_object)
class selected(Base):
    __tablename__ = 'selected'
    profile_id = sq.Column(sq.Integer, primary_key=True)
    worksheet_id = sq.Column(sq.Integer, primary_key=True)

class Tools(Base):
    __tablename__ = 'User'
    profile_id = sq.Column(sq.Integer, primary_key=True)
    worksheet_id = sq.Column(sq.Integer, primary_key=True)

# добавление записи в БД
def add_bd_user (engine, profile_id, worksheet_id):
    with Session(engine) as session:
        to_bd = Tools(profile_id=profile_id, worksheet_id=worksheet_id)
        session.add(to_bd)
        session.commit()

# извлечение записей из БД
def user_check(engine, profile_id, worksheet_id):
    with Session(engine) as session:
        bd_from = (session.query(Tools).filter(Tools.profile_id == profile_id, Tools.worksheet_id == worksheet_id).first()
            )
        return True if bd_from else False

if __name__ == '_main__':
    engine = create_engine(db_url_object)
    Base.metadata.create_all(engine)