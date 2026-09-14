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

## Features

* Desain visual yang terinspirasi dari terminal.
* Tata letak responsif untuk perangkat desktop dan seluler.
* Integrasi Google Fonts.
* Integrasi ikon menggunakan Iconify.
* Navigasi antarbagian menggunakan anchor links.
* Tautan kontak untuk email, LinkedIn, dan GitHub.

## Tech Stack

| Technology          | Purpose                                                |
| ------------------- | ------------------------------------------------------ |
| Django        | Framework web yang digunakan untuk menyusun dan menjalankan situs web                    |           
| HTML5               | Menentukan struktur dan konten situs web     |
| Tailwind CSS        | Mengatur sebagian besar layout, spacing, typography, warna, dan responsive design menggunakan utility classes            |
| CSS3        | Menambahkan styling dan animasi khusus untuk komponen dengan desain kompleks atau komponen yang digunakan berulang melalui `input.css`               |
| Iconify             | Menyediakan icon yang digunakan                    |

## Project Structure

```text
myportofolio/
├── main/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
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
│   │   └── style.css
│   └── img/
│       └── self.png
├── templates/
│   ├── experience.html
│   ├── index.html
│   └── skill.html
├── .gitignore
├── manage.py
├── package-lock.json
├── package.json
├── README.md
└── requirements.txt
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

---

# Jawaban Pertanyaan Reflektif

## Tugas 2

### 1)

Ketika pengguna membuka halaman, misalnya /experience/, browser mengirim HTTP request ke server Django. Request ini kemudian diterima oleh urls.py proyek (portofolio/urls.py), yang berperan sebagai pintu gerbang utama dan mendelegasikan semua path selain admin/ ke main/urls.py melalui include("main.urls"). Selanjutnya, urls.py aplikasi main mencocokkan path experience/ dengan pattern yang terdaftar dan memanggil view yang sesuai, yaitu show_experience di main/views.py.

Di dalam view, data statis (seperti nama) disiapkan, sementara data dinamis diambil dari model melalui query ORM Experience.objects.all(). Query ini diterjemahkan menjadi SQL dan dijalankan ke db.sqlite3 sesuai struktur field yang didefinisikan pada model Experience di main/models.py, menghasilkan queryset berisi data pengalaman. Semua data ini kemudian dikumpulkan dalam dictionary context.

View lalu memanggil render(request, "experience.html", context), sehingga Django mengambil file experience.html dari direktori templates/ dan mengisi placeholder ({{ first_name }}) serta menjalankan tag logika ({% for %}) dengan data dari context, menghasilkan HTML jadi. HTML ini dibungkus dalam HttpResponse dan dikirim ke browser, yang menampilkannya sebagai halaman web lengkap dengan aset statis seperti CSS dan gambar. Alur yang sama berlaku untuk halaman lain, yang membedakan hanya view, model, dan template yang digunakan.


### 2)

Data untuk bagian portofolio baru sebaiknya disimpan pada model agar terpisah dari template sehingga kode lebih rapi dan mudah dikelola. Dengan adanya model, developer cukup mengupdate perubahan melalui model tanpa harus mengubah template sehingga mengurangi risiko error yang dapat terjadi jika melakukan perubahan data pada template.


### 3)

`makemigrations` digunakan untuk membuat file migrasi jika membuat model baru atau menambahkan field baru pada sebuah model, sedangkan `migrate` digunakan untuk menerapkan file migrasi tersebut ke database. Contohnya, ketika membuat model Education, saya menjalankan `python manage.py makemigrations` untuk membuat migrasi, kemudian `python manage.py migrate` untuk menambahkan model baru tersebut ke database.


---

# AI Disclosure

AI digunakan sebagai **alat bantu selama proses pengembangan**, terutama untuk membantu memahami konsep, mengeksplorasi alternatif implementasi, dan melakukan debugging.

AI tidak digunakan sebagai pengganti proses pengambilan keputusan desain. Desain antarmuka website tetap ditentukan berdasarkan preferensi pribadi.

Tools AI yang digunakan: Gemini, Claude

Log penggunaan AI:
https://share.gemini.google/KMqQVLRNFXIK
https://claude.ai/share/9fbb6c5f-f5f3-459d-b2de-c9eaabb30696

## Peran AI

Beberapa hal yang dibantu oleh AI meliputi:

* Membantu mengonfigurasi framework.
* Membantu mengonversi plain CSS ke format class Tailwind CSS dan sebaliknya.
* Membantu memahami implementasi icon.
* Membantu memahami konsep utility grid pada Tailwind.
* Membantu mengidentifikasi kemungkinan masalah pada struktur HTML dan styling.
* Membantu membuat kerangka dan sebagian konten `README.md`.
* Membantu debugging error yang berkaitan dengan database.
* Membantu memahami dan membuat model dengan field bertipe data array

## Keterbatasan AI

Output AI tidak selalu dapat langsung digunakan karena AI dapat menghasilkan kode yang secara sintaks terlihat benar tetapi belum tentu sesuai dengan desain, experience, atau responsivitas yang diinginkan.


## Manual Improvements

Karena keterbatasan tersebut, setiap output AI tetap dievaluasi dan disesuaikan secara manual. Beberapa penyesuaian yang dilakukan meliputi penyesuaian margin, padding, warna, dan layout grid.

---


## License

This project is developed for educational purposes as part of the Pemrograman Berbasis Platform course.
