from enum import Enum
from uuid import UUID

from sqlalchemy import Enum as SQLEnum
from sqlalchemy import String, select
from sqlalchemy.orm import Mapped, mapped_column, relationship, selectinload

from database.base import db, CreatedModel


class User(CreatedModel):
    class Role(Enum):
        ADMIN = 'ADMIN'
        USER = 'USER'

    email: Mapped[str] = mapped_column(String, unique=True)
    username: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String, nullable=True)
    products = relationship("Product", back_populates="user")
    support_messages = relationship("SupportMessage", back_populates="user")
    comments = relationship("Comment", back_populates="user")
    role: Mapped[Role] = mapped_column(
        SQLEnum(Role, name="role"),
        default=Role.USER,

    )

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
