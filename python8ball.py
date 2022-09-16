import random
import time

rand_number = random.randint(1,7)



print("I am the magic 8 ball.")
print("")
time.sleep(1)

#asks for name

name = input("What is your name?: ")

#if the name does not have all letters, ask again

while not name.isalpha():
    name = input("Please enter a valid name: ")




    
print("")
time.sleep(1)
print("Hello", name + ".") #greetings
print("")
time.sleep(1)


#chance function to ask for a number
def chance():
    value = int(input("Pick a number between 1 and 7: "))
    rand_number = random.randint(1,7) #random number
    #delay
    time.sleep(1)
    print("")
    
    if rand_number == value:
        print("You will be the luckiest person in the world " + name + ".")
        

    elif rand_number == 1:
        print("You will accomplish great things " + name + ".")

        
    elif rand_number == 2:
        print("You will retire early " + name + ".")
      
    elif rand_number == 3:
        print("You will receive $1,000,000 in the future " + name + ".")

  
    elif rand_number == 4:
        print("You will be the next Albert Einstein " + name + ".")


    elif rand_number == 5:
        print("You will become a world leader " + name + ".")

    elif rand_number == 6:
        print("You will have good fortune " + name + ".")
    
    else:
        print("You will have eternal life " + name + ".")

    print("")
    time.sleep(1)
    #retry option
    retry = input("Do you want to try again?: ")

    if retry.lower() == "yes" or retry.lower() == "y":
        print("")
        chance()
    else:
        print("See you later.") 



chance() #calls function


"""
This is a magic 8 ball game where it asks you to choose a number between 1 and 7.
It uses an input function to ask for your name, number, and if you would like to retry.
It uses multiple if statements to give different answers based on luck.
It also has a delay after each response so it is easier to read. It uses random.randint to generate
a number between 1 and 7.





"""






