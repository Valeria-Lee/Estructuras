class MergeSort:
    def mergeSort(arr:list):
        if arr == None or len(arr) <= 1:
            return None
        
        n:int = len(arr)
        temp:list = list.copy(arr)
        MergeSort.__mergeSort(arr,temp,0,n-1)
        return arr

    def __mergeSort(arr:list,temp:list,izquierda:int,derecha:int):
        if izquierda < derecha:
            centro = int((izquierda + derecha) / 2)

            MergeSort.__mergeSort(arr,temp,izquierda,centro)
            MergeSort.__mergeSort(arr,temp,centro+1,derecha)

            MergeSort.merge(arr,temp,izquierda,centro,derecha)
            print(f"-{str(temp)}")

    def merge(arr:list,temp:list,izquierda:int,centro:int,derecha:int):
        for i in range(izquierda,derecha+1):
            temp[i] = arr[i]
        
        i = izquierda
        j = centro + 1
        k = izquierda

        while i <= centro and j <= derecha:
            if temp[i] <= temp[j]:
                arr[k] = temp[i]
                i += 1
            else:
                arr[k] = temp[j]
                j += 1
            k += 1
        
        while i <= centro:
            arr[k] = temp[i]
            k += 1
            i += 1