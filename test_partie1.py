import partie1.py
# Création du catalogue de livres
catalog = BookCatalog()

# Ajout de quelques livres
catalog.addBook("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "9780747532743", 5, "Fantasy")
catalog.addBook("The Lord of the Rings", "J.R.R. Tolkien", "9780618517657", 3, "Fantasy")
catalog.addBook("1984", "George Orwell", "9780451524935", 2, "Science fiction")

# Recherche de livres
results = catalog.searchBook("potter")
print("Résultats de la recherche :")
for book in results:
    print("- Titre :", book[0])
    print("  Auteur :", book[1])
    print("  ISBN :", book[2])
    print("  Copies disponibles :", book[3])

# Suppression d'un livre
catalog.removeBook("9780451524935")
