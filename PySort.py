class insertSort():
    def __init__(self, sortList = []):
        self.unsorted = sortList
        self.sorted = []
        self.reverseSorted = []
        #forwards sort (least to greatest)
        arr = self.unsorted
        for i in range(1, len(arr)):
            j = i
            while arr[j-1] > arr[j] and j > 0:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                j -= 1        
        self.sorted = arr

        #backwards or reverse sort (greatest to least)
        arr = self.unsorted
        for i in range(1, len(arr)):
            j = i
            while arr[j-1] < arr[j] and j > 0:
                arr[j-1], arr[j] = arr[j], arr[j-1] 
                j -= 1  
        self.reverseSorted = arr


    def returnUnsorted(self, printUnsorted = False):
        if printUnsorted:
            print(self.unsorted)
        return self.unsorted


    def returnSorted(self, printSorted = False):
        if printSorted:
            print(self.sorted)
        return self.sorted


    def returnReverseSorted(self, printSorted = False):
        if printSorted:
            print(self.reverseSorted)
        return self.reverseSorted

class selectionSort():
    def __init__(self, sortList = []):
        self.unsorted = sortList
        self.sorted = []
        self.reverseSorted = []
        #forwards sort (least to greatest)
        arr = self.unsorted
        for i in range(0, len(arr)-1):
            curMinIndex = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[curMinIndex]:
                    curMinIndex = j
            arr[i], arr[curMinIndex] = arr[curMinIndex], arr[i]
        self.sorted = arr

        #backwards or reverse sort (greatest to least)
        arr = self.unsorted
        for i in range(0, len(arr)-1):
            curMaxIndex = i
            for j in range(i+1, len(arr)):
                if arr[j] > arr[curMaxIndex]:
                    curMaxIndex = j
            arr[i], arr[curMaxIndex] = arr[curMaxIndex], arr[i]
        self.reverseSorted = arr


    def returnUnsorted(self, printUnsorted = False):
        if printUnsorted:
            print(self.unsorted)
        return self.unsorted


    def returnSorted(self, printSorted = False):
        if printSorted:
            print(self.sorted)
        return self.sorted


    def returnReverseSorted(self, printSorted = False):
        if printSorted:
            print(self.reverseSorted)
        return self.reverseSorted

class quickSort():
    def __init__(self, sortList = []):
        self.unsorted = sortList
        self.sorted = []
        self.reverseSorted = []
        
        def forwardsRecursive(arr, left, right):
            if left < right:
                partition_pos = partition(arr, left, right)
                forwardsRecursive(arr, left, partition_pos -1)
                forwardsRecursive(arr, partition_pos+1, right)
            return arr
        def backwardsRecursive(arr):
            reverseArr = []
            for i in range(len(arr)-1, 0):
                reverseArr.append(arr[i])
            return reverseArr


            
        
        def partition(arr, left, right):
            i = left
            j = right-1
            pivot =  arr[right]
            while i < j:
                while i < right and arr[i] < pivot:
                    i += 1
                while j > left and arr[j] > pivot:
                    j -= 1
                if i < j:
                    arr[j], arr[i] = arr[i], arr[j]
            if arr[i] > pivot:
                arr[i], arr[right] = arr[right], arr[i]
                return i 
        #forwards sort (least to greatest)
        arr = self.unsorted
        self.sorted = forwardsRecursive(arr, 0, len(arr)-1)
        #backwards or reverse sort (greatest to least)
        arr = self.unsorted

        self.reverseSorted = backwardsRecursive(arr)
    def returnUnsorted(self, printUnsorted = False):
        if printUnsorted:
            print(self.unsorted)
        return self.unsorted
    def returnSorted(self, printSorted = False):
        arr = self.unsorted

        if printSorted:
            print(self.sorted)
        return self.sorted
    def returnReverseSorted(self, printSorted = False):
        if printSorted:
            print(self.reverseSorted)
        return self.reverseSorted




#DONT USE IN IMPLEMENTION THIS IS A DEV TEMPLATE
class templateAlgo():
    def __init__(self, sortList = []):
        self.unsorted = sortList
        self.sorted = []
        self.reverseSorted = []
        #forwards sort (least to greatest)
        arr = self.unsorted

        self.sorted = arr
        #backwards or reverse sort (greatest to least)
        arr = self.unsorted

        self.reverseSorted = arr
    def returnUnsorted(self, printUnsorted = False):
        if printUnsorted:
            print(self.unsorted)
        return self.unsorted


    def returnSorted(self, printSorted = False):
        if printSorted:
            print(self.sorted)
        return self.sorted


    def returnReverseSorted(self, printSorted = False):
        if printSorted:
            print(self.reverseSorted)
        return self.reverseSorted
    
