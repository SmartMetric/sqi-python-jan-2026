library = [
    {"title": "Things Fall Apart", "author": "Chinua Achebe", "year_of_publication": 1976, "isbn": "987-678-233-889", "available": True},
    {"title": "1984", "author": "George Orwell", "year_of_publication": 1949, "isbn": "978-045-152-4935", "available": True},
    {"title": "The Alchemist", "author": "Paulo Coelho", "year_of_publication": 1988, "isbn": "978-006-112-2415", "available": False},
    {"title": "Purple Hibiscus", "author": "Chimamanda Ngozi Adichie", "year_of_publication": 2003, "isbn": "978-140-003-3416", "available": True},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year_of_publication": 1937, "isbn": "978-054-792-8227", "available": False},
]


def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year_of_publication = int(input("Enter the year of publication: "))
    isbn = input("Enter the ISBN: ")


    book = {
        "title": title,
        "author": author,
        "year_of_publication": year_of_publication,
        "isbn": isbn,
        "available": True
    }

    library.append(book)

    print("Book added successfully")


def view_books():
    for i, book in enumerate(library, start=1):
        availability = "Yes" if book["available"] else "No"
        print(f"{i}. {book["title"]} by {book["author"]} published in {book["year_of_publication"]} with ISBN {book["isbn"]}. Availabile? {availability}")


def search_book(title):
    for book in library:
        if book["title"] == title:
            availability = "Yes"if book["available"] else "No"
            print("Book found")
            return
    print("Book not found")

def borrow_book(isbn):
    for book in library:
        if book["isbn"] == isbn:
            if book["available"] == False:
                print("Book Borrowed successfully. Ensure you return it within 48 hours ")
            else:
                print("This book has been borrowed. You may check back after 48 hours")
            return 
    print("Book not found")

def update_book(isbn):
    for book in library:
        if book["isbn"] == isbn:
            new_title = input("Enter the new title: ")
            new_author = input("Enter the new author: ")
            new_year = int(input("Enter the new year of publication: "))

            book["title"] = new_title
            book["author"] = new_author
            book["year_of_publication"] = new_year

            print("Book updated successfully")
            return

    print("Book not found")

def delete_book(isbn):
    for index, book in enumerate(library):
        if book["isbn"] == isbn:
            library.pop(index)
            print("Book deleted successfully")
            return

    print("Book not found")

def return_book(isbn):
    for book in library:
        if book["isbn"] == isbn:
            if not book["available"]:
                book["available"] = True
                print("Book returned successfully")
            else:
                print("This book was not borrowed")
            return

    print("Book not found")


        
        
           
            







menu = """
1. Add Book
2. View Books
3. Update Book
4. Delete Book
5. Search Book
6. Borrow Book
7. Return Book
8. Quit
"""
while True:
    print(menu)

    choice = input("Enter a choice from 1 to 8: ").strip()

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "5":
        title = input("Enter the title of the book: ")
        search_book(title)
    elif choice == "6":
        isbn = input("Enter the book's ISBN")
        borrow_book(isbn)
    elif choice == "3":
        isbn= input("Enter the book's ISBN")
        update_book(isbn)
    elif choice == "4":
        isbn = input("Enter the book's ISBN")
        delete_book(isbn)
    elif choice == "7":
         isbn = input("Enter the book's ISBN")
         return_book(isbn)
    else:
        print("Quit")

    
















