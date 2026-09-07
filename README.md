# Nabila — Portfolio Website

> Website portofolio pribadi yang saat ini dibuat sebagai web statis untuk menunjukkan latar belakang, kemampuan teknis, dan informasi mengenai kontak.


## About the Project

Project ini merupakan website portofolio pribadi yang dikembangkan sebagai bagian dari penugasan mata kuliah **Pemrograman Berbasis Platform**.

Situs web ini saat ini dirancang sebagai situs statis yang berfokus pada penyajian informasi pribadi melalui antarmuka yang sederhana, mudah dibaca, dan responsif. Desain visualnya terinspirasi dari tampilan terminal.

Versi saat ini memuat tiga bagian:

* **About** — memperkenalkan identitas dan latar belakang secara singkat.
* **Skills** — menyajikan bahasa pemrograman yang biasa digunakan, tech stack untuk data science, dan keterampilan dalam cybersecurity.
* **Contact** — menyediakan cara untuk terhubung melalui email, LinkedIn, dan GitHub.

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
| CSS3        | Membuat custom styling untuk komponen yang digunakan berulang, seperti button dan tag melalui `style.css`               |
| Iconify             | Menyediakan icon yang digunakan                    |

## Project Structure

```text
myportofolio/
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
│   └── index.html
├── manage.py
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

* Setup project
* Mendesign ulang layout, color pallette, dan font yang digunakan pada website ini
* Membuat section skills dan contact
* Deploy ke Pacil Web Service (PWS)
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


---

# AI Disclosure

AI digunakan sebagai **alat bantu selama proses pengembangan**, terutama untuk membantu memahami konsep, mengeksplorasi alternatif implementasi, dan melakukan debugging.

AI tidak digunakan sebagai pengganti proses pengambilan keputusan desain. Desain antarmuka website tetap ditentukan berdasarkan preferensi pribadi.

## Peran AI

Beberapa hal yang dibantu oleh AI meliputi:

* Membantu mengonfigurasi framework.
* Membantu mengonversi plain CSS ke format class Tailwind CSS dan sebaliknya.
* Membantu memahami implementasi icon.
* Membantu memahami konsep utility grid pada Tailwind.
* Membantu mengidentifikasi kemungkinan masalah pada struktur HTML dan styling.
* Membantu membuat kerangka dan sebagian konten `README.md`.

## Keterbatasan AI

Output AI tidak selalu dapat langsung digunakan karena AI dapat menghasilkan kode yang secara sintaks terlihat benar tetapi belum tentu sesuai dengan desain, experience, atau responsivitas yang diinginkan.


## Manual Improvements

Karena keterbatasan tersebut, setiap output AI tetap dievaluasi dan disesuaikan secara manual. Beberapa penyesuaian yang dilakukan meliputi penyesuaian margin, padding, warna, dan layout grid.

---


## License

This project is developed for educational purposes as part of the Pemrograman Berbasis Platform course.
