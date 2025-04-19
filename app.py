import json
import os

data_file = "library.txt"

def load_library():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            try:
                data = json.load(file)
                if isinstance(data, list):
                    return data
                else:
                    return []
            except json.JSONDecodeError:
                print("Warning: library.txt is empty or corrupted. Resetting library.")
                return []
    return []

def save_library(library):
    with open(data_file, "w") as file:
        json.dump(library, file, indent=4)

def add_book(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year of the book: ")
    genre = input("Enter the genre of the book: ")
    read = input("Have you read the book? (yes/no): ").strip().lower() == "yes"
    
    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read,
    }
    library.append(new_book)
    save_library(library)
    print(f'Book "{title}" added successfully!')

def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip().lower()
    initial_length = len(library)
    library = [book for book in library if book['title'].lower() != title]
    if len(library) < initial_length:
        save_library(library)
        print(f'Book "{title}" removed successfully.')
    else:
        print(f'Book "{title}" not found in the library.')
    return library

def search_library(library):
    search_by = input("Search by title or author: ").strip().lower()
    if search_by not in ["title", "author"]:
        print("Invalid search option! Choose 'title' or 'author'.")
        return
    query = input(f"Enter the {search_by}: ").strip().lower()
    results = [book for book in library if query in book[search_by].lower()]
    if results:
        print(f"\nBooks found ({len(results)} result(s)):")
        for book in results:
            print(f"- {book['title']} by {book['author']} ({book['year']}, {book['genre']})")
    else:
        print("No books found matching your query.")

def view_books(library):
    if library:
        print("\nLibrary Collection:")
        for book in library:
            print(f"- {book['title']} by {book['author']} ({book['year']}, {book['genre']})")
    else:
        print("Your library is empty.")

# Main code
print("Welcome to the Library Management System!")
library = load_library()

while True:
    print("\nMenu:")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Search Library")
    print("4. View All Books")
    print("5. Exit")
    choice = input("Choose an option (1-5): ").strip()
    if choice == "1":
        add_book(library)
    elif choice == "2":
        library = remove_book(library)  # Update library list after removal
    elif choice == "3":
        search_library(library)
    elif choice == "4":
        view_books(library)
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid option. Please choose a number between 1 and 5.")

input("Press Enter to exit...")
