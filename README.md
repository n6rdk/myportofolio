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
│   ├── apps.py
│   ├── forms.py
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
│   │   ├── input.css
│   │   └── style.css
│   └── img/
│       └── self.png
├── templates/
│   ├── components/
│   │   ├── command_typing.html
│   │   ├── experience_delete_modal.html
│   │   ├── nav_links.html
│   │   └── project_delete_modal.html
│   ├── base_section.html
│   ├── base.html
│   ├── experience_form.html
│   ├── experience.html
│   ├── index.html
│   ├── project.html
│   ├── project_form.html
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

### Week 3
* Implementasi tutorial 3 (Form dan Data Delivery).
* Membuat halaman project.
* Implementasi form dan data delivery pada halaman experience.
* Menerapkan secret key untuk CRUD pada halaman experience dan project.
* Membuat hamburger navbar untuk tampilan mobile.

---

# Jawaban Pertanyaan Reflektif

## Tugas 3

### 1)

ModelForm membuat form langsung dari model, jadi field, tipe data, dan aturan validasinya (seperti max_length, URLField, dan blank) tidak perlu ditulis ulang. Kita cukup memanggil is_valid() untuk validasi dan save() untuk menyimpan ke database, dan form otomatis ikut menyesuaikan kalau model berubah, sedangkan form HTML manual lebih panjang, rawan tidak sinkron dengan model, dan validasinya mudah terlewat. Adapun `{% csrf_token %}` wajib ada karena browser otomatis menyertakan cookie sesi di setiap request, sehingga situs jahat bisa membuat pengguna yang sedang login mengirim request palsu (serangan CSRF) tanpa disadari. Token acak yang unik ini disisipkan sebagai hidden input dan dicocokkan oleh Django saat POST, sehingga request tanpa token yang valid ditolak dengan error 403.


### 2)

Saat ini, JSON lebih disukai dibandingkan XML pada aplikasi modern (terutama pada arsitektur RESTful API) karena ukurannya yang lebih ringkas, parser yang sangat cepat, dan integrasi yang sangat natural dengan JavaScript di sisi frontend. Ini terlihat pada contoh data Burhan di tutorial: XML harus menulis tag pembuka dan penutup untuk setiap elemen (`<name>Burhan</name>`) plus root element wajib dan prolog, sedangkan JSON cukup pasangan key-value (`"name": "Burhan"`). Hasilnya ukuran data lebih kecil, sehingga lebih hemat bandwidth dan lebih cepat dikirim antara backend dan frontend.


### 3)

Saat view seperti `get_experience_json` dipanggil, Django akan mengambil data dari database dengan `Experience.objects.all()`, tapi hasilnya bukan JSON, melainkan kumpulan objek model Python yang strukturnya rumit (punya method, relasi, dan tipe field khusus seperti UUIDField) jadi kalau langsung dikirim sebagai response akan error, karena JSON hanya mengerti tipe data sederhana seperti string, number, boolean, dsb. Oleh karena itu, diperlukan proses serialization lewat `serializers.serialize("json", experiences)`, yang mengubah objek-objek model itu jadi string JSON yang bisa dibaca sistem lain, baru setelah itu dibungkus ke HttpResponse dengan `content_type="application/json"` dan dikirim ke klien. Jadi serialization itu penting karena berfungsi sebagai "penerjemah" dari struktur data internal Django ke format universal yang bisa dipahami JavaScript, aplikasi mobile, atau sistem lain di luar Django.


---

# AI Disclosure

AI digunakan sebagai **alat bantu selama proses pengembangan**, terutama untuk membantu memahami konsep, mengeksplorasi alternatif implementasi, dan melakukan debugging.

AI tidak digunakan sebagai pengganti proses pengambilan keputusan desain. Desain antarmuka website tetap ditentukan berdasarkan preferensi pribadi.

Tools AI yang digunakan: Gemini, Claude

Log penggunaan AI:
<br>https://share.gemini.google/KMqQVLRNFXIK
<br>https://claude.ai/share/9fbb6c5f-f5f3-459d-b2de-c9eaabb30696
<br>https://claude.ai/share/0928bf74-ea00-4a0b-86ba-df0dd40f78a1

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
* Membuat sebagian unit test.

## Keterbatasan AI

Output AI tidak selalu dapat langsung digunakan karena AI dapat menghasilkan kode yang secara sintaks terlihat benar tetapi belum tentu sesuai dengan desain, experience, atau responsivitas yang diinginkan.


## Manual Improvements

Karena keterbatasan tersebut, setiap output AI tetap dievaluasi dan disesuaikan secara manual. Beberapa penyesuaian yang dilakukan meliputi penyesuaian margin, padding, warna, dan layout grid.

---


## License

This project is developed for educational purposes as part of the Pemrograman Berbasis Platform course.
