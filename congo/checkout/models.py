from congo.database import PkModel, reference_col, relationship


class Checkout(PkModel):
    __tablename__ = "checkout"
    cart_id = reference_col("carts", nullable=True)
    carts = relationship("Cart", backref="checkouts")

    book_id = reference_col("book", nullable=True)
    book = relationship("Book", backref="checkouts")

    def __repr__(self):
        return f"<Checkout(id:{self.id}, user_id:{self.cart_id}, book_id:{self.book_id}>"
