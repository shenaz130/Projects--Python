class Library:
    booklist= []
    def __init__ (self,name):
        self.name = name
        self.booklist = []

    def addBook(self,aBook):
        i = self.findBook(aBook.title)
        #print(i)
        if i == -1:
            self.booklist.append(aBook)
            print("new book added to the library",aBook)
            print("book count is =",len(self.booklist))
            
        else:
            print("Cannot add Book is already there")
        
        
    def findBook(self, title):
        #print("------", (len(self.booklist)))
        for x in range (len(self.booklist)):
            if title == self.booklist[x].title:
              print(title,"- book is in the library")
              return 1
        return -1
        
    def removeBook(self,aBook):
        i = self.findBook(aBook.title)
        if i != -1:
            self.booklist.remove(aBook)
            print ("Book Deleted! - Length",len(self.booklist))
        else:
            print ("Invalid Book Code!")

        
    def displayBooks(self):
        print("---------------------------")
        print("Welcome to the Slone Library")
        print("---------------------------")
        print("Book name -|- Author -|- Type")
        print("---------------------------")
        #print("book count is =",len(self.booklist))
        for x in range (len(self.booklist)):
            print(self.booklist[x].title, "-|-",self.booklist[x].author, "-|-",self.booklist[x].btype)
            print("---------------------------")


l1 = Library("Slone")

class Book(Library):
    def __init__(self, title, author):
        self.title = title
        self.author = author

b1 = Book("Computer-Science", "Jade-David")
#print(b1.title,b1.author)

class AudioBook(Book):
    def __init__(self,title, author,btype,duration, narrator):
        Book.__init__(self, title, author)
        self.btype = btype
        self.duaration = duration
        self.narrator = narrator


ab1 = AudioBook("Automic-habits","Mike-James","Audio_Book",140,"Richard")
#print(ab1.title,ab1.author)


class WrittenBook(Book):
    def __init__(self,title, author,npages):
        Book.__init__(self, title, author)
        self.npages = npages


wb1 = WrittenBook("Computer-Science", "Jade-David",350)
#print(wb1.title,wb1.author,wb1.npages)

class PrintedBook(WrittenBook):
    def __init__(self,title, author,btype,npages,isbn,hardcover):
        WrittenBook.__init__(self, title, author, npages)
        self.btype = btype
        self.isbn = isbn
        self.hardcover = hardcover


pb1 = PrintedBook("Computer-Science", "Jade-David","Printed_Book",350,77888,True)
#print(pb1.title,pb1.author,pb1.npages,pb1.isbn,pb1.hardcover)

class EBook(WrittenBook):
    def __init__(self,title, author,btype,npages,size):
        WrittenBook.__init__(self, title, author, npages)
        self.btype = btype
        self.size = size


eb1 = EBook("Chemistry", "Paul-Morgan","EBook",700,7.8)
#print(eb1.title,eb1.author,eb1.npages,eb1.size)


l1.addBook(ab1)
l1.addBook(eb1)
l1.addBook(pb1)
l1.displayBooks()
#l1.findBook("Chemistry")
l1.removeBook(pb1)
l1.displayBooks()

