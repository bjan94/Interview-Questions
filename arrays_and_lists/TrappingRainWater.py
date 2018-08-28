class Solver:
    """
    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it is able to trap after raining.

    https://leetcode.com/problems/trapping-rain-water/description/

    Example:

    Input: [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    """

    def trap(self, height):
        if height is None or len(height) == 0:
            return 0

        ans = 0
        left = 0
        right = len(height) - 1
        left_max = right_max = 0

        while left < right:
            if height[left] <= height[right]:  # continue in left -> right direction
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1

        return ans


def main():
    solver = Solver()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    print(solver.trap(height))


if __name__ == "__main__":
    main()
