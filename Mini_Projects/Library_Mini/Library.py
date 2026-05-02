class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print('=== Books in library ===')
        for book in self.books:
            print('Title:', book.title, 'Author:', book.author, 'Genre:', book.genre,'\n', sep = '\n')

book1 = Book('Harry Potter and the Goblet of Fire', 'Joanne Rowling', 'Fantasy')
book2 = Book('1984', 'George Orwell', 'Dystopian literature')
book3 = Book('Fahrenheit 451', 'Ray Bradbury', 'Dystopian literature')

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.show_books()
