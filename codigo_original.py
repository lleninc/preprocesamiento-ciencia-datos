import time
import math


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r = int(math.sqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    start = time.perf_counter()
    primes = []
    for num in range(2, 100001):
        if is_prime(num):
            primes.append(num)
    end = time.perf_counter()
    print(f"Found {len(primes)} primes between 1 and 100000")
    print(f"Execution time: {end - start:.6f} seconds")


if __name__ == "__main__":
    main()
