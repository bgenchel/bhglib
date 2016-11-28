#!/bin/python
# import sys


class Heap:
    def __init__(self):
        self.heap = []
        self.__len__ = self.heap.__len__
        self.__str__ = self.heap.__str__

    def swap(self, index1, index2):
        tmp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = tmp
        return

    def getParentIndex(self, index): return abs(index - 1)/2
    def getParent(self, index): return self.heap[self.getParentIndex(index)]
    def hasLeftChild(self, index): return index*2 + 1 < len(self.heap)
    def getLeftChildIndex(self, index): return index*2 + 1
    def getLeftChild(self, index): return self.heap[self.getLeftChildIndex(index)]
    def hasRightChild(self, index): return index*2 + 2 < len(self.heap)
    def getRightChildIndex(self, index): return index*2 + 2
    def getRightChild(self, index): return self.heap[self.getRightChildIndex(index)]

    def getSwapChildIndex(self, index):
        if self.hasLeftChild(index):
            leftChildIndex = self.getLeftChildIndex(index)
            leftChild = self.heap[leftChildIndex]
        else:
            return -1  # if it doesn't have a left child, it doesn't have a right either, bc heap

        if self.hasRightChild(index):
            rightChildIndex = self.getRightChildIndex(index)
            rightChild = self.heap[rightChildIndex]
        else:
            rightChildIndex = -1
            rightChild = (float('-inf'), float('inf'))[self.comp(0, 1)]  # use appropriately with heap direction

        return (rightChildIndex, leftChildIndex)[self.comp(leftChild, rightChild)]

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def pop(self):
        if len(self.heap) == 0:
            return None

        self.swap(0, len(self.heap) - 1)
        minimum = self.heap.pop()
        self.heapifyDown()
        return minimum

    def insert(self, element):
        self.heap.append(element)
        self.heapifyUp()

    def heapifyUp(self):
        index = len(self.heap) - 1
        parent_index = self.getParentIndex(index)
        while self.comp(self.heap[index], self.heap[parent_index]):
            # print "index = %d, parent_index = %d"%(index, parent_index)
            # print "swapping %d and %d"%(self.heap[index], self.heap[parent_index])
            self.swap(index, parent_index)
            index = parent_index
            parent_index = self.getParentIndex(index)
        return

    def heapifyDown(self):
        index = 0
        while True:
            swapChildIndex = self.getSwapChildIndex(index)
            if swapChildIndex < 0:
                break

            if self.comp(self.heap[index], self.heap[swapChildIndex]):
                break
            else:
                self.swap(index, swapChildIndex)
            index = swapChildIndex
        return


class MinHeap(Heap):
    def __init__(self):
        Heap.__init__(self)
        self.comp = lambda x1, x2: x1 < x2


class MaxHeap(Heap):
    def __init__(self):
        Heap.__init__(self)
        self.comp = lambda x1, x2: x1 > x2


class MedianHeap:
    def __init__(self):
        self.minHeap = MinHeap()
        self.maxHeap = MaxHeap()

    def average(self, one, two):
        if one is None or two is None:
            return None
        return (self.minHeap.peek() + self.maxHeap.peek())/float(2)

    def get_median(self):
        if len(self.minHeap) > len(self.maxHeap):
            median = float(self.minHeap.peek())
        elif len(self.minHeap) < len(self.maxHeap):
            median = float(self.maxHeap.peek())
        else:
            median = self.average(self.minHeap.peek(), self.maxHeap.peek())

        return median

    def insert(self, element):
        currMed = self.get_median()
        if currMed is None:
            self.minHeap.insert(element)
        elif element < currMed:
            self.maxHeap.insert(element)
        elif element >= currMed:
            self.minHeap.insert(element)

        if len(self.minHeap) - len(self.maxHeap) > 1:
            self.maxHeap.insert(self.minHeap.pop())
        elif len(self.maxHeap) - len(self.minHeap) > 1:
            self.minHeap.insert(self.maxHeap.pop())
        return

