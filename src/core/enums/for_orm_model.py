from enum import Enum

"""
вынес enum для sqlalchemy в отдельный модуль, потому что есть проблемы с миграциями от алембика,                 # noqa
надо аккуратно править существующие enum, и смотреть за миграциями, возможно надо будет добавить                 # noqa
пакет(alembic-postgresql-enum) или дописывать миграции руками
"""


class EntityType(Enum):
    UNKNOWN = 'unknown'
    MID = 'mid'
    MERCHANT = 'merchant'
