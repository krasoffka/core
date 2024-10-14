from sqlalchemy.orm import Mapped

from core.db.orm_models.base import BaseTableORM


class TestORM(BaseTableORM):
    __tablename__ = 'test'
    id: Mapped[int]
