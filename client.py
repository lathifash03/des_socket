# client.py
import socket
from des_algorithm import des_encrypt  # Mengimpor fungsi enkripsi

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))  # Koneksi ke server

    # Ambil input dari user
    plaintext = input("Masukkan pesan: ")
    encrypted_text = des_encrypt(plaintext)  # Enkripsi pesan dengan fungsi des_encrypt

    # Kirim string terenkripsi
    client_socket.send(encrypted_text)
    print("Pesan terenkripsi dikirim:", encrypted_text)

    client_socket.close()

if __name__ == '__main__':
    main()
