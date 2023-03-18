from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, create_engine, exists

from settings import config
from data_base.dbcore import Base
from models.user import User


class DBManager:
    def __init__(self):
        self.engine = create_engine(
            config.DATABASE_URL,
            echo=False  # будет показывать SQL запросы
        )
        self.session = sessionmaker(
            self.engine,
            expire_on_commit=False
        )
        Base.metadata.create_all(self.engine)

    def add_user(self, user_id: int,
                 username: str,
                 first_name: str,
                 full_name: str):
        """
        Добавляет пользователя
        """
        result = self.get_user(user_id=user_id)
        if not result:
            new_user = User(user_id=user_id,
                            username=username,
                            first_name=first_name,
                            full_name=full_name)
            with self.session() as session:
                session.add(new_user)
                session.commit()

    def get_user(self, user_id: int):
        """
        Возвращает id пользователя
        """
        with self.session() as session:
            result = session.execute(
                select(User).filter_by(user_id=user_id))
            return result.scalars().all()
