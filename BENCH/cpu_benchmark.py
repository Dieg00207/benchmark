import timeit

def cpu_performance():
    test_statement = """
import math
[math.exp(i) * math.sinh(i) for i in range(700)]
"""
    duration = timeit.timeit(stmt=test_statement, number=700)
    print(f"Cpu Benchmark: {duration:.2f} segundos")

if __name__ == "_main_":
    cpu_performance()