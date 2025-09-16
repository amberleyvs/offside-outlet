# offside-outlet
Nama    : Amberley Vidya Putri

NPM     : 2406495533

PWS     : https://pbp.cs.ui.ac.id/amberley.vidya41/offsideoutlet

Tugas 2: Implementasi Model-View-Template (MVT) pada Django


Cara mengimplementasikan checklist step-by-step

1) Membuat proyek Django baru.
Saya membuat repositori Git, menyiapkan virtual environment, memasang dependensi sesuai referensi, lalu menginisiasi proyek bernama offside-outlet di direktori kerja.
2) Membuat aplikasi main.
Saya membuat aplikasi main, mendaftarkannya ke INSTALLED_APPS, dan menyiapkan direktori template agar sistem templating Django dapat menemukan berkas HTML.
3) Routing level proyek.
Saya mengatur URLConf proyek agar mendelegasikan request root (/) ke URLConf milik aplikasi main, sehingga semua request awal dipetakan oleh routing aplikasi.
4) Model Product dengan 6 atribut wajib sesuai soal.
Saya mendefinisikan model Product berisi name (Char), price (Integer), description (Text), thumbnail (URL), category (Char), dan is_featured (Boolean), sesuai dengan ketentuan wajib dari soal lalu menjalankan siklus migrasi agar skema tersimpan di basis data.
5) Fungsi pada view yang merender identitas ke template.
Saya menulis fungsi yang menyiapkan context berisi nama aplikasi serta nama dan kelas saya, kemudian merendernya ke template HTML agar tampil di halaman utama.
6) Routing pada urls.py aplikasi main.
Saya membuat URLConf di aplikasi main yang memetakan path root ke fungsi view tersebut
8) Deployment ke PWS.
Saya membuat proyek baru di PWS, isi environment variables sesuai .env.prod yang sudah ada, menambahkan URL PWS ke ALLOWED_HOSTS, melakukan push ke remote PWS, dan verifikasi status running hingga aplikasi dapat diakses publik.

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

https://drive.google.com/drive/folders/1OwIE0RXecZIE00xECi_yXHVoWoLx6VZu?usp=share_link

Explanation: 
Client Request: Browser mengirimkan permintaan HTTP ke server.
URLConf Proyek (urls.py): Semua permintaan pertama-tama dicek di urls.py level proyek.
Pencocokan pola: Jika ada pattern yang mengarah ke include('main.urls'), kontrol diteruskan ke URLConf aplikasi; jika tidak ada yang cocok, Django memberi respons 404 Not Found.
URLConf Aplikasi (main/urls.py): Permintaan dicocokkan dengan pola rute milik aplikasi.
View: Saat pola ditemukan, Django menjalankan view terkait (function-based atau class-based).

Jelaskan peran settings.py dalam proyek Django!

settings.py merupakan pusat konfigurasi proyek Django. Semua pengaturan penting—mulai dari keamanan, daftar app yang aktif, configuration database, lokasi template dan berkas statik terkonsolidasi di file ini. Saat server dijalankan, Django menetapkan DJANGO_SETTINGS_MODULE ke offside_outlet.settings lalu memuat konfigurasi ini sekali di awal. Setelah itu, seluruh komponen berjalan mengikuti nilai yang didefinisikan di settings.py.

Bagaimana cara kerja migrasi database di Django?

Migrasi database di Django adalah sistem yang memungkinkan untuk mengubah struktur database secara bertahap dan teratur seiring pengembangan aplikasi. Cara kerjanya dengan mendefinisikan atau memodifikasi model data di Django (seperti menambahkan kolom baru), kemudian menggunakan perintah makemigrations untuk membuat file Python yang secara otomatis merangkum perubahan tersebut. Terakhir, jalankan perintah migrate untuk menerapkan perubahan skema yang dijelaskan dalam file tersebut ke database agar memastikan database selalu sinkron dengan model data aplikasi.

Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django cocok untuk pemula karena memiliki fitur yang lengkap. Pola MVT nya mudah diikuti, ada ORM + migrasi untuk database, routing URL, form, auth/login, admin panel, dan keamanan semuanya sudah built-in. Jadi kita bisa bikin aplikasi cepat tanpa harus banyak set up. Django skalabel dan fleksibel jadi pemakaian dapat disesuaikan sesuai kebutuhan. Django juga memakai bahasa python sehingg Karena memakai Python yang ramah pemula dan dokumentasi rapi dan komunitasnya besar jadi kita bisa fokus ke konsep inti pengembangan (sangat beneficial untuk yang baru belajar pengembangan perangkat lunak).

Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Tutorial 1 sangat seru karena saya mengerti dengan cepat. Penjelasannya runtut dan jelas

Tugas 3: Implementasi Form dan Data Delivery pada Django

Mengapa kita memerlukan data delivery?

Karena sistem dalam sebuah aplikasi/web butuh saling tukar data. Contohnya, backend (server) kirim data ke frontend (tampilan web atau app) agar bisa ditampilkan ke pengguna. Data bisa dikirim dalam bentuk HTML (buat ditampilkan ke manusia), atau dalam bentuk JSON/XML (buat dibaca mesin atau aplikasi). Ini bikin aplikasi jadi cepat, mudah di-update, dan bisa dipakai bareng dengan sistem lain seperti app mobile atau API.

Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Dua-duanya sebenarnya sama sama bagus namun beda kegunaan. XML formatnya panjang dan pakai tag-tag seperti HTML jadi lebih bagus untuk data yang butuh struktur rumit dan rapi. JSON lebih pendek, mudah dibaca, dan cocok buat aplikasi web dan mobile karena lebih cepat diproses. JSON lebih populer karena tulisannya lebih singkat, mudah dipahami oleh manusia dan mesin, cocok dengan JavaScript yang banyak dipakai di web, serta ukuran datanya lebih kecil jadi kirimnya lebih cepat.

Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

is_valid() dipakai untuk cek apakah data yang diisi di form itu benar. Misalnya apakah ada kolom yang perlu diisi maka akan dicek. is_valid juga menyocokkan apakah formatnya sesuai, misalnya apakah umur harus berupa integer akan dicek disini. Kalau semua memenuhi ketentuan maka akan lanjut disimpan ke database. Kalau ada yang salah, dapat memberikan pesan error ke pengguna. Jadi, is_valid() itu penting biar data yang masuk ke sistem rapi dan mencegah error.

Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token mencegah Cross-Site Request Forgery (CSRF)—serangan yang “menumpang” sesi login pengguna untuk mengirim POST/aksi sensitif tanpa sepengetahuan mereka. Singkatnya semacam kode rahasia untuk menjaga agar hanya form dari site kita sendiri yang bisa mengirim data ke server. Tanpa token, penyerang dapat memicu request dari situs lain (link, form tersembunyi, atau konten berbahaya) sehingga bisa terjadi hal berbahaya. Django mewajibkan token pada form POST; jadi selalu sisipkan {% csrf_token %} agar server bisa memverifikasi bahwa request memang berasal dari website kita.

Implementasi checklist step-by-step
1) Kerangka tampilan (skeleton): Saya membuat templates/base.html di root dan menambahkan TEMPLATES['DIRS'] = [BASE_DIR / 'templates'] agar terdeteksi. Lalu halaman app (main.html) saya extend dari base.html supaya layout konsisten.
2) Form input: Saya membuat ProductForm di forms.py berisi field yang diperlukan.
3) List + tombol Add & Detail: Di show_main, saya mengambil semua objek model dan kirim ke template. Di main.html, saya tampilkan daftar item dengan tombol “Add” yang akan menuju halaman form dan link “Detail” per item yang menuju view detail
4) Detail page: Saya membuat show_detail menggunakan get_object_or_404(pk=id) dan render ke template detail untuk menampilkan informasi lengkap mengenai produk
5) Data delivery (XML/JSON): Saya menambahkan 
    - view show_xml dan show_json yang memakai serializers.serialize untuk semua objek
    - show_xml_by_id dan show_json_by_id untuk objek spesifik berdasarkan ID. 
    Keduanya sama tujuannya untuk menyajikan data
6) Routing: Semua fungsi view yang telah dibuat (show_main, show_detail, show_xml, show_json, dsb) didaftarkan pada urls.py aplikasi. Setiap path URL dipetakan ke fungsi view terkait dan urls.py aplikasi di include ke urls.py proyek agar semua rute dapat diakses dari root aplikasi.
7) Deployment: Saya push ke pws dan saya jalankan, uji tambah data, cek list dan detail, serta verifikasi endpoint XML/JSON.

Feedback untuk asdos Tutorial 2:
Sangat membantu mengerjakan tugas 3


Screenshots:
![JSON 1](/screenshots/json.jpg)
![JSON 2](/screenshots/json2.jpg)
![XML 1](/screenshots/xml.jpg)
![XML 2](/screenshots/xml2.jpg)