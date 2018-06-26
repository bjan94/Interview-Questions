class Solver:
    """
    There are two sorted arrays nums1 and nums2 of size m and n respectively.

    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

    Example 1:
    nums1 = [1, 3]
    nums2 = [2]

    The median is 2.0
    Example 2:
    nums1 = [1, 2]
    nums2 = [3, 4]

    The median is (2 + 3)/2 = 2.5
    """
    def find_median_sorted_arrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)

        if len1 > len2:
            return self.find_median_sorted_arrays(nums2, nums1)

        start = 0
        end = len1

        while start <= end:
            partition_x = (start + end) // 2
            partition_y = (len1 + len2 + 1) // 2 - partition_x

            # assign -inf to max_left value if partitioned at index 0
            max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
            max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]

            # assign inf to min_right value if partitioned at last index
            min_right_x = float('inf') if partition_x == len1 else nums1[partition_x]
            min_right_y = float('inf') if partition_y == len2 else nums2[partition_y]

            # last element in both left halves are less than first element in both right halves
            # partition found
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if ((len1 + len2) % 2) == 1:  # combined array is of odd length
                    return max(max_left_x, max_left_y)
                else:
                    medians = max(max_left_x, max_left_y) + min(min_right_x, min_right_y)
                    return medians / 2
            elif max_left_x > min_right_y:  # need to move end pointer to the left in x
                end = partition_x - 1
            else:  # need to move start pointer to the right in x
                start = partition_x + 1

        return None  # Array is not sorted...


def main():
    solver = Solver()
    x = [1, 3, 8, 9, 15]
    y = [7, 11, 19, 21, 25]

    print(solver.find_median_sorted_arrays(x, y))


if __name__ == "__main__":
    main()

