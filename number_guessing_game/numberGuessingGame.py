import random

def display_gameplay():
    """
    Displays the gameplay
    : return: None
    """
    print('\nWelcome to Number Guessing Game!')
    print('In this game you\'ve just 10 trials to guess a number between the range of 1-10')
    print('Note: enter \'exit\' to end game')

def startGame():
    """
    Gets user response to start the game
    : return: str
    """
    displayGameplay = display_gameplay()
    POSSIBLE_RESPONSES = ['Y','YES','N','NO','EXIT']
    user_response = input('\nStart game? (yes/no): ').strip().upper()
    while user_response not in POSSIBLE_RESPONSES:
        print('\nInvalid Input!')
        user_response = input('\nStart game? (yes/no): ').strip().upper()
    else: return user_response

def game():
    """
    Controls the game
    : return: None
    """
    play_game = startGame()
    number_of_trials = 7
    while play_game == 'YES' or play_game == 'Y':
        POSSIBLE_NUMBER_PICKS = [str(i) for i in range(1,11)]
        user_number = input('\nGuess a number between the range of 1-10: ').strip().upper()
        while user_number not in POSSIBLE_NUMBER_PICKS and user_number != 'EXIT' :
            print('Invalid Input!')
            user_number = input('\nGuess a valid number between the range of 1-10: ').strip().upper()
        if user_number == 'EXIT':
            print('Bye Player!')
            break
        else:
            computer_number = random.randint(1,10)
            user_number = int(user_number)
            if user_number < computer_number:
                number_of_trials -= 1
                print(f'Oops, {user_number} is too low')
                if number_of_trials != 0:
                    print(f'You\'ve {number_of_trials} trial(s) left')
                    play_game = input('\nGuess again? (yes/no): ').strip().upper()
                else:
                    print(F'\nGame over!, you\'ve 0 trial left')
                    break
            elif user_number > computer_number:
                number_of_trials -= 1
                print(f'Oops, {user_number} is too high')
                if number_of_trials != 0:
                    print(f'You\'ve {number_of_trials} trial(s) left')
                    play_game = input('\nGuess again? (yes/no): ').strip().upper()
                else:
                    print(F'\nGame over!, you\'ve 0 trial left')
                    break
            elif user_number == computer_number:
                number_of_trials -= 1
                print(f'Congratulations!!..you guessed right, after {7 - number_of_trials} trial(s)')
                play_game = input('\nDo you wish to play again? (yes/no): ').strip().upper()
                number_of_trials = 7 

game()
