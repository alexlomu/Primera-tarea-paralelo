# Primera-tarea-paralelo
El link de este repositorio es el siguiente: [GitHub](https://github.com/alexlomu/Primera-tarea-paralelo)

## Hacer el trabajo secuencialmente

El código utilizado es el siguiente:

        def secuencial():
            time = 0
            for url in urls:
                time += scrape(url)[1]
            print("El tiempo total ha sido:",time,"segundos")

Y el output recibido es:

        starting a.com
        finished a.com time taken: 0.649 seconds
        starting b.com
        finished b.com time taken: 0.451 seconds
        starting c.com
        finished c.com time taken: 0.338 seconds
        starting d.com
        finished d.com time taken: 0.462 seconds
        El tiempo total ha sido: 1.9000000000000001 segundos

## Hacer el trabajo con multiprocesos

El código utilizado es el siguiente:

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
