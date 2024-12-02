def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a 2D grid.
    :param grid: List of list of integers (0 for water, 1 for land).
    :return: Integer, the perimeter of the island.
    """
    perimeter = 0

    # Iterate through each cell in the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:  # Land cell found
                # Check all four possible sides
                if row == 0 or grid[row - 1][col] == 0:  # Check top
                    perimeter += 1
                if row == len(grid) - 1 or grid[row + 1][col] == 0:  # Check bottom
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:  # Check left
                    perimeter += 1
                if col == len(grid[0]) - 1 or grid[row][col + 1] == 0:  # Check right
                    perimeter += 1

    return perimeter
