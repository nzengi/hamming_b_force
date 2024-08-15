from parallel_search import parallel_search

if __name__ == "__main__":
    # Başlangıç ve bitiş anahtarları
    start_key = 0x00000000000000000000000000000001
    end_key = 0x000000000000000000000000000000FF
    
    # Hedef Bitcoin adresi ve Hamming mesafesi
    target_address = "1BgGZ9tcN4rm9KBzDn7KprQz87SZ26SAMH"
    target_hamming_distance = 2

    # Paralel arama işlemini başlat
    parallel_search(start_key, end_key, target_address, target_hamming_distance)
