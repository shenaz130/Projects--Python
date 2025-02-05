class Book:
    def __init__(self):
        self.isbn = isbn
        self.author = author
        self.title = title
        self.genre = genre
        self.publisher= publisher
        self.edition= edition

    
b1= Book()
class Library:
    libraryBooks = []
    def __init__ (self):
        self.libraryBooks = []
        #self.numBook = numBook


    def addBook(self):
        nisbn = int(input("Enter the ISBN :"))
        nauthor = input("Enter the Author :")
        ntitle = input("Enter the Title :")
        ngenre = input("Enter the Genre :")
        npublisher = input("Enter the Publisher :")
        nedition = int(input("Enter the Edition :"))
        b1=Library(nisbn,nauthor,ntitle,ngenre,npublisher,nedition)
    
        index = self.findBook(b1.isbn)
        if index == -1:
            libraryBooks.append(b1)
            print("New Book Added!", b1)
        else:
            print("This Book is already in the Collection!", b1)
            print()
            
            
            
    def findBook(self,nIsbn):
        for x in range (len(self.libraryBooks)):
            if nIsbn == self.libraryBooks[x].isbn:
                return x   
        return -1
        



     
    

l1= Library()
l1.addBook()






