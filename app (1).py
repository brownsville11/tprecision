import streamlit as st
from config import ABOUT_TEXT, CHARTS

# ── PAGE CONFIG ──────────────────────────────────────────────
st.set_page_config(
    page_title="TPrecision",
    page_icon="📈",
    layout="wide",
)

# ── ACCENT COLOR (from uploaded swatch) ─────────────────────
ACCENT = "#4a6b6e"
ACCENT_DIM = "rgba(74,107,110,0.15)"
ACCENT_BORDER = "rgba(74,107,110,0.4)"

# ── STYLES ───────────────────────────────────────────────────
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=IBM+Plex+Mono:wght@400;500&family=Barlow:wght@300;400;500;600&display=swap');

html, body, [class*="css"], [data-testid="stAppViewContainer"] {{
    background-color: #080a0c !important;
    color: #dde1e7 !important;
    font-family: 'Barlow', sans-serif !important;
}}
[data-testid="stAppViewBlockContainer"] {{
    padding: 0 !important;
    max-width: 100% !important;
}}
[data-testid="column"] {{
    padding: 0 6px !important;
}}
#MainMenu, footer, header {{ visibility: hidden; }}
.block-container {{ padding: 0 !important; max-width: 100% !important; }}

.tp-header {{
    padding: 22px 52px;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #080a0c;
}}
.tp-logo {{
    font-family: 'Bebas Neue', sans-serif;
    font-size: 30px;
    letter-spacing: 4px;
    color: #dde1e7;
}}
.tp-logo span {{ color: {ACCENT}; }}
.tp-nav {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    color: #606870;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}}

.tp-hero {{
    padding: 90px 52px 70px;
    border-bottom: 1px solid rgba(255,255,255,0.06);
}}
.tp-eyebrow {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    color: {ACCENT};
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}}
.tp-eyebrow::before {{
    content: '';
    display: inline-block;
    width: 24px;
    height: 1px;
    background: {ACCENT};
}}
.tp-h1 {{
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(72px, 10vw, 120px);
    line-height: 0.9;
    letter-spacing: 2px;
    color: #dde1e7;
    margin-bottom: 28px;
}}
.tp-h1 span {{ color: {ACCENT}; }}
.tp-hero-sub {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 14px;
    color: #606870;
    line-height: 1.9;
    max-width: 540px;
    font-weight: 300;
}}

.tp-about {{
    padding: 72px 52px;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    display: grid;
    grid-template-columns: 160px 1fr;
    gap: 60px;
    align-items: start;
}}
.tp-about-label {{
    font-family: 'Bebas Neue', sans-serif;
    font-size: 13px;
    letter-spacing: 3px;
    color: #606870;
    padding-top: 4px;
}}
.tp-about-label::before {{
    content: '';
    display: block;
    width: 2px;
    height: 24px;
    background: {ACCENT};
    margin-bottom: 12px;
}}
.tp-about-body {{
    font-size: 16px;
    font-weight: 300;
    color: #7a8290;
    line-height: 1.95;
    max-width: 720px;
    white-space: pre-line;
}}

.tp-gallery-header {{
    padding: 52px 52px 20px;
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 32px;
}}
.tp-gallery-title {{
    font-family: 'Bebas Neue', sans-serif;
    font-size: 38px;
    letter-spacing: 3px;
    color: #dde1e7;
}}
.tp-gallery-count {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    color: #606870;
    letter-spacing: 1px;
}}

.tp-card {{
    background: #0f1215;
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 8px;
    overflow: hidden;
    margin-bottom: 28px;
}}
.tp-card:hover {{
    border-color: {ACCENT_BORDER};
}}
.tp-card img {{
    width: 100%;
    display: block;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}}
.tp-card-body {{
    padding: 18px 22px 22px;
}}
.tp-card-meta {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
}}
.tp-card-pair {{
    font-family: 'Bebas Neue', sans-serif;
    font-size: 22px;
    letter-spacing: 2px;
    color: #dde1e7;
}}
.tp-card-tf {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    color: {ACCENT};
    letter-spacing: 1px;
    background: {ACCENT_DIM};
    border: 1px solid {ACCENT_BORDER};
    padding: 3px 10px;
    border-radius: 3px;
}}
.tp-card-text {{
    font-size: 14px;
    font-weight: 300;
    color: #7a8290;
    line-height: 1.8;
    font-family: 'Barlow', sans-serif;
}}

.tp-empty {{
    aspect-ratio: 16/9;
    border: 1px dashed rgba(255,255,255,0.07);
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 8px;
    margin-bottom: 28px;
    background: #0f1215;
}}
.tp-empty-pair {{
    font-family: 'Bebas Neue', sans-serif;
    font-size: 20px;
    letter-spacing: 2px;
    color: rgba(255,255,255,0.12);
}}
.tp-empty-label {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    color: rgba(255,255,255,0.1);
    letter-spacing: 1px;
}}

.tp-footer {{
    border-top: 1px solid rgba(255,255,255,0.06);
    padding: 28px 52px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 40px;
}}
.tp-footer-logo {{
    font-family: 'Bebas Neue', sans-serif;
    font-size: 20px;
    letter-spacing: 3px;
    color: #606870;
}}
.tp-footer-logo span {{ color: {ACCENT}; }}
.tp-footer-note {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    color: #606870;
    letter-spacing: 0.5px;
}}
</style>
""", unsafe_allow_html=True)


def tv_to_img(url: str) -> str:
    if not url:
        return ""
    code = url.rstrip("/").split("/")[-1]
    return f"https://s3.tradingview.com/snapshots/s/{code}.png"


# HEADER
st.markdown("""
<div class="tp-header">
  <div class="tp-logo">T<span>Precision</span></div>
  <div class="tp-nav">Forex · S&R Analysis</div>
</div>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="tp-hero">
  <div class="tp-eyebrow">Forex Technical Analysis</div>
  <div class="tp-h1">PRECISION<br><span>IN THE</span><br>LEVELS</div>
  <div class="tp-hero-sub">Hand-drawn support &amp; resistance zones across major forex pairs.<br>No indicators. No noise. Just price.</div>
</div>
""", unsafe_allow_html=True)

# ABOUT
st.markdown(f"""
<div class="tp-about">
  <div class="tp-about-label">About</div>
  <div class="tp-about-body">{ABOUT_TEXT.strip()}</div>
</div>
""", unsafe_allow_html=True)

# GALLERY HEADER
total = sum(1 for c in CHARTS if c["url"])
st.markdown(f"""
<div class="tp-gallery-header">
  <div class="tp-gallery-title">Chart Gallery</div>
  <div class="tp-gallery-count">{total} / {len(CHARTS)} charts live</div>
</div>
""", unsafe_allow_html=True)

# GALLERY GRID — 2 per row
st.markdown('<div style="padding: 0 46px;">', unsafe_allow_html=True)

rows = [CHARTS[i:i+2] for i in range(0, len(CHARTS), 2)]

for row in rows:
    cols = st.columns(2, gap="medium")
    for col, chart in zip(cols, row):
        with col:
            img_url = tv_to_img(chart["url"])
            if img_url:
                st.markdown(f"""
                <div class="tp-card">
                  <img src="{img_url}" alt="{chart['pair']}">
                  <div class="tp-card-body">
                    <div class="tp-card-meta">
                      <div class="tp-card-pair">{chart['pair']}</div>
                      <div class="tp-card-tf">{chart['tf']}</div>
                    </div>
                    <div class="tp-card-text">{chart['text']}</div>
                  </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="tp-empty">
                  <div class="tp-empty-pair">{chart['pair']}</div>
                  <div class="tp-empty-label">{chart['tf']} · coming soon</div>
                </div>
                """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="tp-footer">
  <div class="tp-footer-logo">T<span>Precision</span></div>
  <div class="tp-footer-note">For educational purposes only · Not financial advice</div>
</div>
""", unsafe_allow_html=True)
