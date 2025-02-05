class Book:
    def __init__(self,isbn,author,title,genre,publisher,edition):
        self.isbn = isbn
        self.author = author
        self.title = title
        self.genre = genre
        self.publisher= publisher
        self.edition= edition

def menu():
    print("        Welcome to TPL")  
    print("        ---------------")
    print("Please enter one of the following options: ")
    print("1) Add a Book")
    print("2) Delete a Book")
    print("3) Find a Book")
    print("4) List all Books")
    print("5) List Books for given Genre")
    print("6) Number of books for given author")
    print("7) Total Number of books")
    print("8) List books for given edition")
    print("9) Exit")  

  


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
        b1=Book(nisbn,nauthor,ntitle,ngenre,npublisher,nedition)
    
        index = self.findBook(b1.isbn)
        if index == -1:
            self.libraryBooks.append(b1)
            print("New Book Added!", b1.title)
            print("Length",len(self.libraryBooks))
        else:
            print("This Book is already in the Collection!", b1.title)
            print()
            
            
            
    def findBook(self,nisbn):
        for x in range (len(self.libraryBooks)):
            if nisbn == self.libraryBooks[x].isbn:
                print("This Book is already in the Collection!")
                return x 
    
        return -1
    
    def deletebook(self):
        isbn = int(input("Enter the ISBN :"))
        index = self.findBook(isbn)
        print(index)
        print(isbn)
        self.libraryBooks.pop(index)
        print("successfully deleted.")

    def ListGenre(self):
        genre = input("Enter the genre :")
        for x in range (len(self.libraryBooks)):
            if genre == self.libraryBooks[x].genre:
                self.printBooks()

    def AuthorBooks(self):
        author = input("Enter the author :")
        count = 0
        for x in range (len(self.libraryBooks)):
            if author == self.libraryBooks[x].author:
                count  = count +1
            print (author, "'s Total Number of Book are ", count)

    def BookCount(self):
        print("The Total Books count is- ", len(l1.libraryBooks))

    def BookEdition(self):
        edition = int(input("Enter the edition :"))
        for x in range (len(self.libraryBooks)):
            if edition == self.libraryBooks[x].edition:
                print (edition)
                self.printBooks()
            break
        
        
    def printBooks(self):
        for x in range (len(self.libraryBooks)):
            print("--------------------")
            print("Title  :" , self.libraryBooks[x].title)
            print("Author  :" , self.libraryBooks[x].author)
            print("ISBN  :" , self.libraryBooks[x].isbn) 
            print("Genre  :" , self.libraryBooks[x].genre)
            print("Publisher  :" , self.libraryBooks[x].publisher)
            print("Edition  :" , self.libraryBooks[x].edition)
            print("--------------------")

l1= Library()

i= 1
while i ==1:
    menu()
    choice =int (input("Enter you choice :"))
    if choice ==1:
        l1.addBook()
    elif choice ==2:
        l1.deletebook()
    elif choice ==3:
        nisbn= int(input("Enter the ISBN :"))
        l1.findBook(nisbn)
    elif choice ==4:
        l1.printBooks()
    elif choice ==5:
        l1.ListGenre()
    elif choice ==6:
        l1.AuthorBooks()
    elif choice ==7:
        l1.BookCount()
    elif choice ==8:
        l1.BookEdition()
    elif choice ==9:
        i =0
        print("Thanks.Goodbye!")
    
       




