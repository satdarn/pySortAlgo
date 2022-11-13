class insertSort():
    def __init__(self, sortList = []):
        self.unsorted = sortList
        self.sorted = []
        self.reverseSorted = []
        self.snapshots = {}
    def returnUnsorted(self, printUnsorted = False):
        if printUnsorted:
            print(self.unsorted)
        return self.unsorted
    def returnSorted(self, printSorted = False, snapshots = False):
        arr = self.unsorted
        for i in range(1, len(arr)):
            j = i
            if snapshots:
                    self.snapshots[f"Step {j}"] = arr  
            while arr[j-1] > arr[j] and j > 0:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                j -= 1
                 
        self.sorted = arr
        if printSorted:
            print(self.sorted)
        return self.sorted
    def returnReverseSorted(self, printSorted = False, snapshots = False):
        arr = self.unsorted
        for i in range(1, len(arr)):
            j = i
            if snapshots:
                self.snapshots[f"Reverse Step {i}"] = arr
            while arr[j-1] < arr[j] and j > 0:
                arr[j-1], arr[j] = arr[j], arr[j-1] 
                j -= 1  
        self.reverseSorted = arr
        if printSorted:
            print(self.reverseSorted)
        return self.reverseSorted

class selectionSort():
    def __init__(self, sortList = []):
        self.unsorted = sortList
        self.sorted = []
        self.reverseSorted = []
        self.snapshots = {}
    def returnUnsorted(self, printUnsorted = False):
        if printUnsorted:
            print(self.unsorted)
        return self.unsorted
    def returnSorted(self, printSorted = False, snapshots = False):
        arr = self.unsorted
        for i in range(0, len(arr)-1):
            if snapshots:
                self.snapshots[f"Step {i+1}"] = arr
            curMinIndex = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[curMinIndex]:
                    curMinIndex = j
            arr[i], arr[curMinIndex] = arr[curMinIndex], arr[i]
        self.sorted = arr
        if printSorted:
            print(self.sorted)
        return self.sorted
    def returnReverseSorted(self, printSorted = False, snapshots = False):
        arr = self.unsorted
        for i in range(0, len(arr)-1):
            if snapshots:
                self.snapshots[f"ReverseStep {i+1}"] = arr
            curMaxIndex = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[curMaxIndex]:
                    curMaxIndex = j
            arr[i], arr[curMaxIndex] = arr[curMaxIndex], arr[i]
        self.reverseSorted = arr
        if printSorted:
            print(self.reverseSorted)
        return self.reverseSorted






#DONT USE IN IMPLEMENTION THIS IS A DEV TEMPLATE
class templateAlgo():
    def __init__(self, sortList = []):
        self.unsorted = sortList
        self.sorted = []
        self.reverseSorted = []
        self.snapshots = {}
    def returnUnsorted(self, printUnsorted = False):
        if printUnsorted:
            print(self.unsorted)
        return self.unsorted
    def returnSorted(self, printSorted = False, snapshots = False):
        if printSorted:
            print(self.sorted)
        return self.sorted
    def returnReverseSorted(self, printSorted = False, snapshots = False):
        if printSorted:
            print(self.reverseSorted)
        return self.reverseSorted
    
