class Author:

    def __init__(self, id, last_name, name, date_born=None):
        self.id = id
        self.last_name = last_name
        self.name = name
        self.date_born = date_born


    def full_name(self):
        return f"{self.name} {self.last_name}"