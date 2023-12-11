from advanced_alchemy.exceptions import ConflictError
from advanced_alchemy.filters import CollectionFilter, SearchFilter
from litestar import Controller, get, patch, post
from litestar.di import Provide
from litestar.dto import DTOData
from litestar.exceptions import HTTPException
from litestar.repository import NotFoundError

from app.dtos import (
    AuthorReadDTO,
    AuthorReadFullDTO,
    AuthorUpdateDTO,
    AuthorWriteDTO,
    BookCopyReadDTO,
    BookCopyWriteDTO,
    BookReadDTO,
    BookReadFullDTO,
    BookUpdateDTO,
    BookWriteDTO,
    CategoryReadDTO,
    CategoryWriteDTO,
)
from app.models import Author, Book, BookCopy, Category
from app.repositories import (
    AuthorRepository,
    BookCopyRepository,
    BookRepository,
    CategoryRepository,
    provide_authors_repo,
    provide_book_copies_repo,
    provide_books_repo,
    provide_categories_repo,
)


class AuthorController(Controller):
    path = "/authors"
    tags = ["authors"]
    return_dto = AuthorReadDTO
    dependencies = {"authors_repo": Provide(provide_authors_repo)}

    @get()
    async def list_authors(self, authors_repo: AuthorRepository) -> list[Author]:
        return authors_repo.list()

    @post(dto=AuthorWriteDTO)
    async def create_author(self, data: Author, authors_repo: AuthorRepository) -> Author:
        return authors_repo.add(data)

    @get("/{author_id:int}", return_dto=AuthorReadFullDTO)
    async def get_author(self, author_id: int, authors_repo: AuthorRepository) -> Author:
        try:
            return authors_repo.get(author_id)
        except NotFoundError as e:
            raise HTTPException(detail="Author not found", status_code=404) from e

    @patch("/{author_id:int}", dto=AuthorUpdateDTO)
    async def update_author(
        self, author_id: int, data: DTOData[Author], authors_repo: AuthorRepository
    ) -> Author:
        try:
            author, updated = authors_repo.get_and_update(
                id=author_id, **data.as_builtins(), match_fields=["id"]
            )
            return author
        except NotFoundError as e:
            raise HTTPException(detail="Author not found", status_code=404) from e


class BookController(Controller):
    path = "/books"
    tags = ["books"]
    return_dto = BookReadDTO
    dependencies = {"books_repo": Provide(provide_books_repo)}

    @get()
    async def list_books(self, books_repo: BookRepository) -> list[Book]:
        return books_repo.list()

    @get("/search")
    async def search_books(self, books_repo: BookRepository, q: str) -> list[Book]:
        return books_repo.list(SearchFilter("title", q))

    @post(dto=BookWriteDTO, dependencies={"categories_repo": Provide(provide_categories_repo)})
    async def create_book(
        self, data: Book, books_repo: BookRepository, categories_repo: CategoryRepository
    ) -> Book:
        category_ids = [c.id for c in data.categories]
        data.categories = categories_repo.list(CollectionFilter("id", category_ids))
        return books_repo.add(data)

    @get("/{book_id:int}", return_dto=BookReadFullDTO)
    async def get_book(self, book_id: int, books_repo: BookRepository) -> Book:
        try:
            return books_repo.get(book_id)
        except NotFoundError as e:
            raise HTTPException(detail="Book not found", status_code=404) from e

    @patch("/{book_id:int}", dto=BookUpdateDTO)
    async def update_book(
        self, book_id: int, data: DTOData[Book], books_repo: BookRepository
    ) -> Book:
        try:
            book, updated = books_repo.get_and_update(
                id=book_id, **data.as_builtins(), match_fields=["id"]
            )
            return book
        except NotFoundError as e:
            raise HTTPException(detail="Book not found", status_code=404) from e


class BookCopyController(Controller):
    path = "/book_copies"
    tags = ["book-copies"]
    return_dto = BookCopyReadDTO
    dependencies = {"book_copies_repo": Provide(provide_book_copies_repo)}

    @get()
    async def list_book_copies(self, book_copies_repo: BookCopyRepository) -> list[BookCopy]:
        return book_copies_repo.list()

    @get("/{book_copy_id:int}")
    async def get_book_copy(
        self, book_copy_id: int, book_copies_repo: BookCopyRepository
    ) -> BookCopy:
        try:
            return book_copies_repo.get(book_copy_id)
        except NotFoundError as e:
            raise HTTPException(detail="Book copy not found", status_code=404) from e

    @post(dto=BookCopyWriteDTO)
    async def create_book_copy(
        self, data: BookCopy, book_copies_repo: BookCopyRepository
    ) -> BookCopy:
        try:
            return book_copies_repo.add(data)
        except ConflictError as e:
            raise HTTPException(detail="Error creating book copy", status_code=400) from e

    @patch("/{book_copy_id:int}")
    async def update_book_copy(
        self, book_copy_id: int, data: DTOData[BookCopy], book_copies_repo: BookCopyRepository
    ) -> BookCopy:
        try:
            book_copy, updated = book_copies_repo.get_and_update(
                id=book_copy_id, **data.as_builtins(), match_fields=["id"]
            )
            return book_copy
        except NotFoundError as e:
            raise HTTPException(detail="Book copy not found", status_code=404) from e


class CategoryController(Controller):
    path = "/categories"
    tags = ["categories"]
    return_dto = CategoryReadDTO
    dependencies = {"categories_repo": Provide(provide_categories_repo)}

    @get()
    async def list_categories(self, categories_repo: CategoryRepository) -> list[Category]:
        return categories_repo.list()

    @post(dto=CategoryWriteDTO)
    async def create_category(
        self, data: Category, categories_repo: CategoryRepository
    ) -> Category:
        return categories_repo.add(data)
