import random
from terminaltables import AsciiTable

"""
Rules Of The Game 

1. The total of the two dice are added to the total score
2. If one die is equal to one then all the points acquired are lost
3. If both dice are equal to one then the total score is cleared
4. First person to 100 wins
"""

def main():
    game = game_setup()

    index = 1
    while True:
        # Determine the current player and roll the dice
        player = f"Player {index}"
        score = roll(player, game)

        #  If the roll function does not returns the same score or zero then add the score the dictionary game
        if score != game[player] and score > 0:

            game[player] = score

            # The terminal table is then printed with the current players and scores 
            print_scores(game)

            # Check to see if the current roll has resulted in a winner 
            if winner(score, player):
                break
            
            # Ask the player for another roll 
            another_roll = input(f"\n{player} - Would you like to roll again? ")

            # If the input is yes then we continue to loop with the same player 
            if another_roll.lower().strip() in ['y', 'yes']:
                continue

            # If the input is not no then call the quit game function 
            elif another_roll.lower().strip() not in ['n', 'no']:
                # Quit game returns a boolean value if true then the we break out of the loop 
                if quit_game():
                    break
            
        # We then move on the next player
        game[player] = score
        if index >= len(game): index = 1
        else: index += 1



"""
Game setup determines how many players are involved in pig and 
returns a dictionary with all the players and the initalised score of zero
"""
def game_setup():
    score = {}

    welcome_message = """Welcome To Pig Dice Game\n\nTo Get Started Please Enter The Number Of Players Participating\n\nPlayers: """

    # Gather the number of players from user input
    number_of_players = int(input(welcome_message))

    # Create each player then add them to the dictionary 
    for num in range(number_of_players):
        number = num + 1
        player_name = f"Player {number}"

        score[player_name] = 0

    return score

"""
Dice randomly generates a list of two numbers that range between 1 and 6
"""
def dice():
    return [random.randint(1,6) for _ in range(2)]

"""
Handles the dice rolling and returns the appropriate score
"""
def roll(player, scores={}, roll=[]):

    # Gather the current score 
    current_score = scores[player]

    # This line is for testing purposes, I can pass down rolls not generated through the dice function
    if not roll: roll = dice()

    print(f"\n{player} rolled {roll} \n")

    # f both numbers in the list are equal to one then 0 is returned
    if roll[0] == 1 and roll[1] == 1:
        return 0

    # If either number is equal to one then the current score is returned
    if roll[0] == 1 or roll[1] == 1: return current_score

    # The new score is calculated by gathering the sum of the roll and adding it the current score
    new_score = current_score + sum(roll)
    return new_score       

"""
Determines the winner of the game the player name and score are passed down for evaluation
"""
def winner(score, player):
    if score >= 100:
        print(f"\n{player} is the winner with a total score of {score}") 
        return True
    else: return False

"""
This function is responsible for creating a terminal table and displaying the scores
""" 
def print_scores(game):

    heading, scores = [], []

    # Iterate through the dictionary to get the player name and score
    for player in game:
        heading.append(player)
        scores.append(game[player])
    
    table_data = [
        heading,
        scores
    ]

    table = AsciiTable(table_data)
    print(table.table)

"""
Handles the scenario where a player wants to end the game
""" 
def quit_game():
    quit_game = input("Would you like to exit the current game? ")

    if quit_game.lower().strip() in ['y', 'yes', 'q', 'quit', '']:
        print("Exiting Game")
        return True

    return False

if __name__ == "__main__":
    main()

