import random
print("                             This programm will choose a random movie for selected genere:")
print("                                               Movie Genere:")
print("                                                 1.Action")
print("                                                 2.Adventure")
print("                                                 3.Animation")
print("                                                 4.Comedy")
print("                                                 5.Horror")
print("                                                 6.Indian")
print("                                                 7.Iranian")
print("                                                 8.Korean")
print("                                                 9.Sci-fi")
print("                                                 10.Thriller")
movie_genere = {1:"Action",2:"Adventure",3:"Animation",4:"Comedy",5:"Horror",6:"Indian",7:"Iranian",8:"Korean",9:"Sci-fi",10:"Thriller"}
print("                         How would You Like to select a Movie Genere Automaticaly or Manualy")
print("                                                 1.Automaticaly")
print("                                                 2.Manualy")
option_choose = int(input("                                                 I Choose:"))

if(option_choose == 1):
    user_choose = random.randint(1,10)
    print("="*100)
    print("                                         Genere Recommended : {0}".format(movie_genere[user_choose]))
    
elif(option_choose==2):
    user_choose = int(input("I choose: "))
    print("="*100)
    print("                                                 You Select {0} Genere".format(movie_genere[user_choose]))

def get_movie_num():
    movie_num = random.randint(1,10)
    return movie_num
def get_movie_name():
    if(user_choose == 1):
        action = {1:"Captain America",2:"Avengers",3:"Ironman",4:"Hulk",5:"Thor",6:"Spiderman",7:"Dr. Strange",8:"Black Panther",9:"Man of Steel",10:"Batman"}
        movie_name = action[get_movie_num()]
        return movie_name
        
    elif(user_choose == 2):
        adventure ={1:"Indiana Jones",2:"Journey: To center of earth",3:"Journey:To the mysterius island",4:"The Great OZ",5:"Chronicles of narnia",6:"Jumanji",7:"Gold",8:"Pirates of the carebian",9:"Point Break",10:"WHO am I"}
        movie_name = adventure[get_movie_num()]
        return movie_name
        
    elif(user_choose == 3):
        animation={1:"COCO",2:"Despicable Me",3:"Up",4:"How to train Your Dragon",5:"Megamind",6:"Epic",7:"Rio",8:"The Good Dinosorous",9:"Aladin",10:"Hotel Transylvania"}
        movie_name = animation[get_movie_num()]
        return movie_name
        
    elif(user_choose == 4):
        comedy={1:"The mask",2:"The rat race",3:"Home alone",4:"The Trueman Show",5:"Yesman",6:"American Pie",7:"The Circus",8:"Life of Dog",9:"The Dictator",10:"The Hangover"}
        movie_name = comedy[get_movie_num()]
        return movie_name
        
    elif(user_choose == 5):
        horror={1:"Evil Dead",2:"The Conjuring",3:"The sinister",4:"IT",5:"Abraham Lincon: The vampire Hunter",6:"Resident Evil",7:"Shaun of Dead",8:"room No 302",9:"Raaz",10:"Ragini MMS"}
        movie_name = horror[get_movie_num()]
        return movie_name
        
    elif(user_choose == 6):
        indian={1:"DDLJ",2:"KGKG",3:"Andaz Apna Apna",4:"Kal Ho naa Ho",5:"Calte calte",6:"Race",7:"Krish",8:"Guzarish",9:"mahenjodaro",10:"Bahubali"}
        movie_name = indian[get_movie_num()]
        return movie_name
        
    elif(user_choose == 7):
        iranian={1:"The sellsman",2:"The Prophet(sm)",3:"There Are Things You Don't Know ",4:"Here Without Me ",5:"The Color Purple ",6:"We Only Live Twice ",7:"A Separation",8:"The Song of Sparrows ",9:"Felicity Land ",10:"Border Café"}
        movie_name = iranian[get_movie_num()]
        return movie_name

    elif(user_choose == 8):
        korean={1:"Forgotten",2:"OldBoy",3:"Garo",4:"The Admiral",5:"Ode to My Father",6:"The Thieves ",7:"Miracle in Cell No. 7 ",8:"The Host ",9:"The Attorney ",10:"The King and the Clown"}
        movie_name = korean[get_movie_num()]
        return movie_name
        
    elif(user_choose == 9):
        scifi={1:"Star wars",2:"Star Trek",3:"Future Past",4:"Transporter",5:"The Flash",6:"The fifth Sense",7:"Imitation Game",8:"",9:"",10:""}
        movie_name = scifi[get_movie_num()]
        return movie_name
        
    elif(user_choose == 10):
        thriller={1:"Kill Bill",2:"The Godfather",3:"Goodfellas",4:"Seven",5:"Pulp fiction",6:"Fight Club",7:"Heat",8:"Shawsank Redemption",9:"The Dark Knight",10:"Transporter"}
        movie_name = thriller[get_movie_num()]
        return movie_name
    
print("                                         Movie Recommended :{0}".format(get_movie_name()))
print("="*100)
