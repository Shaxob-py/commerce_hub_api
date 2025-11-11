from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Model


class User(Model):
    email: Mapped[str] = mapped_column(String , primary_key=True)
    username: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    product = relationship("Product", back_populates="user")


