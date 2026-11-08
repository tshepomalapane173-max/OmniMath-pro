import streamlit as st
import sympy as sp
import math_engine as me
import time

st.markdown("<span style='color:#06b6d4; font-size:11px; font-weight:bold;'>YOUR LEARNING SPACE</span>", unsafe_allow_html=True)
st.markdown("<h2 style='margin-top:0;'>Choose a learning phase</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#94a3b8; font-size:13px;'>Choose a lesson to begin your learning path.</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("Σ Senior Phase (Gr 7-9)"):
        st.session_state.phase = "Senior Phase"
        st.success("Senior Phase activated!")
with col2:
    if st.button("∫ FET Advanced (Gr 10-12)"):
        st.session_state.phase = "FET Advanced"
        st.success("FET Advanced activated!")

st.markdown(f"""
<div style="background:#13112b; border:1px solid #232046; border-radius:16px; padding:20px; margin:20px 0;">
    <span style="color:#fbbf24; font-size:10px; font-weight:bold; letter-spacing:1px;">GRADES 7–9 · LEARNING PATH</span>
    <h3 style="margin:5px 0;">Variables & Expressions</h3>
    <div style="background:#1e1b40; border-radius:8px; height:8px; margin:12px 0;"><div style="width:0%; background:#fbbf24; height:100%; border-radius:8px;"></div></div>
    <div style="display:flex; justify-content:space-between; font-size:11px; color:#94a3b8;">
        <span>0 / 4 lessons complete</span>
        <span>0%</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Winding Path Nodes
st.markdown("""
<div style="display:flex; flex-direction:column; align-items:center; gap:16px; padding:15px;">
    <div style="width:65px; height:65px; background:linear-gradient(135deg, #fbbf24, #f59e0b); border-radius:20px; display:flex; align-items:center; justify-content:center; font-size:26px; box-shadow:0 0 15px rgba(251,191,36,0.4); border:2px solid #fff;">⚡</div>
    <div style="width:2px; height:25px; background:#475569;"></div>
    <div style="width:55px; height:55px; background:#1e1b40; border-radius:16px; display:flex; align-items:center; justify-content:center; font-size:20px; border:2px solid #232046; color:#64748b;">🔒</div>
</div>
""", unsafe_allow_html=True)

if "curr_q" not in st.session_state or st.session_state.curr_q is None:
    st.session_state.curr_q = me.generate_senior_question()

q = st.session_state.curr_q
st.markdown("<div style='background:#13112b; border:1px solid #232046; border-radius:18px; padding:20px;'>", unsafe_allow_html=True)
st.write(q["prompt"])
st.latex(q["latex"])

with st.form("learn_form", clear_on_submit=True):
    ans = st.text_input("Your answer", placeholder="Type your answer")
    if st.form_submit_button("Check answer"):
        try:
            correct = float(ans) == float(q["answer"])
        except:
            correct = False
        if correct:
            st.success("Correct! +20 XP")
            st.session_state.xp += 20
            st.session_state.curr_q = None
            time.sleep(0.5)
            st.rerun()
        else:
            st.error("Incorrect. Try again!")
st.markdown("</div>", unsafe_allow_html=True)
    
