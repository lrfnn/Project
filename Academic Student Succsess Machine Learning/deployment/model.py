import streamlit as st
import pandas as pd
import pickle
import ast
import numpy as np

def run():
    st.title('Selamat Datang Di Halaman Model!')
    # Load All Files
    with open('all_process.pkl', 'rb') as file_1:
        all_process = pickle.load(file_1)
       

    # Initialize y_pred_inf as None    
    y_pred_inf = None
    
    # Create Streamlit input widgets for user input
    Curricular_units_2nd_sem_grade = st.number_input(label='Masukan nilai Curricular units 2nd sem grade', min_value=0, max_value=19, value=0)
    Curricular_units_1st_sem_grade = st.number_input(label='Masukan nilai Curricular units 1st sem grade', min_value=0, max_value=19, value=0, key=12)
    Curricular_units_2nd_sem_approved = st.number_input(label='Masukan nilai Curricular units 2nd sem approved', min_value=0, max_value=50, value=0, key=11)
    Curricular_units_1st_sem_approved = st.number_input(label='Masukan nilai Curricular units 1st sem approved', min_value=0, max_value=26, value=0, key=10)
    Curricular_units_1st_sem_evaluations = st.number_input(label='Masukan nilai Curricular units 1st sem evaluations', min_value=0, max_value=45, value=0, key=15)
    Curricular_units_2nd_sem_evaluations = st.number_input(label='Masukan nilai Curricular units 2nd sem evaluations', min_value=0, max_value=33, value=0, key=17)
    Age_at_enrollment = st.number_input(label='Masukan nilai Age at enrollment', min_value=0, max_value=70, value=0, key=20)
    Application_mode = st.number_input(label='Masukan nilai Application mode', min_value=0, max_value=18, value=0, key=21)
    Course = st.number_input(label='Masukan nilai Course', min_value=-2, max_value=17, value=0, key=22)
    
    # Create a dataframe to hold the user input data
    data_inf = pd.DataFrame({
        'Curricular units 2nd sem (grade)': [Curricular_units_2nd_sem_grade],
        'Curricular units 1st sem (grade)': [Curricular_units_1st_sem_grade],
        'Curricular units 2nd sem (approved)': [Curricular_units_2nd_sem_approved],
        'Curricular units 1st sem (approved)': [Curricular_units_1st_sem_approved],
        'Curricular units 1st sem (evaluations)': [Curricular_units_1st_sem_evaluations],
        'Curricular units 2nd sem (evaluations)': [Curricular_units_2nd_sem_evaluations],
        'Age at enrollment': [Age_at_enrollment],
        'Application mode': [Application_mode],
        'Course': [Course]
    })
    
    # Display the user input data in a table
    st.table(data_inf)

    # When the "Prediksi" button is clicked
    if st.button(label='predict'):
    
        # Melakukan prediksi data dummy
        y_pred_inf = all_process.predict(data_inf)

        st.write(y_pred_inf[0])

        if y_pred_inf[0] == 0:
            st.write('Mahasiswa Diprediksi Tidak Lulus')
        else:
            st.write('Mahasiswa Diprediksi Lulus')
