# Define a base class for contributors
class Contributor:
    def __init__(self, name: str):
        self.name = name


# Define specific types of contributors, inheriting from Contributor
class Author(Contributor):
    def __init__(self, name: str):
        super().__init__(name)


class Artist(Contributor):
    def __init__(self, name: str):
        super().__init__(name)


class Editor(Contributor):
    def __init__(self, name: str):
        super().__init__(name)


class Actor(Contributor):
    def __init__(self, name: str):
        super().__init__(name)


class Director(Contributor):
    def __init__(self, name: str):
        super().__init__(name)


# Define a class for library items
class LibraryItem:
    def __init__(self, title: str, upc: str, subject: str, contributors):
        self.title = title
        self.upc = upc
        self.subject = subject
        self.contributors = contributors

    # Method to locate the library item
    def locate(self):
        print(f"Locating item: {self.title}")


# List to store library items
library_items = []


# Function to add an item to the library
def add_item(item: LibraryItem):
    library_items.append(item)


# Function to locate item by title or UPC
def locate(title: str):
    # Find items matching the given title or UPC
    found_items = [item for item in library_items if item.upc == title or item.title == title]
    if found_items:
        for item in found_items:
            item.locate()

    else:
        print(f"No UPC was found or the title was: {title} project")


# Function to handle the add item menu
def add_item_menu():
    title = input("Enter the title of the item:")
    upc = input("Enter the UPC of the item:")
    subject = input("Enter the subject of the item:")
    contributors = input("Enter the name and type of the contributor:")
    item = LibraryItem(title, upc, subject, contributors)
    add_item(item)


# Function to handle the search item menu
def search_item_menu():
    upc = input("Enter the UPC of the item to search:")
    locate(upc)


# Main menu function
def main_menu():
    while True:
        print("library menu")
        print("1. Add item")
        print("2. Search item")
        print("3. Quit")
        choice = input(" Enter your choice:")
        if choice == '1':
            add_item_menu()
        elif choice == '2':
            search_item_menu()
        elif choice == '3':
            print("Quit menu.")
            break
        else:
            print("Invalid selection, please try again.")


# Entry point of the program
if __name__ == "__main__":
    main_menu()
