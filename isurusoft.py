import streamlit as st

st.set_page_config(page_title="සවුත් විෂන් වෙබ් තක්සලාව", page_icon="🎓", layout="wide")

USERS = {"isurusoft": "123456"}

if 'is_logged_in' not in st.session_state:
    st.session_state['is_logged_in'] = False

st.markdown("""
<style>
    .stApp { background-color: #0f172a; }
    .img-container img { width: 100%; border-radius: 10px; pointer-events: none; }
    div[data-testid="stTextInput"] label { display: none !important; }
    .login-box { background: #1e293b; padding: 25px; border-radius: 15px; border: 1px solid #334155; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
    .main-title { text-align: center; color: #ff0000 !important; font-size: 32px; font-weight: 800; margin-bottom: 25px; text-shadow: 1px 1px 2px #000000; }
    .get-member { margin-top: 15px; padding-top: 15px; border-top: 1px solid #334155; text-align: center; }
    .pay-link { color: #28a745 !important; font-weight: bold; text-decoration: none; font-size: 15px; border: 1px solid #28a745; padding: 5px 10px; border-radius: 5px; display: inline-block; }
    .support-text { color: #ffffff; background-color: #ff0000; padding: 10px; border-radius: 5px; text-align: center; font-weight: bold; margin-bottom: 10px; }
    .info-card { background: #1e293b; padding: 15px; border-radius: 10px; border-left: 4px solid #facc15; margin-top: 10px; color: #cbd5e1; font-size: 14px; }
</style>
""", unsafe_allow_html=True)

if not st.session_state['is_logged_in']:
    st.markdown('<h1 class="main-title">සවුත් විෂන් වෙබ් තක්සලාව</h1>', unsafe_allow_html=True)
    col1, col2 = st.columns([1.3, 1], gap="medium")
    with col1:
        st.markdown('<div class="img-container"><img src="https://raw.githubusercontent.com/isurukihanduwage8804/isurusoft/main/2.png"></div>', unsafe_allow_html=True)
        st.markdown('<div class="info-card"><h4 style="color:#facc15; margin-top:0;">🌟 අපේ පෝටල් එකේ විශේෂත්වය</h4><p>අධ්‍යාපනික මෙවලම් 30කට අධික ප්‍රමාණයක් මෙහි ඇතුළත් වේ.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.markdown('<h3 style="color:#facc15; text-align:center; margin:0 0 10px 0;">Member Login</h3>', unsafe_allow_html=True)
        u = st.text_input("User Name", key="u_name", placeholder="User Name")
        p = st.text_input("Password", type="password", key="p_word", placeholder="Password")
        if st.button("LOGIN NOW", use_container_width=True):
            if u in USERS and USERS[u] == p:
                st.session_state['is_logged_in'] = True
                st.rerun()
            else: st.error("වැරදියි!")
        st.markdown('<div class="get-member"><a href="https://wa.me/94750211899" class="pay-link">GET MEMBERSHIP</a></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.sidebar.markdown('<div class="support-text">📞 Support: 075 021 1899</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">සවුත් විෂන් වෙබ් තක්සලාව</h1>', unsafe_allow_html=True)
    if st.sidebar.button("LOGOUT", use_container_width=True):
        st.session_state['is_logged_in'] = False
        st.rerun()
    
    sq_url = "https://car-game-new-ejck93xsrn5wnyfedccxpa.streamlit.app/"
    
    CAT = {
        "🔢 ගණිතය සහ විද්‍යාව": [
            {"n": "Square Racer", "u": sq_url, "i": "🏎️"},
            {"n": "Geometry Dance", "u": "https://shape-aria-m2uzeyna2bdyfdx3xktdgv.streamlit.app/", "i": "📐"},
            {"n": "Graph Art 2", "u": "https://nicegrap2.streamlit.app/", "i": "🎨"},
            {"n": "Periodic Table", "u": "https://prtable.streamlit.app/", "i": "🧪"},
            {"n": "Angle Shape", "u": "https://angaleshape.streamlit.app/", "i": "📐"},
            {"n": "Atom Animation", "u": "https://atomanimation.streamlit.app/", "i": "⚛️"},
            {"n": "Grade 5 Maths", "u": "https://grade5maths.streamlit.app/", "i": "🔢"},
            {"n": "Graph 1", "u": "https://graph-1-4e7bbfbpkg9aw5uvxp9yc6.streamlit.app/", "i": "📊"},
            {"n": "Maths 680", "u": "https://grade-5-maths-680-ad749ecycarfizcfkyspir.streamlit.app/", "i": "🎓"},
            {"n": "Grade 4 Maths Master", "u": "https://grade4maths-mfu74gfzjqfwydpcyeonqi.streamlit.app/", "i": "🏫"}
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
            {"n": "අකුරු බෝල - සිංහල", "u": "https://akuru-ekka-sellam-hcztw5jdbido2yfqpkgnm8.streamlit.app/", "i": "🎈"},
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
            {"n": "විද්‍යාඥයින් කවුද?", "u": "https://sciencetist-question-hknjybq5xxdcmrhcjahqol.streamlit.app/", "i": "🔬"},
            {"n": "ශාක පත්‍ර හඳුනාගනිමු", "u": "https://tree-leave-ht45stbbx8sebv2kjeaguz.streamlit.app/", "i": "🍃"}
        ]
    }
    for cat, links in CAT.items():
        st.markdown(f'<div style="background-color: #1e293b; padding: 8px; border-radius: 8px; color: #facc15; font-weight: bold; margin-top: 20px; border-left: 5px solid #ff0000;">{cat}</div>', unsafe_allow_html=True)
        cols = st.columns(3)
        for i, itm in enumerate(links):
            with cols[i % 3]: st.link_button(f"{itm['i']} {itm['n']}", itm['u'], use_container_width=True)
    st.markdown("---")
    st.markdown("<center>© 2026 South Vision</center>", unsafe_allow_html=True)
