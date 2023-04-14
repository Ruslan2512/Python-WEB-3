import multiprocessing
import logging
from multiprocessing import Pool
import time



logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

def factorize(*number):
    # YOUR CODE HERE
    a = []
    b = []
    c = []
    d = []
    for i in number:
        for j in range(1, i+1):
            if i == number[0]:    
                if i % j == 0:
                    a.append(j)
                else:
                    continue
            elif i == number[1]:    
                if i % j == 0:
                    b.append(j)
                else:
                    continue    
            elif i == number[2]:    
                if i % j == 0:
                    c.append(j)
                else:
                    continue
            elif i == number[3]:    
                if i % j == 0:
                    d.append(j)
                else:
                    continue
            else:
                continue

    return a

if __name__ == '__main__':
    timer = time.time()
    factorize(128, 255, 99999, 10651060)
    timer_count_1 = round(time.time() - timer, 2)
    print(f"Time of program with synchronization : {timer_count_1}")

    with Pool(processes=multiprocessing.cpu_count()) as pool:
        logger.debug(pool.map(factorize, (128, 255, 99999, 10651060)))
    
    timer_count_2 = round(time.time() - timer, 2)
    print(f"Time of program with multiprocessing : {timer_count_2}")
    print("Number of cpu : ", multiprocessing.cpu_count())



