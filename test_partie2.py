# Exemple d'utilisation
catalog = BookCatalog()
catalog.addBook("Natural Language Processing", "Steven Bird, Ewan Klein, and Edward Loper", "0596516495", "NLP")
catalog.addBook("Python for Data Analysis", "Wes McKinney", "1449319793", "Data Science")
catalog.addBook("Data Structures and Algorithms", "Michael T. Goodrich and Roberto Tamassia", "1118771338", "Computer Science")
catalog.addBook("The Design of Everyday Things", "Don Norman", "0465050654", "Design")
catalog.addBook("The Lean Startup", "Eric Ries", "0307887898", "Business")

patron1 = Patron("Alice", ["NLP", "Data Science"])
patron1.readingHistory.append(catalog.books[0])
recommendedBooks = patron1.recommendBooks(catalog)
print("Recommended books for", patron1.name, ":", [book.title for book in recommendedBooks])
