class Solver:
    """
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: "PAHNAPLSIIGYIR"

    Write the code that will take a string and make this conversion given a number of rows:

    string convert(string s, int numRows);
    Example 1:

    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"
    Example 2:

    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:

    P     I    N
    A   L S  I G
    Y A   H R
    P     I
    """
    def convert_to_zigzag(self, s, numRows):
        i = 0
        lists = []
        for j in range(numRows):
            lists.append([])

        while i < len(s):
            for j in range(numRows):  # vertical fill
                if i < len(s):
                    lists[j].append(s[i])
                    i += 1
                else:
                    break
            for j in reversed(range(1, numRows - 1)):  # zig zag fill on all lists except first and last list
                if i < len(s):
                    lists[j].append(s[i])
                    i += 1
                else:
                    break

        for j in range(1, numRows):
            lists[0].extend(lists[j])  # merge all lists into one

        return ''.join(lists[0])


def main():
    solver = Solver()
    print(solver.convert_to_zigzag("PAYPALISHIRING", 3))


if __name__ == "__main__":
    main()
