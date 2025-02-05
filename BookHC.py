class Book:
    def __init__(self,isbn,author,title,genre,publisher,edition):
        self.isbn = isbn
        self.author = author
        self.title = title
        self.genre = genre
        self.publisher= publisher
        self.edition= edition

        
b1= Book (111,"John","Twlight","Fiction","ABC Publishers",3)
b2= Book (111,"John","Twlight","Fiction","ABC Publishers",3)
b3= Book (121,"Dave","Elemental","Science","RTY Publishers",3)
b4= Book (131,"Dave","Elemental","Science","RTY Publishers",3)
b5= Book (141,"Dave","Elemental","Science","RTY Publishers",3)


class Library:
    libraryBooks = []
    def __init__ (self):
        self.libraryBooks = []
        #self.numBook = numBook


    def addBook(self, aBook):
        index = self.findBook(aBook.isbn)
        if index == -1:
            self.libraryBooks.append(aBook)
            print("New Book Added!", aBook)
        else:
            print("This Book is already in the Collection!", aBook)
            print()
            
            
    def deletebook(self, aBook):
        index = self.findBook(aBook.isbn)
        if index != -1:
            self.libraryBooks.remove(aBook)
            print("Book is successfully deleted.")
        else:
            print("Invalid ISBN")
            
    def findBook(self,nIsbn):
        for x in range (len(self.libraryBooks)):
            if nIsbn == self.libraryBooks[x].isbn:
                return x   
        return -1
        
    def BookCount(self):
        print("The Total Books count is- ", len(l1.libraryBooks))

    def ListGenre(self, genre):
        for x in range (len(self.libraryBooks)):
            if genre == self.libraryBooks[x].genre:
                self.printBooks()

    def AuthorBooks(self, author):
        count = 0
        for x in range (len(self.libraryBooks)):
            if author == self.libraryBooks[x].author:
                count  = count +1
            print (author, "'s Total Number of Book are ", count)

    def BookEdition(self, edition):
        for x in range (len(self.libraryBooks)):
            if edition == self.libraryBooks[x].edition:
                print (edition)
                self.printBooks()
            break
     
  
    def printBooks(self):
        print("Length",self.libraryBooks)
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
l1.addBook(b1)
l1.addBook(b3)
l1.addBook(b4)
l1.addBook(b5)
l1.deletebook(b1)
l1.printBooks()
l1.ListGenre("Science")
l1.AuthorBooks("Dave")
l1.BookCount()
l1.BookEdition(3)





