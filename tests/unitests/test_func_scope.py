import pytest
from sqlalchemy import text


@pytest.mark.asyncio(loop_scope='function')
async def test_unitest_dummy() -> None:
    assert True


@pytest.mark.asyncio(loop_scope='function')
async def test_unitest_session(session) -> None:
    result = await session.execute(text('SELECT 1'))
    row = result.scalar()
    print(f'Database connection is working, result: {row}')
    assert True


@pytest.mark.asyncio(loop_scope='function')
async def test_unitest_session2(session) -> None:
    result = await session.execute(text('SELECT 1'))
    row = result.scalar()
    print(f'Database connection is working, result: {row}')
    assert True
