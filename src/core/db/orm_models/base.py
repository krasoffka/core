from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, registry
from sqlalchemy.orm.decl_api import DeclarativeMeta

mapper_registry = registry(
    metadata=sa.MetaData(
        naming_convention={
            'column_names': lambda constraint, table: '__'.join(
                [column.name for column in constraint.columns.values()]  # type: ignore
            ),
            'ix': 'ix__%(table_name)s__%(column_names)s',
            'uq': 'uq__%(table_name)s__%(column_names)s',
            'ck': 'ck__%(table_name)s__%(constraint_name)s',
            'fk': 'fk__%(table_name)s__%(column_names)s__%(referred_table_name)s',
            'pk': 'pk__%(table_name)s',
        }
    )
)


class BaseTableORM(metaclass=DeclarativeMeta):
    __abstract__ = True
    registry = mapper_registry
    metadata = mapper_registry.metadata

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(server_default=sa.func.now())
    updated_at: Mapped[datetime] = mapped_column(onupdate=sa.func.now(), server_default=sa.func.now())

    def __str__(self):
        obj_id = getattr(self, 'id')
        return f'({self.__class__.__name__} {obj_id=})'

    def __repr__(self):
        return self.__str__()
