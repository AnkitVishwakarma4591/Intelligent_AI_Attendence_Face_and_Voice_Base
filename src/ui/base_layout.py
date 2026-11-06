import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
        .stApp {
            background: radial-gradient(ellipse at 15% 10%, #4656e8 0%, #202b74 46%, #111827 100%) fixed;
        }
        [data-testid="stColumn"] > div {
            background: rgba(255,255,255,.94);
            border: 1px solid rgba(255,255,255,.5);
            border-radius: 24px;
            padding: 1.5rem;
            box-shadow: 0 18px 45px rgba(10,15,50,.18);
        }
        [data-testid="stColumn"] h2 { color: #18234b; }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #f4f6ff 0%, #e9edff 55%, #f8faff 100%) fixed;
        }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap');
        #MainMenu, footer {display:none !important;}
        header[data-testid="stHeader"] {display:none !important; height:0 !important;}
        .block-container {max-width: 1120px; padding-top: 1.5rem; padding-bottom: 2rem;}
        h1, h2 {font-family:'Outfit',sans-serif !important; color:#172554; letter-spacing:-.035em;}
        h1 {font-size:clamp(2.2rem,5vw,3.5rem) !important; line-height:1.08 !important;}
        h2 {font-size:2rem !important;}
        h3, h4, p, label, [data-testid="stCaptionContainer"] {font-family:'DM Sans',sans-serif;}
        [data-testid="stTextInput"] input, [data-testid="stSelectbox"] [data-baseweb="select"],
        [data-testid="stTextArea"] textarea {border-radius:12px;}
        div[data-testid="stMetric"] {background:#fff; padding:1rem; border:1px solid #e1e7ff; border-radius:16px;}
        .stButton button {border-radius:12px; font-weight:650; transition:transform .18s ease, box-shadow .18s ease;}
        .stButton button:hover {transform:translateY(-1px); box-shadow:0 8px 18px rgba(42,59,160,.16);}
        button[kind="primary"] {background:linear-gradient(120deg,#5865f2,#4353d7); border:0;}
        button[kind="secondary"] {background:#e84393; border:0; color:white;}
        button[kind="tertiary"] {background:#18234b; border:0; color:white;}
        [data-testid="stDataFrame"] {border:1px solid #dfe5f5; border-radius:14px; overflow:hidden;}
        hr {border-color:#d9e0f0;}
        </style>
    """, unsafe_allow_html=True)
