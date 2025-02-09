class FibonacciIterator:
    def __init__(self, n): #n - max number of Fibonacci
        self.n = n
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration()
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.n -= 1
        return result

fib = FibonacciIterator(10)

for num in fib:
    print(num)

