# Leetcode 509

def fib(n: int) -> int:
    cache_size = 2
    def main(n, cache={}):
        if n <= 1:
            return n
        if n in cache:
            return cache[n]
        cache[n] = main(n-1, cache) + main(n-2, cache)

        if len(cache) > cache_size:
            del cache[next(iter(cache))]
        return cache[n]
    return main(n)
