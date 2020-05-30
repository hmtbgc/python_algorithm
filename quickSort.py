class quickSort:
    def __init__(self):
        pass
    
    def Sort(self, list):
        self.sort(list, 0, len(list) - 1)

    def sort(self, list, l, r):
        if (l > r):
            return 
        pivot = list[l]
        i, j = l + 1, r
        while (i <= j):
            while (i <= j and list[i] < pivot):
                i += 1
            while (i <= j and list[j] > pivot):
                j -= 1
            if (i < j):
                list[i], list[j] = list[j], list[i]
                i += 1
                j -= 1
        list[l], list[j] = list[j], list[l]
        self.sort(list, l, j - 1)
        self.sort(list, j + 1, r)
    

