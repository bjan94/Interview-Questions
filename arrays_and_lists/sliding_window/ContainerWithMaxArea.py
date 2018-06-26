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
    def find_max_area(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
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