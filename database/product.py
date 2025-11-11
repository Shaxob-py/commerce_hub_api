from sqlalchemy import Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Model, User


class Category(Model):
    icon: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    product = relationship("Product", back_populates="category")


class Product(Model):
    name: Mapped[str]
    price: Mapped[float]
    description: Mapped[str]
    lat: Mapped[float] = mapped_column(Float)
    lng: Mapped[float] = mapped_column(Float)

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE")
    )

    user: Mapped["User"] = relationship("User", back_populates="products")

    category_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE")
    )

    category: Mapped["Category"] = relationship("Category", back_populates="products")
