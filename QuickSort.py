class QuickSort:
    def __quickSort(arr:list, primero:int, ultimo:int):
        central:int = int((primero + ultimo) / 2)
        pivote:float = arr[central]
        i:int = primero
        j:int = ultimo

        while i <= j:
            while arr[i] < pivote:
                i = i + 1
            while arr[j] > pivote:
                j = j - 1
            if i <= j:
                aux = arr[i]
                arr[i] = arr[j]
                arr[j] = aux

                i = i + 1
                j = j - 1
            print(f"-{str(arr)}")

        if primero < j:
            QuickSort.__quickSort(arr,primero,j)
        if i < ultimo:
            QuickSort.__quickSort(arr,i,ultimo)

        return arr

    def quickSort(arr:list):
        return QuickSort.__quickSort(arr,0,int(len(arr)-1))