import oldgreeting
import random
print("merge oefening leuk!")

oldgreeting.greet()




def basicHaiku():

    return ["Hallo dit is een code", "test regel","On a day in spring."]

#zet hier je haiku functie neer, zie https://github.com/progsen/haikugitopdracht voor ideeen

haikus = [
    basicHaiku()
]

def randomHaiku():
    return random.choice(haikus)

def start():
    print("starting main")
    
    print(randomHaiku())

    pass



def student1():
    print("mijn naam is mucahid alkan")
    print("ik vind mw2 leuk")
    print("ik wil zometeen naar huis")

def student2Haiku():
    print("Mijn naam is Mostafa Nasar.")
    print("2")
    print("3")



start()