import datetime
import sqlalchemy
from data.db_session import SqlAlchemyBase
from sqlalchemy import orm


class User(SqlAlchemyBase):
    __tablename__ = 'user'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=True)
    is_bot = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    first_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    username = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    language_code = sqlalchemy.Column(sqlalchemy.String, nullable=True)


    # news = orm.relationship("News", back_populates='user')
    def __repr__(self):
        return f"{self.name},{self.about},{self.email},{self.created_date}"