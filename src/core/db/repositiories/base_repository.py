import abc

from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository(abc.ABC):
    def __init__(self, session: AsyncSession):
        self.session = session
