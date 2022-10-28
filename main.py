import oldgreeting
import random
print("merge oefening leuk!")

oldgreeting.greet()




def basicHaiku():
    return ["Toward those short trees","test regel","On a day in spring."]

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

def student2Haiku():
    print("Mijn naam is Mostafa Nasar.")
    print("2")
    print("3")



start()