from numba import jit, prange
from utils import private_key_to_address

@jit(nopython=True)
def hamming_distance(a, b):
    return bin(int(a, 16) ^ int(b, 16)).count('1')

@jit(nopython=True, parallel=True)
def search_in_range(start_key, end_key, target_address, target_hamming_distance):
    for key in prange(start_key, end_key):
        key_hex = f"{key:064x}"  # Özel anahtarı hexadecimal formata çevir
        address = private_key_to_address(key_hex)  # Bitcoin adresini oluştur
        hamming_dist = hamming_distance(address, target_address)
        if hamming_dist <= target_hamming_distance:
            return key  # Hedefe yakın anahtar bulundu
    return None
