import streamlit as st
import pandas as pd
import numpy as np


st. set_page_config(
    page_title='QUIZOOTHON',
    page_icon="📖",
    layout='centered',
    initial_sidebar_state='collapsed'
)

st.title('Welcome to QUIZOOTHON 🧠!')
st.write('This is a fantastic quiz competition!')



with st.sidebar:
    st.header("👨‍💻 About the Author")
    st.write("""
    **Sumeet Deshpande** is a tech enthusiast, student, and coder. Driven by passion and a love for AI and ML, he's developed this platform to make learning more interactive and fun.

    Connect, contribute, or just say hi!
    """)

    st.divider()
    st.subheader("🔗 Connect with Me", anchor=False)
    st.markdown(
            """
           
            - [🌐 Personal Website](https://digital-cv-5tfl.onrender.com/)
            - [👔 LinkedIn](https://www.linkedin.com/in/sumeet-deshpande-b33840227/)
            """
        )