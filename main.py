from functions import shou_menu, game_statistics, start_new_game, roll_dice, start_game, calculate_winner,display_game_results, print_game
from i_or import reading_from_json

def main():
    while True:
        user_input = shou_menu()
       
        if user_input == 1:
            dict_name = start_game()
            calculate_winner(dict_name)
            display_game_results(dict_name)
            
    
        if user_input == 2:
            all_the_game = reading_from_json()
            print_game(all_the_game)

        if user_input == 3:
            game_statistics()
        if user_input == 4:
            break


















if __name__ == "__main__":
    main ()