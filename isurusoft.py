import streamlit as st
import random
import string

# පිටුවේ මූලික සැකසුම්
st.set_page_config(page_title="IsuruSoft Web Dictionary", page_icon="📖", layout="wide")

# Session State එක හරහා දත්ත සහ Login තත්ත්වය පවත්වා ගැනීම
if 'users' not in st.session_state:
    st.session_state['users'] = {"admin@isurusoft.lk": "1234"} # උදාහරණයක් ලෙස පවතින ගිණුමක්
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# --- CSS Styling ---
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; }
    .link-card {
        padding: 20px;
        background-color: #1e293b;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #38bdf8;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MAIN APP LOGIC ---

if not st.session_state['logged_in']:
    # --- LOGIN & REGISTRATION SECTION ---
    st.markdown("<h1 style='text-align: center; color: #00d4ff;'>IsuruSoft Web Dictionary</h1>", unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["📝 Registration", "🔑 Login"])

    with tab1:
        st.subheader("නව ගිණුමක් සාදාගන්න")
        reg_name = st.text_input("ඔබේ නම", key="reg_n")
        if st.button("Generate Account"):
            email = f"{reg_name.lower().replace(' ', '')}{random.randint(100, 999)}@isurusoft.lk"
            password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))
            st.session_state['users'][email] = password
            st.success("ගිණුම නිපදවන ලදී!")
            st.code(f"Email: {email}\nPassword: {password}")

    with tab2:
        st.subheader("Login to your account")
        u_email = st.text_input("Email")
        u_pass = st.text_input("Password", type="password")
        if st.button("Login"):
            if u_email in st.session_state['users'] and st.session_state['users'][u_email] == u_pass:
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("විස්තර වැරදියි, කරුණාකර නැවත උත්සාහ කරන්න.")

else:
    # --- DASHBOARD SECTION (After Login) ---
    st.sidebar.button("Logout", on_click=lambda: st.session_state.update({"logged_in": False}))
    st.markdown(f"<h2 style='color: #4ade80;'>සාදරයෙන් පිළිගන්නවා, {st.session_state.get('reg_n', 'User')}!</h2>", unsafe_allow_html=True)
    st.write("පහත බොත්තම් මගින් අදාළ වෙබ් පිටු වෙත පිවිසෙන්න:")

    # ඔබ එවූ ලේඛනයේ තිබූ ලින්ක්ස් (උදාහරණ ලෙස)
    links = {
        "1": "https://www.facebook.com",  # මෙතනට ඔබ එවූ ලේඛනයේ ලින්ක් ඇතුළත් කරන්න
        "2": "https://www.google.com",
        "3": "https://github.com",
        "4": "https://isurusoft.lk"
    }

    # බොත්තම් පේළියට සැකසීම (Columns)
    cols = st.columns(len(links))
    
    for i, (num, url) in enumerate(links.items()):
        with cols[i]:
            st.markdown(f'<div class="link-card"><h3>Page {num}</h3></div>', unsafe_allow_html=True)
            st.link_button(f"Visit Link {num}", url)

    st.info("සටහන: ඔබට අවශ්‍ය ලින්ක් ප්‍රමාණය අනුව මෙම බොත්තම් ස්වයංක්‍රීයව සැකසේ.")
