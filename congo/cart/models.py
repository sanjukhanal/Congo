from congo.database import PkModel, reference_col, relationship, Column
from congo.extensions import db


class Cart(PkModel):
    __tablename__ = "carts"
    user_id = reference_col("users", nullable=True)
    user = relationship("User", backref="carts")
    is_submitted = Column(db.Boolean())

    def __repr__(self):
        return f"<Cart({self.id}, {self.user_id}>"
