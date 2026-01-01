import streamlit as st
import random

# 1. පිටුවේ මූලික සැකසුම්
st.set_page_config(page_title="සවුත් විෂන් වෙබ් තක්සලාව", page_icon="🎓", layout="wide")

# =========================================================
# යූසර්ලා කළමනාකරණය
# =========================================================
USERS = {
    "isurusoft": "123456",
}

# --- Session State ---
if 'view_count' not in st.session_state:
    st.session_state['view_count'] = 50240 
if 'counted' not in st.session_state:
    st.session_state['view_count'] += random.randint(15, 60)
    st.session_state['counted'] = True
if 'is_logged_in' not in st.session_state:
    st.session_state['is_logged_in'] = False

# --- CSS Styling ---
st.markdown("""
<style>
    .stApp { background-color: #0f172a; }
    .main-title { 
        text-align: center; color: #ff0000 !important; font-size: 32px; 
        font-weight: 800; margin-bottom: 30px; text-shadow: 1px 1px 2px #000000;
    }
    .login-box {
        background: #1e293b; padding: 25px; border-radius: 15px; 
        border: 1px solid #334155; box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .price-card {
        background: #1e293b; padding: 15px; border-radius: 12px; 
        border: 1px solid #facc15; text-align: center; margin-top: 20px;
    }
    .pay-btn-flat {
        background-color: #28a745; color: white !important;
        padding: 8px 15px; border-radius: 5px; text-decoration: none;
        font-weight: bold; display: block; width: 100%; margin-top: 10px;
        font-size: 16px; text-align: center;
    }
    .support-text {
        color: #ffffff; background-color: #ff0000; padding: 10px;
        border-radius: 5px; text-align: center; font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# 1. LOGIN SECTION
if not st.session_state['is_logged_in']:
    st.markdown('<h1 class="main-title">සවුත් විෂන් වෙබ් තක්සලාව</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.2, 1], gap="large")
    
    with col1:
        st.image("https://raw.githubusercontent.com/isurukihanduwage8804/isurusoft/main/2.png", use_container_width=True)
        
    with col2:
        # Login Box
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.markdown('<h3 style="color:#facc15; text-align:center; margin:0 0 15px 0;">Member Login</h3>', unsafe_allow_html=True)
        u = st.text_input("User Name", key="u_name")
        p = st.text_input("Password", type="password", key="p_word")
        if st.button("LOGIN NOW", use_container_width=True):
            if u in USERS and USERS[u] == p:
                st.session_state['is_logged_in'] = True
                st.rerun()
            else:
                st.error("නම හෝ මුද්‍රාපදය වැරදියි!")
        st.markdown('</div>', unsafe_allow_html=True)

        # Membership Section
        st.markdown(f'''
            <div class="price-card">
                <p style="color:#ffffff; margin:0; font-weight:bold; font-size:14px;">💎 LIFETIME ACCESS - Rs. 1,000/=</p>
                <a href="https://wa.me/94750211899?text=I%20want%20to%20get%20South%20Vision%20Membership" class="pay-btn-flat">
                    GET MEMBERSHIP NOW
                </a>
                <p style="color:#94a3b8; font-size:11px; margin-top:8px;">සියලුම ක්‍රීඩා සහ පාඩම් සඳහා ජීවිත කාලයටම ප්‍රවේශය.</p>
            </div>
        ''', unsafe_allow_html=True)

# 2. MAIN HUB SECTION
else:
    st.sidebar.markdown('<div class="support-text">📞 Support: 075 021 1899</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">සවුත් විෂන් වෙබ් තක්සලාව</h1>', unsafe_allow_html=True)
    
    st.sidebar.markdown(f'<h2 style="color:#facc15; text-align:center;">VIEWS: {st.session_state["view_count"]:,}</h2>', unsafe_allow_html=True)
    if st.sidebar.button("LOGOUT", use_container_width=True):
        st.session_state['is_logged_in'] = False
        st.rerun()

    quiz_url = "https://sciencetist-question-hknjybq5xxdcmrhcjahqol.streamlit.app/"

    # --- CATEGORIES (All links fixed) ---
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
        st.markdown(f'<div style="background-color: #1e293b; padding: 8px 15px; border-radius: 8px; color: #facc15; font-size: 17px; font-weight: bold; margin-top: 20px; border-left: 5px solid #ff0000;">{cat_name}</div>', unsafe_allow_html=True)
        cols = st.columns(3)
        for i, item in enumerate(links):
            with cols[i % 3]:
                st.link_button(f"{item['i']} {item['n']}", item['u'], use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #64748b; font-size: 13px;'>
        © 2026 <b>South Vision Web Solutions</b><br>
        Hotline: 075 021 1899
    </div>
""", unsafe_allow_html=True)
