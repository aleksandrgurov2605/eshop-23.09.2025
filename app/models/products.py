from sqlalchemy import String, Boolean, Float, Integer, ForeignKey,text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    image_url: Mapped[str | None] = mapped_column(String(200), nullable=True)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)
    seller_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)  # New
    rating: Mapped[float] = mapped_column(Float, default=0.0, server_default=text('0'))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)



    category: Mapped["Category"] = relationship(back_populates="products")
    reviews: Mapped[list["Review"]] = relationship(back_populates="product")
    seller = relationship("User", back_populates="products")  # New

