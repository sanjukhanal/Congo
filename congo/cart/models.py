from congo.database import PkModel, reference_col, relationship, Column
from congo.extensions import db


class Cart(PkModel):
    __tablename__ = "carts"
    user_id = reference_col("users", nullable=True)
    user = relationship("User", backref="carts")
    is_submitted = Column(db.Boolean(), default=False, nullable=False)

    created_on = Column(db.DateTime, server_default=db.func.now())
    updated_on = Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return f"<Cart({self.id}, {self.user_id}>"
