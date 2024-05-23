class Contributor:
    def __init__(self, name: str):
        self.name = name


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


class LibraryItem:
    def __init__(self, title: str, upc: str, subject: str, contributors):
        self.title = title
        self.upc = upc
        self.subject = subject
        self.contributors = contributors

    def locate(self):
        print(f"Locating item: {self.title}")
