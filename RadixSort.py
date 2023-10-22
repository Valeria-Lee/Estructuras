class RadixSort:
    def radixSort(arr:list):
        length:int = len(arr)
        max:int = RadixSort.getMax(arr, length)
        exponente:int = 1
        while int(max/exponente) > 0:
            RadixSort.ordeningSort(arr,length,exponente)
            exponente *= 10
        return arr

    def getMax(arr:list, length:int):
        max:int = arr[0]
        for i in range(0,length-1,1):
            if arr[i] > max:
                max = arr[i]
        return max

    def ordeningSort(arr:list,length:int,exponente:int):
        salida = [0] * int(length+1)
        orden = [0] * 10
    
        for i in range(length):
            index = int((arr[i]/exponente) % 10)
            orden[index] += 1
            
        for i in range(1,10):
            orden[i] += orden[i - 1]

        for i in range(length-1,-1,-1):
            index = int((arr[i]/exponente)%10)
            salida[orden[index]-1] = arr[i]
            orden[index] -= 1

        print(f"-{str(arr)}")

        for i in range(length):
            arr[i] = salida[i]