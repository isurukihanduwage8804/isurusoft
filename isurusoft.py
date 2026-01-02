import streamlit as st

# 1. පිටුවේ මූලික සැකසුම්
st.set_page_config(page_title="සවුත් විෂන් වෙබ් තක්සලාව", page_icon="🎓", layout="wide")

# =========================================================
# යූසර්ලා කළමනාකරණය
# =========================================================
USERS = {
    "isurusoft": "123456",
}

# --- Session State ---
if 'is_logged_in' not in st.session_state:
    st.session_state['is_logged_in'] = False

# --- CSS Styling ---
st.markdown("""
<style>
    .stApp { background-color: #0f172a; }

    /* පින්තූරයේ පෙනුම */
    .img-container img {
        width: 100%;
        border-radius: 10px;
        pointer-events: none;
    }

    /* ලේබල් සඳහා වෙන්වන හිස් ඉඩ අයින් කිරීම */
    div[data-testid="stTextInput"] label {
        display: none !important;
    }
    
    div[data-testid="stTextInput"] div[data-baseweb="input"] {
        margin-top: -15px;
    }

    /* ලොගින් කොටුවේ පෙනුම */
    .login-box {
        background: #1e293b; 
        padding: 25px; 
        border-radius: 15px; 
        border: 1px solid #334155; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }

    .main-title { 
        text-align: center; color: #ff0000 !important; font-size: 32px; 
        font-weight: 800; margin-bottom: 25px; text-shadow: 1px 1px 2px #000000;
    }

    .get-member {
        margin-top: 15px; padding-top: 15px; border-top: 1px solid #334155;
        text-align: center;
    }
    
    .pay-link {
        color: #28a745 !important; font-weight: bold; text-decoration: none;
        font-size: 15px; border: 1px solid #28a745; padding: 5px 10px;
        border-radius: 5px; display: inline-block; margin-top: 5px;
    }

    .support-text {
        color: #ffffff; background-color: #ff0000; padding: 10px;
        border-radius: 5px; text-align: center; font-weight: bold;
        margin-bottom: 10px;
    }

    .info-card {
        background: #1e293b;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #facc15;
        margin-top: 10px;
        color: #cbd5e1;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# 1. LOGIN SECTION
if not st.session_state['is_logged_in']:
    st.markdown('<h1 class="main-title">සවුත් විෂන් වෙබ් තක්සලාව</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.3, 1], gap="medium")
    
    with col1:
        st.markdown('<div class="img-container"><img src="https://raw.githubusercontent.com/isurukihanduwage8804/isurusoft/main/2.png"></div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <h4 style="color:#facc15; margin-top:0;">🌟 අපේ පෝටල් එකේ විශේෂත්වය</h4>
            <p>අධ්‍යාපනික මෙවලම් 30කට අධික ප්‍රමාණයක් මෙහි ඇතුළත් වේ. 
            ගණිතය, විද්‍යාව සහ භාෂා දැනුම වර්ධනය කරන Interactive Games හරහා ඉගෙනීම විනෝදයක් බවට පත් කරමු.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.markdown('<h3 style="color:#facc15; text-align:center; margin:0 0 10px 0; border:none;">Member Login</h3>', unsafe_allow_html=True)
        
        u = st.text_input("User Name", key="u_name", placeholder="User Name", label_visibility="collapsed")
        st.write("") 
        p = st.text_input("Password", type="password", key="p_word", placeholder="Password", label_visibility="collapsed")
        
        if st.button("LOGIN NOW", use_container_width=True):
            if u in USERS and USERS[u] == p:
                st.session_state['is_logged_in'] = True
                st.rerun()
            else:
                st.error("නම හෝ මුද්‍රාපදය වැරදියි!")
        
        st.markdown(f'''
            <div class="get-member">
                <p style="color:#cbd5e1; font-size:12px; margin-bottom:5px;">Don't have an account?</p>
                <p style="color:#ffffff; font-weight:bold; margin-bottom:10px; font-size:14px;">LIFETIME ACCESS - Rs. 1,000/=</p>
                <a href="https://wa.me/94750211899?text=I%20want%20to%20get%20South%20Vision%20Membership" class="pay-link">
                    GET MEMBERSHIP
                </a>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# 2. MAIN HUB SECTION
else:
    st.sidebar.markdown('<div class="support-text">📞 Support: 075 021 1899</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">සවුත් විෂන් වෙබ් තක්සලාව</h1>', unsafe_allow_html=True)
    
    st.sidebar.markdown('<div style="text-align:center; color:#28a745; font-weight:bold; border:1px solid #28a745; padding:5px; border-radius:5px;">✅ Verified Account</div>', unsafe_allow_html=True)
    st.sidebar.write("")
    
    if st.sidebar.button("LOGOUT", use_container_width=True):
        st.session_state['is_logged_in'] = False
        st.rerun()

    # ලින්ක් එකතු කිරීම
    sci_quiz_url = "https://sciencetist-question-hknjybq5xxdcmrhcjahqol.streamlit.app/"
    tree_quiz_url = "https://tree-leave-ht45stbbx8sebv2kjeaguz.streamlit.app/"
    akuru_bola_url = "https://akuru-ekka-sellam-hcztw5jdbido2yfqpkgnm8.streamlit.app/"
    
    # මෙන්න ඔයා එවපු අලුත්ම ලින්ක් එක
    square_racer_url = "https://car-game-new-ejck93xsrn5wnyfedccxpa.streamlit.app/"

    CATEGORIES = {
        "🔢 ගණිතය සහ විද්‍යාව": [
            {"n": "Square Racer", "u": square_racer_url, "i": "🏎️"},
            {"n": "Geometry Dance", "u": "https://shape-aria-m2uzeyna2bdyfdx3xktdgv.streamlit.app/", "i": "📐"},
            {"n": "Graph Art 2", "u": "https://nicegrap2.streamlit.app/", "i": "🎨"},
            {"n": "Periodic Table", "u": "https://prtable.streamlit.app/", "i": "🧪"},
            {"n": "Angle Shape", "u": "https://angaleshape.streamlit.app/", "i": "📐"},
