from litestar.contrib.sqlalchemy.repository import SQLAlchemySyncRepository
from sqlalchemy.orm import Session

from app.models import Author, Book, BookCopy, Category


class AuthorRepository(SQLAlchemySyncRepository[Author]):
    model_type = Author


async def provide_authors_repo(db_session: Session):
    return AuthorRepository(session=db_session, auto_commit=True)


class BookRepository(SQLAlchemySyncRepository[Book]):
    model_type = Book


async def provide_books_repo(db_session: Session):
    return BookRepository(session=db_session, auto_commit=True)


class BookCopyRepository(SQLAlchemySyncRepository[BookCopy]):
    model_type = BookCopy


async def provide_book_copies_repo(db_session: Session):
    return BookCopyRepository(session=db_session, auto_commit=True)


class CategoryRepository(SQLAlchemySyncRepository[Category]):
    model_type = Category


async def provide_categories_repo(db_session: Session):
    return CategoryRepository(session=db_session, auto_commit=True)
