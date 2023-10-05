import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run():
    
    st.title('Selamat Datang Di Halaman EDA!')    
    plot_selection = st.sidebar.selectbox(label='Pilih Isi',options=['Gender Distribution','Kelas International','PieChart Target',
                                                                 'Mahasiswa yang Beasiswa', 'Status Pernikahan', 'Umur Mahasiswa yang Mendaftar'])
    df = pd.read_csv('dataset.csv')

    # Grafik 1
    def create_plot_1():
        st.header('Gender Distribution')
        fig_1 = plt.figure()
        sns.countplot(data=df, x='Gender', hue='Target', hue_order=['Dropout', 'Enrolled', 'Graduate'])
        plt.xticks(ticks=[0, 1], labels=['Female', 'Male'])
        plt.ylabel('Number of Students')
        st.pyplot(fig_1)
        with st.expander('Penjelasan'):
            st.text('''
                Berdasarkan data diatas, perempuan memiliki jumlah lulusan tertinggi,
                namun juga memiliki jumlah siswa yang paling tinggi yang keluar dari sekolah
                dibandingkan dengan laki-laki. Dengan kata lain, meskipun lebih banyak perempuan
                yang berhasil menyelesaikan pendidikan mereka, tetapi juga terdapat lebih banyak
                perempuan yang tidak melanjutkan pendidikan mereka dibandingkan dengan laki-laki.
            ''')
    # Grafik 2
    def create_plot_2():
        st.header('Kelas International')
        fig_2 = plt.figure()
        sns.countplot(data=df, x='International', hue='Target', hue_order=['Dropout', 'Enrolled', 'Graduate'])
        plt.xticks(ticks=[0,1], labels=['No','Yes'])
        plt.ylabel('Number of Students')
        plt.show()
        st.pyplot(fig_2)
        with st.expander('Penjelasan'):
            st.text('''
                Dapat dilihat ada lebih banyak mahasiswa yang bukan dari kelas internasional, 
                dan jumlah mahasiswa yang lulus dari kelas biasa (non-internasional) juga lebih tinggi.
            ''')

   
    # Grafik 3
    def create_plot_3():
        st.header('PieChart Target')
        fig_3 = plt.figure()
        students_target = df['Target'].value_counts()
        plt.pie(students_target, labels=students_target.index, autopct='%2.1f%%')
        plt.title('Target Distribution dalam persen')
        plt.show()
        st.pyplot(fig_3)
    

    # Grafik 4
    def create_plot_4():
        st.header('Mahasiswa yang Beasiswa')
        fig_4 = plt.figure(figsize=(8, 6))
        sns.countplot(data=df, x="Scholarship holder", hue='Target', hue_order=['Dropout', 'Enrolled', 'Graduate'])
        plt.xticks(ticks=[0,1], labels=['No','Yes'])
        plt.xlabel('Scholarship Holder')
        plt.ylabel('Number of Students')
        plt.show()
        st.pyplot(fig_4)
        with st.expander('Penjelasan'):
            st.text('''
                    Dapat dilihat bahwa dalam data ini, terdapat tiga kategori utama, yaitu 
                    Graduate (lulus), Enrolled (telah mendaftar), dan Dropout (keluar atau tidak lulus). 
                    Paling banyak mahasiswa tergolong dalam kategori Graduate, 
                    yang menandakan bahwa jumlah mahasiswa yang berhasil 
                    menyelesaikan studinya lebih tinggi dibandingkan dengan yang lainnya.''')
            
    # Grafik 5
    def create_plot_5():
        st.header('Melihat Kelulusan Berdasarkan Status Pernikahaan')
        fig_5 = plt.figure()
        crosstab_data = pd.crosstab(df["Marital status"], df["Target"], normalize='index')
        st.bar_chart(crosstab_data, use_container_width=True)
        with st.expander('Penjelasan'):
            st.text('''
                Dari grafik batang di atas, dapat diambil beberapa kesimpulan penting sebagai berikut:

                -    Mahasiswa yang berstatus hukum terpisah (legally separated) memiliki tingkat keluar dari sekolah yang 
                signifikan lebih tinggi dibandingkan dengan mahasiswa dalam status perkawinan lainnya. Hal ini menunjukkan 
                bahwa situasi perkawinan yang terpisah secara hukum dapat menjadi faktor risiko yang signifikan dalam kelulusan.

                -    Mahasiswa yang lajang (single) cenderung memiliki tingkat kelulusan yang lebih tinggi dibandingkan dengan
                yang berstatus perkawinan lainnya. Ini mungkin disebabkan oleh fokus yang lebih besar pada pendidikan mereka 
                tanpa tanggungan keluarga yang sama seperti mahasiswa yang sudah menikah atau bercerai.

                -    Mahasiswa yang menikah (married) dan yang telah bercerai (divorced) memiliki kemungkinan keluar dari 
                sekolah yang lebih tinggi dibandingkan dengan yang lajang. Namun, perbedaan antara tingkat kelulusan dan 
                keluar dari sekolah untuk kedua kelompok ini tidak terlalu besar, menunjukkan adanya faktor-faktor lain yang
                perlu dipertimbangkan.''')
    
    # Grafik 6
    def create_plot_6():
        st.header('Umur Mahasiswa yang Mendaftar')
        fig_6, ax_6 = plt.subplots()
        sns.histplot(data=df, x='Age at enrollment', kde=True, ax=ax_6)
        plt.xlabel('Age at Enrollment')
        plt.ylabel('Number of Students')
        st.pyplot(fig_6)
        with st.expander('Penjelasan'):
            st.text('''
                Dari data tersebut, terlihat bahwa mahasiswa mendaftar dalam rentang usia
                yang bervariasi, mulai dari usia 17 hingga 70 tahun, dengan usia rata-rata 
                (yang menjadi mayoritas) sekitar 23 tahun.''')
            
    # Menampilkan Halaman yang Dipilih
    if plot_selection == "Gender Distribution":
        create_plot_1()
    elif plot_selection == "Kelas International":
        create_plot_2()
    elif plot_selection == "PieChart Target":
        create_plot_3()
    elif plot_selection == "Mahasiswa yang Beasiswa":
        create_plot_4()
    elif plot_selection == "Status Pernikahan":
        create_plot_5()
    elif plot_selection == "Umur Mahasiswa yang Mendaftar":
        create_plot_6()