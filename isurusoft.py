import streamlit as st
import random

# 1. පිටුවේ මූලික සැකසුම්
st.set_page_config(page_title="සවුත් විෂන් වෙබ් තක්සලාව", page_icon="🎓", layout="wide")

# --- Session State ---
if 'view_count' not in st.session_state:
    st.session_state['view_count'] = 50240 
if 'counted' not in st.session_state:
    st.session_state['view_count'] += random.randint(15, 60)
    st.session_state['counted'] = True
if 'is_logged_in' not in st.session_state:
    st.session_state['is_logged_in'] = False

# --- CSS Styling (රතු පාට සහ කුඩා අකුරු) ---
st.markdown("""
<style>
    .stApp { background-color: #0f172a; }
    .main-title { 
        text-align: center; 
        color: #ff0000; /* රතු පාට */
        font-size: 24px; /* අකුරු ප්‍රමාණය කුඩා කළා */
        font-weight: 800; 
        margin-bottom: 20px; 
    }
    .category-header { 
        background-color: #1e293b; 
        padding: 8px 15px; 
        border-radius: 8px; 
        color: #facc15; 
        font-size: 17px; 
        font-weight: bold; 
        margin-top: 25px; 
        border-left: 5px solid #ff0000; 
    }
    .login-container { background: #1e293b; padding: 30px; border-radius: 15px; border: 1px solid #334155; }
    .welcome-text { color: #facc15; font-size: 20px; font-weight: bold; margin-bottom: 20px; }
    
    /* Full Screen Button එක අයින් කිරීමට */
    button[title="View fullscreen"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

# 1. LOGIN SECTION
if not st.session_state['is_logged_in']:
    st.markdown('<h1 class="main-title">සවුත් විෂන් වෙබ් තක්සලාව</h1>', unsafe_allow_html=True)
    col_img, col_form = st.columns([1.2, 1], gap="large")
    with col_img:
        st.image("https://raw.githubusercontent.com/isurukihanduwage8804/isurusoft/main/2.png", use_container_width=True)
    with col_form:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.markdown('<p class="welcome-text">Welcome Back!</p>', unsafe_allow_html=True)
        u = st.text_input("User Name", key="user_input")
        p = st.text_input("Password", type="password", key="pass_input")
        if st.button("LOGIN", use_container_width=True):
            if u == "isurusoft" and p == "123456":
                st.session_state['is_logged_in'] = True
                st.rerun()
            else:
                st.error("Login තොරතුරු වැරදියි!")
        st.markdown('</div>', unsafe_allow_html=True)

# 2. MAIN HUB SECTION (Logged In)
else:
    st.markdown('<h1 class="main-title">සවුත් විෂන් වෙබ් තක්සලාව</h1>', unsafe_allow_html=True)
    st.sidebar.markdown(f'<h2 style="color:#facc15; text-align:center;">VIEWS: {st.session_state["view_count"]:,}</h2>', unsafe_allow_html=True)
    if st.sidebar.button("LOGOUT", use_container_width=True):
        st.session_state['is_logged_in'] = False
        st.rerun()

    # දිග ලින්ක් එක කෑලි වලට කඩා ලියා ඇත
    quiz_url = "https://sciencetist-question-hknjybq5xxdcmrhcjahqol" + ".streamlit.app/"

    CATEGORIES = {
        "🔢 ගණිතය සහ විද්‍යාව": [
            {"n": "Geometry Dance", "u": "https://shape-aria-m2uzeyna2bdyfdx3xktdgv.streamlit.app/", "i": "📐"},
            {"n": "Graph Art 2", "u": "https://nicegrap2.streamlit.app/", "i": "🎨"},
            {"n": "Periodic Table", "u": "https://prtable.streamlit.app/", "i": "🧪"},
            {"n": "Angle Shape", "u": "https://angaleshape.streamlit.app/", "i": "📐"},
            {"n": "Atom Animation", "u": "https://atomanimation.streamlit.app/", "i": "⚛️"},
            {"n": "Grade 5 Maths", "u": "https://grade5maths.streamlit.app/", "i": "🔢"},
            {"n": "Graph 1", "u": "https://graph-1-4e7bbfbpkg9aw5uvxp9yc6.streamlit.app/", "i": "📊"},
            {"n": "Maths 680", "u": "https://grade-5-maths-680-ad749ecycarfizcfkyspir.streamlit.app/", "i": "🎓"}
        ],
        "📚 භාෂාව සහ දැනුම": [
            {"n": "IsuruSoft Portal", "u": "https://isurusoft.streamlit.app/", "i": "🌐"},
            {"n": "Rachana 2", "u": "https://rachana-2new.streamlit.app/", "i": "✍️"},
            {"n": "Grade 5 Sinhala", "u": "https://grade5sinhalanew.streamlit.app/", "i": "📚"},
            {"n": "Word Meaning", "u": "https://word-meaning-ndkg9veahhahsqweqimcrz.streamlit.app/", "i": "📖"},
            {"n": "Budda Darmaya", "u": "https://budda-darmaya-1.streamlit.app/", "i": "☸️"},
            {"n": "BMI Manager", "u": "https://bmimannew.streamlit.app/", "i": "⚖️"}
        ],
        "🎮 ක්‍රීඩා සහ ප්‍රහේලිකා": [
            {"n": "Water Fraction", "u": "https://watergame-jr5z9ffafbsutbl67arjz8.streamlit.app/", "i": "🥤"},
            {"n": "Math Combat", "u": "https://sankaya-gatuma-bgypbr5g5w2dofu9emv9xz.streamlit.app/", "i": "⚔️"},
            {"n": "3D App Best", "u": "https://3dappbest.streamlit.app/", "i": "🧊"},
            {"n": "Sankya Dadayama", "u": "https://sankyadadayamanew2.streamlit.app/", "i": "🎯"},
            {"n": "Maths Puzzle", "u": "https://mathspuzzle1.streamlit.app/", "i": "🧩"},
            {"n": "Real Puzzle 1", "u": "https://real-puzzle-1-csyvarjphxh9z9tndnj4ff.streamlit.app/", "i": "🎮"},
            {"n": "Answer to Ques", "u": "https://anser-to-ques2-c9yurtmondfbzjcpoxguwn.streamlit.app/", "i": "💡"},
            {"n": "Therawili", "u": "https://therawili-gzggdyxieygqhaifx6jp8k.streamlit.app/", "i": "🕵️"},
            {"n": "Money Converter", "u": "https://mony-converter-zhtsej33cdvttrtwqhle4q.streamlit.app/", "i": "💱"},
            {"n": "Shape Converter", "u": "https://shape-converter-fkun3v4m8gx4dyjqkfmt5t.streamlit.app/", "i": "🔄"},
            {"n": "4 Box Game", "u": "https://4-box-game-95ri7jjkakjyjhzgrhfmgc.streamlit.app/", "i": "📦"},
            {"n": "Tetris Maths", "u": "https://tetrics-maths-pawkf7v2qvh52ze8jsqtxn.streamlit.app/", "i": "🕹️"}
        ],
        "🌍 සාමාන්‍ය දැනීම": [
            {"n": "විද්‍යාඥයින් කවුද?", "u": quiz_url, "i": "🔬"}
        ]
    }

    for cat_name, links in CATEGORIES.items():
        st.markdown(f'<div class="category-header">{cat_name}</div>', unsafe_allow_html=True)
        cols = st.columns(3)
        for i, item in enumerate(links):
            with cols[i % 3]:
                st.link_button(f"{item['i']} {item['n']}", item['u'], use_container_width=True)

    st.markdown("---")
    st.caption("© 2026 South Vision Web Solutions")
