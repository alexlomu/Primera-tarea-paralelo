from multiprocessing import Pool
import time
import random

urls = ["a.com", "b.com", "c.com", "d.com"]
def scrape(url):
    print("starting", url)
    duration = round(random.random(),3)
    time.sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration


#Secuencial
def secuencial():
    time_sec = 0
    for url in urls:
        time_sec += scrape(url)[1]
    print("El tiempo total ha sido:",time_sec,"segundos")

#Multiproceamiento
def multiprocesamiento():
    initial_time = time.time()
    pool = Pool(processes=4)
    data = pool.map(scrape, urls)
    pool.close()
    pool.join()
    for row in data:
        print(row)
    time_mult = time.time() - initial_time
    print("El tiempo total ha sido:",time_mult,"segundos")


multiprocesamiento()
    




    