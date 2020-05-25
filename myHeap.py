class myHeap:
    # max priority

    def __init__(self, A):
        self.list = A.copy()
        self.size = len(A)
    
    def __repr__(self):
        out = "["
        for i, num in enumerate(self.list):
            if (i != 0):
                out = out + f" {num}"
            else:
                out = out + f"{num}"
        out = out + "]"
        return out
    
    def make_heap(self):
        for i in range(self.size // 2 - 1, -1, -1):
            self.max_heapify(self.list, i)

    def leftkey(self, A, i):
        if (2 * i + 1 > len(A) - 1):
            return f"key {i} has no leftson!"
        return 2 * i + 1
    
    def rightkey(self, A, i):
        if (2 * i + 2 > len(A) - 1):
            return f"key {i} has no rightson!"
        return 2 * i + 2
    
        
    def max_heapify(self, A, i):
        left = self.leftkey(A, i)
        right = self.rightkey(A, i)
        length = len(A)
        if (type(left) != str and left < length and A[left] > A[i]):
            largest = left
        else:
            largest = i
        if (type(right) != str and right < length and A[right] > A[largest]):
            largest = right
        if (largest != i):
            A[i], A[largest] = A[largest], A[i]
            self.max_heapify(A, largest)
    
    def heapsort(self, ascend=True):
        temp = self.list.copy()
        output = []
        while (len(output) < self.size):
            output.append(temp[0])
            temp[0], temp[-1] = temp[-1], temp[0]
            temp.pop()
            self.max_heapify(temp, 0)
        if (ascend):
            return output[::-1]
        else:
            return output

    def pop_first(self):
        if (not self.list):
            return "The heap is empty!"
        out = self.list[0]
        self.list[0], self.list[-1] = self.list[-1], self.list[0]
        self.list.pop()
        self.max_heapify(self.list, 0)
        return out

    def insert(self, data):
        self.list.append(data)
        length = len(self.list)
        temp = length // 2 - 1
        while (temp >= 0):
            self.max_heapify(self.list, temp)
            temp = temp // 2 - 1
        

    

    

