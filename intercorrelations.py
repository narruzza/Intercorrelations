import random
from categories import categories

grid = [
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
]

def populate_grid(selected_categories, grid):
    row = 0
    for category in selected_categories:
        col = 0
        for word in category["Words"]:
            grid[row][col] = word
            col += 1
        row += 1

def select_categories():
    global selected_categories
    selected_categories = random.sample(categories, 4)

def main():
    # Select four random categories
    select_categories()
    # Populate the grid with words from the selected categories
    populate_grid(selected_categories, grid)

    # Print the grid
    print("Welcome to the Intercorrelations!")
    print("Here's the grid of words you have to connect into categories:")
    print()  # Puts space between the text and the grid
    for row in grid:
        print(row)
    
    print(grid[0][0])

main()