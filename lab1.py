import datetime


class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.borrower_name = None
        self.due_date = None

    def borrow_book(self, borrower_name, days=14):
        if self.is_borrowed:
            return False
        self.is_borrowed = True
        self.borrower_name = borrower_name
        self.due_date = datetime.date.today() + datetime.timedelta(days=days)
        return True

    def return_book(self):
        if not self.is_borrowed:
            return False
        self.is_borrowed = False
        self.borrower_name = None
        self.due_date = None
        return True


class Library:

    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print(f"Error: Book ID {book_id} already exists.")
            return
        self.books[book_id] = Book(book_id, title, author)
        print(f"Success: '{title}' added to the library.")

    def check_out_book(self, book_id, borrower_name):
        book = self.books.get(book_id)
        if not book:
            print("Error: Book not found.")
            return
        if book.borrow_book(borrower_name):
            print(f"Success: '{book.title}' checked out by {borrower_name}.")
            print(f"Due date: {book.due_date}")
        else:
            print(f"Error: '{book.title}' is already borrowed.")

    def check_in_book(self, book_id):
        book = self.books.get(book_id)
        if not book:
            print("Error: Book not found.")
            return
        if book.return_book():
            print(f"Success: '{book.title}' has been returned.")
        else:
            print(f"Error: '{book.title}' was not checked out.")

    def view_records(self):
        if not self.books:
            print("The library catalog is empty.")
            return
        print(f"\n{'ID':<5} | {'Title':<25} | {'Author':<20} | {'Status':<10} | {'Borrower':<15} | {'Due Date'}")
        print("-" * 90)
        for b in self.books.values():
            status = "Borrowed" if b.is_borrowed else "Available"
            borrower = b.borrower_name if b.borrower_name else "-"
            due = str(b.due_date) if b.due_date else "-"
            print(f"{b.book_id:<5} | {b.title:<25} | {b.author:<20} | {status:<10} | {borrower:<15} | {due}")


# Example usage
if __name__ == "__main__":
    library = Library()

    # Add books
    library.add_book("101", "The Hobbit", "J.R.R. Tolkien")
    library.add_book("102", "1984", "George Orwell")

    # View initial records
    library.view_records()

    # Borrow a book
    print("\n--- Borrowing a book ---")
    library.check_out_book("101", "Alice")

    # View updated records
    library.view_records()

    # Return a book
    print("\n--- Returning a book ---")
    library.check_in_book("101")

    # View final records
    library.view_records()
