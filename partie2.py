class BookNode:
    def __init__(self, title, author, ISBN, genre):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.genre = genre


class BookCatalog:
    def __init__(self):
        self.books = []

    def addBook(self, title, author, ISBN, genre):
        book = BookNode(title, author, ISBN, genre)
        self.books.append(book)

    def getBooksByGenre(self, genre):
        return [book.title for book in self.books if book.genre == genre]


class Patron:
    def __init__(self, name, preferredGenres):
        self.name = name
        self.preferredGenres = preferredGenres
        self.readingHistory = []

    def recommendBooks(self, catalog):
        recommendedBooks = []
        self._recommendBooks(catalog, recommendedBooks, self.preferredGenres)
        return recommendedBooks

    def _recommendBooks(self, catalog, recommendedBooks, genresToConsider):
        for genre in genresToConsider:
            booksInGenre = catalog.getBooksByGenre(genre)
            for bookTitle in booksInGenre:
                bookNode = next((book for book in catalog.books if book.title == bookTitle), None)
                if bookNode and bookNode not in self.readingHistory and bookNode not in recommendedBooks:
                    recommendedBooks.append(bookNode)
        if len(genresToConsider) > 1:
            self._recommendBooks(catalog, recommendedBooks, genresToConsider[1:])


