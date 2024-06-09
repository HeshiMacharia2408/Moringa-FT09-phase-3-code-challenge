from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category):
        if (2 <= len(name) <= 16):
            return ValueError("Please input a name containing  between 2 to 16 characters")
        if not isinstance(category, str):
            return TypeError("Please input a category of type str.")
        if len(category) == 0:
            return ValueError("Please fill in the category.")
        
        self.id = id
        self.name = name
        self.category = category

    def id(self):
        return self._id
    
    def name(self):
        return self._name
    
    def category(self):
        return
    
    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        articles = cursor.fetchall()
        conn.close()
        return articles
    
    def contributors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        contributors = cursor.fetchall()
        conn.close()
        return contributors

    def article_titles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        titles = cursor.fetchall()
        conn.close()
        return [title[0] for title in titles] if titles else None

    def contributing_authors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        authors = cursor.fetchall()
        conn.close()
        return [author(author[0], author[1]) for author in authors] if authors else None

    def __repr__(self):
        return f'<Magazine {self.name}>'
