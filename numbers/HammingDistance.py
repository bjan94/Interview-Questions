class Solver:
    """
    The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

    Given two integers x and y, calculate the Hamming distance.

    Note:
    0 ≤ x, y < 231.

    Example:

    Input: x = 1, y = 4

    Output: 2

    Explanation:
    1   (0 0 0 1)
    4   (0 1 0 0)
           ↑   ↑

    The above arrows point to positions where the corresponding bits are different.
    """

    def get_hamming_distance(self, x, y):
        xored = x ^ y
        count = 0

        while xored != 0:
            count += xored & 1
            xored >>= 1

        return count


def main():
    solver = Solver()
    print(solver.get_hamming_distance(1, 4))


if __name__ == "__main__":
    main()