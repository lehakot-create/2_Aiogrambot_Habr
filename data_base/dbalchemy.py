from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, create_engine
from sqlalchemy import update

from settings import config
from data_base.dbcore import Base
from models.user import User
from models.themes import Themes
from utils.parser_habr_themes import get_habr_themes


class DBManager:
    def __init__(self):
        self.engine = create_engine(
            config.DATABASE_URL,
            echo=False  # будет показывать SQL запросы
        )
        _session = sessionmaker(self.engine)
        self.session = _session()
        # Base.metadata.drop_all(self.engine)
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
            self.session.add(new_user)
            self.session.commit()
            self.close()

    def get_user(self, user_id: int):
        """
        Возвращает id пользователя
        """
        result = self.session.query(User).filter_by(user_id=user_id).one_or_none()
        return result

    def get_user_subscribe(self, user_id: int):
        """
        Возвращает подписки пользователя
        """
        result = self.session.query(User).filter_by(user_id=user_id).one_or_none()
        return result

    def get_all_themes(self):
        """
        Возвращает все темы
        """
        result = self.session.query(Themes).all()
        if not result:
            self.init_all_themes()  # вызываем инициализаю тем
            result = self.session.query(Themes).all()
        return result

    def init_all_themes(self):
        """
        получаем все темы с хабра и записываем в БД
        """
        all_themes = get_habr_themes()
        for theme in all_themes:
            obj = Themes(title=theme.get('title'),
                         url=theme.get('url'))
            self.session.add(obj)
        self.session.commit()
        self.close()

    def add_theme_to_my_subscribe(self, id_theme: int, user_id: int):
        """
        Добавляет id темы в подписку
        """
        user_theme = self.get_user_subscribe(user_id=user_id)
        if not user_theme:
            lst = []
            lst.append(id_theme)
            self.session.execute(
                update(User).where(User.user_id == user_id).values(
                    themes_id=lst))
            # self.session.commit()
            # self.close()

    def close(self):
        self.session.close()
