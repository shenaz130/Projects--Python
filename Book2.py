class Book:
    def __init__(self,isbn,title):
        self.isbn = isbn
        self.title = title
      
    
b1= Book (111,"Twlight",)
b2= Book (171,"1984")
b3= Book (121,"Unwind")
b4= Book (131,"Scarlett")
b5= Book (141,"Elemental")
b6= Book (181,"java")


class Library:
    firstlibrary = []
    def __init__ (self):
        self.firstlibrary = []


    def addBook(self, aBook):
        index = self.findBook(aBook.isbn)
        if index == -1:
            self.firstlibrary.append(aBook)
            print("New Book Added!", aBook.title)
        else:
            print("This Book is already in the Collection!", aBook)
            print()
            
            
    def findBook(self,nIsbn):
        for x in range (len(self.firstlibrary)):
            if nIsbn == self.firstlibrary[x].isbn:
                return x   
        return -1

    barrowBooklist = []
    def barrowBook(self,title):
        i = 0
        for x in range (len(self.firstlibrary)):
            if title == self.firstlibrary[x].title:
                self.barrowBooklist.append(self.firstlibrary[x].title)
                i = i +1
                print("You Borrowed ",self.firstlibrary[x].title)
                if i < 2:
                    return print ("Someone already borrowed") 
                break 
            return print ("Book is not in the catelog!")
            
        
    def printBooks(self):
        print("Books available in the First Library: ")
        print("--------------------")
        for x in range (len(self.firstlibrary)):
            print("Title  :" , self.firstlibrary[x].title)

    def returnBook(self,title):
        for x in range (len(self.barrowBooklist)):
            if title == self.barrowBooklist[x]:
                print("You Returned ",self.barrowBooklist[x])
                break

#Second Library ------------------------------------
    secondLibrary = []
    def __init__ (self):
        self.secondLibrary = []


    def addBook2(self, aBook):
        index = self.findBook(aBook.isbn)
        if index == -1:
            self.secondLibrary.append(aBook)
            print("New Book Added to the Second Library!", aBook.title)
        else:
            print("This Book is already in the Collection!", aBook)
            print()
            
            
    def findBook2(self,nIsbn):
        for x in range (len(self.secondLibrary)):
            if nIsbn == self.secondLibrary[x].isbn:
                return x   
        return -1

    barrowBooklist2 = []
    def barrowBook2(self,title):
        i = 0
        for x in range (len(self.secondLibrary)):
            print(len(self.secondLibrary))
            if title == self.secondLibrary[x].title:
                self.barrowBooklist2.append(self.secondLibrary[x].title)
                i = i +1
                print("You Borrowed ",self.secondLibrary[x].title)
                if i < 2:
                    print ("Someone already borrwed") 
                break
            return print ("Book is not in the catelog!")
            
        
    def printBooks2(self):
        print("Books available in the Second Library: ")
        print("--------------------")
        for x in range (len(self.secondLibrary)):
            print(len(self.secondLibrary))
            print("Title  :" , self.secondLibrary[x].title)
            print("--------------------")
        

    def returnBook2(self,title):
        for x in range (len(self.barrowBooklist2)):
            if title == self.barrowBooklist2[x]:
                print("You Returned ",self.barrowBooklist2[x])
                break

        

firstLibrary = Library()
secondLibrary = Library()
print()
print("Library hours:")
print("Library are open daily from 9 am to 5pm.")
print()
print("Library addresses:")
print("10 Main St.")
print("228 Liberty St.")
print()


firstLibrary.addBook(b1)
firstLibrary.addBook(b2)
firstLibrary.addBook(b3)
firstLibrary.addBook(b4)
firstLibrary.addBook(b5)
print("--------------------")
firstLibrary.barrowBook("Twlight")
print("--------------------")
firstLibrary.barrowBook("ABC")
firstLibrary.printBooks()
firstLibrary.returnBook("Twlight")

secondLibrary.addBook2(b6)
secondLibrary.barrowBook2("Twlight")
secondLibrary.barrowBook2("java")
secondLibrary.returnBook2("java")
secondLibrary.printBooks2()
