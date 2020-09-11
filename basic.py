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
