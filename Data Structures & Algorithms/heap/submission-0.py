class MinHeap:
    
    def __init__(self):
        self.arr = []

    def heapify_up(self, idx):
        if idx <= 0:
            return

        parent = (idx - 1) // 2
        if self.arr[idx] < self.arr[parent]:
            self.arr[idx], self.arr[parent] = self.arr[parent], self.arr[idx]
            self.heapify_up(parent)
        return 

    def heapify_down(self, idx):
        if idx >= len(self.arr):
            return

        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < len(self.arr) and right < len(self.arr):
            smaller = left if self.arr[left] < self.arr[right] else right

        elif left < len(self.arr):
            smaller = left

        elif right < len(self.arr):
            smaller = right

        else:
            return

        if self.arr[smaller] < self.arr[idx]:
            self.arr[idx], self.arr[smaller] = self.arr[smaller], self.arr[idx]
            self.heapify_down(smaller)
        return 

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.heapify_up(len(self.arr) - 1)

    def pop(self) -> int:
        if not self.arr:
            return -1
        print(self.arr)
        self.arr[-1], self.arr[0] = self.arr[0], self.arr[-1]
        temp = self.arr.pop()
        self.heapify_down(0)
        return temp

    def top(self) -> int:
        if not self.arr:
            return -1
        return self.arr[0]
        

    def heapify(self, nums: List[int]) -> None:
        for i in nums:
            print(self.arr)
            self.push(i)
        