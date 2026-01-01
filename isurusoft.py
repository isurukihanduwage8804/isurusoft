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

# --- CSS Styling (වැරදි නැතිව Full Screen Hide කර ඇත) ---
st.markdown("""
<style>
    .stApp { background-color: #0f172a; }
    .main-title { text-align: center; color: #ff4b4b; font-size: 45px; font-weight: 800; margin-bottom: 20px; }
    .category-header { background-color: #1e293b; padding: 10px 20px; border-radius: 8px; color: #facc15; font-size: 20px; font-weight: bold; margin-top: 30px; border-left: 5px solid #ff4b4b; }
    .login-container { background: #1e293b; padding: 30px; border-radius: 15px; border: 1px solid #334155; }
    .welcome-text { color: #facc15; font-size: 24px; font-weight: bold; margin-bottom: 20px; }
    
    /* Full Screen Button එක අයින් කරන කෝඩ් එක */
    button[title="View fullscreen"] {
        display: none !important;
    }
    
    [data-testid="stImage"] img {
        border-radius: 15px;
    }
</style>
""", unsafe_allow_html=True)

# 1. LOGIN පරීක්ෂාව
if not st.session_state['is_logged_in']:
    st.markdown('<h1 class="main-title">ISURUSOFT PORTAL</h1>', unsafe_allow_html=True)
    col_img, col_form = st.columns([1.2, 1], gap="large")
    with col_img:
        # ඔයාගේ අලුත් PNG එක ලින්ක් කළා
        st.image("https://raw.githubusercontent.com/isurukihanduwage8804/isurusoft/main/2.png?v=4", use_container_width=True)
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

# 2. LOGIN වූ පසු පෙන්වන කොටස
else:
    st.markdown('<h1 class="main-title">ISURUSOFT EDUCATIONAL HUB</h1>', unsafe_allow_html=True)
    st.sidebar.markdown(f'<h2 style="color:#facc15; text-align:center;">VIEWS: {st.session_state["view_count"]:,}</h2>', unsafe_allow_html=True)
    if st.sidebar.button("LOGOUT", use_container_width=True):
        st.session_state['is_logged_in'] = False
        st.rerun()

    # --- සියලුම ලින්ක්ස් මෙතන තියෙනවා (පරීක්ෂා කර බලන්න) ---
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
            {"name": "BMI Manager", "url": "https://bmimannew.streamlit.app/", "icon": "⚖️"}
        ],
        "🎮 ප්‍රහේලිකා සහ ක්‍රීඩා (Puzzles & Games)": [
            {"name": "Water Fraction", "url": "https://watergame-jr5z9ffafbsutbl67arjz8.streamlit.app/", "icon": "🥤"},
            {"name": "Math Combat", "url": "https://sankaya-gatuma-bgypbr5g5w2dofu9emv9xz.streamlit.app/", "icon": "⚔️"},
            {"name": "3D App Best", "url": "https://3dappbest.streamlit.app/", "icon": "🧊"},
            {"name": "Sankya Dadayama", "url": "https://sankyadadayamanew2.streamlit.app/", "icon": "🎯"},
            {"name": "Maths Puzzle", "url": "https://mathspuzzle1.streamlit.app/", "icon": "🧩"},
            {"name": "Real Puzzle 1", "url": "https://real-puzzle-1-csyvarjphxh9z9tndnj4ff.streamlit.app/", "icon": "🎮"},
            {"name": "Answer to Ques", "url": "https://anser-to-ques2-c9yurtmondfbzjcpoxguwn.streamlit.app/", "icon": "💡"},
            {"name": "Therawili", "url": "https://theraw
