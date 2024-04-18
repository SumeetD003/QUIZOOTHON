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

st.title(":blue[Quizoothon] — Watch. Learn. Quiz. 🧠", anchor=False)
st.write("""
        Have you ever found yourself watching a YouTube video and pondered how effectively you grasped its content? 
        Take a delightful turn: rather than solely viewing on YouTube, engage in Quizoothon to gauge your comprehension!

**How does it work?** 🤔
1. Paste the YouTube video URL of your recently watched video.
2. Enter your [Gemini/Vertex API Key](https://aistudio.google.com/app/apikey).

⚠️ Important: The video **must** have English captions for the tool to work.

After inputting the details, GGWP! Delve into tailored questions designed specifically for you, confirming your thorough understanding of the video's content. Let's challenge your knowledge!
""")