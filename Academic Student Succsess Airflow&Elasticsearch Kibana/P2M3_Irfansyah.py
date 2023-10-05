'''
=======================================================================================================================
Milestone 3

Name: Irfansyah Alif Muhammad
Batch: HCK - 007

Program ini dirancang untuk mengotomatisasi transformasi dan pengisian data dari database PostgreSQL ke Elasticsearch.
Dataset yang digunakan dalam operasi ini berfokus pada Prediksi Drop Out Mahasiswa dan Keberhasilan Akademik.
=======================================================================================================================
'''
import pandas as pd
import psycopg2 as db
from elasticsearch import Elasticsearch

# String koneksi untuk PostgreSQL
conn_string = "dbname='airflow' host='localhost' user='postgres' password='akupopok1'"
conn = db.connect(conn_string)

# Membaca data dari tabel 'table_M3' ke dalam DataFrame
df = pd.read_sql("select * from table_M3", conn)

# Kolom yang akan digunakan
column =['Marital status', 'Application mode', 'Application order', 'Course',
        'Daytime/evening attendance', 'Previous qualification', 'Nacionality',
        "Mother's qualification", "Father's qualification",
        "Mother's occupation", "Father's occupation", 'Displaced',
        'Educational special needs', 'Debtor', 'Tuition fees up to date',
        'Gender', 'Scholarship holder', 'Age at enrollment', 'International',
        'Curricular units 1st sem (credited)',
        'Curricular units 1st sem (enrolled)',
        'Curricular units 1st sem (evaluations)',
        'Curricular units 1st sem (approved)',
        'Curricular units 1st sem (grade)',
        'Curricular units 1st sem (without evaluations)',
        'Curricular units 2nd sem (credited)',
        'Curricular units 2nd sem (enrolled)',
        'Curricular units 2nd sem (evaluations)',
        'Curricular units 2nd sem (approved)',
        'Curricular units 2nd sem (grade)',
        'Curricular units 2nd sem (without evaluations)', 'Unemployment rate',
        'Inflation rate', 'GDP', 'Target']

# Fungsi untuk membersihkan data
def cleaning_data(dataframe):
    # Mengganti nilai Gender
    dataframe['Gender'] = dataframe['Gender'].replace({'0':'male', '1':'female'})
    # Mengubah nama kolom menjadi lowercase
    dataframe.columns = [col.lower() for col in dataframe.columns]
    # Mengganti spasi dengan underscore pada nama kolom
    dataframe.columns = dataframe.columns.str.replace(' ', '_')
    # Menghapus koma atas nama kolom
    dataframe.columns = dataframe.columns.str.replace("'", '')
    # Mengembalikan dataframe yang telah dibersihkan
    return dataframe

# Memanggil fungsi cleaning_data untuk membersihkan dataframe
cleaned_df = cleaning_data(df)

# Menyimpan dataframe yang telah dibersihkan ke file CSV
cleaned_df.to_csv('P2M3_Irfansyah_data_clean.csv', index=False)
print("-------Data Saved------")

# Menghubungkan ke Elasticsearch
es = Elasticsearch("http://elasticsearch:9200")

# Membaca dataframe yang telah dibersihkan dari file CSV
df_cleaned = pd.read_csv('P2M3_Irfansyah_data_clean.csv')

# Mengindeks setiap baris dari dataframe ke elasticsearch
for i, r in df_cleaned.iterrows():
    # Mengonversi baris ke JSON
    doc = r.to_json()
    # Mengindeks data ke Elasticsearch
    res = es.index(index="table_M3", body=doc)  
    print(res)