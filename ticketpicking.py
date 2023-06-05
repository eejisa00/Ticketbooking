user_name_li=[]
pwd_li=[]
moviee_list=[]

class userprofile:
    def __init__(self,user_id,user_name,gender,phone_no,pwd):
        self.user_id=user_id
        self.user_name=user_name
        user_name_li.append(self.user_name)
        self.gender=gender
        self.phone_no=phone_no
        self.pwd=pwd
        pwd_li.append(self.pwd)





    def login(self):
        self.user_name=input("Enter your username : ")
        self.pwd=input("Enter your pwd : ")
        if(self.user_name in user_name_li and self.pwd in pwd_li):
            print("Welcome ",self.user_name+"!")
            x=movie_listings.show_movie(self)
            
            
            
        else:
            print("Invalid Login!!")
            

class movie_list:
    def __init__(self,genre,movie_id,movie_name,length_of_movie,release_date):
        self.genre=genre
        self.movie_id=movie_id
        self.movie_name=movie_name
        
        self.length_of_movie=length_of_movie
        self.release_date=release_date
        

class movie_listings:
    def show_movie(self):
        print("Available Languages : Tamil,Telugu")
        
        lang=input("Enter the language you wish : ")
        if(lang=="Tamil"):
            movie1=movie_list("Love",1,"Remo","2.30","12/06/2023")
            movie2=movie_list("Emotional",2,"Veeran","2.46","23/06/2023")
            movie3=movie_list("Comedy",3,"Komali","2.34","12/06/2023")
            
        elif(lang=="Telugu"):
            movie1=movie_list("Love",1,"Majili","2.30","12/06/2023")
            movie2=movie_list("Comedy",2,"Mento","2.45","13/06/2023")
            movie3=movie_list("Horror",3,"Kanchana","2.30","12/06/2023")
        
        moviee_list.append(movie1)
        moviee_list.append(movie2)
        moviee_list.append(movie3)
        print("Available movies In ",lang)
        print()
        
        for i in moviee_list:
            print("Movie genre: ",i.genre)
            
            print(i.movie_id)
            print(i.movie_name)
            
            print(i.length_of_movie)
            print(i.release_date)
            print("...................................")
            


    
if __name__ == "__main__":
    user1=userprofile(1,"Ajitha","Female",1234567890,"Ajitha123")
    user1=userprofile(2,"Pavan","Male",9876543210,"Pavan123")
    k=user1.login()
   
    
    
    
    
    
    
