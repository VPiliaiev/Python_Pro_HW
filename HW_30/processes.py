import random
import threading
from multiprocessing.pool import ThreadPool
from contextlib import contextmanager
import time


@contextmanager
def timer(message):
    start = time.time()
    yield
    end = time.time()
    print(message.format(end - start))


DATA_SIZE = 10_000_000
lst1 = []
lst2 = []


def fill_data1(n):
    print(threading.current_thread())
    while n > 0:
        n -= 1
        lst1.append(random.randint(1, 100))


def fill_data2(n):
    print(threading.current_thread())
    while n > 0:
        n -= 1
        lst2.append(random.randint(1, 100))


with timer("Elapsed: {}s "):
    fill_data1(DATA_SIZE)

workers = 8
with timer("Elapsed: {}s"):
    with ThreadPool(workers) as pool:
        input_data = [DATA_SIZE // workers for _ in range(workers)]
        pool.map(fill_data1, input_data)
        pool.map(fill_data2, input_data)

with timer('Elapsed: {}s'):
    fill_data1(DATA_SIZE // 2)
    fill_data2(DATA_SIZE // 2)

with timer('Elapsed: {}s'):
    t1 = threading.Thread(target=fill_data1, args=(DATA_SIZE // 2,))
    t2 = threading.Thread(target=fill_data2, args=(DATA_SIZE // 2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

print(f"total len lst1: {len(lst1)}")
print(f"total len lst2: {len(lst2)}")
print(f"first 100 el lst1: {lst1[:100]}")
print(f"first 100 el lst2: {lst2[:100]}")
