import numpy as np
from numba import jit, prange
import multiprocessing as mp

# Hamming mesafesini hesaplayan fonksiyon
@jit(nopython=True)
def hamming_distance(a, b):
    return bin(a ^ b).count('1')

# Bitcoin özel anahtarları arasında paralel arama yapan fonksiyon
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
    
# Belirli bir aralıkta arama yapan fonksiyon
@jit(nopython=True, parallel=True)
def search_in_range(start_key, end_key, target_address, target_hamming_distance):
    for key in prange(start_key, end_key):
        # Anahtarın adresini hesapla
        address = hash_function(key)  # hash_function ile Bitcoin adresini oluştur
        hamming_dist = hamming_distance(address, target_address)
        if hamming_dist <= target_hamming_distance:
            return key  # Hedefe yakın anahtar bulundu
    return None
