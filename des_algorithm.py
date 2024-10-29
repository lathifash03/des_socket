from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import DES

# Kunci DES (harus 8 byte)
key = b'abcdefgh'  # Key ini hardcoded, harus sama di kedua client

def des_encrypt(plain_text):
    """
    Fungsi untuk mengenkripsi teks menggunakan DES
    :param plain_text: Teks yang akan dienkripsi
    :return: Teks terenkripsi dalam bentuk byte
    """
    # Inisialisasi cipher DES dalam mode ECB
    des = DES.new(key, DES.MODE_ECB)
    # Tambahkan padding pada plain text agar panjangnya sesuai kelipatan 8 byte
    padded_text = pad(plain_text.encode(), DES.block_size)
    # Enkripsi teks yang telah di-padding
    encrypted_text = des.encrypt(padded_text)
    return encrypted_text

def des_decrypt(encrypted_text):
    """
    Fungsi untuk mendekripsi teks menggunakan DES
    :param encrypted_text: Teks yang terenkripsi dalam bentuk byte
    :return: Teks asli setelah dekripsi
    """
    # Inisialisasi cipher DES dalam mode ECB
    des = DES.new(key, DES.MODE_ECB)
    # Dekripsi teks
    decrypted_padded_text = des.decrypt(encrypted_text)
    # Hilangkan padding setelah dekripsi
    decrypted_text = unpad(decrypted_padded_text, DES.block_size)
    return decrypted_text.decode()

# Tes sederhana
if __name__ == "__main__":
    message = "Ini adalah pesan rahasia yang panjang lebih dari 8 karakter"
    print("Pesan asli:", message)

    encrypted = des_encrypt(message)
    print("Pesan terenkripsi:", encrypted)

    decrypted = des_decrypt(encrypted)
    print("Pesan setelah dekripsi:", decrypted)
