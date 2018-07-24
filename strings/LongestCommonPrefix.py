class Solver:
    def get_longest_prefix(self, str_array):
        if len(str_array) == 0:
            return ""

        prefix = str_array[0]
        for i in range(1, len(str_array)):
            min_len = min(len(prefix), len(str_array[i]))
            common = 0
            for j in range(min_len):
                if prefix[j] != str_array[i][j]:
                    break
                else:
                    common += 1
            prefix = prefix[:common]

        return prefix


def main():
    solver = Solver()
    print(solver.get_longest_prefix(["flower", "floral", "floght"]))


if __name__ == "__main__":
    main()
