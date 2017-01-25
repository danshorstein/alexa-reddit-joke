import sqlalchemy
from joke_fairy.data.modelbase import SqlAlchemyBase

class Joke(SqlAlchemyBase):
    __tablename__ = 'Joke'

    id = sqlalchemy.Column(sqlalchemy.Integer)
    subreddit = sqlalchemy.Column(sqlalchemy.String)
    title = sqlalchemy.Column(sqlalchemy.String)
    content = sqlalchemy.Column(sqlalchemy.String)
    score = sqlalchemy.Column(sqlalchemy.Integer)
    reddit_id = sqlalchemy.Column(sqlalchemy.String)
