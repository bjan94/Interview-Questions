class Solver:
    """
    Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
    You may assume all four edges of the grid are all surrounded by water.

    Example 1:

    Input:
    11110
    11010
    11000
    00000

    Output: 1
    Example 2:

    Input:
    11000
    11000
    00100
    00011

    Output: 3
    """
    def num_islands(self, grid):
        if grid is None or len(grid) == 0:
            return 0

        cnt = 0
        nr = range(len(grid))
        nc = range(len(grid[0]))

        for i in nr:
            for j in nc:
                if grid[i][j] == "1":
                    cnt += 1
                    self.explore(grid, i, j)

        return cnt

    def explore(self, grid, i, j):
        if grid[i][j] == "0" or i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return

        grid[i][j] = "0"
        self.explore(grid, i + 1, j)
        self.explore(grid, i - 1, j)
        self.explore(grid, i, j + 1)
        self.explore(grid, i, j - 1)

        return


def main():
    solver = Solver()
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

    print(solver.num_islands(grid))


if __name__ == "__main__":
    main()

