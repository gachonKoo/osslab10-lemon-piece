import sys
import math

def divisors(n: int):
    small, large = [], []
    limit = int(math.isqrt(n))
    for d in range(1, limit + 1):
        if n % d == 0:
            small.append(d)
            if d != n // d:
                large.append(n // d)
    return small + large[::-1]  
def main():
    n = int(sys.argv[1]) 
    print(" ".join(map(str, divisors(n))))

if __name__ == "__main__":
    main()
