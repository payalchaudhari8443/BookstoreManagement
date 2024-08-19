class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book_by_title(self, title):
        return [book for book in self.books if book.title == title]

    def calculate_total_value(self):
        return sum(book.price for book in self.books)

# Example usage
if __name__ == "__main__":
    bookstore = Bookstore()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
    book2 = Book("1984", "George Orwell", 8.99)

    bookstore.add_book(book1)
    bookstore.add_book(book2)

    print("Books found:", bookstore.search_book_by_title("1984"))
    print("Total value of books:", bookstore.calculate_total_value())
