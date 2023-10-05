import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_extras.app_logo import add_logo
import model, eda

# Set page title and icon
st.set_page_config(page_title='Milestone 2', page_icon='⭐')

# Create sidebar navigation
st.sidebar.title('')
st.markdown(
        f"""
            <style>
                [data-testid="stSidebar"] {{
                    background-image: url(https://d3g5ywftkpzr0e.cloudfront.net/wp-content/uploads/2020/01/15094433/hacktiv8-1.png);
                    background-repeat: no-repeat;
                    padding-top: 80px;
                    background-position: 20px 20px;
                }}
            </style>
            """,
        unsafe_allow_html=True,
    )
selected_page = st.sidebar.radio('Pilih Halaman', ('Beranda', 'Exploratory Data Analysis', 'Model'))

# Halaman Beranda
if selected_page == 'Beranda':
    st.image("https://www.hacktiv8.com/_next/image?url=%2Flogo.png&w=1920&q=75", use_column_width=True)
    st.title('Irfansyah Alif Muhammad')
    st.header('Milestone 2')
    rain(
    emoji="💯",
    font_size=50,
    falling_speed=10,
    animation_length="infinite")

# Halaman EDA
elif selected_page == 'Exploratory Data Analysis':
    eda.run()
    
# Halaman Model
elif selected_page == 'Model':
    model.run()