from enum import Enum

from sqlalchemy import ForeignKey, Numeric, Enum as SQLEnum, BigInteger, select, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import CreatedModel, db


class Product(CreatedModel):
    class Valute(Enum):
        SUM = 'SUM'
        RUB = 'RUB'
        USD = 'USD'

    name: Mapped[str]
    price: Mapped[float] = mapped_column(Numeric(12, 0))
    description: Mapped[str]
    photo_url: Mapped[str]
    location: Mapped[str] = mapped_column(String)
    currency: Mapped[Valute] = mapped_column(SQLEnum(Valute))
    views: Mapped[int] = mapped_column(BigInteger)
    comments = relationship("Comment", back_populates="product")


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

    @classmethod
    async def get_products_by_category(cls, category_id, limit: int = 10, offset: int = 0):
        query = (
            select(Product)
            .where(Product.category_id == category_id)
            .offset(offset)
            .limit(limit)
        )
        result = await db.execute(query)
        products = result.scalars().all()

        return products
