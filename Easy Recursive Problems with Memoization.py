class memoization:
    def __init__(self):
        self.cache = {}
        self.memo = {}
        self.p_cache = {}
        self.sum_cache = {}

    def fib(self, n):
        if n in self.cache:
            return self.cache[n]
        else:
            self.cache[n] = n if n < 2 else self.fib(n - 2) + self.fib(n -1)
            return self.cache[n]

    def factorial(self, n):
        if n in self.memo:
            return self.memo[n]
        else:
            self.memo[n] = 1 if n == 1 else n*self.factorial(n- 1)
            return self.memo[n]

    def power(self, x, n):
        if n in self.p_cache:
            return self.p_cache[n]
        else:
            self.p_cache[n] = 1 if n == 0 else x*self.power(x, n- 1)
            return self.p_cache[n]

    def sum(self, arr):
        n = len(arr)
        if n in self.sum_cache:
            return self.sum_cache[n]
        else:
            self.sum_cache[n] = arr[0] if n == 1 else self.sum(arr[1:]) + arr[0]
            return self.sum_cache[n]

    def sum_string(self, string):
        string = int(string)
        if string == 0:
            return 0
        else:
            return (string % 10 + self.sum_string(string/10))

    def natural_sum(self, n):
        if n == 0:
            return 0
        else:
            return n + self.natural_sum(n - 1)

def main():
    creator = memoization()
    print(creator.fib(10))
    print(creator.power(2, 5))
    print(creator.sum([1,3,5,6]))
    my_str = '12345'
    print(creator.sum_string(my_str))
    print(creator.natural_sum(6))
main()
