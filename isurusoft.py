import streamlit as st
import random

# 1. පිටුවේ මූලික සැකසුම්
st.set_page_config(page_title="IsuruSoft Educational Portal", page_icon="🎓", layout="wide")

# --- Session State Initializations ---
if 'view_count' not in st.session_state:
    st.session_state['view_count'] = 50240 

if 'counted' not in st.session_state:
    st.session_state['view_count'] += random.randint(15, 60)
    st.session_state['counted'] = True

if 'is_logged_in' not in st.session_state:
    st.session_state['is_logged_in'] = False

if 'user_comments' not in st.session_state:
    st.session_state['user_comments'] = []

# --- ලින්ක් දත්ත ---
CATEGORIES = {
    "🔢 ගණිතය සහ විද්‍යාව (Maths & Science)": [
        {"name": "Geometry Dance", "url": "https://shape-aria-m2uzeyna2bdyfdx3xktdgv.streamlit.app/", "icon": "📐"},
        {"name": "Graph Art 2", "url": "https://nicegrap2.streamlit.app/", "icon": "🎨"},
        {"name": "Periodic Table", "url": "https://prtable.streamlit.app/", "icon": "🧪"},
        {"name": "Angle Shape", "url": "https://angaleshape.streamlit.app/", "icon": "📐"},
        {"name": "Atom Animation", "url": "https://atomanimation.streamlit.app/", "icon": "⚛️"},
        {"name": "Grade 5 Maths", "url": "https://grade5maths.streamlit.app/", "icon": "🔢"},
        {"name": "Graph 1", "url": "https://graph-1-4e7bbfbpkg9aw5uvxp9yc6.streamlit.app/", "icon": "📊"},
        {"name": "Maths 680", "url": "https://grade-5-maths-680-ad749ecycarfizcfkyspir.streamlit.app/", "icon": "🎓"}
    ],
    "📚 භාෂාව සහ පොදු දැනුම (Language & Knowledge)": [
        {"name": "IsuruSoft Portal", "url": "https://isurusoft.streamlit.app/", "icon": "🌐"},
        {"name": "Rachana 2", "url": "https://rachana-2new.streamlit.app/", "icon": "✍️"},
        {"name": "Grade 5 Sinhala", "url": "https://grade5sinhalanew.streamlit.app/", "icon": "📚"},
        {"name": "Word Meaning", "url": "https://word-meaning-ndkg9veahhahsqweqimcrz.streamlit.app/", "icon": "📖"},
        {"name": "Budda Darmaya", "url": "https://budda-darmaya-1.streamlit.app/", "icon": "☸️"},
        {"name": "BMI Manager", "url": "https://bmimannew.streamlit.app/#8b1d9de1", "icon": "⚖️"}
    ],
    "🎮 ප්‍රහේලිකා සහ ක්‍රීඩා (Puzzles & Games)": [
        {"name": "සංඛ්‍යා ගැටුම (Math Combat)", "url": "https://sankaya-gatuma-bgypbr5g5w2dofu9emv9xz.streamlit.app/", "icon": "⚔️"},
        {"name": "3D App Best", "url": "https://3dappbest.streamlit.app/", "icon": "🧊"},
        {"name": "Sankya Dadayama", "url": "https://sankyadadayamanew2.streamlit.app/", "icon": "🎯"},
        {"name": "Maths Puzzle", "url": "https://mathspuzzle1.streamlit.app/", "icon": "🧩"},
        {"name": "Real Puzzle 1", "url": "https://real-puzzle-1-csyvarjphxh9z9tndnj4ff.streamlit.app/", "icon": "🎮"},
        {"name": "Answer to Ques", "url": "https://anser-to-ques2-c9yurtmondfbzjcpoxguwn.streamlit.app/", "icon": "💡"},
        {"name": "Therawili", "url": "https://therawili-gzggdyxieygqhaifx6jp8k.streamlit.app/", "icon": "🕵️"},
        {"name": "Money Converter", "url": "https://mony-converter-zhtsej33cdvttrtwqhle4q.streamlit.app/", "icon": "💱"},
        {"name": "Shape Converter", "url": "https://shape-converter-fkun3v4m8gx4dyjqkfmt5t.streamlit.app/", "icon": "🔄"},
        {"name": "4 Box Game", "url": "https://4-box-game-95ri7jjkakjyjhzgrhfmgc.streamlit.app/", "icon": "📦"},
        {"name": "Tetris Maths", "url": "https://tetrics-maths-pawkf7v2qvh52ze8jsqtxn.streamlit.app/", "icon": "🕹️"}
    ]
}

# --- CSS Styling ---
st.markdown("""
<style>
    .stApp { background-color: #0f172a; }
    .main-title { text-align: center; color: #ff4b4b; font-size: 45px; font-weight: 800; margin-bottom: 20px; }
    .sub-title { text-align: center; color: #cbd5e1; font-size: 18px; margin-bottom: 40px; }
    .category-header { background-color: #1e293b; padding: 10px 20px; border-radius: 8px; color: #facc15; font-size: 20px; font-weight: bold; margin-top: 30px; border-left: 5px solid #ff4b4b; }
    .ad-card { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 10px; text-align: center; transition: 0.3s; }
    .ad-card:hover { border-color: #ff4b4b; transform: scale(1.02); }
    .comment-card
