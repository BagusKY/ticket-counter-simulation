# 🎟️ Ticket Counter Simulation (Queue)

Simulasi sistem antrian loket tiket menggunakan struktur data **Queue (FIFO)** yang diimplementasikan dalam Python.  
Project ini dibuat sebagai bagian dari tugas mata kuliah **Struktur Data**.

---

## 📌 Deskripsi Singkat

Project ini mensimulasikan bagaimana penumpang datang, mengantri, dan dilayani oleh beberapa petugas (agent) dalam sistem loket tiket.

Simulasi menggunakan pendekatan **event-driven**, dengan tiga proses utama:
- Arrival (kedatangan)
- Begin Service (mulai dilayani)
- End Service (selesai dilayani)

---

## 🎯 Tujuan Project

- Memahami konsep **Queue (FIFO)**
- Menganalisis **kompleksitas waktu**
- Melakukan **eksekusi manual algoritma**
- Mengimplementasikan **simulasi antrian**
- Mengevaluasi performa sistem melalui eksperimen

---

## 🧱 Struktur Project

```

ticket-counter-simulation/
│
├── main.py                  # Menjalankan simulasi
├── ticket_simulation.py     # Logika utama simulasi
├── queue.py                 # Implementasi Queue + reverse
│
├── laporan.md               # Jawaban soal 1–6
└── README.md                # Dokumentasi project

```

---

## ⚙️ Cara Menjalankan Program

1. Pastikan Python sudah terinstall
2. Jalankan file berikut:

```

python main.py

```

---

## 🧠 Konsep yang Digunakan

### 🔹 Queue (FIFO)
Struktur data antrian di mana elemen pertama yang masuk akan keluar terlebih dahulu.

### 🔹 Event-Driven Simulation
Simulasi berbasis kejadian:
- Penumpang datang secara acak
- Agent melayani jika tersedia
- Waktu pelayanan dihitung

### 🔹 Multi-Agent System
Simulasi menggunakan lebih dari satu petugas untuk meningkatkan efisiensi layanan.

---

## 📊 Parameter Simulasi

| Parameter | Keterangan |
|----------|-----------|
| num_agents | Jumlah petugas |
| num_seconds | Lama simulasi |
| arrival_prob | Probabilitas kedatangan |
| service_time_range | Rentang waktu pelayanan |

---

## 📈 Contoh Output

```

=== HASIL SIMULASI ===
Total dilayani     : 48
Masih dalam antrean: 3
Rata-rata tunggu   : 2.75 detik

```

---

## 📝 Penjelasan Tugas

Project ini mencakup:

### ✔ Soal 1
Analisis kompleksitas waktu

### ✔ Soal 2 & 3
Eksekusi manual Queue

### ✔ Soal 4
Implementasi simulasi

### ✔ Soal 5
Eksperimen dan analisis performa

### ✔ Soal 6
Reverse Queue

👉 Detail lengkap tersedia di file:
```

laporan.md

```

---

## 🔄 Reverse Queue

Fitur tambahan untuk membalik urutan queue menggunakan bantuan struktur data stack.

---

## ⚠️ Catatan Teknis

- Implementasi queue menggunakan list Python
- Operasi `dequeue()` memiliki kompleksitas O(n)
- Cocok untuk pembelajaran, bukan skala besar

---

## 🚀 Pengembangan Lanjutan (Opsional)

- Visualisasi antrian
- GUI interface
- Statistik lebih detail
- Optimasi menggunakan deque

---

## 👨‍💻 Author
M. Bagus Kuncoro Yekti/072_Manajemen Informatika

Dibuat untuk tugas mata kuliah Struktur Data
```

