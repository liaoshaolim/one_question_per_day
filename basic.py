class Basic:
    def quickSort(self, arr, left, right):
        ''' 快排 '''
        if left >= right:
            return
        i = left
        j = right
        key = arr[i]
        while i < j:
            while i < j and arr[j] >= key:
                j = j - 1
            arr[i] = arr[j]
            while i < j and arr[i] <= key:
                i = i + 1
            arr[j] = arr[i]
        # 确定 key 的位置
        arr[i] = key
        self.quickSort(arr, left, i - 1)
        self.quickSort(arr, i+1, right)

    def binary_search_left(self, arr, target):
        ''' 二分查找之左侧边界 '''
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + int((right - left) / 2)
            if(arr[mid] == target):
                # 收缩右侧边界
                right = mid - 1
            elif(target < arr[mid]):
                right = mid - 1
            elif(target > arr[mid]):
                left = mid + 1
        # 目标数不在 arr 中或者 left 越界
        # DETAIL:需要先判断是否越界
        if(left == len(arr) or target != arr[left]):
            return -1
        return left

    def binary_search_right(self, arr, target):
        ''' 二分查找之右侧边界 '''
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + int((right - left) / 2)
            if(arr[mid] == target):
                # 收缩左侧边界
                left = mid + 1
            elif(target < arr[mid]):
                right = mid - 1
            elif(target > arr[mid]):
                left = mid + 1
        # 目标数不在 arr 中或者 right 越界
        # DETAIL:需要先判断是否越界
        if(right < 0 or arr[right] != target):
            return -1
        return right

    # 斐波那契数列 0、1、1、2、3、5、8、13、21、34
    # F(0) = 0，F(1) = 1,
    # F(n) = F(n - 1) + F(n - 2)（n ≥ 3，n ∈ N*）
    def fib1(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib1(n - 1) + self.fib1(n - 2)

    # 带备忘录的做法
    def fib2(self, n):
        arr = [0] * (n + 1)  # 长度为 n + 1 元素全为 0 的数组
        return self.helper(arr, n)

    def helper(self, arr, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if arr[n] != 0:
            return arr[n]
        else:
            arr[n] = self.helper(arr, n - 1) + self.helper(arr, n - 2)
            return arr[n]

    # dp 数组
    def fib3(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        # dp[-1] 数组的最后一个元素
        return dp[-1]

    # 45度遍历二维数组
    def scanBy45(self, arr):
        def isValid(arr):
            ''' 合法性校验 '''
            if len(arr) <= 0:
                return False
            else:
                count = len(arr[0])
                for item in arr:
                    if len(item) != count:
                        return False
            return True

        if isValid(arr) == False:
            print('二维数组不合法')
            return

        for scanCount in range(len(arr) * 2 - 1):
            for index1 in range(len(arr)):
                index2 = scanCount - index1
                if index2 >= 0 and index2 < len(arr):
                    print(arr[index1][index2], end=' ')
            print('')
