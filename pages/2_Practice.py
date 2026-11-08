import streamlit as st
import time
import math_engine as me

st.markdown("<span style='color:#06b6d4; font-size:11px; font-weight:bold;'>YOUR LEARNING SPACE</span>", unsafe_allow_html=True)
st.markdown("<h2 style='margin-top:0;'>Practice room</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#94a3b8; font-size:13px;'>Take your time. Every attempt is a step forward.</p>", unsafe_allow_html=True)

st.markdown("""
<div style="background:#13112b; border:1px solid #232046; border-radius:18px; padding:20px; margin-bottom:16px;">
    <div style="display:flex; justify-content:space-between; color:#94a3b8; font-size:12px; font-weight:bold; margin-bottom:10px;">
        <span>FOUNDATION</span>
        <span>QUESTION 1</span>
    </div>
    <h1 style="color:#fff; margin:10px 0;">6 + 5 = ?</h1>
    <span style="font-size:12px; color:#94a3b8;">Your answer</span>
</div>
""", unsafe_allow_html=True)

with st.form("practice_form", clear_on_submit=True):
    ans = st.text_input("Type your answer", label_visibility="collapsed", placeholder="Type your answer")
    submitted = st.form_submit_button("Check answer")
    if submitted:
        if ans.strip() == "11":
            st.success("Correct! Well done.")
            st.session_state.xp += 10
        else:
            st.error("Not quite right. Try again!")

st.markdown("""
<div style="background:#13112b; border:1px solid #232046; border-radius:18px; padding:16px; margin-top:16px;">
    <span style="color:#06b6d4; font-size:14px; font-weight:bold;">✨ A thought to take with you</span>
    <p style="font-size:12px; color:#94a3b8; margin:6px 0 10px 0;">A wrong turn is useful information. Keep trying until the idea clicks.</p>
    <a href="#" style="color:#06b6d4; font-size:12px; text-decoration:none;">Need a hint?</a>
</div>
""", unsafe_allow_html=True)
