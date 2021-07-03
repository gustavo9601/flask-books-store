from .entities.Author import Author
from .entities.Book import Book


class BookModel:
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

    @classmethod
    def list_books_sold(cls, db):
        try:
            connection = db.connect()
            cursor = connection.cursor()
            sql = """
                    SELECT p.isbn_book, b.title, b.price,
                    COUNT(p.isbn_book) units_sold
                    FROM purchases p 
                    JOIN books b 
                    ON p.isbn_book = b.isbn
                    GROUP BY p.isbn_book
                    ORDER BY 4 DESC, 2 ASC
                """
            cursor.execute(sql)
            data = cursor.fetchall()
            books = []
            for row in data:
                book = Book(row[0], row[1], None, None, row[2])
                book.units_sold = int(row[3])
                books.append(book)
            return books

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def read_book(cls, db, isbn):
        try:
            connection = db.connect()
            cursor = connection.cursor()
            sql = """
                          SELECT isbn, title, year_published, price
                          FROM books
                          WHERE isbn = %s
                      """
            cursor.execute(sql, (isbn,))
            data = cursor.fetchone()
            return Book(data[0], data[1], None, data[2], data[3])

        except Exception as ex:
            print("error read book > ", ex)
            raise Exception(ex)
