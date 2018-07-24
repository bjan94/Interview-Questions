class Solver:

    """
    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

    Example 1:

    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.
    Example 2:

    Input: "cbbd"
    Output: "bb"
    """

    def longest_palindrome(self, s):
        start = end = 0

        for i in range(len(s)):
            len1 = self.expand_around_center(s, i, i)
            len2 = self.expand_around_center(s, i, i+1)

            maxLen = max(len1, len2)

            if maxLen > end - start:
                start = i - (maxLen - 1) // 2
                end = i + maxLen // 2

        return s[start: end + 1]

    def expand_around_center(self, s, center1, center2):
        while center1 >= 0 and center2 < len(s) \
                        and s[center1] == s[center2]:
            center1 -= 1
            center2 += 1

        return center2 - center1 - 1


def main():
    solver = Solver()
    print(solver.longest_palindrome("babad"))


if __name__ == "__main__":
    main()
