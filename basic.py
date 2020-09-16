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
