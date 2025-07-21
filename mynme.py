import matplotlib.pyplot as plt

def draw_letter_C_in_grid():
    # Create a 10x10 grid layout
    grid_size = 15
    fig, ax = plt.subplots(figsize=(6, 6))

    # Draw the grid lines
    for x in range(grid_size + 1):
        ax.axhline(x, color='black', linewidth=0.5)
        ax.axvline(x, color='black', linewidth=0.5)

    # Turn off axes
    ax.set_xticks([])
    ax.set_yticks([])
    ax.invert_yaxis()  # So (0,0) is top-left like in a matrix

    # Plot the letter "C" using red squares
    red_cells = [
        (2, 2), (2, 3), (2, 4), (2, 5),
        (3, 2), (3, 3), (3, 4), (3, 5),
        (4, 2),
        (5, 2),
        (6, 2),
        (7, 2),
        (8, 2),
        (9, 2), (9, 3), (9, 4), (9, 5),
        (10, 2), (10, 3), (10, 4), (10, 5),
    ]

    for (y, x) in red_cells:
        ax.add_patch(plt.Rectangle((x, y), 2, 2, color='red'))

    # Set grid boundaries
    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    plt.title("Letter C in Red (Grid Layout)")
    plt.show()

# Run the function
draw_letter_C_in_grid()
