# ════════════════════════════════════════════════════════════
#  TPrecision — CONFIG FILE
#  This is the ONLY file you need to edit.
#  Add your TradingView links and text here.
# ════════════════════════════════════════════════════════════


# ── ABOUT TEXT ───────────────────────────────────────────────
# Edit the text that appears in the About section.

ABOUT_TEXT = """
TPrecision documents key support and resistance zones across the forex market
using raw price action and structure. Every screenshot is taken directly from
TradingView — no overlays, no indicators, just clean zones drawn by hand.

The goal is simple: identify where price has reacted before, mark those levels
clearly, and let the market do the rest.
"""


# ── CHARTS ───────────────────────────────────────────────────
# Add your TradingView screenshot links below.
# Each chart has:
#   url   — your TradingView share link (https://www.tradingview.com/x/XXXXXXXX/)
#   pair  — the currency pair name shown under the image
#   tf    — the timeframe shown under the image
#   text  — the analysis text shown above the image (can be as long as you want)
#
# To add more charts, just copy one block and paste it below the last one.
# To leave a slot empty, set url to "".

CHARTS = [

    {
        "url": "https://www.tradingview.com/x/svXf7H36/",
        "pair": "EUR/USD",
        "tf": "H4",
        "text": "Price is approaching a key weekly resistance zone between 1.0920 – 1.0960. "
                "Multiple rejections visible at this level. Watching for a bearish reaction "
                "and potential short setup on lower timeframes.",
    },

    {
        "url": "",
        "pair": "GBP/USD",
        "tf": "H4",
        "text": "Clean support zone sitting at 1.2580 – 1.2610. Price has respected this area "
                "three times already. Looking for a bullish continuation if price returns here.",
    },

    {
        "url": "",
        "pair": "USD/JPY",
        "tf": "D1",
        "text": "Daily resistance at 150.80 – 151.20 aligns with the psychological 151 level. "
                "Bias remains bullish above 149.00 support. Key week ahead with JPY data.",
    },

    {
        "url": "",
        "pair": "AUD/USD",
        "tf": "H4",
        "text": "Range-bound between 0.6480 support and 0.6560 resistance. "
                "No directional bias until a clean break of either level with follow-through.",
    },

    {
        "url": "",
        "pair": "GBP/JPY",
        "tf": "H4",
        "text": "Strong bullish momentum. Demand zone at 187.00 – 187.80 held perfectly. "
                "Next target is the 191.00 supply zone. Trail stops on any longs.",
    },

    {
        "url": "",
        "pair": "EUR/GBP",
        "tf": "D1",
        "text": "Bearish structure intact. Resistance at 0.8600 – 0.8630 has rejected price twice. "
                "Support below at 0.8480. Watching for a continuation lower.",
    },

]
