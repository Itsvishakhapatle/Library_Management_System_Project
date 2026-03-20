import json

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.issued = False


class Library:
    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        try:
            with open('books.json', "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self):
        with open('books.json', 'w') as f:
            json.dump(self.books, f, indent=4)

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        genre = input("Enter book genre: ")

        new_book = Book(title, author, genre)

        self.books.append({
            "title": new_book.title,
            "author": new_book.author,
            "genre": new_book.genre,
            "issued": new_book.issued
        })

        self.save_books()
        print("Book added successfully")

    def remove_book(self):
        title = input("Enter title name: ")
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                self.save_books()
                print("Book removed successfully")
                return
        print("Book not found")

    def search_book(self):
        title = input("Enter title name: ")
        for book in self.books:
            if book["title"] == title:
                print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")
                return
        print("Book not available")

    def issue_book(self):
        title = input("Enter book title: ")
        for book in self.books:
            if book["title"] == title and not book["issued"]:
                book["issued"] = True
                self.save_books()
                print("Book issued successfully")
                return
        print("Book not available or already issued")

    def return_book(self):
        title = input("Enter book title: ")
        for book in self.books:
            if book["title"] == title and book["issued"]:
                book["issued"] = False
                self.save_books()
                print("Book returned successfully")
                return
        print("Book was not issued")


library = Library()

while True:
    print("\n1 -> Add Book")
    print("2 -> Remove Book")
    print("3 -> Search Book")
    print("4 -> Issue Book")
    print("5 -> Return Book")
    print("6 -> Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        library.add_book()
    elif choice == '2':
        library.remove_book()
    elif choice == '3':
        library.search_book()
    elif choice == '4':
        library.issue_book()
    elif choice == '5':
        library.return_book()
    elif choice == '6':
        break
    else:
        print("Invalid choice")
