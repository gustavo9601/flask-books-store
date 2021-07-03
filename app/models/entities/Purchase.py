import datetime

class Purchase:
    def __init__(self, uuid, isbn_book, user_id, created_at=None):
        self.uuid = uuid
        self.isbn_book = isbn_book
        self.user_id = user_id
        self.created_at = created_at

    def formatted_date(self):
        return datetime.datetime.strftime(self.created_at, '%d/%m/%Y - %H:%M:%S')
