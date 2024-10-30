# python3 -m venv env
# source env/bin/activate
# pip install pycryptodome

import socket
from des_algorithm import des_decrypt, des_encrypt

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 12345))
    server_socket.listen(1)
    print("Server berjalan dan menunggu koneksi dari client...")

    conn, addr = server_socket.accept()
    print(f"Koneksi dari: {addr}")

    while True:
        # Terima pesan terenkripsi dalam format biner dari client
        encrypted_data = conn.recv(1024).decode()  # Diterima dalam bentuk string biner
        if not encrypted_data:
            print("Client telah memutus koneksi.")
            break

        # Dekripsi pesan yang diterima
        decrypted_message = des_decrypt(encrypted_data)
        print(f"Pesan terenkripsi diterima dari client: {encrypted_data}")
        print(f"Pesan setelah dekripsi: {decrypted_message}")

        # Jika pesan dari client adalah "x", keluar dari loop
        if decrypted_message.lower() == 'x':
            print("Client menghentikan komunikasi.")
            break

        # Kirim pesan terenkripsi kembali ke client
        response_message = input("Masukkan pesan yang ingin dikirim ke client (atau 'x' untuk keluar): ")
        encrypted_response = des_encrypt(response_message)
        conn.send(encrypted_response.encode())  # Mengirimkan string biner terenkripsi

        if response_message.lower() == 'x':
            print("Menghentikan komunikasi.")
            break

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    main()
