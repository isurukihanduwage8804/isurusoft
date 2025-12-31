import streamlit as st
import random
import string

# 1. පිටුවේ මූලික සැකසුම්
st.set_page_config(page_title="IsuruSoft Web Dictionary", page_icon="📖", layout="wide")

# [cite_start]2. ඔබ එවූ ලින්ක් 23 ම මෙහි අඩංගු වේ [cite: 1]
LINKS_DATA = [
    "https://nicegrap2.streamlit.app/",
    "https://isurusoft.streamlit.app/",
    "https://3dappbest.streamlit.app/",
    "https://prtable.streamlit.app/",
    "https://bmimannew.streamlit.app/#8b1d9de1",
    "https://rachana-2new.streamlit.app/",
    "https://angaleshape.streamlit.app/",
    "https://atomanimation.streamlit.app/",
    "https://grade5maths.streamlit.app/",
    "https://grade5sinhalanew.streamlit.app/",
    "https://sankyadadayamanew2.streamlit.app/",
    "https://mathspuzzle1.streamlit.app/",
    "https://real-puzzle-1-csyvarjphxh9z9tndnj4ff.streamlit.app/",
    "https://anser-to-ques2-c9yurtmondfbzjcpoxguwn.streamlit.app/",
    "https://therawili-gzggdyxieygqhaifx6jp8k.streamlit.app/",
    "https://graph-1-4e7bbfbpkg9aw5uvxp9yc6.streamlit.app/",
    "https://mony-converter-zhtsej33cdvttrtwqhle4q.streamlit.app/",
    "https://word-meaning-ndkg9veahhahsqweqimcrz.streamlit.app/",
    "https://shape-converter-fkun3v4m8gx4dyjqkfmt5t.streamlit.app/",
    "https://4-box-game-95ri7jjkakjyjhzgrhfmgc.streamlit.app/",
    "https://tetrics-maths-pawkf7v2qvh52ze8jsqtxn.streamlit.app/",
    "https://budda-darmaya-1.streamlit.app/",
    "https://grade-5-maths-680-ad749ecycarfizcfkyspir.streamlit.app/"
]

# Session State පවත්වා ගැනීම
if 'users' not in st.session_state:
    st.session_state['users'] = {}
if 'is_logged_in' not in st.session_state:
    st.session_state['is_logged_in'] = False

# 3. CSS Styling (Error එක නිවැරදි කර ඇත)
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; }
    .stButton>button { 
        width: 100%; 
        border-radius: 10px; 
        background: linear-gradient(45deg, #0284c7, #0ea5e9); 
        color: white; 
        font-weight: bold; 
        border: none;
    }
    .link-card {
        padding: 15px;
        background-color: #1e293b;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #334155;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. Login & Registration Logic
if not st.session_state['is_logged_in']:
    st.markdown("<h1 style='text-align: center; color: #38bdf8;'>IsuruSoft Web Dictionary</h1>", unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["📝 Register", "🔑 Login"])

    with tab1:
        reg_name = st.text_input("ඔබේ නම ඇතුළත් කරන්න")
        if st.button("ගිණුමක් සාදන්න"):
            if reg_name:
                email = f"{reg_name.lower().replace(' ', '')}{random.randint(100, 999)}@isurusoft.lk"
                password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
                st.session_state['users'][email] = password
                st.success("සාර්ථකයි!")
                st.code(f"Email: {email}\nPassword: {password}")

    with tab2:
        u_email = st.text_input("Email")
        u_pass = st.text_input("Password", type="password")
        if st.button("Login"):
            if u_email in st.session_state['users'] and st.session_state['users'][u_email] == u_pass:
                st.session_state['is_logged_in'] = True
                st.rerun()
            else:
                st.error("විස්තර වැරදියි!")

# 5. Dashboard (පරිශීලකයා ලොග් වූ පසු)
else:
    st.markdown("<h1 style='text-align: center; color: #4ade80;'>IsuruSoft Dashboard</h1>", unsafe_allow_html=True)
    if st.sidebar.button("Logout"):
        st.session_state['is_logged_in'] = False
        st.rerun()
    
    st.write("පහත සේවාවන් වෙත පිවිසීමට අදාළ බොත්තම ඔබන්න:")
    st.markdown("---")

    # බොත්තම් 23 ම පෙන්වීම
    cols_per_row = 3
    for i in range(0, len(LINKS_DATA), cols_per_row):
        cols = st.columns(cols_per_row)
        for j in range(cols_per_row):
            index = i + j
            if index < len(LINKS_DATA):
                with cols[j]:
                    st.markdown(f'<div class="link-card"><b>Service {index + 1}</b></div>', unsafe_allow_html=True)
                    st.link_button(f"🌐 Open Page {index + 1}", LINKS_DATA[index])
