# LIBRARY CLASS 
class Library:
    def __init__(self):
        self.inventory = []
    
    def add_book(self, book):
        self.inventory.append(book)
    
    def checkout_book(self, book, borrower):
        if book.available:
            book.available = False
            borrower.borrowed_books.append(book)
        else:
            print(book.title + " is not available.")
    
    def return_book(self, book, borrower):
        if book in borrower.borrowed_books:
            book.available = True
            borrower.borrowed_books.remove(book)
        else:
            print(borrower.name + " didn't borrow " + book.title + ".")
    
    def list_available_books(self):
        return [book.title for book in self.inventory if book.available]
