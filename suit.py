import random
import os

def clear_screen():
    """Membersihkan layar"""
    os.system("cls" if os.name == "nt" else 'clear')

def play_suit():
    options = {
        '1' : {'name': 'Rock', 'emoji': '✊', 'beats': 'Scissors'},
        '2': {'name': 'Paper', 'emoji': '✋', 'beats': 'Rock'},
        '3': {'name': 'Scissors', 'emoji': '✌️', 'beats': 'Paper'}
    }

    clear_screen()
    print("===================")
    print("Rock Paper Scissors")
    print("===================")
    print()

    for key, value in options.items():
        print(f"{key}) {value['emoji']}")
    
    player_input = ''
    while player_input not in options:
        player_input = input("Pick a number: ")
        if player_input not in options:
            print("Invalid choice. Please pick 1, 2, or 3.")
    
    player_choice = options[player_input]
    cpu_key = random.choice(list(options.keys()))
    cpu_choice = options[cpu_key]

    print()

    print(f"You chose: {player_choice['emoji']}")
    print(f"CPU chose: {cpu_choice['emoji']}")

    if player_choice['name'] == cpu_choice['name']:
        print("It's a tie!")
    elif player_choice['beats'] == cpu_choice['name']:
        print("The player won!")
    else:
        print("The CPU won!")


if __name__ == "__main__":
    play_suit()