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

    def binary_search(self, arr, target):
        ''' 二分查找 '''
        left = 0
        right = len(arr) - 1
        while(left <= right):
            mid = left + int((right - left) / 2)
            if(arr[mid] == target):
                return mid
            elif(target < arr[mid]):
                right = mid - 1
            else:
                left = mid + 1
