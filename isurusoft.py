import streamlit as st

# 1. පිටුවේ මූලික සැකසුම්
st.set_page_config(page_title="සවුත් විෂන් වෙබ් තක්සලාව", page_icon="🎓", layout="wide")

# යූසර්ලා
USERS = {"isurusoft": "123456"}

if 'is_logged_in' not in st.session_state:
    st.session_state['is_logged_in'] = False

# CSS Styles
st.markdown("""
<style>
    .stApp { background-color: #0f172a; }
    .login-box { background: #1e293b; padding: 25px; border-radius: 15px; border: 1px solid #334155; }
    .main-title { text-align: center; color: #ff0000 !important; font-size: 30px; font-weight: 800; }
    .info-card { background: #1e293b; padding: 15px; border-radius: 10px; border-left: 4px solid #facc15; color: #cbd5e1; }
</style>
""", unsafe_allow_html=True)

# 1. LOGIN SECTION
if not st.session_state['is_logged_in']:
    st.markdown('<h1 class="main-title">සවුත් විෂන් වෙබ් තක්සලාව</h1>', unsafe_allow_html=True)
    c1, c2 = st.columns([1.3, 1])
    with c1:
        st.image("https://raw.githubusercontent.com/isurukihanduwage8804/isurusoft/main/2.png")
        st.markdown('<div class="info-card"><h4>🌟 විශේෂත්වය</h4><p>අධ්‍යාපනික මෙවලම් 30+ මෙහි ඇත.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        u = st.text_input("User Name", placeholder="User Name")
        p = st.text_input("Password", type="password", placeholder="Password")
        if st.button("LOGIN NOW", use_container_width=True):
            if u in USERS and USERS[u] == p:
                st.session_state['is_logged_in'] = True
                st.rerun()
            else: st.error("වැරදියි!")
        st.markdown('</div>', unsafe_allow_html=True)

# 2. MAIN HUB SECTION
else:
    st.sidebar.write("📞 Support: 075 021 1899")
    st.markdown('<h1 class="main-title">සවුත් විෂන් වෙබ් තක්සලාව</h1>', unsafe_allow_html=True)
    if st.sidebar.button("LOGOUT"):
        st.session_state['is_logged_in'] = False
        st.rerun()

    sq_url = "https://car-game-new-ejck93xsrn5wnyfedccxpa.streamlit.app/"
    
    CAT = {
        "🔢 ගණිතය සහ විද්‍යාව": [
            {"n": "Square Racer", "u": sq_url, "i": "🏎️"},
            {"n": "Geometry Dance", "u": "https://shape-aria-m2uzeyna2bdyfdx3xktdgv.streamlit.app/", "i": "📐"},
            {"n": "Periodic Table", "u": "https://prtable.streamlit.app/", "i": "🧪"},
            {"n": "Grade 5 Maths", "u": "https://grade5maths.streamlit.app/", "i": "🔢"}
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

    for cat_name, links in CAT.items():
        st.markdown(f'<div style="color: #facc15; font-weight: bold; margin-top: 20px;">{cat_name}</div>', unsafe_allow_html=True)
        cols = st.columns(3)
        for i, item in enumerate(links):
            with cols[i % 3]:
                st.link_button(f"{item['i']} {item['n']}", item['u'], use_container_width=True)

    st.markdown("<br><center>© 2026 South Vision</center>", unsafe_allow_html=True)
