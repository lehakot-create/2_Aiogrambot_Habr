from sqlalchemy import Column, Integer, String

from data_base.dbcore import Base


class Themes(Base):
    __tablename__ = 'themes'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=True)
    url = Column(String, nullable=True)
