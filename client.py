import socket
from des_algorithm import des_encrypt, des_decrypt

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    while True:
        # Ambil input dari user
        message = input("Masukkan pesan yang ingin dikirim ke server (atau 'x' untuk keluar): ")
        encrypted_message = des_encrypt(message)  # Mendapatkan pesan dalam format biner

        # Kirim pesan terenkripsi dalam format biner
        client_socket.send(encrypted_message.encode())
        print("Pesan terenkripsi dikirim:", encrypted_message)

        if message.lower() == 'x':
            print("Menghentikan komunikasi.")
            break

        # Terima respons terenkripsi dari server dalam format biner
        encrypted_response = client_socket.recv(1024).decode()
        decrypted_response = des_decrypt(encrypted_response)
        print(f"Pesan terenkripsi diterima dari server: {encrypted_response}")
        print(f"Pesan setelah dekripsi: {decrypted_response}")

    client_socket.close()

if __name__ == '__main__':
    main()
