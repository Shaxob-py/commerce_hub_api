from enum import Enum

from sqlalchemy import Float, ForeignKey, String, Numeric, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Model


class Category(Model):
    icon: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    products = relationship("Product", back_populates="category")


class Product(Model):
    class Valute(Enum):
        SUM = 'SUM'
        RUB = 'RUB'
        USD = 'USD'

    name: Mapped[str]
    price: Mapped[float] = mapped_column(Numeric(12, 0))
    description: Mapped[str]
    photo_url: Mapped[str]
    lat: Mapped[float] = mapped_column(Float)
    lng: Mapped[float] = mapped_column(Float)
    currency: Mapped[Valute] = mapped_column(SQLEnum(Valute))

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE")
    )

    user: Mapped["User"] = relationship("User", back_populates="products")

    category_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("categories.id", ondelete="CASCADE")
    )

    category: Mapped["Category"] = relationship("Category", back_populates="products")
