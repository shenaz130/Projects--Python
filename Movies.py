class Movies:
    def __init__(self,mno,title,mtype,rating):
        self.mno= mno
        self.title= title
        self.mtype = mtype
        self.rating = rating
        self.actorlist =[]
        


    def addActor(self,actor):
        self.actorlist.append(actor)
        print(len(self.actorlist),actor)

m1 = Movies(1123,"Run","Sci-fi",3.8)
m1.addActor("Jane,Dave")
m2 = Movies(15623,"Speed","Sci-fi",2.8)
m2.addActor("ABC")
m3 = Movies(14523,"Doctor Strange","Sci-fi",4.8)
m3.addActor("EFG")
m4 = Movies(15223,"ABC","Drama",2.8)
m4.addActor("HIK")
m5 = Movies(19623,"FAD","Drama",2.8)
m5.addActor("LMN")
print(m1.title)


class MovieStore:
    moviestore =[]
    movielist=[]
    def __init__(self):
        self.moviestore =[]
        
        
    def addMovie(self,aMovie):
        num = self.findMovie(aMovie.mno)
        if num == -1:
            self.moviestore.append(aMovie)
            #self.movielist.append(aMovie.title)
            print ("New Movie Added!")
            print("Length",len(self.moviestore))
        else:
            print("This movie already there!")
        
        
    def findMovie(self,mno):
        for x in range (len(self.moviestore)):
            if mno == self.moviestore[x].mno:
                return mno
        return -1
    
    def removeMovie(self,aMovie):
        num = self.findMovie(aMovie.mno)
        if num != -1:
            self.moviestore.remove(aMovie)
            print ("Movie Deleted!")
            print("Length",len(self.moviestore))
        else:
            print("Invalid Movie Code!")

    def removeMovieWithTitle(self,aMovie):
        num = self.findMovie(aMovie.mno)
        if num != -1:
            print( aMovie.title) 
            self.moviestore.remove(aMovie)
            print ("Movie Deleted!")
            print("Length",len(self.moviestore))
        else:
            print("Invalid Movie Code!")

    def displayRating(self, rate):
        for x in range (len(self.moviestore)):
            if rate <=  self.moviestore[x].rating:
                print("Rating",rate," and above movies - ")
                print("--------------------")
                print("Title  :" , self.moviestore[x].title)
                print("Code  :" , self.moviestore[x].mno)
                print("Type  :" , self.moviestore[x].mtype) 
                print("Rating  :" , self.moviestore[x].rating)
                print("Actors  :" , self.moviestore[x].actorlist)
                print("--------------------")
            else:
                print("no movies found!")

    def listType(self, mtype):
        for x in range (len(self.moviestore)):
            if mtype == self.moviestore[x].mtype:
                print("Type - ", mtype)
                print("--------------------")
                print("Title  :" , self.moviestore[x].title)
                print("Code  :" , self.moviestore[x].mno)
                print("Type  :" , self.moviestore[x].mtype) 
                print("Rating  :" , self.moviestore[x].rating)
                print("Actors  :" , self.moviestore[x].actorlist)
                print("--------------------")
    movielist=[]
    def listActors(self, actor):
        for x in range (len(self.moviestore)):
            #print((self.moviestore[x].actorlist))
            if actor in self.moviestore[x].actorlist:
                self.movielist.append(self.moviestore[x].title)
                #print(self.movielist)
                print("###################")
                print("Actor - ", actor)
                print("--------------------")
                print("Title  :" , self.moviestore[x].title)
                print("Code  :" , self.moviestore[x].mno)
                print("Type  :" , self.moviestore[x].mtype) 
                print("Rating  :" , self.moviestore[x].rating)
                print("Actors  :" , self.moviestore[x].actorlist)
                print("--------------------")
        print("Before Sorted Movie List - ",self.movielist)
        self.movielist.sort()
        print("Sorted Movie List - ",self.movielist)
        print("--------------------")
      
       

    def listMovies(self):
        for x in range (len(self.moviestore)):
            print("--------------------")
            print("Title  :" , self.moviestore[x].title)
            print("Code  :" , self.moviestore[x].mno)
            print("Type  :" , self.moviestore[x].mtype) 
            print("Rating  :" , self.moviestore[x].rating)
            print("Actors  :" , self.moviestore[x].actorlist)
            print("--------------------")

    ratelist= []
    def sortbyrating(self, rate):
        for x in range (len(self.moviestore)):
            self.ratelist.append(self.moviestore[x].rating)
            #sorted(self.ratelist)
        sort_numbers = sorted(self.ratelist, reverse=True)
        print("Sorted list (Discending):",sort_numbers)

        print("Printing high rating Movies")
        for x in range (len(self.ratelist)):
            if rate <=  self.moviestore[x].rating:
                    print("Rating",rate," and above movies - ")
                    print("--------------------")
                    print("Title  :" , self.moviestore[x].title)
                    print("Code  :" , self.moviestore[x].mno)
                    print("Type  :" , self.moviestore[x].mtype) 
                    print("Rating  :" , self.moviestore[x].rating)
                    print("Actors  :" , self.moviestore[x].actorlist)
                    print("--------------------")
          

s1 = MovieStore()
s1.addMovie(m1)
s1.addMovie(m2)
s1.addMovie(m3)
s1.addMovie(m4)
s1.addMovie(m5)
#s1.removeMovie(m1)
#s1.removeMovieWithTitle(m3)
s1.listMovies()
print("*******************")
s1.listType("Drama")
s1.listActors("ABC")
s1.listActors("EFG")
s1.displayRating(3)
s1.displayRating(2)
s1.listActors("Jane,Dave")
s1.listActors("HIK")  
s1.sortbyrating(3)     
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        