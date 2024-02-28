import random
#Imports a dictionary with categories to get selected_categories
from categories import categories

lives = 4

grid = [ #Empty grid that will be filled with selected_categories
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
]

def play_again_function(): #Asks user if they want to play again
    while True:
        user_input = input("Wanna play Intercorrelations? (Y or N)").lower()
        if user_input == 'y':
            return True
        elif user_input == 'n':
            print("Goodbye!")
            return False
        else:
            print("Invalid input. Please enter Y or N")

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
    print("Lives: ", lives)
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
        guess = input("Enter four connected words (e.g., cake ice cream pie pudding): ").lower().split()

        #Check if the guess has already been made
        if guess in [item["Guess"] for item in guessed_categories]:
            print("You already guessed this category. Try again.")
            continue

        #Add the guess to the guessed categories dictionary
        guessed_categories.append({"Guess": guess})

        #Check if the guess matches any of the selected categories
        for category in selected_categories:
            if category["Words"] == guess:
                print("Correct guess!")
                return True
        else:
            print("Incorrect guess!")
            return False

def main():
    global lives
    guessed_categories = []  #Dictionary to store guessed categories
    selected_categories = []  #List to store selected categories
    selected_categories = select_categories()
    populate_grid(selected_categories, grid) #Populate the grid with words from the selected categories

    print("Welcome to the Intercorrelations!")
    print("Here's the grid of words you have to group into categories: \n")
    display_game_state(lives)

    while lives > 0:
        if get_guess(guessed_categories, selected_categories):
            #If the guess is correct, remove the guessed category from the list of selected categories
            selected_categories.pop(0)
        
        #Check if all categories have been guessed
        if not selected_categories:
            print("Congratulations! You've won!")
            return

        #Update game state and continue loop
        display_game_state(lives)

    print("You lose!")
    play_again_function()

intercorrelations()