import time

# Recursive Euclidean algorithm

def recursive_gcd(a, b):
    if b == 0:
        return a
    else:
        return recursive_gcd(b, a % b)

# Iterative Euclidean algorithm

def iterative_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Performance analysis

def measure_performance(func, a, b, repeats=1000):
    start_time = time.perf_counter()
    for _ in range(repeats):
        func(a, b)
    end_time = time.perf_counter()
    return (end_time - start_time) / repeats

# Test cases

test_cases = [
    (48, 18),
    (56, 98),
    (101, 103),
    (270, 192),
    (1071, 462)
]

# Run tests
for a, b in test_cases:
    print(f'GCD of {a} and {b} using recursive approach: {recursive_gcd(a, b)}')
    print(f'GCD of {a} and {b} using iterative approach: {iterative_gcd(a, b)}')

# Performance measurement for 1000 repetitions
print('\nPerformance Analysis:')
for a, b in test_cases:
    recursive_time = measure_performance(recursive_gcd, a, b)
    iterative_time = measure_performance(iterative_gcd, a, b)
    print(f'GCD of {a} and {b}: Recursive time = {recursive_time:.10f} sec, Iterative time = {iterative_time:.10f} sec\n')
