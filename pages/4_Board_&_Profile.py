import streamlit as st
st.markdown("### 🏆 LEADERBOARD & PROFILE")
lvl = (st.session_state.get('xp', 754) // 100) + 1
c1, c2, c3 = st.columns(3)
c1.metric("Level", lvl)
c2.metric("Total XP", st.session_state.get('xp', 754))
c3.metric("Streak", f"{st.session_state.get('streak', 10)} Days")
