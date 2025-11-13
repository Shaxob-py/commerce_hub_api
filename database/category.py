from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Model


class Category(Model):
    icon: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    products = relationship("Product", back_populates="category")
