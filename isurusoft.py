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
    div[data-testid="stTextInput"] div[data-baseweb="input"] { margin-top: -15px; }
    .login-box { background: #1e293b; padding: 25px; border-radius: 15px; border: 1px solid #334155; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
    .main-title { text-align: center; color: #ff0000 !important; font-size: 32px; font-weight: 800; margin-bottom: 25px; text-shadow: 1px 1px 2px #000000; }
    .get-member { margin-top: 15px; padding-top: 15px; border-top: 1px solid #334155; text-align: center; }
    .pay-link { color: #28a745 !important; font-weight: bold; text-decoration: none; font-size: 15px; border: 1px solid #28a745; padding: 5px 10px; border-radius: 5px; display: inline-block; margin-top: 5px; }
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
            {"n": "Periodic Table", "u": "https://prtable.streamlit.app/", "i": "🧪"}
        ],
        "📚 භාෂාව සහ වෙනත්": [
            {"n": "IsuruSoft Portal", "u": "https://isurusoft.streamlit.app/", "i": "🌐"},
            {"n": "Rachana 2", "u": "https://rachana-2new.streamlit.app/", "i": "✍️"},
            {"n": "Budda Darmaya", "u": "https://budda-darmaya-1.streamlit.app/", "i": "☸️"}
        ],
        "🎮 ක්‍රීඩා": [
            {"n": "Water Fraction", "u": "https://watergame-jr5z9ffafbsutbl67arjz8.streamlit.app/", "i": "🥤"},
            {"n": "Math Combat", "u": "https://sankaya-gatuma-bgypbr5g5w2dofu9emv9xz.streamlit.app/", "i": "⚔️"}
        ]
    }
    for cat, links in CAT.items():
        st.markdown(f'<div style="background-color: #1e293b; padding: 8px; border-radius: 8px; color: #facc15; font-weight: bold; margin-top: 20px; border-left: 5px solid #ff0000;">{cat}</div>', unsafe_allow_html=True)
        cols = st.columns(3)
        for i, item in enumerate(links):
            with cols[i % 3]: st.link_button(f"{item['i']} {item['n']}", item['u'], use_container_width=True)
    st.markdown("---")
    st.markdown("<center>© 2026 South Vision</center>", unsafe_allow_html=True)
