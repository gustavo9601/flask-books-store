from .entities.Purchase import Purchase
from .entities.Book import Book

from .entities.User import User

class PurchaseModel:
    @classmethod
    def register_purchase(self, db, purchase) -> bool:
        try:
            connection = db.connect()
            cursor = connection.cursor()
            sql = """
                INSERT INTO purchases (uuid, isbn_book, user_id)
                VALUES (uuid(), %s, %s)
            """
            cursor.execute(sql, (purchase.isbn_book.isbn, purchase.user_id.id))
            connection.commit()
            return True
        except Exception as ex:
            print("error find >>> ", ex)
            return False

    @classmethod
    def list_purchases_user(cls, db, user: User):
        try:
            connection = db.connect()
            cursor = connection.cursor()
            sql = """
                SELECT p.created_at, b.isbn, b.title, b.price FROM purchases p 
                JOIN books b 
                ON p.isbn_book = b.isbn
                WHERE user_id = %s
            """
            cursor.execute(sql, (user.id,))
            data = cursor.fetchall()
            purchases = []
            for row in data:
                book = Book(row[1], row[2], None, None, row[3])
                purchase = Purchase(None, book, user, row[0])
                purchases.append(purchase)
            return purchases
        except Exception as ex:
            print("error find >>> ", ex)
            return []
