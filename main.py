import time
from multiprocessing import Pool, cpu_count

def divisors(number: int):
    result = [] 

    for i in range (1, number + 1):
        if number % i == 0:
            result.append(i)

    return result 



def factorize (*numbers):
    result = [] 
    for n in numbers:
        result.append(divisors(n))
    return result 



def factorize_parallel(*numbers):
    with Pool(cpu_count()) as pool:
        return pool.map(divisors, numbers)
    

if __name__ == "__main__":

    start = time.time()
    factorize(128, 255, 99999, 10651060, 206020500)
    end = time.time()


    start1 = time.time()
    factorize_parallel(128, 255, 99999, 10651060, 206020500)
    end1 = time.time()


    print("Default:", end - start)
    print("Parallel:", end1 - start1)




