# Nabila — Portfolio Website

> Website portofolio pribadi yang berisi profil, latar belakang akademik, pengalaman, serta berbagai kemampuan teknis yang sedang dipelajari dan dikembangkan.

Live site: nabila-oktavia51-myportofolio.pws.cs.ui.ac.id
## About the Project

Project ini merupakan website portofolio pribadi yang dikembangkan sebagai bagian dari penugasan mata kuliah **Pemrograman Berbasis Platform**.

Situs web ini dibangun menggunakan Django dan terdiri dari beberapa halaman yang dapat diakses melalui routing terpisah. Desain visualnya terinspirasi dari tampilan terminal.

Versi saat ini memuat tiga halaman:

* **Profile** (halaman utama) — memperkenalkan identitas, latar belakang singkat, riwayat pendidikan, dan bagian kontak.
* **Experience** — menampilkan pengalaman organisasi, kegiatan volunteer, dan kompetisi yang pernah diikuti.
* **Skill** — menyajikan field dan tech-stack yang sedang dieksplorasi.
* **Project** — menampilkan proyek-proyek yang pernah/sedang dikerjakan.

## Features

* Desain visual yang terinspirasi dari terminal.
* Tata letak responsif untuk perangkat desktop dan seluler.
* Integrasi Google Fonts.
* Integrasi ikon menggunakan Iconify.
* Navigasi antarbagian menggunakan anchor links.
* Tautan kontak untuk email, LinkedIn, dan GitHub.
* Pencarian proyek berdasarkan judul secara real-time melalui query parameter.
* Endpoint JSON (`/experience/xml` dan `/project/json`) yang menyajikan data pengalaman dan proyek dalam format JSON menggunakan Django serializer.
* Fitur tambah, ubah, dan hapus data (experience & project) yang dilindungi dengan secret key untuk mencegah perubahan oleh pengguna yang tidak berwenang.
* Notifikasi pesan (success/error) menggunakan Django messages framework untuk memberi feedback setelah setiap aksi.

## Tech Stack

| Technology          | Purpose                                                |
| ------------------- | ------------------------------------------------------ |
| Django        | Framework web yang digunakan untuk menyusun dan menjalankan situs web                    |           
| HTML5               | Menentukan struktur dan konten situs web     |
| Tailwind CSS        | Mengatur layout, spacing, typography, warna, dan responsive design menggunakan utility classes            |
| CSS3        | Menambahkan styling dan animasi khusus untuk komponen dengan desain kompleks atau komponen yang digunakan berulang melalui `input.css`               |
| Iconify             | Menyediakan icon yang digunakan                    |

## Project Structure

```text
myportofolio/
├── main/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── api_urls.py
│   ├── api_views.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests_api.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── portofolio/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── static/
│   ├── css/
│   │   ├── input.css
│   │   └── style.css
│   ├── img/
│   │   └── self.png
│   └── js/
│       └── toast.js
├── templates/
│   ├── components/
│   │   ├── command_typing.html
│   │   ├── experience_form_modal.html
│   │   ├── nav_links.html
│   │   ├── project_form_modal.html
│   │   ├── project_star.html
│   │   ├── skill_form_modal.html
│   │   └── toast.html
│   ├── base_section.html
│   ├── base.html
│   ├── experience_form.html
│   ├── experience.html
│   ├── index.html
│   ├── login.html
│   ├── project.html
│   ├── project_form.html
│   ├── register.html
│   └── skill.html
├── .gitignore
├── manage.py
├── package-lock.json
├── package.json
├── README.md
├── requirements.txt
└── test_e2e.py
```


## Getting Started

### Prerequisites

Pastikan sudah memiliki:

* Python
* Django
* Git

### Installation

Clone repository:

```bash
git clone <repository-url>
cd myportofolio
```

Buat dan aktifkan virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Jalankan development server:

```bash
python manage.py runserver
```

Kemudian buka website melalui alamat development server yang diberikan oleh Django.

## Weekly Progress

### Week 1

* Setup project.
* Mendesign ulang layout, color pallette, dan font yang digunakan pada website ini.
* Membuat section skills dan contact.
* Deploy ke Pacil Web Service (PWS).

### Week 2
* Implementasi tutorial 2 (MVT pada Django).
* Migrasi Tailwind CSS dari CDN ke local build.
* Memindahkan section skill pada halaman profile menjadi halaman skill tersendiri.
* Membuat section education pada halaman profile.
* Membuat section experience.
* Membuat animasi untuk beberapa teks.
* Menambahkan 3 model baru, yaitu education, experience, dan skill.
* Membuat unit test untuk skenario aksesibilitas halaman, isolasi data antarhalaman, navigasi antarhalaman, halaman tidak ditemukan, perilaku model, dan kondisi data kosong.

### Week 3
* Implementasi tutorial 3 (Form dan Data Delivery).
* Membuat halaman project.
* Implementasi form dan data delivery pada halaman experience.
* Menerapkan secret key untuk CRUD pada halaman experience dan project.
* Membuat hamburger navbar untuk tampilan mobile.

### Week 4
* Implementasi tutorial 4 (Authentication, Session and Cookies Implementation).
* Mengimplementasikan hak akses editor, yaitu memiliki hak akses user biasa dan dapat mengedit project.
* Menyembunyikan tombol `Add Project`, `Add Experience`, delete project, dan delete experience dari user selain superuser.
* Menyembunyikan tombol edit project dan edit experience dari user selain superuser dan editor.

### Week 5
* Implementasi tutorial 5 (Web Interactivity with JavaScript).
* Menghapus secret key untuk aktivitas CRUD.
* Mengubah pengambilan data pada halaman experience dari Django template menjadi AJAX.
* Mengimplementasikan operasi tambah, edit, dan hapus experience menggunakan AJAX.
---

# Jawaban Pertanyaan Reflektif

## Tugas 1
### 1)

Dalam pengembangan website pada Tugas 1 ini, saya hanya menggunakan elemen `<section>` karena menurut saya tidak terdapat konten independen yang sesuai untuk menggunakan elemen `<article>`, sebagaimana dijelaskan pada [artikel mengenai penggunaan elemen `<section>` dan `<article>` yang saya baca](https://bahasaweb.com/penggunaan-elemen-section-dan-article-di-html/). Selain itu, saya juga tidak menggunakan elemen `<aside>` karena website yang saya kembangkan tidak atau belum memiliki konten tambahan atau informasi pendukung yang bersifat terpisah dari konten utama.

### 2)

Dalam mengatur CSS agar tetap responsif, tantangan yang saya temukan adalah menyesuaikan ukuran dan posisi elemen agar tetap proporsional ketika ukuran layar berubah, terutama saat berpindah dari tampilan desktop ke mobile.

Untuk menentukan elemen yang perlu diubah posisi atau ukurannya, saya mengevaluasi tampilan website pada beberapa ukuran layar dan memperhatikan apakah terdapat elemen yang saling bertumpuk, teks yang terlalu kecil atau terpotong, serta jarak antar elemen yang terlalu rapat. Saya memprioritaskan elemen (terutama layout) berdasarkan estetika dan kenyamanan pengguna (contohnya menyesuaikan ukuran font pada versi mobile).

### 3)

Batasan dari web statis yang saya rasakan sejauh ini, antara lain jika terdapat informasi yang ingin di-update, harus hardcode melalui index.html dan tidak ada timbal-balik dengan pengunjung secara langsung.

Rencana fitur dinamis yang akan saya tambahkan nanti adalah kolom komentar yang dapat digunakan untuk berinteraksi dengan pengunjung.

## Tugas 2
### 1)
Ketika pengguna membuka halaman, misalnya /experience/, browser mengirim HTTP request ke server Django. Request ini kemudian diterima oleh urls.py proyek (portofolio/urls.py), yang berperan sebagai pintu gerbang utama dan mendelegasikan semua path selain admin/ ke main/urls.py melalui include("main.urls"). Selanjutnya, urls.py aplikasi main mencocokkan path experience/ dengan pattern yang terdaftar dan memanggil view yang sesuai, yaitu show_experience di main/views.py.

Di dalam view, data statis (seperti nama) disiapkan, sementara data dinamis diambil dari model melalui query ORM Experience.objects.all(). Query ini diterjemahkan menjadi SQL dan dijalankan ke db.sqlite3 sesuai struktur field yang didefinisikan pada model Experience di main/models.py, menghasilkan queryset berisi data pengalaman. Semua data ini kemudian dikumpulkan dalam dictionary context.

View lalu memanggil render(request, "experience.html", context), sehingga Django mengambil file experience.html dari direktori templates/ dan mengisi placeholder ({{ first_name }}) serta menjalankan tag logika ({% for %}) dengan data dari context, menghasilkan HTML jadi. HTML ini dibungkus dalam HttpResponse dan dikirim ke browser, yang menampilkannya sebagai halaman web lengkap dengan aset statis seperti CSS dan gambar. Alur yang sama berlaku untuk halaman lain, yang membedakan hanya view, model, dan template yang digunakan.

### 2)
Data untuk bagian portofolio baru sebaiknya disimpan pada model agar terpisah dari template sehingga kode lebih rapi dan mudah dikelola. Dengan adanya model, developer cukup mengupdate perubahan melalui model tanpa harus mengubah template sehingga mengurangi risiko error yang dapat terjadi jika melakukan perubahan data pada template.

### 3)
`makemigrations` digunakan untuk membuat file migrasi jika membuat model baru atau menambahkan field baru pada sebuah model, sedangkan `migrate` digunakan untuk menerapkan file migrasi tersebut ke database. Contohnya, ketika membuat model Education, saya menjalankan `python manage.py makemigrations` untuk membuat migrasi, kemudian `python manage.py migrate` untuk menambahkan model baru tersebut ke database.

## Tugas 3
### 1)
ModelForm membuat form langsung dari model, jadi field, tipe data, dan aturan validasinya (seperti max_length, URLField, dan blank) tidak perlu ditulis ulang. Kita cukup memanggil is_valid() untuk validasi dan save() untuk menyimpan ke database, dan form otomatis ikut menyesuaikan kalau model berubah, sedangkan form HTML manual lebih panjang, rawan tidak sinkron dengan model, dan validasinya mudah terlewat. Adapun `{% csrf_token %}` wajib ada karena browser otomatis menyertakan cookie sesi di setiap request, sehingga situs jahat bisa membuat pengguna yang sedang login mengirim request palsu (serangan CSRF) tanpa disadari. Token acak yang unik ini disisipkan sebagai hidden input dan dicocokkan oleh Django saat POST, sehingga request tanpa token yang valid ditolak dengan error 403.

### 2)
Saat ini, JSON lebih disukai dibandingkan XML pada aplikasi modern (terutama pada arsitektur RESTful API) karena ukurannya yang lebih ringkas, parser yang sangat cepat, dan integrasi yang sangat natural dengan JavaScript di sisi frontend. Ini terlihat pada contoh data Burhan di tutorial: XML harus menulis tag pembuka dan penutup untuk setiap elemen (`<name>Burhan</name>`) plus root element wajib dan prolog, sedangkan JSON cukup pasangan key-value (`"name": "Burhan"`). Hasilnya ukuran data lebih kecil, sehingga lebih hemat bandwidth dan lebih cepat dikirim antara backend dan frontend.

### 3)
Saat view seperti `get_experience_json` dipanggil, Django akan mengambil data dari database dengan `Experience.objects.all()`, tapi hasilnya bukan JSON, melainkan kumpulan objek model Python yang strukturnya rumit (punya method, relasi, dan tipe field khusus seperti UUIDField) jadi kalau langsung dikirim sebagai response akan error, karena JSON hanya mengerti tipe data sederhana seperti string, number, boolean, dsb. Oleh karena itu, diperlukan proses serialization lewat `serializers.serialize("json", experiences)`, yang mengubah objek-objek model itu jadi string JSON yang bisa dibaca sistem lain, baru setelah itu dibungkus ke HttpResponse dengan `content_type="application/json"` dan dikirim ke klien. Jadi serialization itu penting karena berfungsi sebagai "penerjemah" dari struktur data internal Django ke format universal yang bisa dipahami JavaScript, aplikasi mobile, atau sistem lain di luar Django.

## Tugas 4
*Tidak ada pertanyaan reflektif.*

## Tugas 5

### 1)
Debouncing adalah teknik yang menunda eksekusi suatu fungsi hingga pengguna berhenti memicu event dalam jangka waktu tertentu, sehingga fungsi hanya dijalankan sekali setelah jeda tersebut. Pada fitur pencarian berbasis AJAX, teknik ini penting karena tanpa debouncing setiap ketikan akan mengirim satu request ke server sehingga menimbulkan banyak permintaan yang tidak diperlukan. Dengan adanya debouncing, request hanya dikirim setelah pengguna selesai mengetik sehingga beban server berkurang dan tampilan website tidak dirender berulang kali.

### 2)
`await` pada `fetch()` berfungsi untuk menjeda eksekusi fungsi `async` sampai permintaan ke server selesai, lalu mengambil objek Response yang ada di dalam Promise yang dikembalikan `fetch()`. Dengan begitu, kode setelahnya seperti pengecekan `response.ok` baru dijalankan ketika data benar-benar sudah tersedia. Jika `await` tidak digunakan, eksekusi tidak menunggu permintaan selesai sehingga kode berikutnya berjalan lebih dulu, variabel hanya berisi Promise yang masih pending, dan pemanggilan seperti `response.json()` akan menimbulkan error karena data yang dibutuhkan belum ada. Selain itu, error dari `fetch()` juga tidak akan tertangkap oleh blok `try...catch`.

### 3)
XSS (Cross-Site Scripting) adalah serangan yang menyisipkan kode JavaScript berbahaya ke dalam halaman tepercaya sehingga dieksekusi di browser pengguna lain, misalnya untuk mencuri sesi login atau mengalihkan ke situs berbahaya. Data yang ditampilkan melalui AJAX/JavaScript lebih rentan dibandingkan template Django karena template Django secara otomatis meng-escape setiap variabel {{ }} sehingga karakter seperti < dan > tampil sebagai teks biasa, sedangkan JavaScript tidak memiliki perlindungan serupa.

## Tugas 6
### 1)
REST (REpresentational State Transfer) adalah gaya arsitektur untuk membuat API web yang memisahkan client dan server dengan interface yang seragam. Return JSON saja belum cukup disebut RESTful karena API juga harus mengikuti constraint REST (stateless, cacheable, uniform interface, dst.) dan memakai HTTP verb serta status code dengan benar (Level 2 Richardson Maturity Model). PUT mengganti seluruh resource sehingga semua field harus dikirim, sedangkan PATCH hanya mengubah sebagian field yang dikirim.

### 2)
Serializer di DRF berperan untuk mengubah model/QuerySet menjadi tipe data Python (lalu JSON) saat mengirim response; dan mengubah JSON dari request menjadi data yang sudah divalidasi lewat .is_valid() sebelum disimpan. Keuntungannya dibanding merakit dictionary manual dengan JsonResponse, yaitu aturan validasi seperti max_length, unique, dan nullability otomatis diambil dari model, create() dan update() sudah disediakan oleh DRF (kalau pakai ModelSerializer), dan bisa menambah validasi sendiri lewat validate_<field> tanpa menulis ulang logika di tiap view.

### 3)
Autentikasi memastikan siapa jenis user apa yang login (misal apakah user tersebut user biasa, superuser, atau user dengan grup tertentu), sedangkan otorisasi menentukan apakah user itu boleh mengakses suatu resource. Hak akses harus dicek di server karena menyembunyikan tombol di template hanya mengubah tampilan, padahal endpoint API tetap bisa dipanggil langsung lewat Postman atau curl oleh siapa saja.

### 4)
Dengan SessionAuthentication, browser otomatis menempelkan cookie sesi ke setiap request, termasuk yang dipicu situs lain, jadi request pengubah data bisa dipalsukan, makanya DRF mewajibkan token CSRF lewat header X-CSRFToken. force_authenticate tidak cukup sebagai bukti karena ia melewati proses autentikasi (termasuk pengecekan CSRF), jadi test tetap lolos meski perlindungannya tidak jalan.

---

# AI Disclosure

AI digunakan sebagai **alat bantu selama proses pengembangan**, terutama untuk membantu memahami konsep, mengeksplorasi alternatif implementasi, dan melakukan debugging.

AI tidak digunakan sebagai pengganti proses pengambilan keputusan desain. Desain antarmuka website tetap ditentukan berdasarkan preferensi pribadi.

Tools AI yang digunakan: Gemini, Claude

Log penggunaan AI:
<br>https://share.gemini.google/KMqQVLRNFXIK
<br>https://claude.ai/share/9fbb6c5f-f5f3-459d-b2de-c9eaabb30696
<br>https://claude.ai/share/0928bf74-ea00-4a0b-86ba-df0dd40f78a1
<br>https://claude.ai/share/ace62fc8-5c46-4f80-a725-30572f514ad0
<br>https://claude.ai/share/478ef425-fbd0-4721-a855-8d9511479019
<br>https://claude.ai/share/951d2376-5e56-434d-ab5c-79a9bb9de084

## Peran AI

Beberapa hal yang dibantu oleh AI meliputi:

* Membantu mengonfigurasi framework.
* Brainstorming desain.
* Membantu mengonversi plain CSS ke format class Tailwind CSS dan sebaliknya.
* Membantu memahami implementasi icon.
* Membantu memahami konsep utility grid pada Tailwind.
* Membantu mengidentifikasi kemungkinan masalah pada struktur HTML dan styling.
* Membantu membuat kerangka dan sebagian konten `README.md`.
* Membantu debugging error yang berkaitan dengan database.
* Membantu memahami dan membuat model dengan field bertipe data array.
* Membantu memahami konsep-konsep yang ada di pertanyaan reflektif.
* Membantu memahami implementasi AJAX.
* Membuat sebagian unit test.
* Membantu memahami `prefetch_related` dan masalah N+1 query pada relasi many-to-many.
* Membantu memahami alur request-response pada Django, termasuk perbedaan jalur halaman HTML dan jalur API DRF (URL routing, view, serializer, permission).
* Membantu debugging fitur star

## Keterbatasan AI

Output AI tidak selalu dapat langsung digunakan karena AI dapat menghasilkan kode yang secara sintaks terlihat benar tetapi belum tentu sesuai dengan desain, experience, responsivitas, atau alur eksekusi yang diinginkan.


## Manual Improvements

Karena keterbatasan tersebut, setiap output AI tetap dievaluasi dan disesuaikan secara manual. Beberapa penyesuaian yang dilakukan meliputi penyesuaian margin, padding, warna, dan layout grid. Selain itu, beberapa bagian logika juga disesuaikan agar sesuai dengan alur kerja aplikasi, seperti cara data ditampilkan dan diproses, setelah ditemukan bahwa saran AI tidak selalu cocok dengan arsitektur yang digunakan.

---


## License

This project is developed for educational purposes as part of the Pemrograman Berbasis Platform course.
