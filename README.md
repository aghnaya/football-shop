# Tugas 3 PBP 
# 1. Mengapa kita memerlukan data delivery dalam platform? 
Data delivery dibutuhkan agar platform dapat berjalan secara efisien dan tetap aman. Karena tanpa adanya data delivery platform tidak bisa berjalan dengan baik.

# 2. Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer? 
Menurut saya, JSON lebih mudah dipahami. Kemungkinan JSON lebih populer adalah karena lebih praktis penggunaanya.

# 3. Fungsi dari is_valid() pada form Django  
Fungsi is_valid berfungsi untuk memvalidasi data input sesuai dengan aturan field. Hal ini agar tidak ada data invalid yang masuk

# 4. Mengapa perlu csrf_token di form Django?  
csrf_token berfungsi untuk mencegah adanya CSRF atau serangan Cross-Site Request Forgery. CSRF adalah salah satu serangan yang dapat membuat pengguna web melakukan tindakan yang tidak diinginkan tanpa sepengetahuan mereka. 

# 5. Step-by-step implementasi checklist:  
1. Menambahkan views untuk json dan xml.  
2. Menambahkan routing pada urls.py. 
3. Membuat tombol add dan detail.
4. Membuat file baru forms.py untuk menambahkan objek.  
5. Melakukan testing dengan browser dan Postman.  
6. Commit & push ke GitHub.  

# 6. Feedback untuk asdos:  
Menurut saya, tutorial 2 cukup mudah dipahami. Namun saya masih belum familiar dengan aplikasi Postman.

## 7. Screenshots Postman
- JSON 
  https://docs.google.com/document/d/1k4wvmzEX9uwfPA6IIUr_0PzFv8a9mYXWIeBiDz1ro2E/edit?tab=t.0

- XML   
  https://docs.google.com/document/d/1k4wvmzEX9uwfPA6IIUr_0PzFv8a9mYXWIeBiDz1ro2E/edit?tab=t.majroqxq6znb

- JSON by ID
  https://docs.google.com/document/d/1k4wvmzEX9uwfPA6IIUr_0PzFv8a9mYXWIeBiDz1ro2E/edit?tab=t.ifbh1gefsbqp

- XML by ID  
  https://docs.google.com/document/d/1k4wvmzEX9uwfPA6IIUr_0PzFv8a9mYXWIeBiDz1ro2E/edit?tab=t.wr99vip6fq3y

-----------------------------------------------------------
# Tugas 4 PBP
# 1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
AuthenticationForm adalah form bawaan Django yang digunakan untuk melakukan login. AuthenticationForm memiliki kelebihan dan kekurangan. Kelebihan: Praktis, aman, langsung terintegrasi dengan sistem autentikasi Django.
Kekurangan: Tampilan standar, kurang fleksibel.

# 2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
-Autentikasi: Mengecek identitas user (login dengan username & password).
-Otorisasi: Mengecek izin yang dimiliku user (apa yang boleh atau tidak boleh dilakukan setelah login).

Django mengimplementasikan autentikasi lewat AuthenticationForm/User, dan melakukan otorisasi lewat permissions & decorator seperti @login_required.

# 3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
-Session: Data disimpan di server, lebih aman, tapi butuh resource server.
-Cookies: Data disimpan di browser, ringan, tapi agak kurang aman kalau tidak diamankan.

# 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Cookies tidak sepenuhnya aman. Data di browser bisa dicuri kalau tidak dilindungi. Karena itu, cookies perlu dikonfigurasi dengan benar. Django menangani hal ini dengan opsi seperti HttpOnly (supaya cookie tidak bisa diakses via JavaScript), Secure (cookie hanya dikirim lewat HTTPS), dan SESSION_COOKIE_AGE (mengatur masa berlaku cookie). Dengan pengaturan ini, risiko yang mungkin terjadi dapat berkurang.

# 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
-Register, login, logout: Menggunakan UserCreationForm & AuthenticationForm. Menambahkan view & template.
-Dummy data: Membuat 2 akun user, menambahkan masing-masing 3 produk.
-Relasi Product-User: Menambahkan field user = models.ForeignKey(User, ...) di model.
-Last login & username: Menyimpan last_login di cookies, lalu ditampilkan bersama username di halaman utama.

----------------------------------------------------------
# Tugas 5 PBP
# Tugas Desain Web - Endorphins Shop
## Checklist (yang sudah diimplementasikan)
- Mengimplementasikan fitur edit product
- Mengimplementasikan fitur delete product 
- Kustomisasi halaman: login, register, add product, edit product, detail product.
- Halaman daftar product responsive, bisa menampilkan gambar dan penjelasan kalau produknya kosong.
- Setiap card product punya tombol Edit & Delete. Edit & Delete cuma bisa dilakukan penjual
- Navbar responsive.

## 1. Urutan prioritas CSS selector
Urutan prioritas (specificity) dari rendah ke tinggi:
1. Selector element (contoh: `div`, `p`).
2. Selector class/atribut/pseudo-class (contoh: `.card`, `[type="text"]`, `:hover`).
3. Selector ID (`#main`).
4. Inline style (contoh: `<div style="color:red">`).
5. Kalau ada dua aturan `!important`, yang punya specificity lebih tinggi yang menang.

Selain specificity, urutan deklarasi juga berpengaruh: jika specificity sama, yang terakhir ditulis menang.


## 2. Mengapa responsive design penting?
Responsive design penting karena bisa menyesuaikan ukuran layarnya, ini bisa memudahkan pengguna juga. 
Contoh yang sudah responsive : Twitter
Contoh yang belum responsive : https://jatirejo.semarangkota.go.id/en/web-pemerintahan

## 3. Perbedaan margin, border, padding
Box model:
- margin: ruang di luar border; memisahkan elemen satu dengan lainnya.
- border : garis pembatas di konten dan padding
- padding: ada di dalam border, memisahkan konten dengan border.

Contoh css:
.box {
  margin: 16px;  /* jarak ke elemen luar */
  border: 2px solid #ccc; /* garis */
  padding: 8px; /* jarak antara konten dan border */
}

## Jelaskan konsep flex box dan grid layout beserta kegunaannya!
- Flexbox : cara menata elemen dalam satu baris atau kolom sehingga mudah diratakan dan disesuaikan ukurannya, cocok untuk navbar atau daftar item. 
- Grid layout : untuk menata elemen dalam baris dan kolom sekaligus, cocok untuk layout kompleks (dashboard, gallery)

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
- Menambah Tailwind
- Menambahkan edit_news dan delete_news di views.py
- Menambahkan path edit_news dan delete_news di urls.py
- Menambahkan navbar.html
- Update login.html, register.html, main.html, add_product.html, product_detail.html
- Menambahkan card_product.html dan edit_product.html
- menambahkan folder image lalu gambar no-product

----------------------------------------------------------
# Tugas 6 PBP
# Apa perbedaan antara synchronous request dan asynchronous request?
- Synchronous: browser minta data lalu menunggu sampai server jawab — selama itu halaman bisa nge-freeze.
- Asynchronous: browser kirim permintaan lalu lanjut,  ketika jawab datang, JavaScript yang update tampilan. 

# Bagaimana AJAX bekerja di Django (alur request–response)?
User tekan tombol -> JS pakai fetch() kirim request ke URL Django -> view di Django proses (validasi, DB, auth) -> view balas JsonResponse (atau kode 201/400, dsb) -> JS terima, parse JSON, lalu update DOM tanpa reload halaman.

# Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
- Halaman nggak perlu reload, jadi terasa lebih cepat.
- Hemat data karena hanya kirim/terima JSON, bukan HTML penuh.
- Bisa tampilkan loading/empty/error/toast dengan cepat.

# Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
- Pakai HTTPS.
- Pakai CSRF token untuk POST (header X-CSRFToken).
- Validasi & sanitasi di server (pakai Django forms).
- Jangan simpan password di URL; pakaiPOST.
- Batasi percobaan login (rate limit) dan pakai cookie HttpOnly untuk session.

# Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
AJAX membuat interaksi terasa instan (modal close, toast, list update tanpa reload). Jika ditangani buruk, bisa membingungkan user (tidak ada feedback atau gagal silent). Jadi selalu tampilkan loading, error, dan konfirmasi sukses.