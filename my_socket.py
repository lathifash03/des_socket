import socket
from des_algorithm import DES  # Pastikan ini adalah kode DES yang telah dibuat

# Kunci DES yang disepakati kedua user
KEY = 'abcdefgh'  # Contoh key 8 karakter

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server menunggu koneksi...")

    conn, addr = server_socket.accept()
    print(f"Koneksi diterima dari {addr}")

    encrypted_text = conn.recv(1024).decode()  # Terima string terenkripsi
    print("Pesan terenkripsi diterima:", encrypted_text)

    des = DES(KEY)
    decrypted_text = des.decrypt(encrypted_text)  # Dekripsi pesan
    print("Pesan setelah dekripsi:", decrypted_text)

    conn.close()
    server_socket.close()

if __name__ == '__main__':
    main()
