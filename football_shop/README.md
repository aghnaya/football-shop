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