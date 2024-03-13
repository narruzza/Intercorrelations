from random import shuffle, sample
from time import sleep
from sys import stdout
#Imports a dictionary with categories to get selected_categories
from categories import categories

lives = 4

grid = [
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
]

correct_guesses_grid = [["" for _ in range(4)] for _ in range(4)]  #Empty grid that will be filled with selected_categories

def typewriter_effect(text):
    for character in text:
        stdout.write(character)
        stdout.flush()
        sleep(0.02)

def shuffle_grid(grid):
    flat_grid = [word for row in grid for word in row if word != ""] #Turns the grid into a list of all the words in the grid
    shuffle(flat_grid)
    index = 0
    for row in range(len(grid)): #Puts grid back together with the shuffled words
        for col in range(len(grid[row])):
            if grid[row][col] != "": 
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

def populate_grid(selected_categories, grid): #Takes the selected categoiries and puts them into the grid
    row = 0
    for category in selected_categories:
        col = 0
        for word in category["Words"]:
            grid[row][col] = word
            col += 1
        row += 1

def display_game_state(lives, grid, correct_guesses_grid): #function that prints lives and both grids
    print("\033[1;37mLives:", lives, "\n\033[0m")
    print("\033[1;31m\033[4mMain Grid:\033[0m")
    display_grid(grid)
    print("\033[1;33m\033[4mCorrect Guesses Grid:\033[0m")
    display_grid(correct_guesses_grid)

def display_grid(grid):
    #Find the length of the longest word in the grid
    max_word_length = max(len(word) if word else 0 for row in grid for word in row)
    #Print the grid with remaining words
    for row in grid:
        for word in row:
            print("\033[1;37m" + (word.ljust(max_word_length) if word else "".ljust(max_word_length)) + "\033[0m", end=" | ")
        print()

def select_categories():
    selected_categories = sample(categories, 4)
    return selected_categories

def transfer_correct_guess_to_grid(guess, grid, correct_grid): #Removes the correct guess from the main grid and puts it into the correct guesses grid
    for word in guess:
        for row in grid:
            if word in row:
                #Find the next available row in the correct grid
                correct_row_index = None
                for i in range(len(correct_grid)):
                    if "" in correct_grid[i]:
                        correct_row_index = i
                        break
                
                if correct_row_index is not None:
                    #Find the column index where the word will be placed
                    correct_col_index = correct_grid[correct_row_index].index("")
                    #Transfer the word from the main grid to the correct grid
                    correct_grid[correct_row_index][correct_col_index] = row.pop(row.index(word))
                    row.append("")  #Maintain the structure of the grid by adding an empty string
                    break

def check_win(guessed_categories, selected_categories):
    for selected_category in selected_categories:
        if selected_category not in guessed_categories: #If any selected category is not found in the guessed categories, return False 
            return False
    return True #If all selected categories are found in the guessed categories, return True (game won)

def reshape_grid(grid):
    #Flatten the grid
    flat_grid = [word for row in grid for word in row if word]
    
    #Calculate the new number of rows and columns
    num_rows = max(len(grid) - 1, 1)  #Ensure there is at least one row
    num_cols = len(grid[0]) if num_rows > 1 else len(flat_grid)

    # Initialize the new grid with empty strings
    new_grid = [["" for _ in range(num_cols)] for _ in range(num_rows)]

    #Fill in the new grid with the remaining words
    word_index = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if word_index < len(flat_grid):
                new_grid[row][col] = flat_grid[word_index]
                word_index += 1

    grid = new_grid
    return grid

def get_guess(guessed_categories, selected_categories, grid, correct_guesses_grid):
    global lives
    while True:
        guess = input("\033[1;37m\nTake a guess (e.g., cake icecream pie pudding): \033[0m").lower().split()

        #Shuffle the grid if the user enters "shuffle"
        if guess == ["shuffle"]:
            shuffle_grid(grid)
            typewriter_effect("\033[1;37mGrid shuffled!\033[0m")
            display_game_state(lives, grid, correct_guesses_grid)
            continue
        elif len(guess) != 4 or any(not word.isalpha() for word in guess): #Guess must be in correct syntax or user trys again
            typewriter_effect("\033[1;37mInvalid input. Please enter four alphabetical words separated by spaces.\033[0m")
            continue

        #Check if the guess has already been made
        if guess in [item["Guess"] for item in guessed_categories]:
            typewriter_effect("\033[1;37mYou already guessed this category. Try again.\033[0m")
            continue

        #Sort the guessed words so that the same words cannot be guessed in a different order
        guess.sort()

        #Add the guess to the guessed categories dictionary
        guessed_categories.append({"Guess": guess})
        
        for category in selected_categories:
            if sorted(category["Words"]) == sorted(guess):
                transfer_correct_guess_to_grid(guess, grid, correct_guesses_grid)
                typewriter_effect("\033[1;37mCorrect guess!\033[0m")
                grid = reshape_grid(grid)
                return True
            
        typewriter_effect("\033[1;37mIncorrect guess!\033[0m")
        lives -= 1
        return False

def main():
    global lives
    global grid
    game_won = False
    guessed_categories = [] #Dictionary to store guessed categories
    selected_categories = select_categories() #List to store selected categories
    populate_grid(selected_categories, grid) #Populate the grid with words from the selected categories

    typewriter_effect("\033[1;37m\nWelcome to Intercorrelations!\n\033[0m")
    typewriter_effect("\033[1;37mHere's the grid of words you have to group into categories: \n\033[0m")
    shuffle_grid(grid)
    display_game_state(lives, grid, correct_guesses_grid)

    while lives > 0 and not game_won:
        if get_guess(guessed_categories, selected_categories, grid, correct_guesses_grid):
            #Remove the guessed category from the list of selected categories
            for category in selected_categories:
                if sorted(category["Words"]) == sorted(guessed_categories[-1]["Guess"]):
                    selected_categories.remove(category)
                    break

        #If all the selected categories are removed, the player wins
        if not selected_categories:
            game_won = True
                    
        #Update game state and continue loop
        display_game_state(lives, grid, correct_guesses_grid)

    if game_won:
        typewriter_effect("\033[1;37mCongrats! You won!\n\033[0m")
    else:
        typewriter_effect("\033[1;37mYou lose!\n\033[0m")
    play_again_function()

intercorrelations()