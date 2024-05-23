class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books()

    def add_book(self,title,author):
            book = Book(title,author)
            self.books.append(book)
    def display_book(self):
        for book in self.books:
            print(f'title:{book.title},Author:{book.author}')

def main():
    library = Library()
    library.add_book("The Catcher in the Rye", "J.D. Salinger")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("1984", "George Orwell")

    library.display_books()

if __name__ =="_main_":
    main()