import os
from multiprocessing import Pool, cpu_count
import time
import random
from src.utils.logger import logger

def worker(x:int ,y:int ,z:int) :
    t: int = random.randint(1, 5)
    pid = os.getpid()  # 현재 프로세스 ID 가져오기
    time.sleep(t)  # 1~3초 사이의 시간이 걸리는 작업
    r =  x * y + z
    logger.info(f"[PID={pid}] : Task {r} is done.")
    return r

# Helper function to unpack arguments
# winodws에서는 lambda 함수를 사용할 수 없음
def unpack_args(args):
    return worker(*args)

if __name__ == '__main__':
    # 인자 목록: (x, y, z) 형태의 튜플 리스트
    tasks = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (10, 11, 12),
        (13, 14, 15),
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (10, 11, 12),
        (13, 14, 15),
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (10, 11, 12),
        (13, 14, 15)
    ]
    num_cores = 3 # cpu_count()  # 시스템의 CPU 코어 수를 가져옴
    logger.info(f"Number of cores: {num_cores}")
    with Pool(processes=num_cores) as pool:  # 4개의 프로세스 생성
        results = pool.imap_unordered(unpack_args, tasks)

        for r in results:
            logger.info(f"Result: {r}")
            


# The error message you're encountering, _pickle.PicklingError: Can't pickle <function <lambda> at ...>, occurs because the lambda function used within multiprocessing.Pool cannot be pickled. This is a limitation of Python's multiprocessing module, particularly when working with Windows. Unlike Unix-based systems where fork is used, Windows uses spawn, requiring objects to be pickle-able.

# To resolve this, we should avoid using lambda functions and instead pass a top-level (module-level) function that can be properly pickled. Let’s refactor your code to use a helper function that will unpack the arguments and call the worker function.