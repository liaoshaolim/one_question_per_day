from node import TreeNode


class Solution:
    # 14. 最长公共前缀
    # 编写一个函数来查找字符串数组中的最长公共前缀。

    # 如果不存在公共前缀，返回空字符串 ""。

    # 示例 1:

    # 输入: ["flower","flow","flight"]
    # 输出: "fl"

    def longestCommonPrefix(self, strs):
        result = ''
        # zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
        # 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
        # print(*strs)
        # flower flow flight
        # print(strs)
        # ['flower', 'flow', 'flight']
        new_list = list(zip(*strs))

        print("new_list 为：{}".format(new_list))

        for item in new_list:
            if len(set(item)) == 1:
                result += item[0]
            else:
                break
        return result

    # 349.给定两个数组，编写一个函数来计算它们的交集。

    # 示例 1：

    # 输入：nums1 = [1, 2, 2, 1], nums2 = [2, 2]
    # 输出：[2]
    # 说明：

    # 输出结果中的每个元素一定是唯一的。
    # 我们可以不考虑输出结果的顺序。

    def intersection(self, nums1, nums2):
        result = []
        num1_set = set(nums1)
        num2_set = set(nums2)
        for item1 in num1_set:
            for item2 in num2_set:
                if item1 == item2:
                    result.append(item1)
        return result

    # 349.进阶，两个有序数组的交集
    # 双指针
    def intersection_sorted(self, nums1, nums2):
        result = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            # 若相同，同时移动指针
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            # 移动小的指针
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
        return result

    # 704
    # 双指针
    # 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
    def binary_search(self, arr, target):
        ''' 二分查找 '''
        # 思路：不停的调整搜索区间 + 细节把控
        left = 0
        right = len(arr) - 1
        # DETAIL：这里使用 <= ，因为 right 就是数组末尾下标，这个区间其实就是每次进行搜索的区间
        while(left <= right):
            # DETAIL：left + (right - left) / 2 就和 (left + right) / 2 的结果相同，但是有效防止了 left 和 right 太大直接相加导致溢出
            mid = left + int((right - left) / 2)
            if(arr[mid] == target):
                return mid
            elif(target < arr[mid]):
                right = mid - 1
            # DETAIL：不出现 else,因为这样可以清楚地展现所有细节
            elif(target > arr[mid]):
                left = mid + 1
        return -1

    # 剑指 Offer 50。
    # 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
    def firstUniqChar(self, s: str):
        # 利用哈希表
        # 遍历字符串 s,使用哈希表统计”各字符数量是否 > 1”
        # 再次遍历 s，在哈希表中找到为 true 的字符
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for c in s:
            if dic[c]:
                return c
        return ''

    # 88. 合并两个有序数组
    # 双指针 思路
    def merge(self, nums1, nums2):
        i = 0
        j = 0
        result = []
        nums1Len = len(nums1)
        nums2Len = len(nums2)
        while i < nums1Len and j < nums2Len:
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        while i < nums1Len:
            result.append(nums1[i])
            i += 1
        while j < nums2Len:
            result.append(nums2[j])
            j += 1
        return result

    # 20. 有效的括号
    # 栈 思路
    def checkValidString(self, s: str):
        stack = []
        # 字典的的巧妙赋值
        dic = {')': '(', ']': '[', '}': '{'}
        for c in s:
            # 字符不在字典的 key 中时，压栈
            if c not in dic:
                stack.append(c)
            # eg:not [] 返回 true，not [1,2,3] 返回 false
            # 栈为空（上来就不入栈）或者弹栈元素与新的不匹配
            elif not stack or dic[c] != stack.pop():
                return False
        return True

    # 7. 整数反转
    # 注意溢出的情况
    # 语法学习，return 的时候可以 if else
    def reverse(self, x: int):
        y = abs(x)
        res = 0
        boundary = 2 ** 31 - 1 if x > 0 else 2 ** 31
        while y != 0:
            res = res * 10 + y % 10
            if res > boundary:
                return 0
            y //= 10
        return res if x > 0 else -res

    # 344. 反转字符串
    def reverseString(self, s):
        # 先转为字符数组
        strList = []
        for c in s:
            strList.append(c)

        left = 0
        right = len(strList) - 1
        while left <= right:
            temp = strList[left]
            strList[left] = strList[right]
            strList[right] = temp
            left += 1
            right -= 1
        # 字符数组转字符串
        return ''.join(strList)

    # 136. 只出现一次的数字
    # 任何数和 0 异或，结果仍为这个数
    # 相同的两个数异或为 0
    # 和同一个数连续异或两次，结果仍为这个数
    def singleNumber(self, nums):
        a = 0
        for i in nums:
            a = a ^ i
        return a

    # 剑指 Offer 10- II. 青蛙跳台阶问题
    # 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
    # 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
    # dp:Dynamic Programming
    def numWays(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

    # 322. 零钱兑换 TODO：重新捋思路
    # 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
    def coinChange(self, coins, amount: int):
        # 备忘录
        memo = dict()

        # 输入一个目标金额 n，返回凑出目标金额 n 的最少硬币数量。
        def dp(n):
            # 查备忘录，避免重复计算
            if n in memo:
                return memo[n]
            # base case
            if n == 0:
                return 0
            if n < 0:
                return -1
            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1:
                    continue
                # 1 + subproblem: 1 为 1、2、5 减去的那个情况
                res = min(res, 1 + subproblem)

            # 记入备忘录
            memo[n] = res if res != float('INF') else -1
            return memo[n]
        return dp(amount)

    # 242. 有效的字母异位词
    # 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
    # 思路1：两个字符串排序后比对 O(NlogN)
    # 思路2：记录字符出现的个数 O(N)
    def isAnagram(self, s: str, t: str):
        dic1 = {}
        dic2 = {}
        for c in s:
            dic1[c] = dic1.get(c, 0) + 1
        for c in t:
            dic2[c] = dic2.get(c, 0) + 1
        return dic1 == dic2

    # 9. 回文数
    # -121 也是返回 False
    def isPalindrome(self, x: int):
        if x < 0:
            return False

        def reverse(x):
            y = abs(x)
            res = 0
            while y != 0:
                res = res * 10 + y % 10  # 取最后一位
                y //= 10  # 降位 // 返回的是整数结果(可以理解为 / 的整数部分)
            return res if x > 0 else -res
        return x == reverse(x)

    # 1.两数之和
    def two_sum(self, nums, target):
        dic = {}
        for i, n in enumerate(nums):
            temp = target - n
            if temp in dic:
                return[dic[temp], i]
            else:
                dic[n] = i

    # 13.罗马数字转整数
    def romanToInt(self, s: str):
        hashMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        # 这里 range(len(s) - 1) 是为了下面取下一位的时候不越界
        for index in range(len(s) - 1):
            # 左边代表的数小于右边代表的数 - 当前数
            if hashMap[s[index]] < hashMap[s[index + 1]]:
                result -= hashMap[s[index]]
                # 左边代表的数大于右边代表的数 + 当前数
            else:
                result += hashMap[s[index]]
        # 因为上面 range(len(s) - 1)，所以要加上最后一位
        return result + hashMap[s[-1]]

    # 3. 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
    # DETAIL：滑动窗口思路
    # left 每次滑动 1，right 滑动到最大无重位置
    def lengthOfLongestSubstring(self, s: str):
        hashSet = set()
        strLen = len(s)
        right = 0
        res = 0
        for left in range(strLen):
            while right < strLen and s[right] not in hashSet:
                hashSet.add(s[right])
                right += 1
            if len(hashSet) > res:
                res = len(hashSet)
            hashSet.remove(s[left])
        return res

    # 100. 相同的树
    def isSameTree(self, p: TreeNode, q: TreeNode):
        # 如果两个二叉树都为空，则两个二叉树相同
        if not p and not q:
            return True
        # 如果两个二叉树中有且只有一个为空，则两个二叉树一定不相同
        elif not p or not q:
            return False
        # 如果两个二叉树都不为空，那么首先判断它们的根节点的值是否相同，若不相同则两个二叉树一定不同，若相同，再分别判断两个二叉树的左子树是否相同以及右子树是否相同
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # 101. 对称二叉树
    # 思路：树左侧跟树右侧是相等的数
    def isSymmetric(self, root: TreeNode):
        def isSameTree(p: TreeNode, q: TreeNode):
            # 如果两个二叉树都为空，则两个二叉树相同
            if not p and not q:
                return True
            # 如果两个二叉树中有且只有一个为空，则两个二叉树一定不相同
            elif not p or not q:
                return False
            # 如果两个二叉树都不为空，那么首先判断它们的根节点的值是否相同，若不相同则两个二叉树一定不同，若相同，再分别判断两个二叉树的左子树是否相同以及右子树是否相同
            elif p.val != q.val:
                return False
            else:
                # DETAIL： 与 相同的树 不同的地方：递归时，传参不同
                return isSameTree(p.left, q.right) and isSameTree(p.right, q.left)
        if not root:
            return True
        return isSameTree(root.left, root.right)

    # 104. 二叉树的最大深度
    def maxDepth(self, root: TreeNode):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

    # 剑指 Offer 42. 连续子数组的最大和
    # 输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
    # 输出: 6
    # 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
    def maxSubArray(self, nums) -> int:
        maxNum = nums[0]
        for i in range(1, len(nums)):
            pre_num = nums[i - 1]
            if pre_num > 0:
                nums[i] += pre_num
            maxNum = max(maxNum, nums[i])
        return maxNum
