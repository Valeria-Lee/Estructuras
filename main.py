from QuickSort import QuickSort
from RadixSort import RadixSort
from MergeSort import MergeSort
from BubbleSort import BubbleSort

def main():
    arrToQuickSort = (351, 33, 42, 110, 14, 919, 27, 1144, 216, 311, 0)
    arrToRadixSort = (351, 33, 42, 110, 14, 919, 27, 1144, 216, 311, 0)
    arrToMergeSort = (351, 33, 42, 110, 14, 919, 27, 1144, 216, 311, 0)
    arrToBubbleSort = (351, 33, 42, 110, 14, 919, 27, 1144, 216, 311, 0)

    print("Array ordenado con QuickSort:")
    print("Antes: " + str(arrToQuickSort))
    arrQuickSort = QuickSort.quickSort(list(arrToQuickSort))
    print("Ahora: " + str(arrQuickSort) + "\n")

    print("Array ordenado con RadixSort:")
    print("Antes: " + str(arrToRadixSort))
    arrRadixSort = RadixSort.radixSort(list(arrToRadixSort))
    print("Ahora: " + str(arrRadixSort) + "\n")

    print("Array ordenado con MergeSort:")
    print("Antes: " + str(arrToMergeSort))
    arrMergeSort = MergeSort.mergeSort(list(arrToMergeSort))
    print("Ahora: " + str(arrMergeSort) + "\n")

    print("Array ordenado con BubbleSort:")
    print("Antes: " + str(arrToBubbleSort))
    arrBubbleSort = BubbleSort.bubbleSort(list(arrToBubbleSort))
    print("Ahora: " + str(arrBubbleSort) + "\n")

main()