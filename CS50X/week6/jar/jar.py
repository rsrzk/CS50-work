class Jar:
    def __init__(self, capacity=12):
        if capacity > 0:
                self._capacity = capacity
                self._size = 10
        else:
             raise ValueError('Capacity value needs to be an integer more than')


    def __str__(self):
         return "🍪" * self._size


    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError('Exceed jar capacity')
        self._size += n

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError('Exceed jar contents')
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar(30)
    print(str(jar.capacity))
    print(str(jar))
    jar.deposit(15)
    print(str(jar))
    jar.withdraw(40)
    print(str(jar))

main()
