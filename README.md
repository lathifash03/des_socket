## Nama: Lathifah Sahda
NRP: 5025221159

# DES Encryption/Decryption with Socket Programming
## Deskripsi
Proyek ini merupakan implementasi algoritma enkripsi DES (Data Encryption Standard) menggunakan socket programming untuk mentransfer string terenkripsi antar dua pengguna. Proyek ini terdiri dari beberapa file yang bekerja sama untuk menyediakan fungsionalitas enkripsi dan dekripsi.

## Table of Contents

- [Struktur Proyek](#StrukturProyek)
- [Cara Menjalankan Proyek](#CaraMenjalankanProyek)
- [Catatan](#catatan)
- [Contoh](#contoh)

## StrukturProyek
/socket │ ├── client.py ├── server.py ├── des_algorithm.py └── README.md


### 1. `client.py`
Client akan digunakan untuk:
- Membuat koneksi ke server.
- Mengirim string terenkripsi ke server setelah mengenkripsi input pengguna.
- Menerima respons dari server, yang merupakan string yang didekripsi.

**Alur Kerja:**
- Menginisialisasi socket dan menghubungkannya ke server.
- Meminta input dari pengguna untuk string yang akan dienkripsi.
- Menggunakan kelas `DES` dari `des_algorithm.py` untuk mengenkripsi string.
- Mengirimkan string terenkripsi ke server.
- Menerima string terdekripsi dari server dan menampilkannya.

### 2. `server.py`
File ini dibuat untuk:
- Menerima koneksi dari client.
- Menerima string terenkripsi dari client.
- Menggunakan kelas `DES` dari `des_algorithm.py` untuk mendekripsi string.
- Mengirimkan string yang telah didekripsi kembali ke client.

**Alur Kerja:**
- Menginisialisasi socket server dan mendengarkan koneksi di port tertentu.
- Menerima koneksi dari client.
- Menerima string terenkripsi dari client.
- Menggunakan kelas `DES` untuk mendekripsi string.
- Mengirimkan string terdekripsi kembali ke client.

### 3. `des_algorithm.py`
File ini berisi implementasi dari algoritma DES, termasuk fungsi untuk:
- Enkripsi dan dekripsi string.
- Penanganan padding untuk memastikan string input sesuai dengan blok DES.

**Fungsi Utama:**
- `encrypt(data: str, key: str) -> str`: Menerima string dan kunci, kemudian mengembalikan string terenkripsi.
- `decrypt(data: str, key: str) -> str`: Menerima string terenkripsi dan kunci, kemudian mengembalikan string yang didekripsi.
le ini berfungsi sebagai panduan untuk proyek, menjelaskan struktur dan alur kerja dari file-file yang ada. Ini bertujuan untuk memberikan pemahaman yang jelas kepada pengguna tentang cara menjalankan dan menggunakan proyek ini.

## CaraMenjalankanProyek
1. **Install Dependencies:**
```bash
   pip install pycryptodome
```

2. **Jalankan Server:**
 Di terminal pertama, jalankan server:
```bash
python server.py
```


3. **Jalankan Client:**
 Di terminal pertama, jalankan server:
```bash
python client.py
```

4. **Masukkan Input:** 
Masukkan string yang ingin Anda enkripsi saat diminta oleh client.

## Catatan:

- Pastikan tidak ada aplikasi lain yang menggunakan port yang sama (misalnya 12345).
- Untuk menutup server, cukup tekan Ctrl+C di terminal yang menjalankan server.

## Contoh: 

Untuk menjalankan program dapat dilakukan dengan dua terminal agar dapat saling mengirim dan menerima pesan. 

**Menjalankan Server**
1. Server menunggu permintaan dari client
<img width="616" alt="Screenshot 2567-10-30 at 23 08 28" src="https://github.com/user-attachments/assets/e204c4f2-f3a5-4135-a3ef-33b22ea92314">

2. Server siap menerima pesan dari client
<img width="615" alt="Screenshot 2567-10-30 at 23 09 19" src="https://github.com/user-attachments/assets/9cb971d7-d139-419e-9850-223ece607ac3">

3. Server menerima pesan
<img width="1293" alt="Screenshot 2567-10-30 at 23 12 32" src="https://github.com/user-attachments/assets/3b662a84-9b76-4fec-8390-a63d79568731">


**Menjalankan Client**
1. Client dijalankan
<img width="659" alt="Screenshot 2567-10-30 at 23 10 48" src="https://github.com/user-attachments/assets/8b052a61-e940-4ad3-8a74-0f6208035cb1">

2. Pesan dikirim
<img width="1293" alt="Screenshot 2567-10-30 at 23 12 32" src="https://github.com/user-attachments/assets/3b662a84-9b76-4fec-8390-a63d79568731">

