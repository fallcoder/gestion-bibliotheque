class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def display_info(self):
        print(f"[Livre] Titre : {self.title}, Auteur : {self.author}")
        
class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
        
    def display_info(self):
        print(f"[Ebook] Titre : {self.title}, Auteur : {self.author}, Taille : {self.file_size} MB")
        
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        print("Livre ajouté avec succès")
        
    def display_books(self):
        if not self.books:
            print("la bibliothèque est vide")
        else:
            print("\n Liste des livres dans la bibliothèque")
            for book in self.books:
                book.display_info()
            print()
            
    def search_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print("Livre trouvé : ")
                book.display_info()
                return
        print("Livre non trouvé")
        
    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print("Livre supprimer avec succès : ")
                self.books.remove(book)
                return
        print("Livre supprimer non trouvé")
        

def menu():
    library = Library()
    
    while True:
        print("\n ------ MENU BIBLIOTHEQUE ------")
        print("1. ajouter un livre")
        print("2. ajouter un ebook")
        print("3. afficher tous les livres")
        print("4. rechercher un livre par titre")
        print("5. supprimer un livre")
        print("6. quitter")
        
        
        choix = input("Entrer votre choix (1-6) : ")
    
        if choix == "1":
            title = input("Titre : ")
            author = input("Auteur : ")
            book = Book(title, author)
            library.add_book(book)
            
        elif choix == "2":
            title = input("Titre : ")
            author = input("Auteur : ")
            try:
                file_size = float(input("Taille du fichier (en MB) : "))
                ebook = Ebook(title, author, file_size)
                library.add_book(ebook)
            except ValueError:
                print("taille invalide. Entrez un nombre")
                
        elif choix == "3":
            library.display_books()
            
        elif choix == "4":
            title = input("titre du livre à rechercher : ")
            library.search_by_title(title)
            
        elif choix == "5":
            title = input("titre du livre à supprimer : ")
            library.remove_book(title)
            
        elif choix == "6":
            print("merci d'avoir utilisé ce programme ! ")
            break
        
        else:
            print("choix invalide. Veuillez entrer un nombre entre 1 et 6")
        

if __name__ == "__main__":
    menu()
        