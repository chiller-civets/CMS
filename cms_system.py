# cms_system.py

from article import Article
from author import Author
from comment import Comment

# Create authors
author1 = Author(1, "Alice", "alice@example.com")
author2 = Author(2, "Bob", "bob@example.com")

# Create comments
comment1 = Comment(101, "Great article!", author1)
comment2 = Comment(102, "I enjoyed reading this.", author2)

# Create articles
article1 = Article(1001, "Introduction to Python", "This is an introductory article about Python.", author1)
article1.comments.append(comment1)

article2 = Article(1002, "Advanced Python Techniques", "Explore advanced Python techniques in this article.", author2)
article2.comments.append(comment2)

# Display information
print("Article Information:")
article1.display_info()
print()
article2.display_info()
