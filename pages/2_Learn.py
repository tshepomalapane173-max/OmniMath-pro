import streamlit as st, time
import math_engine as me

st.markdown("### ⚡ SPEED-RUN ARCADE")
if "t_act" not in st.session_state: st.session_state.t_act = False

if not st.session_state.t_act:
    if st.button("▶ START 60s RUN"):
        st.session_state.t_act, st.session_state.t_start, st.session_state.t_score = True, time.time(), 0
        st.session_state.t_curr = me.generate_speedrun()
        st.rerun()
else:
    rem = max(0, int(60 - (time.time() - st.session_state.t_start)))
    if rem <= 0:
        st.error(f"Time's Up! Score: {st.session_state.t_score}")
        st.session_state.xp += st.session_state.t_score * 5
        if st.button("Finish"): st.session_state.t_act = False; st.rerun()
    else:
        st.write(f"⏱ Time: {rem}s | Score: {st.session_state.t_score}")
        st.latex(f"{st.session_state.t_curr['latex']} = ?")
        with st.form("sf_page", clear_on_submit=True):
            u = st.text_input("Answer:")
            if st.form_submit_button("Submit"):
                if u.isdigit() and int(u) == st.session_state.t_curr["answer"]:
                    st.session_state.t_score += 1
                st.session_state.t_curr = me.generate_speedrun()
                st.rerun()
              
