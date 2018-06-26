class Solver:
    """
    Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
    n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
    Find two lines, which together with x-axis forms a container, such that the container contains the most water.

    Note: You may not slant the container and n is at least 2.
    """
    def find_max_area(self, height):
        start = 0
        end = len(height) - 1
        max_area = 0

        while start < end:
            max_area = max(max_area, min(height[start], height[end]) * (end - start))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_area


def main():
    solver = Solver()
    height = [1, 5, 4, 0, 8, 2]

    print(solver.find_max_area(height))


if __name__ == "__main__":
    main()
