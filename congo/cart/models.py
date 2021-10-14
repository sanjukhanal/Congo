from congo.database import PkModel, reference_col, relationship


class Cart(PkModel):
    __tablename__ = "carts"
    user_id = reference_col("users", nullable=True)
    user = relationship("User", backref="carts")

    def __repr__(self):
        return f"<Cart({self.id}, {self.user_id}>"