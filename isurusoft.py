import streamlit as st
import random

# 1. පිටුවේ මූලික සැකසුම්
st.set_page_config(page_title="සවුත් විෂන් වෙබ් තක්සලාව", page_icon="🎓", layout="wide")

# --- Session State ---
if 'view_count' not in st.session_state:
    st.session_state['view_count'] = 50240 
if 'counted' not in st.session_state:
    st.session_state['view_count'] += random.randint(15, 60)
    st.session_state['counted'] = True
if 'is_logged_in' not in st.session_state:
    st.session_state['is_logged_in'] = False

# --- CSS Styling (Layout එක හරියටම පෙනෙන විදිහට) ---
st.markdown("""
<style>
    .stApp { background-color: #0f172a; }
    
    .main-title { 
        text-align: center; 
        color: #ff0000 !important; 
        font-size: 26px; 
        font-weight: 800; 
        margin-bottom: 10px;
        text-shadow: 1px 1px 2px #000000;
    }
    
    input { color: #000000 !important; }
    
    .login-container { 
        background: #1e293b; 
        padding: 20px; 
        border-radius: 12px; 
        border: 1px solid #334155;
    }
    
    .support-text {
        color: #ffffff;
        background-color: #ff0000;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        font-weight: bold;
        font-size: 15px;
        margin-bottom: 10px;
    }

    .category-header { 
        background-color: #1e293b; 
        padding: 8px 15px; 
        border-radius: 8px; 
        color: #facc15; 
        font-size: 17px; 
        font-weight: bold; 
        margin-top: 20px; 
        border-left: 5px solid #ff0000; 
    }

    /* අනවශ්‍ය ඉඩවල් ඉවත් කිරීම */
    [data-testid="stVerticalBlock"] { gap: 0.2rem; }
    .block-container { padding-top: 2rem; }

    button[title="View fullscreen"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

# 1. LOGIN SECTION (පින්තූරය වම් පැත්තේ සහ Login දකුණු පැත්තේ)
if not st.session_state['is_logged_in']:
    st.markdown('<h1 class="main-title">සවුත් විෂන් වෙබ් තක්සලාව</h1>', unsafe_allow_html=True)
    
    # 60% වමට සහ 40% දකුණට බෙදීම
    col1, col2 = st.columns([1.2, 1], gap="medium")
    
    with col1:
        # වම් පැත්තේ පින්තූරය (2.png)
        st.image("https://raw.githubusercontent.com/isurukihanduwage8804/isurusoft/main/2.png", use_container_width=True)
        
    with col2:
        # දකුණු පැත්තේ Customer Support
        st.markdown('<div class="support-text">📞 Customer Support: 0766 770 856</div>', unsafe_allow_html=True)
        
        # Login Box
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.markdown('<p style="color:#facc15; font-weight:bold; margin-bottom:5px;">Login to Your Account</p>', unsafe_allow_html=True)
        
        # Form එකක් ලෙස භාවිතයෙන් අනවශ්‍ය කොටු ඉවත් කිරීම
        with st.form("login_form", clear_on_submit=False):
            u = st.text_input("User Name", placeholder="Username", label_visibility="collapsed")
            p = st.text_input("Password", type="password", placeholder="Password", label_visibility="collapsed")
            submit = st.form_submit_button("LOGIN", use_container_width=True)
            
            if submit:
                if u == "isurusoft" and p == "123456":
                    st.session_state['is_logged_in'] = True
                    st.rerun()
                else:
                    st.error("Login තොරතුරු වැරදියි!")
        st.markdown('</div>', unsafe_allow_html=True)

# 2. MAIN HUB SECTION (Logged In)
else:
    st.sidebar.markdown('<div class="support-text">📞 Support: 0766 770 856</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">සවුත් විෂන් වෙබ් තක්සලාව</h1>', unsafe_allow_html=True)
    
    st.sidebar.markdown(f'<h2 style="color:#facc15; text-align:center;">VIEWS: {st.session_state["view_count"]:,}</h2>', unsafe_allow_html=True)
    if st.sidebar.button("LOGOUT", use_container_width=True):
        st.session_state['is_logged_in'] = False
        st.rerun()

    quiz_url = "https://sciencetist-question-hknjybq5xxdcmrhcjahqol.streamlit.app/"

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
            {"n": "BMI Manager", "u": "https://bmimannew.streamlit.
