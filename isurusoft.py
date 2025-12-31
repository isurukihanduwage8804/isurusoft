import streamlit as st
import random
import string
import time

# පිටුවේ සැකසුම්
st.set_page_config(page_title="IsuruSoft Web Dictionary", page_icon="📖", layout="centered")

# --- CSS මගින් පෙනුම වෙනස් කිරීම ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .header-text {
        font-size: 45px;
        font-weight: bold;
        color: #00d4ff;
        text-align: center;
        margin-bottom: 5px;
        text-shadow: 2px 2px 4px #000000;
    }
    .sub-text {
        font-size: 18px;
        color: #94a3b8;
        text-align: center;
        margin-bottom: 30px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background: linear-gradient(45deg, #007bff, #00d4ff);
        color: white;
        border: none;
        padding: 10px;
        font-size: 18px;
    }
    .login-card {
        background-color: #1e293b;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #00d4ff;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header කොටස ---
st.markdown('<p class="header-text">IsuruSoft Web Dictionary</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">ස්වයංක්‍රීය ලියාපදිංචි පද්ධතිය</p>', unsafe_allow_html=True)

# --- Function to generate credentials ---
def create_user(full_name):
    # Email සාදා ගැනීම
    clean_name = full_name.lower().replace(" ", "")
    user_email = f"{clean_name}{random.randint(100, 999)}@isurusoft.lk"
    
    # ආරක්ෂිත මුරපදයක් සාදා ගැනීම
    chars = string.ascii_letters + string.digits + "@#$*"
    user_password = ''.join(random.choice(chars) for i in range(10))
    
    return user_email, user_password

# --- UI එක ---
with st.container():
    name = st.text_input("ඔබේ නම ඇතුළත් කරන්න", placeholder="උදා: Isuru Perera")
    
    if st.button("ගිණුම නිර්මාණය කරන්න"):
        if name:
            with st.spinner('දත්ත සකසමින් පවතී...'):
                time.sleep(1)
                email, password = create_user(name)
                
                st.balloons()
                
                # තොරතුරු පෙන්වන Card එක
                st.markdown(f"""
                <div class="login-card">
                    <h3 style='color: #ffffff; margin-top: 0;'>🎉 සාර්ථකයි! ඔබේ ගිණුම සූදානම්.</h3>
                    <p style='color: #cbd5e1;'>මෙම දත්ත භාවිතා කර <b>IsuruSoft Dictionary</b> වෙත පිවිසෙන්න.</p>
                    <hr style='border: 0.5px solid #334155;'>
                    <p style='font-size: 18px;'>📧 <b>Email:</b> <code>{email}</code></p>
                    <p style='font-size: 18px;'>🔑 <b>Password:</b> <code>{password}</code></p>
                </div>
                """, unsafe_allow_html=True)
                
                # Copy කරගැනීමට පහසුවට
                st.write("")
                st.code(f"User: {email}\nPass: {password}")
        else:
            st.error("කරුණාකර වලංගු නමක් ඇතුළත් කරන්න.")

# Footer
st.markdown("<br><p style='text-align: center; color: #475569;'>© 2025 IsuruSoft Web Solutions</p>", unsafe_allow_html=True)
