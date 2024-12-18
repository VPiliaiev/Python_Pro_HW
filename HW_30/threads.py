import os
import random
import string
import requests
from multiprocessing.pool import ThreadPool
from contextlib import contextmanager
import time


@contextmanager
def timer(message):
    start = time.time()
    yield
    end = time.time()
    print(message.format(end - start))


def fetch_pic(num_pic):
    url = 'https://picsum.photos/400/600'
    path = os.path.join(os.getcwd(), 'img')
    for _ in range(num_pic):
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'{path}/{random_name}.jpg', 'wb') as f:
                f.write(response.content)


workers = 100
DATA_SIZE = 100
with timer("Elapsed: {}s "):
    with ThreadPool(workers) as pool:
        input_data = [DATA_SIZE // workers for _ in range(workers)]
        pool.map(fetch_pic, input_data)
