import streamlit as st
import random
import string

# 1. පිටුවේ මූලික සැකසුම් (Page Config)
st.set_page_config(page_title="IsuruSoft Web Dictionary", page_icon="📖", layout="wide")

# 2. ඔබ එවූ නිවැරදි ලින්ක් 23 කේතයට ඇතුළත් කිරීම
LINKS_DATA = [
    "https://nicegrap2.streamlit.app/",
    "https://isurusoft.streamlit.app/",
    "https://3dappbest.streamlit.app/",
    "https://prtable.streamlit.app/",
    "https://bmimannew.streamlit.app/#8b1d9de1",
    "https://rachana-2new.streamlit.app/",
    "https://angaleshape.streamlit.app/",
    "https://atomanimation.streamlit.app/",
    "https://grade5maths.streamlit.app/",
    "https://grade5sinhalanew.streamlit.app/",
    "https://sankyadadayamanew2.streamlit.app/",
    "https://mathspuzzle1.streamlit.app/",
    "https://real-puzzle-1-csyvarjphxh9z9tndnj4ff.streamlit.app/",
    "https://anser-to-ques2-c9yurtmondfbzjcpoxguwn.streamlit.app/",
    "https://therawili-gzggdyxieygqhaifx6jp8k.streamlit.app/",
    "https://graph-1-4e7bbfbpkg9aw5uvxp9yc6.streamlit.app/",
    "https://mony-converter-zhtsej33cdvttrtwqhle4q.streamlit.app/",
    "https://word-meaning-ndkg9veahhahsqweqimcrz.streamlit.app/",
    "https://shape-converter-fkun3v4m8gx4dyjqkfmt5t.streamlit.app/",
    "https://4-box-game-95ri7jjkakjyjhzgrhfmgc.streamlit.app/",
    "https://tetrics-maths-pawkf7v2qvh52ze8jsqtxn.streamlit.app/",
    "https://budda-darmaya-1.streamlit.app/",
    "https://grade-5-maths-680-ad749ecycarfizcfkyspir.streamlit.app/"
]

# 3. Session State හරහා දත්ත පවත්වා ගැනීම
if 'users' not in st.session_state:
    st.session_state['users'] = {}
if 'is_logged_in' not in st.session_state:
    st.session_state['is_logged_in'] = False
if 'current_user' not in st.session_state:
    st.session_state['current_user'] = ""

# 4. CSS Styling (ලස්සන පෙනුම සඳහා)
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; }
    .stButton>button { 
        width: 100%; 
        border-radius: 10px; 
        background: linear-gradient(45deg, #0284c7, #0ea5e9); 
        color: white; 
        font-weight: bold; 
        border: none;
    }
    .link-card {
        padding: 15px;
        background-color: #1e293b;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #334155;
        margin-top: 10px;
    }
