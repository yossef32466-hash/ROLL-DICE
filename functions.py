import random
from i_or import writing_for_json, reading_from_json
global ROUNDS 
ROUNDS = len(reading_from_json())
def shou_menu():
    while True:
            text = input("""===============================
                        ROLL DICE
            ================================

            🎲1. Start New Game
            🎲2. View Game History
            🎲3. View Statistics
            🎲4. Exit
            Choose an option:   """)
            if not text.isdigit():
                print("Please enter a number.")
                continue
            num = int(text)
            if num < 1 or num > 4:
                print("The number must be between 1 and 4.")
                continue
            return num
def start_new_game():
    while True:
        user_name = input("Plaese enter your name:   ").strip()
        raound_game = input("Enter the number of rounds you want.")
        if user_name == '':
            continue

        if not raound_game.isdigit():
            print("Please enter a number.")
            continue

        num = int(raound_game)
        if num < 1 or num > 10:
            print("The number must be between 1 and 4.")
            continue
        return user_name, num

def player_queue_input():
    input("Roll the die by pressing a key.  🎲")
        

def roll_dice()-> int:
    return random.randint(1,6)



def start_game():
    global ROUNDS
    ROUNDS +=1
    user_name, raound_game = start_new_game()
    Player_Turns = 0
    Computer_Queues = 0
    for i in range(raound_game):
        player_queue_input()
        Player_Turn = roll_dice()
        print(f"Player_Turn:{Player_Turn}")
        Computer_Queue = roll_dice()
        print(f"Computer_Queue:{Computer_Queue}")
        if Player_Turn > Computer_Queue:
            Player_Turns += 1
        elif Player_Turn < Computer_Queue:
            Computer_Queues += 1
        else:
            pass
              


    dict_game =  {
            "round": ROUNDS,
            "player_dice":  Player_Turns,
            "computer_dice": Computer_Queues,
            "winner": user_name
                }

    
    writing_for_json(dict_game)
    return dict_game


def calculate_winner(dicti):
    if dicti['player_dice'] > dicti['computer_dice']:
        return dicti
    if dicti['player_dice'] < dicti['computer_dice']:
        new_dicti = dicti['winner'] = 'computer'
        return new_dicti
    else:
        return dicti
                
def display_game_results(game):
    print(game)

  


def print_game(list_game):
    for dicti in list_game:
        print(f"Number Game: {dicti['round']}\n player_dice: {dicti['player_dice']}\n computer_dice: {dicti['computer_dice']}\n winner: {dicti['winner']}")
        print("-----------------------")



def game_statistics():
    global ROUNDS
    data_games = reading_from_json()
    {"player_name": "Moshe",
    "rounds": ROUNDS,
    "player_score": 2,
    "computer_score": 1,
    "winner": "Moshe",
    "results":m }



