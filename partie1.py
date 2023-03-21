class BookNode:
    def __init__(self, title, author, isbn, copies, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        self.genre = genre
        self.next = None


class BookCatalog:
    def __init__(self):
        self.head = None
    
    def addBook(self, title, author, isbn, copies, genre):
        book = BookNode(title, author, isbn, copies, genre)
        if self.head is None:
            self.head = book
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = book
    
    def removeBook(self, isbn):
        current = self.head
        if current is not None and current.isbn == isbn:
            self.head = current.next
            current = None
            return
        while current is not None:
            if current.isbn == isbn:
                break
            prev = current
            current = current.next
        if current == None:
            return
        prev.next = current.next
        current = None
    
    def searchBook(self, query):
        results = []
        current = self.head
        while current is not None:
            if query in current.title or query in current.author:
                results.append((current.title, current.author, current.isbn, current.copies))
            current = current.next
        return results
