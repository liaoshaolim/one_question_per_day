from leetcode_easy import Solution
from basic import Basic


def main():
    print('come on!')

    print('----------------- 2020年09月09日 -----------------')

    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))

    print('----------------- 2020年09月11日 -----------------')
    basic = Basic()
    testArr = [1, 8, 5, 2, 1, 5, 6, 3, 9, 7, 4]
    print(testArr)
    basic.quickSort(testArr, 0, len(testArr) - 1)
    print(testArr)


if __name__ == "__main__":
    main()
