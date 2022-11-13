#Joseph Bronsten Nov 13 2022
#PySort is an Expanding Libary of Python Sorting Algos 
#
#Each Algo accepts a list of Ints and will return
#
#
#
#

class insertSort():
    def __init__(self, sortList = []):
        self.unsorted = sortList
        self.sorted = []
    def returnUnsorted(self, printUnsorted = False):
        if printUnsorted:
            print(self.unsorted)
        return self.unsorted
    def returnSorted(self, printSorted = False):
        arr = self.unsorted
        for i in range(1, len(arr)):
            j = i
            while arr[j-1] < arr[j] and j > 0:
                arr[j-1], arr[j] = arr[j], arr[j-1] 
                j -= 1  
        self.sorted = arr
        if printSorted:
            print(self.sorted)
        return self.sorted
        
print(insertSort([2,6,5,1,3,4]).returnSorted())

