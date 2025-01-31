
class Library:

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks


    def DisplayAvailableBooks(self):
        print("available books")
        for book in self.availableBooks:
            print(book)
    
    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("you have borrowewd the books")
            self.availableBooks.remove(requestedBook)
        else:
            print("sorry the ook is not available in out list")

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("you have returned the book!")


class Customer:
    def requestBook(self):
        print("enter the name of book you would like to borrow: ")
        self.book = input()
        return self.book

    def returnBook(self):
        print("enter the nameof the book which are returing")
        self.book = input()
        return self.book

library=Library(['Think adn Grow','Who will cry','Rich Dad'])

customer= Customer()
while True:
    print("enter 1 to display avaiable books ")
    print("enter 2 to request  books ")
    print("enter 3 to return a book")
    print("enter 4 to exit")
    userChoice = int(input())
    if userChoice is 1:
        library.DisplayAvailableBooks()

    elif userChoice is 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice is 3:
        returnedBook = customer.requestBook()
        library.addBook(returnedBook)
    elif userChoice is 4:
        quit()




