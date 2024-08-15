import hashlib
import codecs
import ecdsa
import base58

# Özel anahtarı WIF (Wallet Import Format) formatına dönüştürme
def private_key_to_wif(private_key_hex):
    private_key_bytes = codecs.decode(private_key_hex, 'hex')
    extended_key = b'\x80' + private_key_bytes  # Bitcoin Mainnet prefix
    sha256_1 = hashlib.sha256(extended_key).digest()
    sha256_2 = hashlib.sha256(sha256_1).digest()
    checksum = sha256_2[:4]
    wif = base58.b58encode(extended_key + checksum)
    return wif.decode()

# Özel anahtardan Bitcoin adresi oluşturma
def private_key_to_address(private_key_hex):
    private_key_bytes = codecs.decode(private_key_hex, 'hex')
    
    # ECDSA imzası ve SHA-256
    sk = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    public_key = b'\x04' + vk.to_string()
    
    sha256_1 = hashlib.sha256(public_key).digest()
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256_1)
    hashed_public_key = ripemd160.digest()
    
    mainnet_key = b'\x00' + hashed_public_key  # Bitcoin Mainnet prefix
    sha256_2 = hashlib.sha256(mainnet_key).digest()
    sha256_3 = hashlib.sha256(sha256_2).digest()
    checksum = sha256_3[:4]
    
    binary_address = mainnet_key + checksum
    address = base58.b58encode(binary_address)
    
    return address.decode()
