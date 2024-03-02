from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# making new database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///book-library.db"
db = SQLAlchemy(app)

# making a new table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    author = db.Column(db.String(30), nullable=False)
    rating = db.Column(db.Float, nullable=False)


def create_new_db():
    """ create a new table"""
    with app.app_context():
        db.create_all()

def add_value():
    """add value for the existing table"""
    with app.app_context():
        newbook = Book(id=1, title="Harry Potter", author="J.K. Rowling", rating="9.2")
        db.session.add(newbook)
        db.session.commit()


def read_all_books():
    """ read all books"""
    with app.app_context():
        all_books = db.session.query(Book).all()


def read_book(title):
    """ read specific book(param as title of the book"""
    with app.app_context():
        book = Book.query.filter_by(title=title).first()


def update_book(title, to_change):
    """update an existing book's title as param"""
    book_to_update = Book.query.filter_by(title=title).first()
    book_to_update.title = to_change
    with app.app_context():
        db.session.commit()


def update_book_by_id(to_change):
    """update an existing book's title by id as param"""
    book_id = 1
    book_to_update = Book.query.get(book_id)
    book_to_update.title = to_change
    with app.app_context():
        db.session.commit()


def delete_book(title):
    """delete existing book by title as param"""
    book_to_delete = Book.query.filter_by(title=title)
    db.session.delete(book_to_delete)
    with app.app_context():
        db.session.commit()


def delete_by_id(id:int):
    """delete existing book by id as param"""
    book_id = id
    book_to_delete = Book.query.get(id)
    db.session.delete(book_to_delete)
    with app.app_context():
        db.session.commit()

read_book("Harry Potter")

if __name__ == "__main__":
    app.run(debug=True)
