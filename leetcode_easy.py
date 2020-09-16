class Solution:
    # 14. 最长公共前缀
    # 编写一个函数来查找字符串数组中的最长公共前缀。

    # 如果不存在公共前缀，返回空字符串 ""。

    # 示例 1:

    # 输入: ["flower","flow","flight"]
    # 输出: "fl"

    def longestCommonPrefix(self, strs) -> str:
        result = ''
        # zip函数作用：将列表解开成两个独立的参数，传入函数
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
    # 双指针解
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