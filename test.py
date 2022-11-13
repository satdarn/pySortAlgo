import PySort

arr = [3,5,1,8,6,7,4,10,9,2]

insertion = PySort.insertSort(arr)
selection = PySort.selectionSort(arr)

insertion.returnSorted(False,True)
selection.returnSorted(True,True)

print(insertion.snapshots)
