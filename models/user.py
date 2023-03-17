from sqlalchemy import Column, Integer, String

from data_base.dbcore import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    full_name = Column(String, nullable=True)
