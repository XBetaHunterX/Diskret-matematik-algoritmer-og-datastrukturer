"""A max heap is a complete binary tree [CBT] (implemented using array)
in which each node has a value larger than its sub-trees"""

from math import ceil
import sys



class MaxHeap:
    def __init__(self, arr=None):
        self.heap = []
        self.heap_size = 0
        if arr is not None:
            self.create_max_heap(arr)
            self.heap = arr
            self.heap_size = len(arr)

    def create_max_heap(self, arr):
        """
        Converts a given array into a max heap
        :param arr: input array of numbers
        """
        n = len(arr)

        # last n/2 elements will be leaf nodes (CBT property) hence already max heaps
        # loop from n/2 to 0 index and convert each index node into max heap
        for i in range(int(n / 2), -1, -1):
            self.max_heapify(i, arr, n)

    def max_heapify(self, indx, arr, size):
        """
        Assuming sub trees are already max heaps, converts tree rooted at current indx into a max heap.
        :param indx: Index to check for max heap
        """

        # Get index of left and right child of indx node
        left_child = indx * 2 + 1
        right_child = indx * 2 + 2

        largest = indx

        # check what is the largest value node in indx, left child and right child
        if left_child < size:
            if arr[left_child] > arr[largest]:
                largest = left_child
        if right_child < size:
            if arr[right_child] > arr[largest]:
                largest = right_child

        # if indx node is not the largest value, swap with the largest child
        # and recursively call min_heapify on the respective child swapped with
        if largest != indx:
            arr[indx], arr[largest] = arr[largest], arr[indx]
            self.max_heapify(largest, arr, size)

    def insert(self, value):
        """
        Inserts an element in the max heap
        :param value: value to be inserted in the heap
        """
        self.heap.append(value)
        self.heap_size += 1

        indx = self.heap_size - 1

        # Get parent index of the current node
        parent = int(ceil(indx / 2 - 1))

        # Check if the parent value is smaller than the newly inserted value
        # if so, then replace the value with the parent value and check with the new parent
        while parent >= 0 and self.heap[indx] > self.heap[parent]:
            self.heap[indx], self.heap[parent] = self.heap[parent], self.heap[indx]
            indx = parent
            parent = int(ceil(indx / 2 - 1))

    def delete(self, indx):
        """
        Deletes the value on the specified index node
        :param indx: index whose node is to be removed
        :return: Value of the node deleted from the heap
        """
        if self.heap_size == 0:
            print("Heap Underflow!!")
            return

        self.heap[-1], self.heap[indx] = self.heap[indx], self.heap[-1]
        self.heap_size -= 1

        self.max_heapify(indx, self.heap, self.heap_size)

        return self.heap.pop()

    def extract_max(self):
        """
        Extracts the maximum value from the heap
        :return: extracted max value
        """
        return self.delete(0)

    def print(self):
        print(*self.heap)


if __name__ == "__main__": 
    #startHeap="[space separated list of numbers]" insert="[space separated list of numbers]"
    startHeap = []
    toBeInserted = []
    noInfoGiven = True
    for arg in sys.argv:
        if arg.startswith("insert="):
            toBeInserted = arg.split("=")[1].replace("\"", "").replace(",", "").split(" ")
            toBeInserted = list(map(int, toBeInserted))
            noInfoGiven = False
        elif arg.startswith("startHeap="):
            startHeap = arg.split("=")[1].replace("\"", "").replace(",", "").split(" ")
            startHeap = list(map(int, startHeap))
            noInfoGiven = False

    # For each input block and wait for user
    if noInfoGiven:
        temp = input("Enter startHeap as space separated list of numbers (or none):\n").replace(",", "").split(" ")
        if len(temp) > 1:
            startHeap = list(map(int, temp))
        
        temp2 = input("Enter inserted numbers as space separated list of numbers:\n").replace(",", "").split(" ")
        if len(temp2) > 1:
            toBeInserted = list(map(int, temp2))

    # Create a max heap with the given startHeap numbers if provided
    heap = MaxHeap(startHeap)
    # Create a max heap with the given input numbers
    for num in toBeInserted:
        heap.insert(num)

    # Print the max heap
    print("Heap layout:")
    heap.print()

"""
print('Heap: ')
heap.print()
# print(heap.delete(2))
#print('Extract: ')
heap.extract_max()
heap.print()
# hvis der skal udføres 2 heap extract max kør "heap.extract_max()" 2 gange
heap.extract_max()
heap.print()
heap.print()
print('Max-heapify: ')
heap.print()
print('Insert: ')
heap.insert(6)
heap.insert(12)
heap.insert(13)
heap.insert(4)
heap.insert(8)
heap.insert(14)
heap.insert(5)
heap.print() 
"""
