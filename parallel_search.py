import multiprocessing as mp
from hamming import search_in_range

def parallel_search(start_key, end_key, target_address, target_hamming_distance):
    pool = mp.Pool(mp.cpu_count())
    results = []

    # İşçilere iş atama
    for key in range(start_key, end_key, 100000):  # Anahtar aralığını işçilere bölme
        results.append(pool.apply_async(search_in_range, args=(key, key + 100000, target_address, target_hamming_distance)))

    # İşçilerin sonuçlarını toplama
    pool.close()
    pool.join()
    
    # Bulunan sonuçlar
    for result in results:
        if result.get():
            print(f"Found a match: {result.get()}")
