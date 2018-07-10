class Solver:
    """
    Given a string, find the length of the longest substring without repeating characters.

    Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
    """

    def length_of_longest_substring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen = {}
        start = max_len = 0

        for end in range(len(s)):
            if s[end] in last_seen:
                start = max(start, last_seen[s[end]])

            max_len = max(max_len, end - start + 1)
            last_seen[s[end]] = end + 1

        return max_len


def main():
    solver = Solver()
    print(solver.length_of_longest_substring("abcabcdd"))


if __name__ == "__main__":
    main()