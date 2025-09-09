# offside-outlet
Tugas 2: Implementasi Model-View-Template (MVT) pada Django

Nama    : Amberley Vidya Putri

NPM     : 2406495533

PWS     : https://pbp.cs.ui.ac.id/amberley.vidya41/offsideoutlet


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