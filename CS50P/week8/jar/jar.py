class Jar:
    def __init__(self, capacity=12):
        if isinstance(capacity, int) and capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError("Invalid capacity")
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self._size + n <= self.capacity:
            self._size += n
        else:
            raise ValueError("Too many cookies!")

    def withdraw(self, n):
        if self._size - n >= 0:
            self._size -= n
        else:
            raise ValueError("Not enough cookies!")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar(20)
    print(f"Capacity: {jar.capacity}")
    jar.deposit(10)
    print(jar)
    jar.withdraw(5)
    print(jar)

if __name__ == "__main__":
    main()
