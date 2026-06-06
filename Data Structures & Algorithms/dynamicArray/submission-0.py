class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be greater than 0")

        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        lastValue = self.arr[self.size - 1]
        self.size -= 1
        return lastValue
 
    def resize(self) -> None:
        newArr = [0] * (self.capacity * 2)
        
        for i in range (self.size):
            newArr[i] = self.arr[i]

        self.arr = newArr
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
        
    def getCapacity(self) -> int:
        return self.capacity