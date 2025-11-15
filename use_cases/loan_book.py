class LoanBookUseCase:

    def __init__(self, book_repo: BookRepository):
        self.book_repo = book_repo

    def execute(self, book_id: int):
        book = self.book_repo.get_by_id(book_id)
        if book is None:
            raise Exception("Book not found")

        if not book.available:
            raise Exception("Book already loaned")

        book.available = False
        self.book_repo.update(book)
        return book
