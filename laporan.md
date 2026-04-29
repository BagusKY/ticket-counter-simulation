# LAPORAN TUGAS STRUKTUR DATA
## Ticket Counter Simulation (Queue)

---

## 1. Analisis Kompleksitas Waktu (Worst Case)

Pada simulasi ini digunakan struktur data Queue untuk mengelola antrian penumpang.

- **enqueue() → O(1)**  
  Penambahan elemen dilakukan di akhir list.

- **dequeue() → O(n)**  
  Menggunakan `pop(0)` sehingga seluruh elemen bergeser.

- **isEmpty() → O(1)**  
  Hanya mengecek panjang list.

- **run() → O(n × m)**  
  Dengan:
  - n = jumlah waktu simulasi
  - m = jumlah agent  
  Karena setiap detik dilakukan pengecekan untuk semua agent.

- **_handleArrival() → O(1)**  
- **_handleBeginService() → O(m)**  
- **_handleEndService() → O(m)**  

### Kesimpulan:
Operasi dasar queue relatif efisien, namun proses dequeue memiliki kompleksitas lebih tinggi karena implementasi list.

---

## 2. Eksekusi Manual Queue (Kondisi 1)

Kode:
values = Queue()
for i in range(16):
if i % 3 == 0:
values.enqueue(i)


### Proses:
| i  | Operasi   | Queue              |
|----|----------|--------------------|
| 0  | enqueue  | [0]                |
| 3  | enqueue  | [0, 3]             |
| 6  | enqueue  | [0, 3, 6]          |
| 9  | enqueue  | [0, 3, 6, 9]       |
| 12 | enqueue  | [0, 3, 6, 9, 12]   |
| 15 | enqueue  | [0, 3, 6, 9, 12, 15] |

### Hasil Akhir:
[0, 3, 6, 9, 12, 15]


---

## 3. Eksekusi Manual Queue (Kondisi 2)

Kode:
values = Queue()
for i in range(16):
if i % 3 == 0:
values.enqueue(i)
elif i % 4 == 0:
values.dequeue()


### Proses:
| i  | Operasi        | Queue            |
|----|---------------|------------------|
| 0  | enqueue       | [0]              |
| 3  | enqueue       | [0, 3]           |
| 4  | dequeue       | [3]              |
| 6  | enqueue       | [3, 6]           |
| 8  | dequeue       | [6]              |
| 9  | enqueue       | [6, 9]           |
| 12 | enqueue       | [6, 9, 12]       |
| 15 | enqueue       | [6, 9, 12, 15]   |

### Hasil Akhir:
[6, 9, 12, 15]


### Catatan:
Kondisi `if` dieksekusi terlebih dahulu sebelum `elif`, sehingga pada i = 12 dilakukan enqueue.

---

## 4. Implementasi Simulasi

Simulasi menggunakan pendekatan event-driven:

- **Arrival**
  Penumpang datang secara acak dan masuk ke dalam queue.

- **Begin Service**
  Jika agent kosong dan queue tidak kosong, maka agent akan mengambil penumpang.

- **End Service**
  Setelah waktu pelayanan selesai, agent kembali kosong dan waktu tunggu dihitung.

Setiap agent bekerja secara independen.

---

## 5. Modifikasi ke Detik dan Eksperimen

Simulasi diubah menggunakan satuan detik.

### Parameter:
- Agent: 2
- Waktu simulasi: 100 detik
- Probabilitas kedatangan: 0.3
- Waktu pelayanan: 2–5 detik

### Contoh Hasil:
| Total Dilayani | Sisa Antrian | Rata-rata Tunggu |
|---------------|-------------|------------------|
| 48            | 3           | 2.75 detik       |

### Analisis:
- Semakin tinggi kedatangan → antrian meningkat
- Semakin banyak agent → waktu tunggu menurun

---

## 6. Reverse Queue

Fungsi reverse queue digunakan untuk membalik urutan elemen dalam queue.

### Konsep:
Menggunakan stack sebagai bantuan (LIFO).

### Langkah:
1. Keluarkan semua elemen dari queue ke stack
2. Masukkan kembali ke queue dari stack

### Kompleksitas:
- Waktu: O(n)
- Ruang: O(n)

---

## Kesimpulan

Queue sangat efektif digunakan dalam simulasi antrian.  
Namun, pemilihan implementasi mempengaruhi efisiensi, terutama pada operasi dequeue.

Simulasi menunjukkan bahwa jumlah agent dan tingkat kedatangan sangat mempengaruhi performa sistem antrian.