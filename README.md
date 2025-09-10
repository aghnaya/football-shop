# App's name : Endorphins Shop
link : https://aghnaya-kenarantanov-footballshop.pbp.cs.ui.ac.id/

## Langkah Pengerjaan

1. Membuat proyek Django dengan `django-admin startproject`.
2. Membuat app `main` dengan `python manage.py startapp main`.
3. Melakukan routing agar app bisa dijalankan di root URL.
4. Membuat model `Product` sesuai ketentuan dan melakukan migrasi.
5. Membuat fungsi view untuk menampilkan info diri dan nama aplikasi.
6. Melakukan routing dari app ke view tersebut.
7. Menambahkan template HTML.
8. Melakukan deployment ke PWS.

## Bagan request client
https://docs.google.com/document/d/1xgGbrqNQ5LQcDUVP2adBJyY-kk0Wy4mFjwyu7iXKkeQ/edit?usp=sharing

### Penjelasan:
- `urls.py` mengarahkan request ke `views.py`.
- `views.py` memproses request, bisa membaca dari `models.py`.
- Hasil dari `views.py` diberikan ke HTML template sebagai response.

## Peran settings.py
File `settings.py` fungsinya sebagai pusat konfigurasi proyek Django:
- Untuk menentukan apps yang digunakan (`INSTALLED_APPS`)
- Konfigurasi database, static files, templates, security
- Setting untuk deployment (DEBUG, ALLOWED_HOSTS)

## Cara Kerja Migrasi Database di Django
1. Definisikan model di `models.py`.
2. Jalankan `makemigrations` untuk membuat skrip migrasi.
3. Jalankan `migrate` untuk menerapkan perubahan ke database.

## Django Cocok Untuk Pemula
- Karena penggunaannya mudah dipahami

## Feedback dari asdos di Tutorial 1
Di tutorial 1, saya belum mengaktifkan Autosave. Saat ini saya sudah mengaktifkan autosave

