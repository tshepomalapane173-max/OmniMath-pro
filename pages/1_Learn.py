import streamlit as st, time, sympy as sp
import math_engine as me

st.markdown(f"### 🗺️ LEARNING PATH ({st.session_state.get('phase', 'Senior Phase')})")

# Winding path UI
st.markdown("""
<div style="display:flex; flex-direction:column; align-items:center; gap:15px; padding:10px;">
    <div style="background:#10b981; width:50px; height:50px; border-radius:50%; display:flex; align-items:center; justify-content:center;">✔</div>
    <div style="background:#f43f5e; width:65px; height:65px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:24px;">⚡</div>
    <div style="background:#1e1b40; width:50px; height:50px; border-radius:50%; display:flex; align-items:center; justify-content:center; color:#64748b;">🔒</div>
</div>
""", unsafe_allow_html=True)

if "curr_q" not in st.session_state or st.session_state.curr_q is None:
    phase = st.session_state.get("phase", "Senior Phase")
    st.session_state.curr_q = me.generate_senior_question() if phase == "Senior Phase" else me.generate_fet_question()

q = st.session_state.curr_q
st.write(q["prompt"])
st.latex(q["latex"])

with st.form("learn_page_form", clear_on_submit=True):
    ans = st.text_input("Your Answer:")
    if st.form_submit_button("Submit"):
        correct = False
        if q.get("type") == "symbolic":
            try: correct = sp.simplify(sp.sympify(ans) - sp.sympify(q["answer_str"])) == 0
            except: correct = False
        else:
            try: correct = float(ans) == float(q["answer"])
            except: correct = False
            
        if correct:
            st.success("Correct! +20 XP")
            st.session_state.xp += 20
            st.session_state.curr_q = None
            time.sleep(0.6)
            st.rerun()
        else:
            st.error("Incorrect. Try again!")
          
