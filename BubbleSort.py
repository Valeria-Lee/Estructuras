class BubbleSort:
    def bubbleSort(arr:list):
        n = len(arr)

        for i in range(n-1):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    BubbleSort.swap(arr, j, j+1)
            print(f"-{str(arr)}")
        return arr
            
    def swap(arr:list,a:int,b:int):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp