# offside-outlet

**Nama**: Amberley Vidya Putri  
**NPM**: 2406495533  
**PWS**: https://amberley-vidya41-offsideoutlet.pbp.cs.ui.ac.id  

---

## Tugas 2: Implementasi Model-View-Template (MVT) pada Django

### Cara Mengimplementasikan Checklist Step-by-Step

1. **Membuat proyek Django baru**  
   Saya membuat repositori Git, menyiapkan virtual environment, memasang dependensi sesuai referensi, lalu menginisiasi proyek bernama offside-outlet di direktori kerja.

2. **Membuat aplikasi main**  
   Saya membuat aplikasi main, mendaftarkannya ke `INSTALLED_APPS`, dan menyiapkan direktori template agar sistem templating Django dapat menemukan berkas HTML.

3. **Routing level proyek**  
   Saya mengatur `URLConf` proyek agar mendelegasikan request root (/) ke `URLConf` milik aplikasi main, sehingga semua request awal dipetakan oleh routing aplikasi.

4. **Model Product dengan 6 atribut wajib sesuai soal**  
   Saya mendefinisikan model Product berisi `name` (Char), `price` (Integer), `description` (Text), `thumbnail` (URL), `category` (Char), dan `is_featured` (Boolean), sesuai dengan ketentuan wajib dari soal lalu menjalankan siklus migrasi agar skema tersimpan di basis data.

5. **Fungsi pada view yang merender identitas ke template**  
   Saya menulis fungsi yang menyiapkan context berisi nama aplikasi serta nama dan kelas saya, kemudian merendernya ke template HTML agar tampil di halaman utama.

6. **Routing pada urls.py aplikasi main**  
   Saya membuat `URLConf` di aplikasi main yang memetakan path root ke fungsi view tersebut.

7. **Deployment ke PWS**  
   Saya membuat proyek baru di PWS, isi environment variables sesuai `.env.prod` yang sudah ada, menambahkan URL PWS ke `ALLOWED_HOSTS`, melakukan push ke remote PWS, dan verifikasi status running hingga aplikasi dapat diakses publik.

---

### Bagan Request-Response Django

[Link Bagan](https://drive.google.com/drive/folders/1OwIE0RXecZIE00xECi_yXHVoWoLx6VZu?usp=share_link)

**Penjelasan:**
- **Client Request**: Browser mengirimkan permintaan HTTP ke server.
- **URLConf Proyek (urls.py)**: Semua permintaan pertama-tama dicek di `urls.py` level proyek.
- **Pencocokan pola**: Jika ada pattern yang mengarah ke `include('main.urls')`, kontrol diteruskan ke `URLConf` aplikasi; jika tidak ada yang cocok, Django memberi respons 404 Not Found.
- **URLConf Aplikasi (main/urls.py)**: Permintaan dicocokkan dengan pola rute milik aplikasi.
- **View**: Saat pola ditemukan, Django menjalankan view terkait (function-based atau class-based).

---

### Jelaskan Peran settings.py dalam Proyek Django!

`settings.py` merupakan pusat konfigurasi proyek Django. Semua pengaturan penting—mulai dari keamanan, daftar app yang aktif, konfigurasi database, lokasi template, dan berkas statik—terkonsolidasi di file ini. Saat server dijalankan, Django menetapkan `DJANGO_SETTINGS_MODULE` ke `offside_outlet.settings` lalu memuat konfigurasi ini sekali di awal. Setelah itu, seluruh komponen berjalan mengikuti nilai yang didefinisikan di `settings.py`.

---

### Bagaimana Cara Kerja Migrasi Database di Django?

Migrasi database di Django adalah sistem yang memungkinkan untuk mengubah struktur database secara bertahap dan teratur seiring pengembangan aplikasi. Cara kerjanya:
1. Mendefinisikan atau memodifikasi model data di Django (seperti menambahkan kolom baru).
2. Menggunakan perintah `makemigrations` untuk membuat file Python yang secara otomatis merangkum perubahan tersebut.
3. Menjalankan perintah `migrate` untuk menerapkan perubahan skema yang dijelaskan dalam file tersebut ke database agar memastikan database selalu sinkron dengan model data aplikasi.

---

### Mengapa Framework Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak?

Django cocok untuk pemula karena memiliki fitur yang lengkap. Pola MVT-nya mudah diikuti, ada ORM + migrasi untuk database, routing URL, form, auth/login, admin panel, dan keamanan semuanya sudah built-in. Jadi kita bisa bikin aplikasi cepat tanpa harus banyak set up. Django skalabel dan fleksibel, jadi pemakaian dapat disesuaikan sesuai kebutuhan. Django juga memakai bahasa Python yang ramah pemula, dokumentasi rapi, dan komunitasnya besar sehingga kita bisa fokus ke konsep inti pengembangan (sangat beneficial untuk yang baru belajar pengembangan perangkat lunak).

---

### Feedback untuk Asisten Dosen Tutorial 1

Tutorial 1 sangat seru karena saya mengerti dengan cepat. Penjelasannya runtut dan jelas.

---

## Tugas 3: Implementasi Form dan Data Delivery pada Django

### Mengapa Kita Memerlukan Data Delivery?

Karena sistem dalam sebuah aplikasi/web butuh saling tukar data. Contohnya, backend (server) kirim data ke frontend (tampilan web atau app) agar bisa ditampilkan ke pengguna. Data bisa dikirim dalam bentuk HTML (buat ditampilkan ke manusia), atau dalam bentuk JSON/XML (buat dibaca mesin atau aplikasi). Ini bikin aplikasi jadi cepat, mudah di-update, dan bisa dipakai bareng dengan sistem lain seperti app mobile atau API.

---

### Mana yang Lebih Baik antara XML dan JSON? Mengapa JSON Lebih Populer Dibandingkan XML?

Dua-duanya sebenarnya sama-sama bagus namun beda kegunaan. XML formatnya panjang dan pakai tag-tag seperti HTML jadi lebih bagus untuk data yang butuh struktur rumit dan rapi. JSON lebih pendek, mudah dibaca, dan cocok buat aplikasi web dan mobile karena lebih cepat diproses. JSON lebih populer karena tulisannya lebih singkat, mudah dipahami oleh manusia dan mesin, cocok dengan JavaScript yang banyak dipakai di web, serta ukuran datanya lebih kecil jadi kirimnya lebih cepat.

---

### Jelaskan Fungsi dari Method is_valid() pada Form Django dan Mengapa Kita Membutuhkan Method Tersebut?

`is_valid()` dipakai untuk cek apakah data yang diisi di form itu benar. Misalnya apakah ada kolom yang perlu diisi maka akan dicek. `is_valid` juga menyocokkan apakah formatnya sesuai, misalnya apakah umur harus berupa integer akan dicek di sini. Kalau semua memenuhi ketentuan maka akan lanjut disimpan ke database. Kalau ada yang salah, dapat memberikan pesan error ke pengguna. Jadi, `is_valid()` itu penting biar data yang masuk ke sistem rapi dan mencegah error.

---

### Mengapa Kita Membutuhkan csrf_token saat Membuat Form di Django?

csrf_token mencegah Cross-Site Request Forgery (CSRF)—serangan yang “menumpang” sesi login pengguna untuk mengirim POST/aksi sensitif tanpa sepengetahuan mereka. Singkatnya, semacam kode rahasia untuk menjaga agar hanya form dari site kita sendiri yang bisa mengirim data ke server. Tanpa token, penyerang dapat memicu request dari situs lain (link, form tersembunyi, atau konten berbahaya) sehingga bisa terjadi hal berbahaya. Django mewajibkan token pada form POST; jadi selalu sisipkan `{% csrf_token %}` agar server bisa memverifikasi bahwa request memang berasal dari website kita.

---

### Implementasi Checklist Step-by-Step

1. **Kerangka Tampilan (Skeleton)**  
   Saya membuat `templates/base.html` di root dan menambahkan `TEMPLATES['DIRS'] = [BASE_DIR / 'templates']` agar terdeteksi. Lalu halaman app (`main.html`) saya extend dari `base.html` supaya layout konsisten.

2. **Form Input**  
   Saya membuat `ProductForm` di `forms.py` berisi field yang diperlukan.

3. **List + Tombol Add & Detail**  
   Di `show_main`, saya mengambil semua objek model dan kirim ke template. Di `main.html`, saya tampilkan daftar item dengan tombol “Add” yang akan menuju halaman form dan link “Detail” per item yang menuju view detail.

4. **Detail Page**  
   Saya membuat `show_detail` menggunakan `get_object_or_404(pk=id)` dan render ke template detail untuk menampilkan informasi lengkap mengenai produk.

5. **Data Delivery (XML/JSON)**  
   Saya menambahkan:  
   - View `show_xml` dan `show_json` yang memakai `serializers.serialize` untuk semua objek.  
   - `show_xml_by_id` dan `show_json_by_id` untuk objek spesifik berdasarkan ID.  
   Keduanya sama tujuannya untuk menyajikan data.

6. **Routing**  
   Semua fungsi view yang telah dibuat (`show_main`, `show_detail`, `show_xml`, `show_json`, dsb) didaftarkan pada `urls.py` aplikasi. Setiap path URL dipetakan ke fungsi view terkait dan `urls.py` aplikasi di-include ke `urls.py` proyek agar semua rute dapat diakses dari root aplikasi.

7. **Deployment**  
   Saya push ke PWS dan saya jalankan, uji tambah data, cek list dan detail, serta verifikasi endpoint XML/JSON.

---

### Feedback untuk Asdos Tutorial 2

Sangat membantu saya mengerjakan tugas 3.

---

### Screenshots

![JSON 1](/screenshots/json.jpg)  
![JSON 2](/screenshots/json2.jpg)  
![XML 1](/screenshots/xml.jpg)  
![XML 2](/screenshots/xml2.jpg)

---

## Tugas 4: Implementasi Form dan Data Delivery pada Django

### Apa itu Django AuthenticationForm? Jelaskan Juga Kelebihan dan Kekurangannya.

Django AuthenticationForm adalah built in form Django untuk melakukan login. Form ini sudah menyediakan field username dan password, serta validasi built-in untuk mengecek kredensial ke database dan memastikan user aktif.

**Kelebihan:**
- Sudah built-in dan terintegrasi langsung dengan sistem autentikasi Django.
- Validasi aman dan mengikuti best practice.
- Mudah digunakan dan bisa langsung dipakai tanpa harus membuat form baru.
- Bisa di custom

**Kekurangan:**
- Kurang fleksibel kalau mau UI/UX yang sangat bagus.
- Default styling sederhana, jadi butuh CSS tambahan kalau mau lebih menarik.
- Tidak menangani captcha atau 2FA. Harus ada tambahan eksternal nya.

---

### Apa Perbedaan antara Autentikasi dan Otorisasi? Bagaimana Django Mengimplementasikan Kedua Konsep Tersebut?

**Autentikasi**: Proses memverifikasi identitas pengguna. Di Django, autentikasi dilakukan melalui login dengan `AuthenticationForm`, lalu data pengguna disimpan di session.  
**Otorisasi**: Proses mengecek apakah pengguna memiliki izin untuk melakukan sesuatu. Django menangani ini lewat `@login_required`, `@permission_required`

**Implementasi di Django:**
- **Autentikasi**: `authenticate()`, `login()`, `logout()`, dan middleware session.
- **Otorisasi**: Decorator seperti `login_required`

---

### Apa Saja Kelebihan dan Kekurangan Session dan Cookies dalam Konteks Menyimpan State di Aplikasi Web?

Dalam aplikasi web, session memiliki kelebihan karena data disimpan di sisi server sehingga lebih aman dan mampu store informasi dalam jumlah besar. Namun, kelemahannya adalah penggunaan memori di server semakin besar seiring banyaknya pengguna dan session tetap memerlukan cookie atau session ID untuk menghubungkan klien dengan datanya. Sementara itu, cookie lebih praktis karena langsung disimpan di sisi klien, mudah digunakan oleh browser, dan tetap ada meskipun server dimatikan. Kekurangannya adalah cookie lebih rentan terhadap manipulasi atau pencurian dan hanya mampu menyimpan data dalam ukuran yang terbatas sekitar 4KB.

---

### Apakah Penggunaan Cookies Aman Secara Default dalam Pengembangan Web?
Penggunaan cookie dalam aplikasi web memiliki beberapa risiko. Cookie dapat dilihat dan bahkan dimodifikasi langsung oleh pengguna, sehingga data di dalamnya tidak sepenuhnya aman. Selain itu, karena cookie otomatis dikirim pada setiap request, ada kemungkinan data tersebut disalahgunakan. Risiko lain muncul jika penyerang berhasil menyuntikkan script berbahaya (XSS), maka cookie bisa dicuri. Untuk menangani hal ini, Django memiliki beberapa mekanisme keamanan. Django dapat mencegah akses JavaScript ke cookie dengan pengaturan tertentu, menyediakan CSRF token untuk melindungi form POST dari request palsu, memastikan cookie hanya dikirim melalui koneksi HTTPS, dan menyimpan informasi sensitif seperti status login di session di server, bukan langsung di cookie.

---

### Implementasi Step-by-Step

1. **Membuat Fitur Register**  
   Saya membuat fitur register dengan menambahkan `register()` di `views.py` menggunakan `UserCreationForm`. Kemudian saya membuat `register.html` dan routing ke `/register/` pada `urls.py`.

2. **Membuat Fitur Login dan Logout**  
- Untuk login, saya pakai `AuthenticationForm` dan membuat fungsi `login_user()` di `views.py`. Di dalamnya, saya cek `form.is_valid()`, lalu pakai `login()` untuk menyimpan session. Saya juga set cookie `last_login` di response.  
- Untuk logout, saya buat `logout_user()` yang pakai `logout()` dari Django dan sekaligus menghapus cookie `last_login` dengan `response.delete_cookie()`.

3. **Proteksi Main Page dan See Details**  
   Supaya hanya bisa diakses user yang sudah login, di `views.py`, saya menambahkan `@login_required` di atas fungsi `show_main` dan `show_detail`. Jadi kalau belum login, user akan otomatis diarahkan ke halaman login.

4. **Menghubungkan Model Product dengan User**  
   Di model Product, saya menambahkan field `user = models.ForeignKey()` supaya setiap produk ada owner-nya. Lalu di `add_product()`, saya set `product.user = request.user` sebelum `save()` supaya tahu siapa yang menambahkan produk.

5. **Menampilkan User yang Sedang Logged In dan Menerapkan Cookies Last Login**  
   Melanjutkan poin ke-2, saya menambahkan tulisan “Hello, {{ user_logged }}!” dan “Sesi terakhir login: {{ last_login }}” di atas daftar produk, dengan data dari context di `views.py`.

---

## Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS

### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan: Inline style - External & Internal style sheets - Browser default 

---
### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive design penting karena user menggunakan berbagai macam device. Ada yang pakai handphone, ada yang pakai laptop. Jadi, agar user nyaman memakai website, kita sebagai developer harus menyesuaikan  agar website dapat digunakan dengan mudah baik itu di mobile handphone atau di laptop dengan layar yang besar. Dengan responsive design juga web terlihat lebih rapih dan profesional.

**Contoh aplikasi**
- **Yang sudah menerapkan responsive design:** Instagram, Tokopedia, Netflix, Spotify. Aplikasi tersebut dapat digunakan dengan mudah baik dari handphone dan laptop. Bahkan kalau Netflix dan Spotify dapat digunakan di TV juga.
- **Yang belum:** web sekolah yang hanya di design untuk di laptop atau web lama yang memang tidak di develop untuk berbagai device

---

### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin adalah ruang di luar border. Kalau kita mau memberi jarak antara satu elemen dengan elemen lainnya di halaman, kita atur marginnya. Border adalah garis yang mengelilingi isi dan padding. Border bisa dikasih warna, ketebalan, bahkan bentuk (misalnya dibikin bulat pakai border-radius). Border adalah garis yang mengelilingi isi dan padding. Border bisa dikasih warna, ketebalan, dan bentuk. Jadi urutannya dari dalam ke luar: content - padding - border - margin

**cara implementasi:**
```css
.card {
  /* jarak ke elemen lain */
  margin: 16px;

  /* garis tepi */
  border: 1px solid #e5e7eb;
  border-radius: 12px;

  /* ruang dalam kotak, sekitar content */
  padding: 16px;
}
```

---

### Jelaskan konsep flex box dan grid layout beserta kegunaannya!
**Flexbox** bekerja dalam satu sumbu tunggal, either baris atau kolom. Kegunaan: navbar, baris tombol, center alignment, menyusun item sejajar. Cocok untuk membuat navbar, button satu baris, dsb.

**CSS Grid** dalam 2 dimensi, ada baris dan kolom sehingga bisa untuk tampilan yang lebih kompleks seperti product card yang diimplementasikan juga di tugas 5 ini.

---

### Implementasi Step-by-Step

1. **Menyiapkan Tailwind dan static files**  
   Agar bisa styling cepat dan responsif dengan Tailwind. Pada base.html saya menambahkan meta viewport & CDN Tailwind dan load CSS kustom dari static. Kemudian saya konfigurasi static pada settings.py. Saya juga menambahkan static/css/global.css dan mengisi global.css dengan kelas util form sesuai materi agar input, select, checkbox terlihat rapi dan konsisten.

2. **Menambahkan navigation bar responsive**  
   Saya membuat templates/navbar.html yang isinya ada menu Home, Create Product, Wishlist, area user (Login/Register vs Logout + identitas). Terdapat tombol hamburger untuk mobile.

3. **Menambahkan fitur edit product dan remove product**  
   Untuk user yang memiliki product tersebut. Sama seperti konsep minggu lalu, saya menambahkan function di views.py kemudian add path di urls.py dan di render di card_product.html

4. **Membuat card_product.html**  
   Untuk display product yang lebih bagus. Pada owner action terdapat edit dan remove product. Jika bukan owner, terdapat button show detail.

5. **Customize semua page**  
   Semua page mulai dari register, login, home page, product page, semuanya saya customize agar terlihat lebih menarik (mostly mengacu tutorial kecuali card saya improve sendiri)

6. **Menambahkan fitur wishlist dengan tombol heart**  
   Ketika user login menekan icon hati, produk masuk/keluar Wishlist. Ada menu Wishlist di navbar + counter di samping label "Wishlist". Saya mengikuti github tersebut dan import icon yang dibutuhkan.

**Referensi Wishlisht**: https://github.com/bedimcode/productcard/blob/main/index.html

---
## Tugas 6: Javascript dan AJAX

### Apa perbedaan antara synchronous request dan asynchronous request?
**Synchronous**
Di mode ini, browser menunggu server. Kode JavaScript berhenti sejenak sampai respons datang, baru lanjut menjalankan berikutnya. Jadi interaksi lebih kaku karena sering membutuhkan reload page sehingga pengalaman pengguna lebih rendah terutama kalau respons lambat
**Asynchronous**
Permintaan dikirim “di belakang layar” jadi tidak nge-block eksekusi JavaScript lain. Hanya bagian halaman yang diperbarui tanpa reload page penuh

---

### Bagaimana AJAX bekerja di Django (alur request–response)?
Di halaman, saat pengguna klik tombol atau submit form, JavaScript pakai `fetch()` buat memanggil URL Django. Di server, view Django mengolah request tersebut dan return data dalam bentuk JSON atau status 201 kalau berhasil membuat data baru. Di browser, JS membaca hasilnya `response.json()`, lalu set tampilan: show loading, tampilkan error kalau gagal, atau render konten kalau sukses. Kontennya disusun jadi elemen HTML card atau article dan dimasukkan langsung ke DOM—jadi agar tidak perlu reload page.

---

### Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
- Tidak perlu reload halaman jadi lebih cepat dan hemat bandwidth.
- UX lebih halus karena ada loading state, error state, dan empty state
- Lebih interaktif
- Lebih rapih karena view JSON (API mini) terpisah dari presentasi dan front-end yang mengatur DOM.
- Mudah dipakai ulang untuk fitur lain

---

### Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
1. Aktifkan CSRF. Kirim CSRF token saat POST (di form HTML ada {% csrf_token %}; pada fetch, kirim header X-CSRFToken dari cookie/hidden input).
2. Validasi & otorisasi di server. Semua input login/register harus divalidasi di Django view/form (bukan hanya di JS).
3. Untuk backend, gunakan strip_tags() pada field teks user-generated 
4. Untuk frontend, jika harus memasukkan HTML ke DOM, sanitasi dulu dengan DOMPurify.
5. Hindari innerHTML langsung dari data mentah.
6. Gunakan HTTPS agar cookie sesi/autentik aman di jaringan.
7. Pesan error minimal seperti "password atau email salah: saja
8. Jangan kirim data sensitif dalam respons JSON.

---

### Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
1. Lebih responsif & cepat: hanya area yang berubah yang diload
2. Feedback jelas karena terlihat Loading / Error dan lain lain
3. Interupsi lebih sedikit. Misal form modal + toast sukses/gagal pengguna tetap di konteks yang sama
4. Mobile-friendly interaksi ringan seperti pull-to-refresh, tombol refresh, update
5. Lebih terasa seperti aplikasi, bukan halaman web biasa yang sering reload.