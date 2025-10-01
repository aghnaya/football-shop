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