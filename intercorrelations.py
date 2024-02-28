import random
#Imports a dictionary with categories to get selected_categories
from categories import categories
import time
import sys
lives = 4

grid = [ #Empty grid that will be filled with selected_categories
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
]

def typewriter_effect(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)

def shuffle_grid(grid):
    flat_grid = [word for row in grid for word in row] #Turns the grid into a list of all the words in the grid
    random.shuffle(flat_grid) #Shuffles the list of words
    index = 0
    for row in range(len(grid)): #Puts grid back together with the shuffled words
        for col in range(len(grid[row])):
            grid[row][col] = flat_grid[index]
            index += 1

def play_again_function(): #Asks user if they want to play again
    while True:
        user_input = input("Wanna play Intercorrelations? (Y or N)").lower()
        if user_input == 'y':
            return True
        elif user_input == 'n':
            typewriter_effect("Goodbye!\n")
            break
        else:
            typewriter_effect("Invalid input. Please enter Y or N")

def intercorrelations():
    play_game = True
    while play_game:
        main()
        play_game = play_again_function()

def populate_grid(selected_categories, grid):
    row = 0
    for category in selected_categories:
        col = 0
        for word in category["Words"]:
            grid[row][col] = word
            col += 1
        row += 1

def display_game_state(lives):
    if not game_won:
        print("Lives: ", lives, "\n")
        typewriter_effect("Enter 'shuffle' at any point to shuffle the board\n\n")
        for row in grid:
            print(row)

def select_categories(): #Selects categories for the game
    selected_categories = random.sample(categories, 4)
    return selected_categories

def check_win(guessed_categories, selected_categories):
    for selected_category in selected_categories:
        if selected_category not in guessed_categories: #If any selected category is not found in the guessed categories, return False
            return False
    return True #If all selected categories are found in the guessed categories, return True (game won)

def get_guess(guessed_categories, selected_categories):
    while True:
        global lives
        guess = input("\nTake a guess (e.g., cake icecream pie pudding): ").lower().split()

        #Shuffle the grid if the user enters "shuffle"
        if guess == ["shuffle".lower()]:
            shuffle_grid(grid)
            typewriter_effect("Grid shuffled!")
            display_game_state(lives)
            continue
        elif len(guess) != 4 or any(not word.isalpha() for word in guess): #Guess must be in correct syntax or user trys again
            typewriter_effect("Invalid input. Please enter four alphabetical words separated by spaces.")
            get_guess(guessed_categories, selected_categories)

        #Check if the guess has already been made
        if guess in [item["Guess"] for item in guessed_categories]:
            typewriter_effect("You already guessed this category. Try again.")
            continue

        #Sort the guessed words so that the same words cannot be guessed in a different order
        guess.sort()

        #Add the guess to the guessed categories dictionary
        guessed_categories.append({"Guess": guess})

        #Check if the guess matches any of the selected categories
        for category in selected_categories:
            if sorted(category["Words"]) == sorted(guess):
                typewriter_effect("Correct guess!")
                return True
        else:
            typewriter_effect("Incorrect guess!")
            lives -= 1
            return False

def main():
    global game_won
    global lives
    game_won = False
    guessed_categories = []  #Dictionary to store guessed categories
    selected_categories = []  #List to store selected categories
    selected_categories = select_categories()
    populate_grid(selected_categories, grid) #Populate the grid with words from the selected categories

    typewriter_effect("\nWelcome to the Intercorrelations! \n")
    typewriter_effect("Here's the grid of words you have to group into categories: \n")
    shuffle_grid(grid)
    display_game_state(lives)

    while lives > 0 and not game_won:
        if get_guess(guessed_categories, selected_categories):
            #Remove the guessed category from the list of selected categories
            for category in selected_categories:
                if sorted(category["Words"]) == sorted(guessed_categories[-1]["Guess"]):
                    selected_categories.remove(category)
                    break  #Exit the loop after removing the category

        #If all the selected categories are removed, the player wins
        if not selected_categories:
            game_won = True

        #Update game state and continue loop
        display_game_state(lives)

    if game_won:
        typewriter_effect("Congrats! You won!\n")
    else:
        typewriter_effect("You lose!\n")
    play_again_function()

intercorrelations()