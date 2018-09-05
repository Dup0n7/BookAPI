from BookModel import *


def validBookObject(bookObject):
    if ("isbn" in bookObject):
        print("first if true")
        isbn_db = Book.json(Book.query.filter_by(isbn="1111").first())
        print(isbn_db)
        print(isbn_db['isbn'])
        if 1111 == isbn_db['isbn']:
            return True
        else:
            print("2nd false")
            return False

    else:
        print("1st false")
        return False

def letstrythis(number):
    if 1 == number['number']:
        return True
    else:
        return False