import streamlit as st

st.set_page_config(page_title="OmniMath Academy Pro", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")

# Styling to match your exact theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    .stApp { background: linear-gradient(135deg, #020617 0%, #0b091a 50%, #13112b 100%); color: #f8fafc; font-family: 'Inter', sans-serif; }
    .top-stats { display: flex; justify-content: space-around; background: #13112b; border: 1px solid #232046; border-radius: 16px; padding: 10px; font-weight: bold; margin-bottom: 20px; }
    .dark-card { background: #13112b; border: 1px solid #232046; border-radius: 18px; padding: 20px; margin-bottom: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.3); }
    .phase-card-senior { border: 2px solid #fbbf24; background: linear-gradient(135deg, rgba(251,191,36,0.1), #13112b); border-radius: 18px; padding: 20px; text-align: center; }
    .phase-card-fet { border: 2px solid #f43f5e; background: linear-gradient(135deg, rgba(244,63,94,0.1), #13112b); border-radius: 18px; padding: 20px; text-align: center; }
    .stButton>button { background: linear-gradient(90deg, #10b981, #059669) !important; color: #fff !important; font-weight: 700 !important; border-radius: 14px !important; border: none !important; padding: 12px !important; width: 100%; }
</style>
""", unsafe_allow_html=True)

for k, v in {"xp": 0, "streak": 1, "keys": 5, "phase": "Senior Phase"}.items():
    st.session_state.setdefault(k, v)

# Top Bar
st.markdown(f"""
<div class="top-stats">
    <span style="color:#fbbf24;">🪙 {st.session_state.xp} XP</span>
    <span style="color:#06b6d4;">🔑 {st.session_state.keys} Keys</span>
    <span style="color:#f97316;">🔥 {st.session_state.streak} Day</span>
</div>
""", unsafe_allow_html=True)

st.markdown("<span style='color:#06b6d4; font-size:11px; font-weight:bold; letter-spacing:1px;'>YOUR LEARNING SPACE</span>", unsafe_allow_html=True)
st.markdown("<h2 style='margin-top:0;'>Good to see you, learner.</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#94a3b8; font-size:13px;'>Small steps add up. Pick a path and make today count.</p>", unsafe_allow_html=True)

st.markdown(f"""
<div class="dark-card">
    <div style="display:flex; justify-content:space-between; align-items:center;">
        <span style="color:#94a3b8; font-size:12px; font-weight:bold;">PLAYER LEVEL</span>
        <span style="color:#fbbf24; font-size:12px;">Your current plan</span>
    </div>
    <h3 style="margin:5px 0;">Level 1</h3>
    <span style="font-size:12px; color:#94a3b8;">{st.session_state.xp} total XP</span>
    <div style="background:#1e1b40; border-radius:8px; height:8px; margin:12px 0;"><div style="width:0%; background:#8b5cf6; height:100%; border-radius:8px;"></div></div>
    <div style="display:flex; justify-content:space-between; font-size:11px; color:#94a3b8;">
        <span>0 XP</span>
        <span>100 XP to next level</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Three Stat Blocks matching image_12.png
c1, c2, c3 = st.columns(3)
c1.markdown('<div class="dark-card" style="text-align:center; padding:12px;"><span style="color:#06b6d4; font-size:18px;">✔</span><br><b>0</b><br><span style="font-size:11px; color:#94a3b8;">Correct</span></div>', unsafe_allow_html=True)
c2.markdown(f'<div class="dark-card" style="text-align:center; padding:12px;"><span style="color:#fbbf24; font-size:18px;">🪙</span><br><b>{st.session_state.xp}</b><br><span style="font-size:11px; color:#94a3b8;">Total XP</span></div>', unsafe_allow_html=True)
c3.markdown(f'<div class="dark-card" style="text-align:center; padding:12px;"><span style="color:#f97316; font-size:18px;">🔥</span><br><b>{st.session_state.streak}</b><br><span style="font-size:11px; color:#94a3b8;">day streak</span></div>', unsafe_allow_html=True)

st.markdown("""
<div class="dark-card" style="display:flex; align-items:center; gap:12px;">
    <span style="font-size:20px; color:#fbbf24;">⚡</span>
    <div>
        <div style="font-weight:bold; font-size:14px;">Break problems into smaller steps.</div>
        <div style="font-size:12px; color:#94a3b8;">Structured guidance through difficult equations.</div>
    </div>
</div>
""", unsafe_allow_html=True)
