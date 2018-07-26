class Solver:
    """
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

    Example:

    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
    Follow up:

    If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
    """
    def max_subarray_sum(self, array):
        if not array:
            return 0

        maxAtIndex = []
        maxAtIndex.append(array[0])
        maxSum = maxAtIndex[0]

        for i in range (1, len(array)):
            maxAtIndex.append(max(array[i], maxAtIndex[i-1] + array[i]))
            maxSum = max(maxSum, maxAtIndex[i])

        return maxSum


def main():
    solver = Solver()
    array = [-2, 1, -3,4, -1, 2, 1, -5, 4]

    print(solver.max_subarray_sum(array))


if __name__ == "__main__":
    main()
