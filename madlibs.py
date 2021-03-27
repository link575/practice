import sys
print("Welcome to Mad Libs by OTIS")
while True:
    print("Please choose if you would like a space adventure (1) or horror story (2)")
    choice = int(input())
    if choice == 1:
        print("You chose a space adventure. Let's get started!")
        print("Pick a name")
        name = input()
        print("Pick an adjective")
        adj1 = input()
        print("Pick a verb ending in ing")
        vrb1 = input()
        print("Pick a noun")
        noun1 = input()
        print("Pick an adjective")
        adj2 = input()
        print("Now let's make a story")
        print("Long ago, there was a young boy named " + name + ". " + name + " was the leader of the most" + adj1 + " pirate space group in the entire\
 universe. One day, " + name + " thought about changing his life around and " + vrb1 + " for truth and justice. So he picked\
 up his " + noun1 + " and set off for a " + adj2 + " adventure.")
        print("Would you like to try again? (y/n)")
        retry = input()
        if retry == "y":
            continue
        elif retry == "n":
            break
        else:
            continue
    elif choice == 2:
        print("You chose a horror story....be prepared")
        print("Pick a name")
        name = input()
        print("Pick an adjective")
        adj1 = input()
        print("Pick a verb ending in ing")
        vrb1 = input()
        print("Pick a noun")
        noun1 = input()
        print("Pick an adjective")
        adj2 = input()
        print("Let's make something scary")
        print("One day, a boy named " + name + "decided he would visit a haunted house. " + name + " knew ghosts weren't " + adj1 + ", just a figment of\
the imagination. Suddenly," + name + " heard a crazy ass sound coming from the basement and started " + vrb1 + " for his life. He made it to the\
front" + noun1 + " turned the " + adj2 + " knob and then died. The end")
        print("Would you like to try again? (y/n)")
        retry = input()
        if retry == "y":
            continue
        elif retry == "n":
            break
        else:
            continue
print("I hope you enjoyed this copy of Otis' Mad Libs. type e to exit")
while True:
    e = str(input())
    if e == "e":
        sys.exit()
    else:
        print("Please type e to exit")
        continue
