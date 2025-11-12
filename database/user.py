
from sqlalchemy import String , select
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Model
from database.base import db


class User(Model):
    email: Mapped[str] = mapped_column(String , unique=True)
    username: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String, nullable=True)
    products = relationship("Product", back_populates="user")

    @classmethod
    async def get_by_email(cls , email):
        query = select(cls).where(cls.email == email)
        return (await db.execute(query)).scalar()