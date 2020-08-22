import memory_profiler
import time

# List comprehension
# result = [2 * i - 1 for i in [1, 2, 3, 4, 5]]

# Generator comprehension
# result = (2 * i - 1 for i in [1, 2, 3, 4, 5])

# print(result)

def f_list(x):
    result = []
    for i in x:
        result.append(2 * i - 1)
    return result

def f_gen(x):
    for i in x:
        yield(2 * i - 1)

if __name__ == '__main__':
    mem_before = memory_profiler.memory_usage()[0]
    t1 = time.time()

    # output = f_list(range(100000000))
    output = f_gen(range(100000000))

    mem_after = memory_profiler.memory_usage()[0]
    t2 = time.time()

    print(f'Execution time: {t2 - t1} seconds')
    print(f'Memory used: {mem_after - mem_before} Mb')
