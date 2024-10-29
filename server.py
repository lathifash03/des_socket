# python3 -m venv env
# source env/bin/activate
# pip install pycryptodome

import socket
from des_algorithm import DES  # Pastikan des_algorithm.py berisi implementasi DES yang telah kamu buat

# Key yang disepakati oleh server dan client
KEY = "DESCRYPT"  # Panjangnya 8 karakter, sesuai DES 64-bit

# Inisialisasi socket untuk server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))  #Binding di port 12345
server_socket.listen(1)  # Maksimal satu client yang terhubung

print("Server berjalan dan menunggu koneksi dari client...")

# Menerima koneksi dari client
client_socket, client_address = server_socket.accept()
print(f"Koneksi dari: {client_address}")

# Menerima pesan terenkripsi dari client
encrypted_data = client_socket.recv(1024)  # Maksimal menerima 1024 byte
encrypted_data = encrypted_data.decode()

print(f"Data terenkripsi diterima dari client: {encrypted_data}")

# Dekripsi data terenkripsi menggunakan DES
des = DES(KEY)  # Inisialisasi objek DES dengan KEY
decrypted_data = des.decrypt(encrypted_data)

print(f"Data setelah dekripsi: {decrypted_data}")

# Tutup koneksi
client_socket.close()
server_socket.close()
