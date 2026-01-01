import streamlit as st
import random
import os

# 1. පිටුවේ මූලික සැකසුම්
st.set_page_config(page_title="IsuruSoft Educational Portal", page_icon="🎓", layout="wide")

# --- Session State Initializations ---
if 'view_count' not in st.session_state:
    st.session_state['view_count'] = 50240 

if 'counted' not in st.session_state:
    st.session_state['view_count'] += random.randint(15, 60)
    st.session_state['counted'] = True

if 'is_logged_in' not in st.session_state:
    st.session_state['is_logged_in'] = False

if 'user_comments' not in st.session_state:
    st.session_state['user_comments'] = []

# Quiz එක පාලනය කරන Session States
if 'show_quiz' not in st.session_state:
    st.session_state.show_quiz = False
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'quiz_options' not in st.session_state:
    st.session_state.quiz_options = []
if 'show_info' not in st.session_state:
    st.session_state.show_info = False

# --- CSS Styling ---
st.markdown("""
<style>
    .stApp { background-color: #0f172a; }
    .main-title { text-align: center; color: #ff4b4b; font-size: 45px; font-weight: 800; margin-bottom: 20px; }
    .sub-title { text-align: center; color: #cbd5e1; font-size: 18px; margin-bottom: 40px; }
    .category-header { background-color: #1e293b; padding: 10px 20px; border-radius: 8px; color: #facc15; font-size: 20px; font-weight: bold; margin-top: 30px; border-left: 5px solid #ff4b4b; }
    .ad-card { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 10px; text-align: center; }
    .comment-card { background: #1e293b; padding: 10px; border-radius: 8px; margin-bottom: 5px; border-left: 3px solid #facc15; color: #cbd5e1; }
    .login-container { background: #1e293b; padding: 30px; border-radius: 15px; border: 1px solid #334155; }
    .quiz-card { background: #1e293b; padding: 25px; border-radius: 15px; border: 2px solid #ff4b4b; margin-top: 20px; }
</style>
""", unsafe_allow_html=True)

# --- Quiz Data (ප්‍රශ්න 25) ---
questions_list = [
    {"q_no": 1, "file": "1", "answer": "අයිසැක් නිව්ටන්", "info": "ගුරුත්වාකර්ෂණ නියම සහ චලිත නියම සොයාගත් ශ්‍රේෂ්ඨ විද්‍යාඥයෙකි."},
    {"q_no": 2, "file": "4", "answer": "ගැලීලියෝ ගැලිලි", "info": "නූතන තාරකා විද්‍යාවේ පියා ලෙස හැඳින්වේ. දුරේක්ෂය දියුණු කළේය."},
    {"q_no": 3, "file": "7", "answer": "නීල් ආම්ස්ට්‍රෝන්", "info": "හඳ මත පා තැබූ ලොව පළමු මිනිසා මොහු වේ."},
    {"q_no": 4, "file": "8", "answer": "යූරි ගගාරින්", "info": "අභ්‍යවකාශයට ගිය ලොව ප්‍රථම මිනිසා වේ."},
    {"q_no": 5, "file": "9", "answer": "අර්නස්ට් රදර්ෆර්ඩ්", "info": "පරමාණුවේ න්‍යෂ්ටිය සොයාගත් න්‍යෂ්ටික භෞතික විද්‍යාවේ පියා වේ."},
    {"q_no": 6, "file": "10", "answer": "හයිසන්බර්ග්", "info": "ක්වොන්ටම් යාන්ත්‍ර විද්‍යාව පිළිබඳ 'අනිශ්චිතතා මූලධර්මය' ඉදිරිපත් කළේය."},
    {"q_no": 7, "file": "11", "answer": "ඇලෙක්සැන්ඩර් ග්‍රැහැම් බෙල්", "info": "ලොව ප්‍රථම ප්‍රායෝගික දුරකථනය නිපදවූ නව නිපැයුම්කරු වේ."},
    {"q_no": 8, "file": "12", "answer": "ජෝන් ලොගී බෙයාර්ඩ්", "info": "ලොව ප්‍රථම රූපවාහිනී යන්ත්‍රය නිපදවූ පුරෝගාමියා වේ."},
    {"q_no": 9, "file": "13", "answer": "මාරි කියුරි", "info": "රේඩියම් සහ පොලෝනියම් සොයාගත් විද්‍යාඥවරියකි."},
    {"q_no": 10, "file": "14", "answer": "පියරේ කියුරි", "info": "මාරි කියුරි සමඟ එක්ව විකිරණශීලීතාව පිළිබඳ පර්යේෂණ කළේය."},
    {"q_no": 11, "file": "15", "answer": "වෝල්ටා", "info": "ලොව ප්‍රථම විද්‍යුත් බැටරිය නිපදවූ විද්‍යාඥයෙකි."},
    {"q_no": 12, "file": "17", "answer": "නිකොලා ටෙස්ලා", "info": "ප්‍රත්‍යාවර්ත ධාරා (AC) විදුලි පද්ධතිය පිළිබඳ පුරෝගාමියෙකි."},
    {"q_no": 13, "file": "18", "answer": "ජොහැන්නස් කෙප්ලර්", "info": "ග්‍රහලෝක වල චලිතය පිළිබඳ නියමයන් ඉදිරිපත් කළේය."},
    {"q_no": 14, "file": "19", "answer": "ගැලීලියෝ ගැලිලි", "info": "නිරීක්ෂණාත්මක තාරකා විද්‍යාවේ පුරෝගාමියෙකි."},
    {"q_no": 15, "file": "20", "answer": "ඇලෙක්සැන්ඩර් ෆ්ලෙමින්", "info": "ලොව ප්‍රථම ප්‍රතිජීවක ඖෂධය (පෙනිසිලින්) සොයාගත්තේය."},
    {"q_no": 16, "file": "21", "answer": "ඇල්බට් අයින්ස්ටයින්", "info": "සාපේක්ෂතාවාදය පිළිබඳ E=mc² සමීකරණය ඉදිරිපත් කළේය."},
    {"q_no": 17, "file": "22", "answer": "තෝමස් එඩිසන්", "info": "විදුලි බුබුල ඇතුළු නව නිපැයුම් දහසකට වඩා ලොවට දුන්නේය."},
    {"q_no": 18, "file": "23", "answer": "චාල්ස් ඩාවින්", "info": "ජීවීන්ගේ පරිණාමවාදය පිළිබඳ නියමය ඉදිරිපත් කළේය."},
    {"q_no": 19, "file": "24", "answer": "ලුවී පාස්චර්", "info": "එන්නත්කරණය සහ කිරි විෂබීජහරණය පිළිබඳ සොයාගැනීම් කළේය."},
    {"q_no": 20, "file": "25", "answer": "ලියනාඩෝ ඩා වින්චි", "info": "ශ්‍රේෂ්ඨ චිත්‍ර ශිල්පියෙකු මෙන්ම දක්ෂ විද්‍යාඥයෙකි."},
    {"q_no": 21, "file": "26", "answer": "ජේම්ස් වොට්", "info": "වාෂ්ප එන්ජිම දියුණු කර කර්මාන්ත විප්ලවයට දායක විය."},
    {"q_no": 22, "file": "27", "answer": "මයිකල් ෆැරඩේ", "info": "විද්‍යුත් චුම්බක ප්‍රේරණය සොයාගත් අතර විද්‍යුත් මෝටරය නිපදවීය."},
    {"q_no": 23, "file": "28", "answer": "ග්‍රෙගර් මෙන්ඩල්", "info": "ප්‍රවේණි විද්‍යාවේ පියා ලෙස හැඳින්වේ."},
    {"q_no": 24, "file": "29", "answer": "සිග්මන්ඩ් ෆ්‍රොයිඩ්", "info": "මනෝ විශ්ලේෂණ වාදය ඉදිරිපත් කළේය."},
    {"q_no": 25, "file": "30", "answer": "ස්ටීව් ජොබ්ස්", "info": "Apple සමාගමේ නිර්මාතෘවරයා වන මොහු තාක්ෂණික විප්ලවයක් ඇති කළේය."}
]

extra_names = ["ස්ටීවන් හෝකින්", "මැක්ස් ප්ලෑන්ක්", "එඩ්වින් හබල්", "රිචඩ් ෆෙයින්මන්", "ඇල්ෆ්‍රඩ් නොබෙල්", "ජෝන් ඩෝල්ටන්", "ගුග්ලීල්මෝ මාකෝනි", "විල්හෙල්ම් රොන්ට්ගන්", "දිමිත්‍රි මෙන්ඩලීව්", "ඇලන් ටියුරින්", "බෙන්ජමින් ෆ්‍රැන්ක්ලින්", "ආකිමිඩීස්", "පයිතගරස්", "ඇරිස්ටෝටල්", "චාල්ස් බැබේජ්"]
all_distractors = list(set([q["answer"] for q in questions_list] + extra_names))

# --- APP FLOW ---
if not st.session_state['is_logged_in']:
    st.markdown('<h1 class="main-title">ISURUSOFT PORTAL</h1>', unsafe_allow_html=True)
    col_img, col_form = st.columns([1.2, 1], gap="large")
    with col_img:
        st.image("https://raw.githubusercontent.com/isurukihanduwage8804/isurusoft/main/2.jpg", use_container_width=True)
    with col_form:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        u = st.text_input("User Name", key="user_input")
        p = st.text_input("Password", type="password", key="pass_input")
        if st.button("LOGIN", use_container_width=True):
            if u == "isurusoft" and p == "123456":
                st.session_state['is_logged_in'] = True
                st.rerun()
            else: st.error("වැරදියි!")
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- LOGGED IN MAIN PAGE ---
    st.markdown('<h1 class="main-title">ISURUSOFT EDUCATIONAL HUB</h1>', unsafe_allow_html=True)
    st.sidebar.markdown(f'<h2 style="color:#facc15; text-align:center;">VIEWS: {st.session_state["view_count"]:,}</h2>', unsafe_allow_html=True)
    
    if st.sidebar.button("LOGOUT", use_container_width=True):
        st.session_state['is_logged_in'] = False
        st.session_state.show_quiz = False
        st.rerun()

    # QUIZ පෙන්වනවාද නැද්ද යන්න තීරණය කිරීම
    if st.session_state.show_quiz:
        if st.button("⬅️ ආපසු Home වෙත"):
            st.session_state.show_quiz = False
            st.rerun()
            
        st.markdown('<div class="quiz-card">', unsafe_allow_html=True)
        if st.session_state.current_index < len(questions_list):
            q = questions_list[st.session_state.current_index]
            img_filename = next((f for f in [f"{q['file']}.jpg", q['file'], f"{q['file']}.png"] if os.path.exists(f)), None)
            
            if not st.session_state.quiz_options:
                opts = random.sample([n for n in all_distractors if n != q["answer"]], 3) + [q["answer"]]
                random.shuffle(opts)
                st.session_state.quiz_options = opts

            st.write(f"### ප්‍රශ්නය {q['q_no']} / 25")
            c1, c2 = st.columns(2)
            with c1:
                if img_filename: st.image(img_filename, use_container_width=True)
                else: st.warning("පින්තූරය හමු නොවීය.")
            with c2:
                user_choice = st.radio("මොහු කවුද?", st.session_state.quiz_options, key=f"q{st.session_state.current_index}")
                if not st.session_state.show_info:
                    if st.button("තහවුරු කරන්න"):
                        st.session_state.show_info = True
                        if user_choice == q["answer"]: st.session_state.score += 1
                        st.rerun()
                else:
                    if user_choice == q["answer"]: st.success(f"නිවැරදියි! ✅ {q['info']}")
                    else: st.error(f"වැරදියි! ❌ පිළිතුර: {q['answer']}. {q['info']}")
                    if st.button("ඊළඟ ප්‍රශ්නය ➡️"):
                        st.session_state.current_index += 1
                        st.session_state.quiz_options = []
                        st.session_state.show_info = False
                        st.rerun()
        else:
            st.balloons()
            st.success(f"වැඩසටහන අවසන්! ඔබේ ලකුණු: {st.session_state.score} / 25")
            if st.button("නැවත පටන් ගන්න"):
                st.session_state.score = 0
                st.session_state.current_index = 0
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        # සාමාන්‍ය CATEGORIES පෙන්වීම
        st.markdown('<p class="sub-title">අනාගත පරපුර වෙනුවෙන් තැනූ නවීන අධ්‍යාපනික මෙවලම් කට්ටලය</p>', unsafe_allow_html=True)
        
        # මෙතැන ඔයාගේ Categories ටික තියෙනවා
        CATEGORIES = {
            "🔢 ගණිතය සහ විද්‍යාව": [
                {"name": "Geometry Dance", "url": "https://shape-aria-m2uzeyna2bdyfdx3xktdgv.streamlit.app/", "icon": "📐"},
                {"name": "Graph Art 2", "url": "https://nicegrap2.streamlit.app/", "icon": "🎨"},
                {"name": "Periodic Table", "url": "https://prtable.streamlit
