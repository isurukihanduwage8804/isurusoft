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
# මෙතන triple quotes හරියට පියවා ඇති බව තහවුරු කළා
st.markdown("""
<style>
    .stApp { background-color: #0f172a; }
    .main-title { text-align: center; color: #ff4b4b; font-size: 45px; font-weight: 800; margin-bottom: 20px; }
    .sub-title { text-align: center; color: #cbd5e1; font-size: 18px; margin-bottom: 40px; }
    .category-header { background-color: #1e293b; padding: 10px 20px; border-radius: 8px; color: #facc15; font-size: 20px; font-weight: bold; margin-top: 30px; border-left: 5px solid #ff4b4b; }
    .ad-card { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 10px; text-align: center; }
    .comment-card { background: #1e293b; padding: 10px; border-radius: 8px; margin-bottom: 5px; border-left: 3px solid #facc15; color: #cbd5e1; }
    .login-container { background: #1e293b; padding: 30px; border-radius: 15px; border: 1px solid #334155; }
</style>
""", unsafe_allow_html=True)

# --- APP FLOW ---
if not st.session_state['is_logged_in']:
    st.markdown('<h1 class="main-title">ISURUSOFT PORTAL</h1>', unsafe_allow_html=True)
    
    col_img, col_form = st.columns([1.2, 1], gap="large")
    
    with col_img:
        LOGIN_IMAGE_URL = "https://raw.githubusercontent.com/isurukihanduwage8804/isurusoft/main/2.jpg"
        st.image(LOGIN_IMAGE_URL, use_container_width=True)
        
    with col_form:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.markdown('<p style="color:#facc15; font-size:18px; font-weight:bold;">Welcome Back!</p>', unsafe_allow_html=True)
        u = st.text_input("User Name", key="user_input", placeholder="Enter username")
        p = st.text_input("Password", type="password", key="pass_input", placeholder="Enter password")
        if st.button("LOGIN", use_container_width=True):
            if u == "isurusoft" and p == "123456":
                st.session_state['is_logged_in'] = True
                st.rerun()
            else:
                st.error("වැරදි තොරතුරු ඇතුළත් කළා!")
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # MAIN CONTENT (LoggedIn)
    st.markdown('<h1 class="main-title">ISURUSOFT EDUCATIONAL HUB</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">අනාගත පරපුර වෙනුවෙන් තැනූ නවීන අධ්‍යාපනික මෙවලම් කට්ටලය</p>', unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.markdown(f'<h2 style="color:#facc15; text-align:center;">VIEWS: {st.session_state["view_count"]:,}</h2>', unsafe_allow_html=True)
    st.sidebar.markdown("---")
    
    # Sidebar Comment Box
    st.sidebar.markdown("<h3 style='color:#facc15;'>ඔබේ අදහස කියන්න</h3>", unsafe_allow_html=True)
    new_comment = st.sidebar.text_area("අදහස් මෙතැන ලියන්න...", key="comment_area")
    if st.sidebar.button("ඇතුළත් කරන්න", use_container_width=True):
        if new_comment:
            st.session_state.user_comments.append(new_comment)
            st.sidebar.success("අදහස ඇතුළත් කළා!")
    
    if st.session_state.user_comments:
        st.sidebar.markdown("---")
        for comment in reversed(st.session_state.user_comments[-5:]):
            st.sidebar.markdown(f'<div class="comment-card">{comment}</div>', unsafe_allow_html=True)

    st.sidebar.markdown("---")
    
    # Ad Section
    AD_IMAGE_URL = "https://raw.githubusercontent.com/isurukihanduwage8804/isurusoft/main/ad1.jpg"
    ARIYADASA_URL = "https://web.facebook.com/ariyadasabookshop/?_rdc=1&_rdr#"
    
    st.sidebar.markdown(f"""
        <a href="{ARIYADASA_URL}" target="_blank" style="text-decoration:none;">
            <div class="ad-card">
                <img src="{AD_IMAGE_URL}" style="width:100%; border-radius:8px;">
                <p style="color:#facc15; margin-top:10px;">G.H. Ariyadasa Book Shop</p>
            </div>
        </a>
    """, unsafe_allow_html=True)
    
    st.sidebar.markdown("---")
    if st.sidebar.button("LOGOUT", use_container_width=True):
        st.session_state['is_logged_in'] = False
        st.rerun()

    for cat_name, links in CATEGORIES.items():
        st.markdown(f'<div class="category-header">{cat_name}</div>', unsafe_allow_html=True)
        cols = st.columns(3)
        for idx, item in enumerate(links):
            with cols[idx % 3]:
                st.link_button(f"{item['icon']} {item['name']}", item['url'], use_container_width=True)

    st.markdown("---")
    st.caption("© 2025 IsuruSoft Web Solutions")
