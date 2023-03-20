# EXEMPLE 1:
# creer un catalogue de livres et ajouter des livres
catalog = BookCatalog ()
catalog . addBook ( " Natural ␣ Language ␣ Processing " ,\\
" Steven ␣ Bird , ␣ Ewan ␣ Klein , ␣ and ␣ Edward ␣ Loper " , " 0596516495 " , 2 , " NLP " )
catalog . addBook ( " Python ␣ for ␣ Data ␣ Analysis " , " Wes ␣ McKinney " ,\\
" 1449319793 " , 1 , " Data ␣ Science " )
catalog . addBook ( " Data ␣ Structures ␣ and ␣ Algorithms ␣ in ␣ Python " ,\\
" Michael ␣ T . ␣ Goodrich , ␣ Roberto ␣ Tamassia , ␣ and ␣ Michael ␣ H . ␣ Goldwasser " ,\\
" 1118290275 " , 3 , " Algorithms " )
catalog . addBook ( " The ␣ Catcher ␣ in ␣ the ␣ Rye " , " J . D . ␣ Salinger " , " 0316769177 " ,\\
2 , " Fiction " )
catalog . addBook ( " To ␣ Kill ␣ a ␣ Mockingbird " , " Harper ␣ Lee " , " 0446310786 " ,\\
1 , " Fiction " )
# creer un usager avec des genres preferes
patron = Patron ( " Alice " , [ " NLP " , " Fiction " ])
# recommander des livres au visiteur en fonction de ses genres preferes
recommended_books = recommendBooks ( patron , catalog )
for book in recommended_books :
print ( book )
# Resultat :
Natural Language Processing
The Catcher in the Rye
To Kill a Mockingbird
# EXEMPLE 2:
catalog = BookCatalog ()
catalog . addBook ( " The ␣ Hitchhiker ’s ␣ Guide ␣ to ␣ the ␣ Galaxy " , " Douglas ␣ Adams " ,\\
" 0345391802 " , 3 , " Science ␣ Fiction " )
catalog . addBook ( " Neuromancer " , " William ␣ Gibson " , " 0441569595 " , 1 ,\\
" Science ␣ Fiction " )
catalog . addBook ( " The ␣ Shining " , " Stephen ␣ King " , " 0385121679 " , 2 , " Horror " )
catalog . addBook ( " The ␣ Stand " , " Stephen ␣ King " , " 0385199570 " , 3 , " Horror " )
catalog . addBook ( " The ␣ Great ␣ Gatsby " , " F . ␣ Scott ␣ Fitzgerald " ,\\
" 9780743273565 " , 1 , " Fiction " )
4
patron = Patron ( " Bob " , [ " Horror " ])
recommended_books = recommendBooks ( patron , catalog )
for book in recommended_books :
print ( book )
# Resultat :
The Shining
The Stand
