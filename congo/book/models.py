from congo.database import PkModel, Column
from congo.extensions import db


class Book(PkModel):
    __tablename__ = "book"
    primary_isbn10 = Column(db.BigInteger(), unique=True, nullable=False)
    primary_isbn13 = Column(db.BigInteger(), unique=True, nullable=False)
    publisher = Column(db.String(256))
    description = Column(db.String(512))
    price = Column(db.Float())
    title = Column(db.String(256))
    author = Column(db.String(256))
    contributor = Column(db.String(256))
    book_image_url = Column(db.String(256))

    def __repr__(self):
        return f"<Book(id:{self.id}, title:{self.title}, author:{self.author} isbn:{self.primary_isbn13}>"
