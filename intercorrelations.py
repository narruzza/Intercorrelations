import random
#Imports a dictionary with categories to get selected_categories
from categories import categories

lives = 4
play_game = True

grid = [ #Empty grid that will be filled with selected_categories
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
]

def play_again_function(): #Asks user if they want to play again
    user_input = input("Wanna play Intercorrelations? (Y or N)").lower()
    if user_input == 'Y' or user_input == 'y':
        intercorrelations()
        return True
    elif user_input == 'N' or user_input == 'n':
        print("Goodbye!")
        return False
    else:
        print("Invalid input. Please enter Y or N")
        play_again_function()
    
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
    global selected_categories
    selected_categories = random.sample(categories, 4)

def main():
    # Select four random categories
    select_categories()
    # Populate the grid with words from the selected categories
    populate_grid(selected_categories, grid)

    # Print the grid
    print("Welcome to the Intercorrelations!")
    print("Here's the grid of words you have to group into categories: \n")
    display_game_state(lives)

intercorrelations()