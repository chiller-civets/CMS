# author.py

class Author:
    def __init__(self, author_id, name, email):
        self.author_id = author_id
        self.name = name
        self.email = email

    def display_info(self):
        print(f"Author ID: {self.author_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
