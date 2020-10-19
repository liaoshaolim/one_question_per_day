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
    print(solution.firstUniqChar('abaaccdeff'))
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

    print('----- 2020年09月29日 -----')
    print(solution.isPalindrome(-121))
    print(solution.two_sum([1, 2, 7, 10], 9))

    print('----- 2020年10月19日 -----')
    print(solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(solution.romanToInt('MCMXCIV'))

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
    print('构造单向链表')
    head = None
    cur = None
    for i in range(1, 11):
        node = Node(i)
        node.next = None
        if head == None:
            head = node
        else:
            cur.next = node
        # 设置当前节点为新节点
        cur = node

    util = LinkListUtil()
    util.printAll(head)
    print(util.length(head))
    print(util.isHasCycle(head))
    util.printAll(util.reverse(head))

    print('----- 2020年10月10日 -----')
    arr1 = [
        [1, 2, 3, 4],
        [4, 5, 6],
        [7, 8, 9],
    ]
    basic.scanBy45(arr1)

    arr2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    basic.scanBy45(arr2)


if __name__ == "__main__":
    main()
