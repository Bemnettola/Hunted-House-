
def welcome_scene():
    dark_start()
def dark_start():
#welcome scene
    print("Welcome to the Haunted Forest game!")
    input("Press any key to continue\n")
    first_choice()
def  first_choice(): 
    print("You are walking through a dark and scary forest and you find yourself at a crossroad.")
    print("One of the paths appears to be covered in cobwebs and insects")
    print("You see something at the end of the path, but it is not compltely clear")
    print("It appears to be alive")
    print("The other is full of dead trees and appears to lead to a rundown house")
    print("(a) to go down the first path.")
    print("(b) to go down the second path.")
    choice = input("what do you choose?")
 
    if choice == 'a':
       spider_scene()
 
       
    elif choice == 'b':
        walk_scene()
        mess_scene()
 
       
def spider_scene():
    print("you see a house")
    print("you get happy because you love houses and walk towards it")
    print('You hear a strange cackling coming from the house')
    print('Completely oblivious to the danger you are facing, you continue to walk')
    print('Red smoke starts coming out of the house and the door opens on its own')
    print('You continue walking with a huge grin on your face for some reason')
    print("while you were walking there were traps in the tree that you did not see")
    print("you fell into one of the traps and you die")
    print("Dont walk towards strangers houses in haunted forests")
    print("Game Over")
def walk_scene():  
    print("you see a giant spider, sitting on a giant web")
    print("it is sleeping")
    print('Youre are absolutely terrified')
    print('You see bones scattered about the area')
    print('This spider seems formidable')
    input("press any key to continue\n")  
def mess_scene():    
    print("you get closer to find a way to more forward")
    print("but it seems like the spider is in your way")
    print("what do you do?")
    print("(a) run away and go back to where you came")
    print("(b) poke it with a branch to make it move")
    choice = input("what do you choose?")
    if choice == 'a':
        walk_scene()
        mess_scene()
    elif choice =='b':
           spider_talking_scene()
def spider_talking_scene():  
    print("you wake the spider by poking it")
    print("Ouch! schrieks the spider in a surprisingly high pitched voice")
    print("In awe of the fact that a spider can talk you stand there speechless")
    print("That was not a very nice way to greet someone, the spider continues")
    print("The spider then tells you that he is not to be feared and in fact wants to help you")
    print("The spider helps you and you find a way out") 
    print('You arrive at witches house and the Spider, whos name you have discovered is Gerald, tells you that this witch cursed him')
    print('Gerald tells you that it is up to you to defeat the witch and save him from this curse')
    print('All you need to do is get her to say "What?"')
    input('You walk up to the door, press any key to start mumbling')
    print('What!? the witch yells')
    print('Immediately, Gerald and the witch return to being normal')
    print('Gerald jumps for joy and the former witch storms')
    print('Gerald gives you a ride home in his mini cooper')
    print("You won the game")
 
if __name__ == '__main__':
    welcome_scene()

