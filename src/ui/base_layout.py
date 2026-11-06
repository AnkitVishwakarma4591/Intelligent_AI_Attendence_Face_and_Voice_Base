import streamlit as st


APP_BACKGROUND = "radial-gradient(ellipse at 15% 10%, #4656e8 0%, #202b74 46%, #111827 100%) fixed"


def style_background_home():
    """Keep the home portal cards distinct while using the shared app theme."""
    st.markdown("""
        <style>
        [data-testid="stColumn"] > div {
            background: rgba(255,255,255,.94);
            border: 1px solid rgba(255,255,255,.5);
            border-radius: 24px;
            padding: 1.5rem;
            box-shadow: 0 18px 45px rgba(10,15,50,.18);
        }
        .stApp h2.home-portal-title {color:#18234b !important;}
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    """Retained for older imports; the shared theme is applied in style_base_layout."""


def style_base_layout():
    """Apply one consistent theme to every screen and in-app dashboard tab."""
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap');
        #MainMenu, footer {{display:none !important;}}
        header[data-testid="stHeader"] {{display:none !important; height:0 !important;}}

        .stApp {{background:{APP_BACKGROUND} !important; color:#eef1ff;}}
        [data-testid="stAppViewContainer"], [data-testid="stMain"] {{background:transparent !important;}}
        .block-container {{max-width:1120px; padding-top:1.5rem; padding-bottom:2rem;}}

        .stApp h1, .stApp h2, .stApp h3, .stApp h4 {{
            color:#eef1ff !important;
            font-family:'Outfit',sans-serif !important;
            letter-spacing:-.025em;
        }}
        .stApp h1 {{font-size:clamp(2.2rem,5vw,3.5rem) !important; line-height:1.08 !important;}}
        .stApp h2 {{font-size:2rem !important;}}
        .stApp p, .stApp label, .stApp [data-testid="stCaptionContainer"] {{font-family:'DM Sans',sans-serif;}}
        .stApp [data-testid="stMarkdownContainer"] p {{color:#eef1ff;}}
        .stApp label {{color:#eef1ff;}}
        .stApp h2.home-portal-title {{color:#18234b !important;}}

        [data-testid="stTextInput"] input, [data-testid="stSelectbox"] [data-baseweb="select"],
        [data-testid="stTextArea"] textarea {{border-radius:12px;}}
        div[data-testid="stMetric"] {{background:#fff; padding:1rem; border:1px solid #e1e7ff; border-radius:16px;}}
        .stButton button {{border-radius:12px; font-weight:650; transition:transform .18s ease, box-shadow .18s ease;}}
        .stButton button:hover {{transform:translateY(-1px); box-shadow:0 8px 18px rgba(42,59,160,.16);}}
        button[kind="primary"] {{background:linear-gradient(120deg,#5865f2,#4353d7); border:0; color:white;}}
        button[kind="secondary"] {{background:#e84393; border:0; color:white;}}
        button[kind="tertiary"] {{background:#18234b; border:0; color:white;}}
        [data-testid="stDataFrame"] {{border:1px solid #dfe5f5; border-radius:14px; overflow:hidden;}}
        hr {{border-color:rgba(238,241,255,.25);}}
        </style>
    """, unsafe_allow_html=True)
