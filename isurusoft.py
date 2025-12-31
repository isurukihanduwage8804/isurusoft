import streamlit as st
import random
import string

# පිටුවේ මූලික සැකසුම්
st.set_page_config(page_title="IsuruSoft Web Dictionary", page_icon="📖")

# දත්ත තාවකාලිකව මතකයේ තබා ගැනීමට (Session State)
if 'users' not in st.session_state:
    st.session_state['users'] = {} # {email: password} ලෙස ගබඩා වේ

# Header
st.markdown("<h1 style='text-align: center; color: #00d4ff;'>IsuruSoft Web Dictionary</h1>", unsafe_allow_html=True)

# Tabs දෙකක් සෑදීම
tab1, tab2 = st.tabs(["📝 Registration", "🔑 Login"])

# --- REGISTRATION TAB ---
with tab1:
    st.subheader("නව ගිණුමක් සාදාගන්න")
    name = st.text_input("ඔබේ නම ඇතුළත් කරන්න", key="reg_name")
    
    if st.button("ගිණුම නිර්මාණය කරන්න"):
        if name:
            # Auto Generation
            email = f"{name.lower().replace(' ', '')}{random.randint(100, 999)}@isurusoft.lk"
            password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))
            
            # Session State එකේ දත්ත ගබඩා කිරීම
            st.session_state['users'][email] = password
            
            st.success("ලියාපදිංචිය සාර්ථකයි!")
            st.info(f"ඔබේ ලොගින් තොරතුරු පහතින් බලන්න:")
            st.code(f"Email: {email}\nPassword: {password}")
        else:
            st.warning("කරුණාකර නමක් ඇතුළත් කරන්න.")

# --- LOGIN TAB (මෙන්න ඔබට අවශ්‍ය කොටස) ---
with tab2:
    st.subheader("පද්ධතියට ඇතුළු වන්න")
    login_email = st.text_input("Email ලිපිනය", placeholder="example@isurusoft.lk")
    login_password = st.text_input("මුරපදය (Password)", type="password")
    
    if st.button("Login"):
        # දත්ත පරීක්ෂා කිරීම
        if login_email in st.session_state['users']:
            if st.session_state['users'][login_email] == login_password:
                st.balloons()
                st.success(f"සාදරයෙන් පිළිගන්නවා! ඔබ සාර්ථකව IsuruSoft පද්ධතියට ඇතුළු වුණා.")
            else:
                st.error("වැරදි මුරපදයක්. කරුණාකර නැවත උත්සාහ කරන්න.")
        else:
            st.error("මෙම Email ලිපිනය පද්ධතියේ නැත. කරුණාකර ලියාපදිංචි වන්න.")

# Footer
st.markdown("---")
st.caption("© 2025 IsuruSoft Web Solutions")
