
import time
import random
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import sympy as sp

# ==========================================
# 0. PAGE CONFIGURATION & STYLING
# ==========================================
st.set_page_config(
    page_title="OmniMath Academy Pro",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    
    .stApp { 
        background: linear-gradient(135deg, #020617 0%, #0b091a 50%, #13112b 100%); 
        color: #f8fafc; 
        font-family: 'Inter', sans-serif; 
    }
    
    /* Top Header Stats Bar */
    .top-stats {
        display: flex; 
        justify-content: space-around; 
        align-items: center;
        background: #13112b; 
        border: 1px solid #232046; 
        border-radius: 20px;
        padding: 12px 15px; 
        margin-bottom: 20px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
    }
    .stat-pill {
        display: flex; 
        align-items: center; 
        gap: 6px; 
        font-weight: 700; 
        font-size: 15px;
    }
    
    /* Card Styles */
    .dark-card {
        background: #13112b; 
        border: 1px solid #232046; 
        border-radius: 18px;
        padding: 22px; 
        margin-bottom: 16px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
    }
    .phase-card-senior {
        border: 2px solid #fbbf24; 
        background: linear-gradient(135deg, rgba(251,191,36,0.12), #13112b);
        border-radius: 18px; 
        padding: 20px; 
        text-align: center;
        box-shadow: 0 0 15px rgba(251, 191, 36, 0.15);
    }
    .phase-card-fet {
        border: 2px solid #f43f5e; 
        background: linear-gradient(135deg, rgba(244,63,94,0.12), #13112b);
        border-radius: 18px; 
        padding: 20px; 
        text-align: center;
        box-shadow: 0 0 15px rgba(244, 63, 94, 0.15);
    }
    
    /* Progress Bars */
    .progress-bg { 
        width: 100%; 
        background: #1e1b40; 
        border-radius: 10px; 
        height: 10px; 
        margin: 12px 0; 
        overflow: hidden;
    }
    .progress-fill { 
        height: 100%; 
        background: linear-gradient(90deg, #8b5cf6, #06b6d4); 
        border-radius: 10px; 
    }
    
    /* Custom Streamlit Button Styling */
    .stButton>button {
        background: linear-gradient(90deg, #10b981, #059669) !important; 
        color: #ffffff !important; 
        font-weight: 700 !important;
        border-radius: 14px !important; 
        border: none !important; 
        padding: 12px 20px !important; 
        width: 100%;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 1. EMBEDDED MATH ENGINE (LaTeX & Generators)
# ==========================================
x, y, z = sp.symbols('x y z')

def generate_senior_question():
    """Generates Senior Phase (Grades 7–9) structured mathematical expressions."""
    q_type = random.choice(["linear_eq", "pythagoras", "exponent", "ratio"])
    
    if q_type == "linear_eq":
        a = random.randint(2, 6)
        ans = random.randint(1, 10)
        c = a * ans
        return {
            "prompt": "Solve for the unknown variable $x$ in the equation:",
            "latex": f"{a}x = {c}",
            "answer": ans,
            "type": "numeric"
        }
    elif q_type == "pythagoras":
        a, b = random.choice([(3, 4), (5, 12), (6, 8), (9, 12)])
        ans = int((a**2 + b**2)**0.5)
        return {
            "prompt": "Calculate the hypotenuse $c$ using right-triangle properties:",
            "latex": f"c = \\sqrt{{{a}^2 + {b}^2}}",
            "answer": ans,
            "type": "numeric"
        }
    elif q_type == "exponent":
        base = random.randint(2, 5)
        p1, p2 = random.randint(2, 3), random.randint(1, 3)
        ans = base ** (p1 + p2)
        return {
            "prompt": "Simplify and evaluate the exponential expression:",
            "latex": f"{base}^{{{p1}}} \\times {base}^{{{p2}}}",
            "answer": ans,
            "type": "numeric"
        }
    else:
        n, d = random.randint(1, 4), random.randint(5, 9)
        return {
            "prompt": "Find the missing numerator value for $x$:",
            "latex": f"\\frac{{x}}{{{d}}} = \\frac{{{n}}}{{{d}}}",
            "answer": n,
            "type": "numeric"
        }

def generate_fet_question():
    """Generates FET Advanced Phase (Grades 10–12) calculus and algebra items."""
    q_type = random.choice(["derivative", "quadratic"])
    
    if q_type == "derivative":
        a = random.randint(2, 5)
        n = random.randint(2, 4)
        expr = a * x**n
        derived = sp.diff(expr, x)
        return {
            "prompt": "Determine the symbolic derivative $\\frac{dy}{dx}$ for:",
            "latex": f"y = {sp.latex(expr)}",
            "answer_str": sp.latex(derived),
            "type": "symbolic"
        }
    else:
        r1, r2 = random.randint(-3, 3), random.randint(1, 4)
        expr = sp.expand((x - r1) * (x - r2))
        return {
            "prompt": "Find the maximum positive root for the quadratic equation:",
            "latex": f"{sp.latex(expr)} = 0",
            "answer": max(r1, r2),
            "type": "numeric"
        }

def generate_speedrun_question(difficulty="Easy"):
    """Generates lightning mental math problems for the arcade speed-run mode."""
    ops = {"Easy": ["+", "-"], "Medium": ["+", "-", "\\times"], "Hard": ["\\times", "\\div"], "Expert": ["\\times", "\\div", "^"]}
    op = random.choice(ops.get(difficulty, ["+"]))
    
    if op in ["+", "-"]:
        a, b = random.randint(5, 50), random.randint(5, 50)
        ans = a + b if op == "+" else a - b
    elif op == "\\times":
        a, b = random.randint(3, 12), random.randint(3, 12)
        ans = a * b
    elif op == "\\div":
        b = random.randint(2, 10)
        ans = random.randint(2, 10)
        a = b * ans
    else:
        a, b = random.randint(2, 4), random.randint(2, 3)
        ans = a ** b
        op = "^"
        
    latex_eq = f"{a} {op} {b}" if op != "^" else f"{a}^{{{b}}}"
    return {"latex": latex_eq, "answer": ans}

# ==========================================
# 2. SESSION STATE MANAGEMENT
# ==========================================
defaults = {
    "xp": 754, 
    "streak": 10, 
    "keys": 5, 
    "correct": 6,
    "nav_tab": "Home", 
    "selected_phase": "Senior Phase", 
    "diff": "Easy", 
    "curr_q": None,
    "t_active": False, 
    "t_score": 0, 
    "t_start": None, 
    "t_q": "", 
    "t_ans": 0
}

for key, val in defaults.items():
    st.session_state.setdefault(key, val)

lvl = (st.session_state.xp // 100) + 1
xp_next = st.session_state.xp % 100

# ==========================================
# 3. TOP STATS BAR & NAVIGATION TABS
# ==========================================
st.markdown(f"""
<div class="top-stats">
    <div class="stat-pill" style="color:#fbbf24;">🪙 {st.session_state.xp} XP</div>
    <div class="stat-pill" style="color:#06b6d4;">🔑 {st.session_state.keys} Keys</div>
    <div class="stat-pill" style="color:#f97316;">🔥 {st.session_state.streak} Days</div>
</div>
""", unsafe_allow_html=True)

tabs = ["Home", "Learn", "Practice", "Papers", "Memos", "Board", "Profile"]
cols = st.columns(len(tabs))
for i, tab_name in enumerate(tabs):
    if cols[i].button(tab_name, key=f"nav_{tab_name}"):
        st.session_state.nav_tab = tab_name
        st.session_state.curr_q = None
        st.rerun()

st.markdown("---")

# ==========================================
# 4. TAB ROUTING & CONTENT MODULES
# ==========================================

# --- HOME TAB ---
if st.session_state.nav_tab == "Home":
    st.markdown(f"""
    <div class="dark-card">
        <span style="color:#8b5cf6; font-size:11px; font-weight:bold;">PLAYER LEVEL STATUS</span>
        <h2 style="margin:4px 0;">Level {lvl}</h2>
        <span style="color:#94a3b8; font-size:13px;">{st.session_state.xp} total earned XP</span>
        <div class="progress-bg"><div class="progress-fill" style="width:{xp_next}%;"></div></div>
        <div style="text-align:right; font-size:12px; color:#94a3b8;">{100-xp_next} XP to next level rank</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### CHOOSE YOUR GRADE MODULE")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="phase-card-senior">
            <h1 style="color:#fbbf24; margin:0;">Σ</h1>
            <h3 style="color:#fbbf24; margin:5px 0;">Senior Phase</h3>
            <p style="font-size:12px; color:#94a3b8;">Grades 7–9<br>Algebra, linear equations & geometry</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Select Senior Phase", key="sel_s"):
            st.session_state.selected_phase = "Senior Phase"
            st.session_state.nav_tab = "Learn"
            st.session_state.curr_q = None
            st.rerun()
            
    with c2:
        st.markdown("""
        <div class="phase-card-fet">
            <h1 style="color:#f43f5e; margin:0;">∫</h1>
            <h3 style="color:#f43f5e; margin:5px 0;">FET Advanced</h3>
            <p style="font-size:12px; color:#94a3b8;">Grades 10–12<br>Calculus, derivatives & quadratic equations</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Select FET Advanced", key="sel_f"):
            st.session_state.selected_phase = "FET Advanced"
            st.session_state.nav_tab = "Learn"
            st.session_state.curr_q = None
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="dark-card" style="border-left: 4px solid #06b6d4;">
        <h4 style="color:#06b6d4; margin:0;">⚡ MATH SPEED-RUN ARCADE</h4>
        <p style="font-size:12px; color:#94a3b8; margin:5px 0 0 0;">Test your mental arithmetic speed and build streak multipliers!</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Launch Speed-Run Arena"):
        st.session_state.nav_tab = "Practice"
        st.rerun()

# --- LEARN TAB ---
elif st.session_state.nav_tab == "Learn":
    phase = st.session_state.selected_phase
    color = "#fbbf24" if phase == "Senior Phase" else "#f43f5e"
    
    st.markdown(f"""
    <div class="dark-card" style="border-color:{color};">
        <span style="color:{color}; font-size:11px; font-weight:bold; letter-spacing:1px;">{phase.upper()} · ACTIVE CURRICULUM</span>
        <h3 style="margin:6px 0;">Interactive Problem Solving Matrix</h3>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.curr_q is None:
        st.session_state.curr_q = generate_senior_question() if phase == "Senior Phase" else generate_fet_question()
        
    q = st.session_state.curr_q
    
    st.markdown("<div class='dark-card'>", unsafe_allow_html=True)
    st.write(q["prompt"])
    st.latex(q["latex"])
    
    with st.form("learn_answer_form", clear_on_submit=True):
        user_input = st.text_input("Enter your calculated answer:")
        submitted = st.form_submit_button("Verify Answer")
        
        if submitted:
            is_correct = False
            if q.get("type") == "symbolic":
                try:
                    is_correct = sp.simplify(sp.sympify(user_input) - sp.sympify(q["answer_str"])) == 0
                except:
                    is_correct = False
            else:
                try:
                    is_correct = float(user_input) == float(q["answer"])
                except:
                    is_correct = False
                    
            if is_correct:
                st.success("💥 CRITICAL IMPACT! Core calibrated successfully.")
                st.session_state.xp += 20
                st.session_state.correct += 1
                st.session_state.curr_q = None
                time.sleep(0.7)
                st.rerun()
            else:
                st.error("❌ Hull Integrity Compromised. Review alternative calculations.")
                
    if st.button("Next Problem Wave ➔"):
        st.session_state.curr_q = None
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- PRACTICE TAB ---
elif st.session_state.nav_tab == "Practice":
    st.markdown("### ⚡ 60-SECOND SPEED-RUN CHALLENGE")
    st.session_state.diff = st.radio("SELECT DIFFICULTY TIER:", ["Easy", "Medium", "Hard", "Expert"], horizontal=True)
    
    st.markdown("<div class='dark-card'>", unsafe_allow_html=True)
    if not st.session_state.t_active:
        if st.button("▶ START PRACTICE SEQUENCE"):
            st.session_state.t_active = True
            st.session_state.t_start = time.time()
            st.session_state.t_score = 0
            q_data = generate_speedrun_question(st.session_state.diff)
            st.session_state.t_q = q_data["latex"]
            st.session_state.t_ans = q_data["answer"]
            st.rerun()
    else:
        elapsed = time.time() - st.session_state.t_start
        remaining = max(0, int(60 - elapsed))
        
        if remaining <= 0:
            st.error("⏰ TIMELINE COLLAPSED! Challenge Session Ended.")
            earned_xp = st.session_state.t_score * 5
            st.markdown(f"### Final Score: **{st.session_state.t_score} correct** (+{earned_xp} XP earned)")
            st.session_state.xp += earned_xp
            if st.button("Reboot Protocol"):
                st.session_state.t_active = False
                st.session_state.curr_q = None
                st.rerun()
        else:
            col_t, col_s = st.columns(2)
            col_t.metric("Time Remaining", f"{remaining}s")
            col_s.metric("Matrix Score", st.session_state.t_score)
            
            st.markdown("#### Solve Target Expression:")
            st.latex(f"{st.session_state.t_q} = ?")
            
            with st.form("speedrun_form", clear_on_submit=True):
                u_val = st.text_input("Integer Answer:")
                sub = st.form_submit_button("Submit Data")
                
                if sub:
                    try:
                        if int(u_val.strip()) == st.session_state.t_ans:
                            st.session_state.t_score += 1
                    except:
                        pass
                    q_data = generate_speedrun_question(st.session_state.diff)
                    st.session_state.t_q = q_data["latex"]
                    st.session_state.t_ans = q_data["answer"]
                    st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- PAPERS TAB ---
elif st.session_state.nav_tab == "Papers":
    st.markdown("### 📄 PAST EXAM PAPERS")
    grade_sel = st.selectbox("Select Grade Level", ["Gr 7", "Gr 8", "Gr 9", "Gr 10", "Gr 11", "Gr 12"])
    year_sel = st.selectbox("Select Year", ["All Years", "2018", "2019", "2020", "2021", "2022", "2023"])
    
    paper_list = [
        ("November Examination Paper 1", "100 marks", "No Calculator"),
        ("November Examination Paper 2", "150 marks", "Standard Calculator Allowed"),
        ("July Controlled Test", "25 marks", "Short Form"),
        ("June Mid-Year Examination", "50 marks", "Standard")
    ]
    
    for title, marks, notes in paper_list:
        st.markdown(f"""
        <div class="dark-card" style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <span style="color:#06b6d4; font-weight:bold;">{grade_sel}</span> — <strong>{title}</strong><br>
                <span style="font-size:12px; color:#94a3b8;">{marks} · {notes}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Download / Open {title[:12]}...", key=f"paper_{title}_{grade_sel}"):
            st.info(f"Opening {grade_sel} {title} document payload...")

# --- MEMOS TAB ---
elif st.session_state.nav_tab == "Memos":
    st.markdown("### 📝 EXAM MEMORANDUMS")
    st.markdown("Full step-by-step answers with working out and mark allocations.")
    
    memo_list = [
        ("November Paper 1 (Memo)", "63 detailed answers"),
        ("November Paper 2 (Memo)", "85 detailed answers"),
        ("July Controlled Test (Memo)", "20 detailed answers"),
        ("June Mid-Year Exam (Memo)", "33 detailed answers")
    ]
    
    for title, answers_count in memo_list:
        st.markdown(f"""
        <div class="dark-card">
            <strong style="color:#06b6d4;">{title}</strong><br>
            <span style="font-size:12px; color:#10b981;">✔ Available · {answers_count}</span>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"View {title}", key=f"memo_{title}"):
            st.success(f"Loading memorandum solutions for {title}...")

# --- BOARD TAB ---
elif st.session_state.nav_tab == "Board":
    st.markdown("### 🏆 HALL OF FAME & LEADERBOARD")
    st.markdown("Top performing mathematicians across the academy network this week.")
    
    st.markdown(f"""
    <div class="dark-card" style="border: 1px solid #fbbf24;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <span style="font-size:18px;">🥇</span> <strong>You (Master Explorer)</strong><br>
                <span style="font-size:12px; color:#94a3b8;">Rank #1 · 🔥 {st.session_state.streak} day streak</span>
            </div>
            <div style="text-align: right; color:#fbbf24; font-weight: bold; font-size: 16px;">
                🪙 {st.session_state.xp} XP
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.write("Simulated Academy Growth Trajectory:")
    sim_data = np.cumsum(np.random.randint(1, 8, size=8))
    fig, ax = plt.subplots(figsize=(8, 3))
    fig.patch.set_facecolor('#13112b')
    ax.set_facecolor('#13112b')
    ax.plot(sim_data, color='#00f2fe', marker='o', linewidth=2)
    ax.tick_params(colors='white')
    for spine in ax.spines.values():
        spine.set_color('#232046')
    st.pyplot(fig)

# --- PROFILE TAB ---
elif st.session_state.nav_tab == "Profile":
    st.markdown("### 👤 PLAYER PROFILE & SETTINGS")
    
    st.markdown(f"""
    <div class="dark-card" style="text-align: center; padding: 25px;">
        <div style="width: 70px; height: 70px; background: #8b5cf6; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 28px; font-weight: bold; margin: 0 auto 10px auto;">
            T
        </div>
        <h3 style="margin: 0;">tshepomalapane173</h3>
        <span style="font-size: 12px; color: #94a3b8;">Unique Code: 53B18C77</span>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Level", lvl)
    col2.metric("Total XP", st.session_state.xp)
    col3.metric("Streak", f"{st.session_state.streak} Days")
    col4.metric("Correct", st.session_state.correct)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### APP SETTINGS")
    st.toggle("Sound Effects (Pass/Fail tones)", value=True)
    st.toggle("Daily Practice Reminders", value=False)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚪 LOG OUT / RESET PROFILE"):
        st.session_state.xp = 754
        st.session_state.streak = 10
        st.session_state.correct = 6
        st.success("Profile data re-synchronized.")
        st.rerun()
      
