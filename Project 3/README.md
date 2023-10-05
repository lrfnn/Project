[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/tq4JuFZa)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12122313&assignment_repo_type=AssignmentRepo)
# Milestone 3

_Milestone 3 ini dibuat guna mengevaluasi pembelajaran pada Hacktiv8 Data Science Fulltime Program khususnya pada Phase 2._

---

## Assignment Objectives

Milestone 3 ini dibuat guna mengevaluasi konsep pembelajaran Phase 2 sebagai berikut:

- Mampu menggunakan Airflow
- Mampu melakukan validasi data dengan menggunakan Great_Expectations
- Mampu memahami konsep NoSQL secara keseluruhan.
- Mampu mempersiapkan data untuk digunakan sebelum masuk ke database NoSQL.
- Mampu mengolah dan memvisualisasikan data dengan menggunakan Kibana.

---

## Dataset

### Ketentuan Dataset
1. Pilihlah dataset yang paling nyaman digunakan karena tidak ada batasan untuk memilih dataset dalam mengerjakan Milestone 3. **Disarankan menggunakan dataset dan pekerjaan yang telah dipakai dalam mengerjakan Graded Challenge 7 Phase 2**.

2. **Konsultasikan terlebih dahulu dataset yang hendak digunakan ke buddy masing-masing student. Jika disetujui, maka silakan dikerjakan. Jika tidak disetujui, maka cari dataset yang lain dan konsultasikan lagi mengenai dataset yang baru ini.**

3. Student tidak boleh menggunakan dataset yang sudah dipakai dalam sesi pembelajaran saat dikelas bersama instruktur atau dataset pada tugas-tugas terdahulu dari Phase 0 hingga Phase 2.

4. **Student dilarang untuk melakukan scraping dataset** karena dikhawatirkan proses pembuatan scraper dan proses scraping akan memakan waktu. Gunakan public dataset yang tersedia diberbagai macam situs Internet.

### Data Sources
Student dapat memilih dataset dari salah satu repository dibawah ini. Popular open data repositories :

- [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)
- [Kaggle datasets](https://www.kaggle.com/datasets)
- [Amazon’s AWS datasets](https://registry.opendata.aws/)

Meta portals :

- [Data Portals](http://dataportals.org/)
- [OpenDataMonitor](https://opendatamonitor.eu/frontend/web/index.php?r=dashboard%2Findex)
- [Quandl](https://www.quandl.com/)
- Sumber lain yang kredibel.

---

## Problems

Objective : Buatlah report yang berisi Exploratory Data Analysis dengan menggunakan dataset yang sudah terlebih dahulu dilakukan Data Cleaning dan validasi data menggunakan Gx. Semua proses dilakukan dengan pipeline yang dijalankan menggunakan Airflow. 

Berikut ini adalah langkah-langkah yang harus dilakukan : 

1. Tentukan dataset yang hendak dipakai. Beri nama dataset ini dengan `P2M3_<nama-student>_data_raw.csv`. Contoh : `P2M3_raka_ardhi_data_raw.csv`.
1. Masukan data tersebut ke dalam PostgreSQL local masing-masing student. Beri nama :
   - Database : `db_phase2`
   - Table : `table_M3`
1. Setelah data berada didalam database, ambil semua data dari database dengan menggunakan Python dan lakukan beberapa Data Cleaning berikut ini :
   - Hapus data yang duplikat. Anda boleh menggunakan sintaks SQL untuk bagian ini.
   - Fiksasi tipe masing-masing column/attribute.
     + Contoh 1 : misalkan terdapat column `Age` saat pengambilan data berbentuk floating point (`17.0`, `21.0`) diubah menjadi tipe integer (`17`, `20`).
     + Contoh 2 : column `salary` saat pengambilan data berbentuk string yang seharusnya integer.
   - Normalisasi column dengan cara : 
     + Semua nama column menjadi lowercase. Contoh : `ID` → `id`, `EDUCATION` → `education`.
     + Spasi pada nama column diubah menjadi `_` (underscore). Contoh : `First Name` → `first_name`, `HOME ADDRESS` → `home_address`.
     + Menghapus spasi/tab/simbol yang dirasa tidak diperlukan pada nama column. Contoh : `  name` → `name`, `|car_price|` → `car_price`.
   - Handling Missing Values
1. Setelah dilakukan Data Cleaning, simpan data clean ini ke dalam CSV file dengan nama `P2M3_<nama-student>_data_clean.csv`. Contoh : `P2M3_raka_ardhi_data_clean.csv`
1. Lakukan validasi data menggunakan Great Expectations. Lakukan minimal 7 Expectations yang didalamnya harus ada Expectation untuk:
   - not to be empty
   - to be unique
   - should be between x and y
   - expect column values to be in set
   - dan lain sebagainya
1. Simpan `index.html` dari hasil Great Expectations dengan nama `P2M3_raka_ardhi_GX.html`.
1. Selain disimpan ke dalam file CSV, data clean ini juga akan dimasukkan ke dalam Elastic Search dengan menggunakan Python.
1. Lakukan automasi dengan membuat DAG yang berisi `Fetch Postgresql > Data Cleaning > Post Kibana`. Simpan DAG dengan nama `P2M3_raka_ardhi_DAG.py`
1. Buatlah dashboard dengan Kibana terhadap data clean ini dengan ketentuan :
   - Jelaskan mengenai objective Exploratory Data Analysis yang hendak dilakukan.
   - Buatlah minimal 6 visualisasi terhadap data tersebut yang mendukung tercapainya objective dari proses EDA yang dilakukan.
   - Tambahkan 1 visualisasi dibagian atas berupa `Markdown` yang berisi :
     + Identitas student.
     + Penjelasan objective.
   - Tambahkan 1 visualisasi dibagian akhir berupa `Markdown` yang berisi :
     + Kesimpulan eksplorasi yang dilakukan.
     + Saran lanjutan atau insight bisnis terhadap eksplorasi yang dilakukan.
   - Total visualisasi : 6 visualisasi + 1 visualisasi Markdown mengenai indetitas + 1 visualisasi Markdown mengenai kesimpulan = 8 visualiasi.
   - Student dipersilakan membuat skenario/situasi fiksi terhadap dataset yang dipakai.
   - Student dipersilakan untuk mengaplikasikan teori mengenai Business Knowledge pada tugas ini.
1. Dashboard yang terbentuk kemudian akan disimpan ke dalam format PDF dengan cara :
   - Tampilkan dashboard secara Full Screen.
   - Tekan `command+p` atau `ctrl+p` untuk print.
   - Lalu simpan sebagai PDF dengan ukuran A4.
   - Format penyimpanan : `P2M3_<nama-student>_report.pdf`. Contoh : `P2M3_raka_ardhi_report.pdf`.

---
## Conceptual Problems

*Jawab pertanyaan berikut:*

1. Jelaskan apa yang kalian ketahui dari Airflow menggunakan pemahaman yang kalian ketahui!
1. Jelaskan apa yang kalian ketahui dari Great Expectations menggunakan pemahaman yang kalian ketahui!
1. Jelaskan apa yang kalian ketahui dari Batch Processing menggunakan pemahaman yang kalian ketahui!


---

## Assignment Instructions

*Milestone 3* dikerjakan dalam format ***Python script (.py)*** dengen beberapa **kriteria wajib** di bawah ini:

1. *Project* dinyatakan selesai dan diterima untuk dinilai jika script dapat dijalankan dengan baik di prompt maupun terminal.

2. Pada tugas Milestone 3, student akan diminta untuk membuat :
   1. `P2M3_<nama-student>_ddl.sql`
      - File ini berisi syntax DDL untuk pembuatan database dan table.
      - Contoh penamaan : `P2M3_raka_ardhi_ddl.sql
   2. `P2M3_<nama-student>_data_raw.csv`
      - File ini berisi dataset original yang akan dimasukkan ke dalam database PostgreSQL.
      - Contoh penamaan : `P2M3_raka_ardhi_data_raw.csv`.
   3. `P2M3_<nama-student>_data_clean.csv`
      - File ini berisi data yang telah dilakukan Data Cleaning.
      - Contoh penamaan : `P2M3_raka_ardhi_data_clean.csv`.
   4. `P2M3_<nama-student>.py`
      - File ini berisi :
        + Python code untuk mengambil data dari database PostgreSQL.
        + Python code untuk melakukan proses Data Cleaning seperti yang sudah ditentukan.
        + Python code untuk menyimpan data clean ke file CSV.
        + Python code untuk memasukkan data clean ke dalam Elastic Search.
      - Contoh penamaan : `P2M3_raka_ardhi.py`.
   5. `P2M3_<nama-student>_report.pdf`.
      - File ini berisi report mengenai dashboard yang dibuat dengan minimal 8 buah visualisasi.
      - Contoh penamaan : `P2M3_raka_ardhi_report.pdf`.
   6. `P2M3_<nama-student>_conceptual.txt`.
      - File ini berisi jawaban conceptual problem.
   7. `P2M3_<nama-student>_GX.html`
      - File ini berisi hasil/report dari Great Expectations
   8. `P2M3_<nama-student>_DAG.py`
      - File ini berisi DAG untuk dijalankan di Airflow

3. **Tidak diperkenankan** membuat program dalam format notebook.

4. Pada file Python, **wajib** memberikan keterangan atau pengenalan dengan menggunakan `comment` atau `docstring` yang berisikan : Judul tugas, Nama, Batch, dan penjelasan singkat tentang program yang dibuat, fitur-fitur. Contoh:
    ```py
    '''
    =================================================
    Milestone 3

    Nama  : Raka Ardhi
    Batch : FTDS-001-RMT

    Program ini dibuat untuk melakukan automatisasi transform dan load data dari PostgreSQL ke ElasticSearch. Adapun dataset yang dipakai adalah dataset mengenai penjualan mobil di Indonesia selama tahun 2020.
    =================================================
    '''
    ```

5. Pisahkan tiap code Python dengan penggunaan function/class agar flow dari code yang dibuat mudah diikuti. Berikan penjelasan pada setiap class dan function yang dibuat dengan menggunakan docstring seperti : 
   ```py
   def get_data_from_postgresql(url, database, table):
     '''
     Fungsi ini ditujukan untuk mengambil data dari PostgreSQL untuk selanjutnya dilakukan Data Cleaning.

     Parameters:
      url: string - lokasi PostgreSQL
      database: string - nama database dimana data disimpan
      table: string - nama table dimana data disimpan

     Return
      data: list of str - daftar data yang ada di database
        
     Contoh penggunaan:
     data = get_data_from_postgresql('localhost', 'db_phase2', 'table_gc7')
     '''

     return data

   ```

---

## Assignment Submission

- Push Assignment yang telah Anda buat ke akun GitHub Classroom Anda masing-masing.
- Contoh bentuk repository :
  ```
  P2-GC7-Set-1/raka-ardhi
  |
  ├── P2M3_raka_ardhi_ddl.sql
  ├── P2M3_raka_ardhi_data_raw.csv
  ├── P2M3_raka_ardhi_data_clean.csv
  ├── P2M3_raka_ardhi.py
  ├── P2M3_raka_ardhi_report.pdf
  ├── P2M3_raka_ardhi_conceptual.txt
  ├── P2M3_raka_ardhi_GX.html
  ├── P2M3_raka_ardhi_DAG.py
  └── README.md
  ```

---

## Assignment Rubrics

### Code Review

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
|DAG|DAG yang digunakan dapat dijalankan tanpa error| 20 pts |
|GX|Mampu membuat 7 Expectations dengan 0 Error| 2pts/exp |
| Data Visualization | Mampu membuat minimal 6 visualisasi dengan menggunakan Kibana | 4 pts / visualisasi |
| Insight | Menampilkan **insight di setiap visualisasi** yang ditampilkan pada dashboard | 4 pts / insight |
| Conclusion | Penarikan kesimpulan yang dilakukan sejalan dengan tujuan dilakukannya eksplorasi dan terdapat saran/tindakan lanjutan/rekomendasi terhadap insight yang dihasilkan | 8 pts |
| Runs Perfectly | Kode berjalan tanpa ada error. Seluruh kode berfungsi dan dibuat dengan benar. | 10 pts |

### Concepts

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| NoSQL | Mampu menjawab pertanyaan dengan singkat, jelas, dan padat serta sesuai dengan konsep dan logika yang ada mengenai Conceptual Problems (3 pts each) | 9 pts |

### Readability

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Tertata Dengan Baik | Semua baris kode terdokumentasi dengan baik dengan Markdown untuk penjelasan kode | 15 pts |

```
Kriteria tertata dengan baik diantaranya adalah: 

1. Tidak menyalin markdown dari tugas lain.
2. Import library rapih (terdapat dalam 1 cell dan tidak ada unused libs).
3. Terdapat komentar pada setiap baris kode.
4. Adanya pemisah yang jelas antar section, dll.
5. Tidak adanya typo.
```

---

```
Total Points : 124
```

---

## Notes

* **Deadline : P2W3D3 pukul 23:59 WIB.**

* **Keterlambatan pengumpulan tugas mengakibatkan skor Milestone 3 menjadi 0.**
