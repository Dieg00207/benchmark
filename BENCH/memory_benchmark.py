import time
def memory_performance():
    large_list = [i for i in range(1000000)]
    start_time = time.time()


    for i in range(1000000):
        large_list[i] = large_list[i] + 1

    end_time = time.time()
    print(f"Memoria RAM: {end_time - start_time:.2f} Seconds")

if __name__ == "__main__":
    memory_performance()
