import random
import textwrap

def print_bold(msg, end='\n'):
    print("\033[1m" + msg + "\033[0m", end=end)

def print_dotted_line(width=72):
    print('-'*width)

def show_theme_message(width):
    print_dotted_line()
    print("\033[1m" + "Attack of The Orcs v0.0.1;" + "\033[0m")

    msg = (
            "The war between humans and their arch enemies, Orcs, was in the "
            "offing. Sir Foo, one of the brave knights guarding the southern "
            "plains began a long journey towards the east through an unknown "
            "dense forest. On his way, he spotted a small isolated settlement."
            " Tired and hoping to replenish his food stock, he decided to take"
            " a detour. As he approached the village, he saw five huts. There "
            "was no one to be seen around. Hesitantly, he  decided to enter.."
          )
    print(textwrap.fill(msg, width=width))

def show_game_mission():
    print_bold("Mission:")
    print("\tChoose a hut where Sir Foo can rest...")
    print_bold("TIP:")
    print("Be careful as there are enemies lurking around!")
    print_dotted_line()

def occupy_huts():
    huts = []
    occupants = ['enemy', 'friend', 'unoccupied']
    while len(huts) < 5:
        coumputer_choice = random.choice(occupants)
        huts.append(coumputer_choice)
    return huts

def reveal_occupants(idx, huts):
    # Print the occupant info
    print("Revealing the occupants...")
    # print('*'*5, idx, huts[idx-1])
    msg = ""
    for i in range(len(huts)):
        occupant_info = "<%d:%s>" % (i + 1, huts[i])
        if i + 1 == idx:
            occupant_info = "\033[1m" + occupant_info + "\033[0m"
        msg += occupant_info + " "
    print("\t" + msg)
    print_dotted_line()

def process_user_choice():
    # Prompt user to select a hut
    msg = "\033[1m" + "Choose a hut number to enter (1-5): " + "\033[0m"
    user_choice = input("\n" + msg)
    idx = int(user_choice)
    return idx

def main():
    keep_playing = 'y'
    width = 72
    show_theme_message(width)
    show_game_mission()

    while keep_playing == 'y':
        huts = occupy_huts()
        idx = process_user_choice()
        reveal_occupants(idx, huts)

        print("\033[1m" + "Entering hut %d..." % idx + "\033[0m", end=' ')

        # Determine and announce the winner
        if huts[idx-1] == 'enemy':
            print("\033[1m" + "YOU LOSE :( Better luck next time!" +
                  "\033[0m")
        else:
            print("\033[1m" + "Congratulations! YOU WIN!!!" + "\033[0m")

        print_dotted_line()
        keep_playing = input("Play again? Yes(y)/No(n):")

if __name__ == "__main__":
    main()
