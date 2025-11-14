from uuid import UUID

from sqlalchemy import String, select
from sqlalchemy.orm import Mapped, mapped_column, relationship, selectinload

from database.base import db, CreatedModel


class User(CreatedModel):
    email: Mapped[str] = mapped_column(String, unique=True)
    username: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String, nullable=True)
    products = relationship("Product", back_populates="user")
    support_messages = relationship("SupportMessage", back_populates="user")


    @classmethod
    async def get_by_email(cls, email: str):
        query = select(cls).where(cls.email == email)
        return (await db.execute(query)).scalar()

    @classmethod
    async def get_user_with_products(cls, user_id: UUID):
        result = await db.execute(
            select(cls)
            .where(cls.id == user_id)
            .options(selectinload(cls.products))
        )
        return result.scalar()
