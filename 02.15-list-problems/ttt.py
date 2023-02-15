# Simulate a game of tic-tac-toe.


def get_move():
    """
    Get the next move from user input.
    """
    pass


def check_grid(player, grid):
    """
    Check to see if a given player has won.

    :param player: Either "X" or "O"
    :param grid: A 3x3 list of lists
    :return: Whether or not that player has won
    """
    pass


def check_row(player, grid):
    """
    Check to see if a given player has won via a row.

    :param player: Either "X" or "O"
    :param grid: A 3x3 list of lists
    :return: Whether or not that player has placed three marks in a row
    """
    for row in grid:
        won = True

        for cell in row:
            # Note that, regardless of how this condition is set up, we cannot
            #  necessarily return here: if the cell is equal to the player, we
            #  still need to check the rest of the cells in the same row; if it
            #  is not equal, we still need to check the rest of the rows.
            if cell != player:
                won = False

        # If, after the inner loop finishes, the flag is still true, we must
        #  never have found a cell that was not equal to the player, that is,
        #  every cell must be equal to the player, and the player has won.
        if won:
            return True

    return False


def check_column(player, grid):
    """
    Check to see if a given player has won via a column.

    :param player: Either "X" or "O"
    :param grid: A 3x3 list of lists
    :return: Whether or not that player has placed three marks in a column
    """
    # Since the columns aren't lists of their own, the interpreter won't know
    #  how to access them; we'll need to manage their indices ourselves.

    # The number of columns is the length of each "inner" list:
    for col in range(len(grid[0])):
        won = True

        # The number of rows is the length of the "outer" list:
        for row in range(len(grid)):
            if grid[row][col] != player:
                won = False

        if won:
            return True

    return False


def check_diagonal(player, grid):
    """
    Check to see if a given player has won via a diagonal.

    :param player: Either "X" or "O"
    :param grid: A 3x3 list of lists
    :return: Whether or not that player has placed three marks in a diagonal
    """
    # Note that there are only two possibilities -- if we know that we don't
    #  need a generalized loop, maybe it's not worth the time to figure out
    #  what that loop is supposed to look like...
    return ((grid[0][0] == grid[1][1] == grid[2][2] == player)
            or (grid[2][0] == grid[1][1] == grid[0][2] == player))


def main():
    # Each mark will be a string, either "X" or "O"; by convention, the "X"s
    #  go first:
    mark = "X"

    # The grid will be a 3x3 list of lists -- note that we don't want to use a
    #  list of strings, because strings are immutable, and we want to be able
    #  to change the marks on the board later:
    grid = [[None, None, None],
            [None, None, None],
            [None, None, None]]


if __name__ == "__main__":
    main()
