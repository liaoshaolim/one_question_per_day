from leetcode_easy import Solution
from basic import Basic
from node import Node, LinkListUtil


def main():
    print('come on!')

    print('======================================== 力扣 ========================================')
    print('----- 2020年09月09日 -----')
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))

    print('----- 2020年09月11日 -----')
    print(solution.intersection([1, 2, 2, 1], [2, 2]))
    print(solution.intersection_sorted([1, 2, 3, 4, 4, 13], [1, 4, 9, 10]))

    print('----- 2020年09月16日 -----')
    print(solution.binary_search([1, 2, 3, 46, 100], 100))

    print('----- 2020年09月21日 -----')
    print(solution.firstUniqChar('abaccdeff'))
    print(solution.merge([1, 2, 3, 4, 5], [2, 5, 6]))
    print(solution.checkValidString('(){}[]'))
    print(solution.reverse(123))
    print(solution.reverseString('hello'))
    print(solution.singleNumber([4, 1, 2, 1, 2]))

    print('----- 2020年09月22日 -----')
    print(solution.numWays(7))

    print('----- 2020年09月23日 -----')
    print(solution.coinChange([1, 2, 5], 11))
    print(solution.isAnagram('art', 'rat'))

    print('======================================== 基础 ========================================')
    print('----- 2020年09月11日 -----')
    basic = Basic()
    testArr = [1, 8, 5, 2, 1, 5, 6, 3, 9, 7, 4]
    print(testArr)
    basic.quickSort(testArr, 0, len(testArr) - 1)
    print(testArr)

    print('----- 2020年09月16日 -----')
    print(basic.binary_search_left([1, 2, 2, 2, 3], 0))
    print(basic.binary_search_right([1, 2, 2, 2, 3], 2))

    print('----- 2020年09月22日 -----')
    # for i in range(101):
    print(basic.fib1(10))
    print(basic.fib2(10))
    print(basic.fib3(10))

    print('----- 2020年09月24日 -----')
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None

    util = LinkListUtil()
    util.printAll(node1)
    print(util.length(node1))
    print(util.isHasCycle(node1))
    util.printAll(util.reverse(node1))


if __name__ == "__main__":
    main()
