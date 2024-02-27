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
    user_input = str(input("Wanna play again? (Y or N)"))
    if user_input == "Y":
        play_again = True
        intercorrelations()
    elif user_input == "N":
        play_again = False
        StopIteration
    else:
        play_again()
    
def intercorrelations():
    play_game = True

    while play_game is True:
        main()

def populate_grid(selected_categories, grid):
    row = 0
    for category in selected_categories:
        col = 0
        for word in category["Words"]:
            grid[row][col] = word
            col += 1
        row += 1



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
    for row in grid:
        print(row)
    play_again_function()

intercorrelations()