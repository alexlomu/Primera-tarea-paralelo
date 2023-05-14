from multiprocessing import Pool
import time
import random


def scrape(url):
    print("starting", url)
    duration = round(random.random(),3)
    time.sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration
urls = ["a.com", "b.com", "c.com", "d.com"]

#Secuencial
def secuencial():
    time = 0
    for url in urls:
        time += scrape(url)[1]
    print("El tiempo total ha sido:",time,"segundos")
secuencial()
#Multiproceamiento
def multiprocesamiento():
    initial_time = time.time()
    pool = Pool(processes=4)
    data = pool.map(scrape, urls)
    pool.close()

    