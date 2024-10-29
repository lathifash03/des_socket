import socket
from des_algorithm import DES  

KEY = 'abcdefgh'  # Contoh key 8 karakter

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))  # Koneksi ke server

    # Ambil input dari user dan pad jika lebih dari 8 karakter
    plaintext = input("Masukkan pesan: ")
    des = DES(KEY)
    encrypted_text = des.encrypt(plaintext)  # Enkripsi pesan

    # Kirim string terenkripsi
    client_socket.send(encrypted_text.encode())
    print("Pesan terenkripsi dikirim:", encrypted_text)

    client_socket.close()

if __name__ == '__main__':
    main()
