from random import shuffle, sample
from time import sleep
from sys import stdout
#Imports a dictionary with categories to get selected_categories
from categories import categories

lives = 4

grid = [ #Empty grid that will be filled with selected_categories
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
]

def typewriter_effect(text):
    for character in text:
        stdout.write(character)
        stdout.flush()
        sleep(0.02)

def shuffle_grid(grid):
    flat_grid = [word for row in grid for word in row] #Turns the grid into a list of all the words in the grid
    shuffle(flat_grid) #Shuffles the list of words
    index = 0
    for row in range(len(grid)): #Puts grid back together with the shuffled words
        for col in range(len(grid[row])):
            grid[row][col] = flat_grid[index]
            index += 1

def play_again_function(): #Asks user if they want to play again
    while True:
        user_input = input("\033[1;37mWanna play Intercorrelations? (Y or N)\033[0m").lower()
        if user_input == 'y':
            return True
        elif user_input == 'n':
            typewriter_effect("\033[1;37mGoodbye!\n\033[0m")
            break
        else:
            typewriter_effect("\033[1;37mInvalid input. Please enter Y or N\033[0m")

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
    print("\033[1;37mLives:", lives, "\n\033[0m")
    print("\033[1;37mEnter 'shuffle' at any point to shuffle the remaining words\n\033[0m")

    #Find the length of the longest word in the grid
    max_word_length = max(len(word) for row in grid for word in row)

    #Print the grid with remaining words
    for row in grid:
        for word in row:
            print("\033[1;37m" + word.ljust(max_word_length) + "\033[0m", end=" | ")  #Highlight words in yellow with proper spacing
        print()

def select_categories(): #Selects categories for the game
    selected_categories = sample(categories, 4)
    return selected_categories

def check_win(guessed_categories, selected_categories):
    for selected_category in selected_categories:
        if selected_category not in guessed_categories: #If any selected category is not found in the guessed categories, return False 
            return False
    return True #If all selected categories are found in the guessed categories, return True (game won)

def get_guess(guessed_categories, selected_categories):
    while True:
        global lives
        guess = input("\033[1;37m\nTake a guess (e.g., cake icecream pie pudding): \033[0m").lower().split()

        #Shuffle the grid if the user enters "shuffle"
        if guess == ["shuffle".lower()]:
            shuffle_grid(grid)
            typewriter_effect("\033[1;37mGrid shuffled!\033[0m")
            display_game_state(lives)
            continue
        elif len(guess) != 4 or any(not word.isalpha() for word in guess): #Guess must be in correct syntax or user trys again
            typewriter_effect("\033[1;37mInvalid input. Please enter four alphabetical words separated by spaces.\033[0m")
            get_guess(guessed_categories, selected_categories)

        #Check if the guess has already been made
        if guess in [item["Guess"] for item in guessed_categories]:
            typewriter_effect("\033[1;37mYou already guessed this category. Try again.\033[0m")
            continue

        #Sort the guessed words so that the same words cannot be guessed in a different order
        guess.sort()

        #Add the guess to the guessed categories dictionary
        guessed_categories.append({"Guess": guess})

        #Check if the guess matches any of the selected categories
        for category in selected_categories:
            if sorted(category["Words"]) == sorted(guess):
                typewriter_effect("\033[1;37mCorrect guess!\033[0m")
                return True
        else:
            typewriter_effect("\033[1;37mIncorrect guess!\033[0m")
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

    typewriter_effect("\033[1;37m\nWelcome to the Intercorrelations!\n\033[0m")
    typewriter_effect("\033[1;37mHere's the grid of words you have to group into categories: \n\033[0m")
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
        typewriter_effect("\033[1;37mCongrats! You won!\n\033[0m")
    else:
        typewriter_effect("\033[1;37mYou lose!\n\033[0m")
    play_again_function()

intercorrelations()