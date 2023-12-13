# comment.py

class Comment:
    def __init__(self, comment_id, content, author):
        self.comment_id = comment_id
        self.content = content
        self.author = author

    def display_info(self):
        print(f"Comment ID: {self.comment_id}")
        print(f"Content: {self.content}")
        self.author.display_info()
