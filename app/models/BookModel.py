from .entities.Author import Author
from .entities.Book import Book


class BookModel():

    @classmethod
    def list_books(self, db):
        try:
            connection = db.connect()
            cursor = connection.cursor()
            sql = """
            SELECT isbn, title, year_published, price, last_name, name
            FROM books JOIN authors ON books.author_id = authors.id
            ORDER BY title ASC;
            """
            cursor.execute(sql)
            data = cursor.fetchall()
            books = []
            for row in data:
                author = Author(0, row[4], row[5])
                book = Book(row[0], row[1], author, row[2], row[3])
                books.append(book)
            return books

        except Exception as ex:
            raise Exception(ex)
