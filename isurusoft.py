import streamlit as st

# 1. පිටුවේ මූලික සැකසුම් සහ නම
st.set_page_config(page_title="ඉසුරු සර්ගේ අධ්‍යාපනික ක්‍රීඩා පුවරුව", page_icon="📖", layout="wide")

# 2. Page View Counter එක සකස් කිරීම
if 'view_count' not in st.session_state:
    st.session_state['view_count'] = 0
st.session_state['view_count'] += 1

# 3. ඔබ ලබාදුන් සියලුම ලින්ක් 23 (පරීක්ෂා කර අවසන්)
LINKS_DATA = [
    {"name": "Graph Art 2", "url": "https://nicegrap2.streamlit.app/", "icon": "🎨"},
    {"name": "IsuruSoft Portal", "url": "https://isurusoft.streamlit.app/", "icon": "🌐"},
    {"name": "3D App Best", "url": "https://3dappbest.streamlit.app/", "icon": "🧊"},
    {"name": "Periodic Table", "url": "https://prtable.streamlit.app/", "icon": "🧪"},
    {"name": "BMI Manager", "url": "https://bmimannew.streamlit.app/#8b1d9de1", "icon": "⚖️"},
    {"name": "Rachana 2", "url": "https://rachana-2new.streamlit.app/", "icon": "✍️"},
    {"name": "Angle Shape", "url": "https://angaleshape.streamlit.app/", "icon": "📐"},
    {"name": "Atom Animation", "url": "https://atomanimation.streamlit.app/", "icon": "⚛️"},
    {"name": "Grade 5 Maths", "url": "https://grade5maths.streamlit.app/", "icon": "🔢"},
    {"name": "Grade 5 Sinhala", "url": "https://grade5sinhalanew.streamlit.app/", "icon": "📚"},
    {"name": "Sankya Dadayama", "url": "https://sankyadadayamanew2.streamlit.app/", "icon": "🎯"},
    {"name": "Maths Puzzle", "url": "https://mathspuzzle1.streamlit.app/", "icon": "🧩"},
    {"name": "Real Puzzle 1", "url": "https://real-puzzle-1-csyvarjphxh9z9tndnj4ff.streamlit.app/", "icon": "🎮"},
    {"name": "Answer to Ques", "url": "https://anser-to-ques2-c9yurtmondfbzjcpoxguwn.streamlit.app/", "icon": "💡"},
    {"name": "Therawili", "url": "https://therawili-gzggdyxieygqhaifx6jp8k.streamlit.app/", "icon": "🕵️"},
    {"name": "Graph 1", "url": "https://graph-1-4e7bbfbpkg9aw5uvxp9yc6.streamlit.app/", "icon": "📊"},
    {"name": "Money Converter", "url": "https://mony-converter-zhtsej33cdvttrtwqhle4q.streamlit.app/", "icon": "💱"},
    {"name": "Word Meaning", "url": "https://word-meaning-ndkg9veahhahsqweqimcrz.streamlit.app/", "icon": "📖"},
    {"name": "Shape Converter", "url": "https://shape-converter-fkun3v4m8gx4dyjqkfmt5t.streamlit.app/", "icon": "🔄"},
    {"name": "4 Box Game", "url": "https://4-box-game-95ri7jjkakjyjhzgrhfmgc.streamlit.app/", "icon": "📦"},
    {"name": "Tetris Maths", "url": "https://tetrics-maths-pawkf7v2qvh52ze8jsqtxn.streamlit.app/", "icon": "🕹️"},
    {"name": "Budda Darmaya", "url": "https://budda-darmaya-1.streamlit.app/", "icon": "☸️"},
    {"name": "Maths 680", "url": "https://grade-5-maths-680-ad749ecycarfizcfkyspir.streamlit.app/", "icon": "🎓"}
]

# 4. Login තත්ත්වය පරීක්ෂා කිරීම
if 'is_logged_in' not in st.session_state:
    st.session_state['is_logged_in'] = False

# 5. CSS Styling (වර්ණ සහ UI)
st.markdown("""
<style>
    .stApp { background-color: #0f172a; }
    
    /* රතු පැහැති මාතෘකාව */
    .red-title {
        text-align: center; 
        color: #FF0000 !important; 
        font-size: 42px !important; 
        font-weight: bold !important;
        text-shadow: 2px 2px 4px #000;
        margin-bottom: 25px;
        display: block;
    }

    /* කහ පැහැති ලේබල් */
    .yellow-text {
        color: #facc15 !important; 
        font-weight: bold; 
        font-size: 1.1rem;
        margin-bottom: 5px;
    }

    /* බොත්තම් (Buttons) */
    .stButton>button { 
        width: 100%; border-radius: 12px; 
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%); 
        color: #38bdf8; font-weight: bold; border: 1px solid #334155; height: 4em;
        transition: 0.3s;
    }
    .stButton>button:hover {
        border-color: #38bdf8;
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)

# 6. LOGIN SECTION
if not st.session_state['is_logged_in']:
    st.markdown('<div class="red-title">ඉසුරු සර්ගේ අධ්‍යාපනික ක්‍රීඩා පුවරුව</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<p class="yellow-text">පරිශීලක නම (Username)</p>', unsafe_allow_html=True)
        user_input = st.text_input("", key="final_user_in", label_visibility="collapsed")
        
        st.markdown('<p class="yellow-text">මුරපදය (Password)</p>', unsafe_allow_html=True)
        pass_input = st.text_input("", type="password", key="final_pass_in", label_visibility="collapsed")
        
        st.write("") 
        if st.button("ඇතුළු වන්න (Login)"):
            if user_input == "isurusoft" and pass_input == "123456":
                st.session_state['is_logged_in'] = True
                st.rerun()
            else:
                st.error("පරිශීලක නම හෝ මුරපදය වැරදියි!")

# 7. DASHBOARD SECTION (ලොග් වූ පසු)
else:
    st.markdown('<div class="red-title">ඉසුරු සර්ගේ අධ්‍යාපනික ක්‍රීඩා පුවරුව</div>', unsafe_allow_html=True)
    
    # Sidebar එකේ Page Views පෙන්වීම
    st.sidebar.markdown(f'<p class="yellow-text">Page Views: {st.session_state["view_count"]}</p>', unsafe_allow_html=True)
    if st.sidebar.button("Logout"):
        st.session_state['is_logged_in'] = False
        st.rerun()
    
    st.markdown('<p class="yellow-text">ඔබට අවශ්‍ය ක්‍රීඩාව හෝ සේවාව තෝරාගන්න:</p>', unsafe_allow_html=True)
    st.markdown("---")

    # බොත්තම් 23 පේළියට 3 බැගින් ප්‍රදර්ශනය කිරීම
    cols_per_row = 3
    for i in range(0, len(LINKS_DATA), cols_per_row):
        cols = st.columns(cols_per_row)
        for j in range(cols_per_row):
            index = i + j
            if index < len(LINKS_DATA):
                item = LINKS_DATA[index]
                with cols[j]:
                    st.link_button(f"{item['icon']} {item['name']}", item['url'])

    st.markdown("---")
    st.caption("© 2025 IsuruSoft Web Solutions")
