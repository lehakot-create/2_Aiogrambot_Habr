from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from data_base.dbcore import Base


user_themes = Table(
    'association',
    Base.metadata,
    Column('id_user', Integer(), ForeignKey('users.id')),
    Column('id_themes', Integer(), ForeignKey('themes.id')))


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_telegram_id = Column(Integer, index=True)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    full_name = Column(String, nullable=True)
    theme = relationship('Themes',
                         secondary=user_themes,
                         backref='users',
                         lazy=True)


class Themes(Base):
    __tablename__ = 'themes'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=True)
    url = Column(String, nullable=True)
