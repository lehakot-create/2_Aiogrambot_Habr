from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

from settings import config
from data_base.dbcore import Base
from models.user import User


class DBManager:
    def __init__(self):
        self.engine = create_async_engine(
            config.DATABASE_URL,
            echo=True  # будет показывать SQL запросы
        )
        async_session = sessionmaker(
            self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )
        self._asession = async_session()

    async def init_models(self):
        """
        Очистка и воссоздание таблиц
        """
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.meta_data.create_all)

    def add_user(self, user_id: int,
                 username: str,
                 first_name: str,
                 full_name: str):
        """
        Добавляет id пользователя
        """
        new_user = User(user_id=user_id,
                        username=username,
                        first_name=first_name,
                        full_name=full_name)
        self._asession.add(new_user)
        self._asession.commit()
        self._asession.close()
        return new_user

    async def get_user(self, user_id: int):
        """
        Возвращает id пользователя
        """
        result = await self._asession.execute(
            select(User).filter_by(user_id=user_id))
        self._asession.close()
        return result.scalars().all()
