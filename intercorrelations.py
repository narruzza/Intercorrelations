from random import shuffle, sample
from time import sleep
from sys import stdout
#Imports a dictionary with categories to get selected_categories
from categories import fortnite_categories, minecraft_categories, cod_categories, fifa_categories, among_us_categories, rocketleague_categories
from os import system

system('printf "\\e[8;40;150t"')
system('mode con: cols=150 lines=40')

lives = 4

grid = [] #Main grid for the game
for _ in range(4):
    grid_row = []
    for _ in range(4):
        grid_row.append("Word")
    grid.append(grid_row)

correct_guesses_grid = [] #Empty grid that will be filled with correctly guessed categories
for _ in range(4):
    correct_guesses_grid_row = []
    for _ in range(4):
        correct_guesses_grid_row.append("")
    correct_guesses_grid.append(correct_guesses_grid_row)

def choose_theme(): #Asks user which theme they want for the game
    while True:
        choice = input("\033[1;37mChoose a theme for the Intercorrelations game (Fortnite, Minecraft, COD, Fifa or AmongUs):\033[0m").lower()
        if choice == "fortnite":
            print("""\033[1;37m
 ____  ____  ____  ____  ____  ____  ____  ____  _________  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____ 
||F ||||O ||||R ||||T ||||N ||||I ||||T ||||E ||||       ||||C ||||O ||||R ||||R ||||E ||||L ||||A ||||T ||||I ||||O ||||N ||||S ||
||__||||__||||__||||__||||__||||__||||__||||__||||_______||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||
|/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/_______\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\|
            \033[0m""")
            return fortnite_categories
        elif choice == "minecraft":
            print("""\033[1;37m
 ____  ____  ____  ____  ____  ____  ____  ____  ____  _________  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____ 
||M ||||I ||||N ||||E ||||C ||||R ||||A ||||F ||||T ||||       ||||C ||||O ||||R ||||R ||||E ||||L ||||A ||||T ||||I ||||O ||||N ||||S ||
||__||||__||||__||||__||||__||||__||||__||||__||||__||||_______||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||
|/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/_______\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\|
            \033[0m""")
            return minecraft_categories
        elif choice == "cod":
            print("""\033[1;37m
 ____  ____  ____  _________  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____ 
||C ||||O ||||D ||||       ||||C ||||O ||||R ||||R ||||E ||||L ||||A ||||T ||||I ||||O ||||N ||||S ||
||__||||__||||__||||_______||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||
|/__\||/__\||/__\||/_______\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\|
            \033[0m""")
            return cod_categories
        elif choice == "fifa":
            print("""\033[1;37m
 ____  ____  ____  ____  _________  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____ 
||F ||||I ||||F ||||A ||||       ||||C ||||O ||||R ||||R ||||E ||||L ||||A ||||T ||||I ||||O ||||N ||||S ||
||__||||__||||__||||__||||_______||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||
|/__\||/__\||/__\||/__\||/_______\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\|
            \033[0m""")
            return fifa_categories
        elif choice == "amongus":
            print("""\033[1;37m
 ____  ____  ____  ____  ____  _________  ____  ____  _________  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____ 
||A ||||M ||||O ||||N ||||G ||||       ||||U ||||S ||||       ||||C ||||O ||||R ||||R ||||E ||||L ||||A ||||T ||||I ||||O ||||N ||||S ||
||__||||__||||__||||__||||__||||_______||||__||||__||||_______||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||
|/__\||/__\||/__\||/__\||/__\||/_______\||/__\||/__\||/_______\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\|
            \033[0m""")
            return among_us_categories
        elif choice == "fong":
            print("""\033[1;37m
 ____  ____  ____  ____  _________  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____ 
||F ||||O ||||N ||||G ||||       ||||C ||||O ||||R ||||R ||||E ||||L ||||A ||||T ||||I ||||O ||||N ||||S ||
||__||||__||||__||||__||||_______||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||
|/__\||/__\||/__\||/__\||/_______\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\|
            \033[0m""")
            return rocketleague_categories
        else:
            typewriter_effect("\033[1;37mInvalid input. Please enter Fortnite, Minecraft, COD, Fifa or AmongUs\033[0m\n")

def typewriter_effect(text): #Adds an effect to printed text
    for character in text:
        stdout.write(character)
        stdout.flush()
        sleep(0.02)

def shuffle_grid(grid): #Shuffles the grid
    #Turns the grid into a list of all the words in the grid
    flat_grid = []
    for row in grid:
        for word in row:
            if word != "":
                flat_grid.append(word)
    shuffle(flat_grid)
    index = 0
    for row in range(len(grid)): #Puts grid back together with the shuffled words
        for col in range(len(grid[row])):
            if grid[row][col] != "":
                grid[row][col] = flat_grid[index]
                index += 1

def play_again_function(): #Asks user if they want to play again
    play_game_question = True
    while play_game_question == True:
        user_input = input("\033[1;37mWanna play Intercorrelations again? (Y or N)\033[0m").lower()
        if user_input == 'y':
            return True
        elif user_input == 'n':
            typewriter_effect("\033[1;37mGoodbye!\n\033[0m")
            play_game_question = False
            quit()
        else:
            typewriter_effect("\033[1;37mInvalid input. Please enter Y or N\033[0m")

def intercorrelations(): #Run Game
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
    typewriter_effect("\033[1;37mType 'SHUFFLE' at any time to shuffle the grid\n\033[0m")
    print("\033[1;31m\033[4mMain Grid:\033[0m")
    display_grid(grid)
    print("\033[1;33m\033[4mCorrect Guesses Grid:\033[0m")
    display_grid(correct_guesses_grid)

def display_grid(grid):  #Prints the grid
    max_word_length = 0
    for row in grid:
        for word in row:
            if word:  #Checking if word is not an empty string
                max_word_length = max(max_word_length, len(word))
    max_word_length += 5  #Adding 5 to the length of the longest word

    horizontal_line = '-' * (max_word_length + 3) * len(grid[0])

    #Print the grid with remaining words
    print("\033[1;37m" + horizontal_line + "\033[0m")
    for row in grid:
        print()
        for word in row:
            print("\033[1;37m" + (word.center(max_word_length) if word else "".center(max_word_length)) + "\033[0m", "\033[1;37m", end=" | " "\033[0m")
        print()
        print()
        print("\033[1;37m" + horizontal_line + "\033[0m")

def select_categories(): #Selects 4 random categories from the selected_categories
    selected_categories = sample(choose_theme(), 4)
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
    flat_grid = []
    for row in grid: #Put the 4x4 grid in a 1x16 list
        for word in row:
            if word:
                flat_grid.append(word)

    num_rows = max(len(grid) - 1, 1)
    num_cols = len(grid[0]) if num_rows > 1 else len(flat_grid)

    #Initialize the new grid with empty strings
    new_grid = []
    for _ in range(num_rows):
        new_row = ["" for _ in range(num_cols)]
        new_grid.append(new_row)

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
        found = False
        for item in guessed_categories:
            if guess == item["Guess"]:
                found = True
                break

        if found:
            typewriter_effect("\033[1;37mYou already guessed this category. Try again.\033[0m")
            continue
        
        #Sort the guessed words so that the same words cannot be guessed in a different order
        guess.sort()

        guessed_categories.append({"Guess": guess})

        #Add the guess to the guessed categories dictionary
        for category in selected_categories:
            if sorted(category["Words"]) == sorted(guess):
                transfer_correct_guess_to_grid(guess, grid, correct_guesses_grid)
                typewriter_effect("\033[1;37mCorrect guess!\033[0m")
                print("\033[1;33m\nCategory:", category["Connecting Word"], "\n\033[0m")
                grid = reshape_grid(grid)
                return True

        typewriter_effect("\033[1;37mIncorrect guess!\033[0m")
        lives -= 1
        return False

def main(): #Main Game Loop
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

    if game_won and lives > 1:
        typewriter_effect("\033[1;37mCongrats! You won!\n\033[0m")
    elif game_won:
        typewriter_effect("\033[1;37mPhew!\n\033[0m")
    else:
        typewriter_effect("\033[1;37mYou lose!\n\033[0m")

intercorrelations()