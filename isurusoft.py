import streamlit as st
import random
import string

# 1. පිටුවේ මූලික සැකසුම්
st.set_page_config(page_title="IsuruSoft Web Dictionary", page_icon="📖", layout="wide")

# 2. ඔබ එවූ ලින්ක් 23 සහ ඒවාට අදාළ අයිකන් (Icons)
LINKS_DATA = [
    {"name": "Graph Art 2", "url": "https://nicegrap2.streamlit.app/", "icon": "🎨"},
    {"name": "IsuruSoft Portal", "url": "https://isurusoft.streamlit.app/", "icon": "🌐"},
    {"name": "3D App Best", "url": "https://3dappbest.streamlit.app/", "icon": "🧊"},
    {"name": "Periodic Table", "url": "https://prtable.streamlit.app/", "icon": "🧪"},
    {"name": "BMI Manager", "url": "https://bmimannew.streamlit.app/#8b1d9de1", "icon": "⚖️"},
    {"name": "Rachana 2", "url": "https://rachana-2new.streamlit.app/", "icon": "✍️"},
    {"name": "Angle Shape", "url": "https://angaleshape.streamlit.app/", "icon": "📐"},
    {"name": "Atom Animation", "url": "https://atomanimation.streamlit.app/", "icon": "⚛️"},
    {"name": "Grade 5 Maths", "url": "https://grade5maths.streamlit.app/", "icon": "🔢"},
    {"name": "Grade 5 Sinhala", "url": "https://grade5sinhalanew.streamlit.app/", "icon": "📚"},
    {"name": "Sankya Dadayama", "url": "https://sankyadadayamanew2.streamlit.app/", "icon": "🎯"},
    {"name": "Maths Puzzle", "url": "https://mathspuzzle1.streamlit.app/", "icon": "🧩"},
    {"name": "Real Puzzle 1", "url": "https://real-puzzle-1-csyvarjphxh9z9tndnj4ff.streamlit.app/", "icon": "🎮"},
    {"name": "Answer to Ques", "url": "https://anser-to-ques2-c9yurtmondfbzjcpoxguwn.streamlit.app/", "icon": "💡"},
    {"name": "Therawili", "url": "https://therawili-gzggdyxieygqhaifx6jp8k.streamlit.app/", "icon": "🕵️"},
    {"name": "Graph 1", "url": "https://graph-1-4e7bbfbpkg9aw5uvxp9yc6.streamlit.app/", "icon": "📊"},
    {"name": "Money Converter", "url": "https://mony-converter-zhtsej33cdvttrtwqhle4q.streamlit.app/", "icon": "💱"},
    {"name": "Word Meaning", "url": "https://word-meaning-ndkg9veahhahsqweqimcrz.streamlit.app/", "icon": "📖"},
    {"name": "Shape Converter", "url": "https://shape-converter-fkun3v4m8gx4dyjqkfmt5t.streamlit.app/", "icon": "🔄"},
    {"name": "4 Box Game", "url": "https://4-box-game-95ri7jjkakjyjhzgrhfmgc.streamlit.app/", "icon": "📦"},
    {"name": "Tetris Maths", "url": "https://tetrics-maths-pawkf7v2qvh52ze8jsqtxn.streamlit.app/", "icon": "🕹️"},
    {"name": "Budda Darmaya", "url": "https://budda-darmaya-1.streamlit.app/", "icon": "☸️"},
    {"name": "Maths 680", "url": "https://grade-5-maths-680-ad749ecycarfizcfkyspir.streamlit.app/", "icon": "🎓"}
]

# Session State පවත්වා ගැනීම
if 'users' not in st.session_state:
    st.session_state['users'] = {}
if 'is_logged_in' not in st.session_state:
    st.session_state['is_logged_in'] = False

# 3. CSS Styling
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; }
    .stButton>button { 
        width: 100%; 
        border-radius: 12px; 
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%); 
        color: #38bdf8; 
        font-weight: bold; 
        border: 1px solid #334155;
        height: 4em;
        transition: 0.3s;
    }
    .stButton>button:hover {
        border: 1px solid #38bdf8;
        transform: scale(1.02);
        color: white;
    }
    .link-card {
        padding: 10px;
        text-align: center;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. Login & Registration
if not st.session_state['is_logged_in']:
    st.markdown("<h1 style='text-align: center; color: #38bdf8;'>IsuruSoft Web Dictionary</h1>", unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["📝 ලියාපදිංචිය", "🔑 පිවිසෙන්න"])

    with tab1:
        reg_name = st.text_input("ඔබේ නම ඇතුළත් කරන්න")
        if st.button("ගිණුමක් සාදන්න"):
            if reg_name:
                email = f"{reg_name.lower().replace(' ', '')}{random.randint(100, 999)}@isurusoft.lk"
                password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
                st.session_state['users'][email] = password
                st.success("ගිණුම නිපදවන ලදී!")
                st.code(f"Email: {email}\nPassword: {password}")

    with tab2:
        u_email = st.text_input("Email")
        u_pass = st.text_input("Password", type="password")
        if st.button("Log In"):
            if u_email in st.session_state['users'] and st.session_state['users'][u_email] == u_pass:
                st.session_state['is_logged_in'] = True
                st.rerun()
            else:
                st.error("විස්තර වැරදියි!")

# 5. Dashboard (ලොග් වූ පසු)
else:
    st.markdown("<h1 style='text-align: center; color: #4ade80;'>IsuruSoft Dashboard</h1>", unsafe_allow_html=True)
    st.sidebar.button("Logout", on_click=lambda: st.session_state.update({"is_logged_in": False}))
    
    st.write("ඔබට අවශ්‍ය සේවාව තෝරාගන්න:")
    st.markdown("---")

    # බොත්තම් 23 පේළියට 3 බැගින් අයිකන් සමඟ පෙන්වීම
    cols_per_row = 3
    for i in range(0, len(LINKS_DATA), cols_per_row):
        cols = st.columns(cols_per_row)
        for j in range(cols_per_row):
            index = i + j
            if index < len(LINKS_DATA):
                item = LINKS_DATA[index]
                with cols[j]:
                    # අයිකන් එක සහ නම සහිත බොත්තම
                    st.link_button(f"{item['icon']} {item['name']}", item['url'])
