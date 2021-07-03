from app.models.entities.Author import Author


class Book:

    def __init__(self, isbn, title, author, year_published, price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year_published = year_published
        self.price = price
        self.units_sold = 0
