from leetcode_easy import Solution
from basic import Basic


def main():
    print('come on!')

    print('----------------- 2020年09月09日 -----------------')

    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))

    print('----------------- 2020年09月11日 -----------------')
    print(solution.intersection([1, 2, 2, 1], [2, 2]))
    print(solution.intersection_sorted([1, 2, 3, 4, 4, 13], [1, 4, 9, 10]))

    print('----------------- 2020年09月11日 -----------------')
    basic = Basic()
    testArr = [1, 8, 5, 2, 1, 5, 6, 3, 9, 7, 4]
    print(testArr)
    basic.quickSort(testArr, 0, len(testArr) - 1)
    print(testArr)

    print('----------------- 2020年09月16日 -----------------')
    print(basic.binary_search(testArr, 5))


if __name__ == "__main__":
    main()
