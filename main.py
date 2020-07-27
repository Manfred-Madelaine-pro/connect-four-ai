def print_menu():
    print ("Welcome to Puissance 4 !\n")

def make_a_choice(choices, actions):
    #print choices
    for idx, c in enumerate(choices):
        print("\t" + str(idx) + ") " + c)

    choice = input("\nSelect an option\n> ")

    while choice not in [str(i) for i in range(len(choices))]:
        choice = input("\nNot a valid choice ! Please, try again\n> ")
    
    #do the correecsponding action
    actions[int(choice)]()

def quit_game():
    print ("Good bye !")

def play():
    print ("play")

# --------------------------------------
#               Main
# --------------------------------------

if __name__ == '__main__':
    print_menu()
    start = ["play", "quit"]
    make_a_choice(start, [play, quit_game])