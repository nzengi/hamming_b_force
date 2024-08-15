import numpy as np
from numba import jit, prange

# Hamming mesafesini hesaplayan fonksiyon
@jit(nopython=True)
def hamming_distance(a, b):
    return bin(a ^ b).count('1')

# Belirli bir aralıkta arama yapan fonksiyon (paralel işlemli)
@jit(nopython=True, parallel=True)
def search_in_range(start_key, end_key, target_address, target_hamming_distance):
    for key in prange(start_key, end_key):
        address = hash_function(key)  # hash_function ile Bitcoin adresini oluştur
        hamming_dist = hamming_distance(address, target_address)
        if hamming_dist <= target_hamming_distance:
            return key  # Hedefe yakın anahtar bulundu
    return None
