"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

    return


def reverse(nums, start):
    end = len(nums) - 1

    while start < end:
        swap(nums, start, end)
        start += 1
        end -= 1

    return


def next_permutation(nums):
    i = len(nums) - 2

    while i >= 0 and nums[i+1] <= nums[i]:
        i -= 1

    if i >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        swap(nums, i, j)

    reverse(nums, i + 1)

    return


def main():
    lst = [1, 2, 3]
    next_permutation(lst)
    print(lst)

    lst = [3, 2, 1]
    next_permutation(lst)
    print(lst)

    lst = [1, 1, 5]
    next_permutation(lst)
    print(lst)


if __name__ == "__main__":
    main()