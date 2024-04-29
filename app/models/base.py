from typing import Any

from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncAttrs, AsyncSession
from sqlalchemy.orm import declared_attr, DeclarativeBase
from starlette import status


class Base(AsyncAttrs, DeclarativeBase):
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()

    async def save_and_refresh(self, db_session: AsyncSession):
        """

        :param db_session:
        :return:
        """
        try:
            db_session.add(self)
            await db_session.commit()
            await db_session.refresh(self)
            return self
        except (SQLAlchemyError, HTTPException) as ex:
            await db_session.rollback()
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=repr(ex)
            ) from ex
        finally:
            await db_session.close()
