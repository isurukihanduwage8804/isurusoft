import streamlit as st
import random

# 1. පිටුවේ මූලික සැකසුම්
st.set_page_config(page_title="ඉසුරු සර්ගේ අධ්‍යාපනික ක්‍රීඩා පුවරුව", page_icon="📖", layout="wide")

# --- Page View Counter (50,000 සිට ආරම්භ වේ) ---
if 'view_count' not in st.session_state:
    st.session_state['view_count'] = 50240 

if 'counted' not in st.session_state:
    st.session_state['view_count'] += random.randint(10, 50)
    st.session_state['counted'] = True

# --- ලින්ක් 23 දත්ත ---
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

if 'is_logged_in' not in st.session_state:
    st.session_state['is_logged_in'] = False

# --- CSS Styling ---
st.markdown("""
<style>
    .stApp { background-color: #0f172a; }
    .red-title {
        text-align: center; color: #FF0000 !important; font-size: 38px !important; 
        font-weight: bold !important; text-shadow: 2px 2px 4px #000; margin-bottom: 25px;
    }
    .yellow-text { color: #facc15 !important; font-weight: bold; }
    .ad-card {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        border: 2px solid #facc15; border-radius: 12px; padding: 15px; text-align: center;
    }
    .stButton>button { 
        width: 100%; border-radius: 10px; background: #1e293b; color: #38bdf8;
        border: 1px solid #334155; font-weight: bold; height: 3.5em;
    }
</style>
""", unsafe_allow_html=True)

# --- LOGIN ---
if not st.session_state['is_logged_in']:
    st.markdown('<div class="red-title">ඉසුරු සර්ගේ අධ්‍යාපනික ක්‍රීඩා පුවරුව</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown('<p class="yellow-text">User Name</p>', unsafe_allow_html=True)
        u = st.text_input("", key="login_u", label_visibility="collapsed")
        st.markdown('<p class="yellow-text">Password</p>', unsafe_allow_html=True)
        p = st.text_input("", type="password", key="login_p", label_visibility="collapsed")
        if st.button("LOGIN"):
            if u == "isurusoft" and p == "123456":
                st.session_state['is_logged_in'] = True
                st.rerun()
            else: st.error("වැරදි විස්තර ඇතුළත් කළා!")

# --- MAIN DASHBOARD ---
else:
    st.markdown('<div class="red-title">ඉසුරු සර්ගේ අධ්‍යාපනික ක්‍රීඩා පුවරුව</div>', unsafe_allow_html=True)
    
    # Sidebar with View Count
    st.sidebar.markdown(f'<h3 style="color:#facc15;">Views: {st.session_state["view_count"]:,}</h3>', unsafe_allow_html=True)
    st.sidebar.markdown("---")
    
    # AD SECTION
    st.sidebar.markdown('<p style="color:white; font-size:12px; font-weight:bold;">අනුග්‍රාහක දැන්වීම්</p>', unsafe_allow_html=True)
    
    # පින්තූරය ලැබෙන තෙක් තාවකාලික පින්තූරයක් යොදා ඇත
    AD_IMAGE_URL = "https://via.placeholder.com/300x200.png?text=Ad+Space+Available"
    
    st.sidebar.markdown(f"""
        <div class="ad-card">
            <img src="{AD_IMAGE_URL}" style="width:100%; border-radius:8px; margin-bottom:10px;">
            <p style="color:#cbd5e1; font-size:13px;">ඔබේ ව්‍යාපාරය දහස් ගණනක් වෙත ගෙන යන්න.</p>
            <a href="https://wa.me/94XXXXXXXXX" target="_blank" style="text-decoration:none;">
                <div style="background:#facc15; color:black; padding:8px; border-radius:5px; font-weight:bold;">දැන්වීම් පළ කිරීමට</div>
            </a>
        </div>
    """, unsafe_allow_html=True)
    
    st.sidebar.markdown("---")
    if st.sidebar.button("Logout"):
        st.session_state['is_logged_in'] = False
        st.rerun()

    # Main Grid
    st.markdown('<p class="yellow-text">අවශ්‍ය සේවාව තෝරාගන්න:</p>', unsafe_allow_html=True)
    cols = st.columns(3)
    for idx, item in enumerate(LINKS_DATA):
        with cols[idx % 3]:
            st.link_button(f"{item['icon']} {item['name']}", item['url'], use_container_width=True)

    st.markdown("---")
    st.caption("© 2025 IsuruSoft Web Solutions")
