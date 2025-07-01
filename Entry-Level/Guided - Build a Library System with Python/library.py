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
    
