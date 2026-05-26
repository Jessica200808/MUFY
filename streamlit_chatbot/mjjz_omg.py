import random
import streamlit as st

# -----------------------------------------------------------------------------
# 1. CUTE APP THEME & DESIGN
# -----------------------------------------------------------------------------
# We configure the page and inject a bit of styling to make it look cozy and soft
st.set_page_config(page_title="CozySpace | Student Oasis", page_icon="☁️", layout="centered")

# Custom CSS to make buttons cute, round, and change background colors gently
st.markdown("""
    <style>
    /* Main background and font styling */
    .stApp { background-color: #FAF5F5; }
    h1, h2, h3 { color: #6D5D6E; font-family: 'Comic Sans MS', sans-serif; }
    
    /* Make buttons look soft and pastel purple */
    div.stButton > button:first-child {
        background-color: #E3DFFD;
        color: #463C51;
        border-radius: 20px;
        border: 1px solid #D1C9FF;
        font-weight: bold;
    }
    div.stButton > button:first-child:hover {
        background-color: #D1C9FF;
        color: #463C51;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. MOTIVATIONAL DATA BANK
# -----------------------------------------------------------------------------
STUDENT_QUOTES = [
    "🌸 ”You don't have to see the whole staircase, just take the first step.” — Martin Luther King Jr.",
    "🧸 ”It always seems impossible until it's done. You're doing great!”",
    "💫 ”Your worth is not defined by a exam grade. Breathe, you are learning and growing.”",
    "🌱 ”Progress over perfection. A little progress each day adds up to big results.”",
    "🧁 ”Be proud of how hard you are trying today.”"
]

STRESS_RELIEF_TIPS = [
    "Drop your shoulders right now and unclench your jaw. Take a deep breath... Hold it... and let it out. 🌬️",
    "Go drink a refreshing glass of water! Your brain needs hydration to stay happy. 💧",
    "Stand up and stretch your arms up high like a lazy cat for 15 seconds. 🐈",
    "Step away from the screen, look out the window, and find 3 blue things. Give your eyes a break! 👀",
    "Put on your favorite song right now and just dance or hum along for 3 minutes! 🎧"
]

# -----------------------------------------------------------------------------
# 3. APP MEMORY (Session State)
# -----------------------------------------------------------------------------
if "journal" not in st.session_state:
    st.session_state.journal = []
if "goals" not in st.session_state:
    st.session_state.goals = [
        {"task": "📚 Complete today's revision", "done": False},
        {"task": "💧 Drink 2 liters of water", "done": False}
    ]

# -----------------------------------------------------------------------------
# 4. MAIN APP INTERFACE
# -----------------------------------------------------------------------------

# Cute Header Banner
st.write("# ☁️ CozySpace")
st.write("##### *Your tiny, stress-free corner to breathe, track goals, and feel motivated.* 🍰")
st.write("---")

# Main Navigation Tabs
tab1, tab2, tab3 = st.tabs(["✨ Daily Motivate & Destress", "🎯 My Goals", "📝 Vent & Reflection"])

# --- TAB 1: DESTRESS & MOTIVATION ---
with tab1:
    st.write("### 🍯 Quick Mood Booster")
    st.write("Feeling overwhelmed with study? Let's take a tiny break.")
    
    # Stress Buster Button
    if st.button("🍩 Give me a Stress-Relief Tip!"):
        tip = random.choice(STRESS_RELIEF_TIPS)
        st.info(f"**Self-Care Reminder:** {tip}")
        
    st.write("---")
    st.write("### 🎒 Spark of Motivation")
    # Always display a random motivational quote to start the day
    if "current_quote" not in st.session_state:
        st.session_state.current_quote = random.choice(STUDENT_QUOTES)
        
    st.success(st.session_state.current_quote)
    
    if st.button("🔄 Change Quote"):
        st.session_state.current_quote = random.choice(STUDENT_QUOTES)
        st.rerun()

# --- TAB 2: CUTE BUCKET LIST / GOALS ---
with tab2:
    st.write("### 🐼 My Goal Tracker")
    st.write("Break your big tasks into tiny, bite-sized goals!")
    
    # Add a new goal
    new_goal = st.text_input("What do you want to achieve next?", placeholder="e.g., Finish math homework, Clean my desk...")
    if st.button("✨ Add to List"):
        if new_goal.strip():
            st.session_state.goals.append({"task": f"⭐ {new_goal}", "done": False})
            st.rerun()

    st.write("")
    st.write("##### Check off your victories:")
    
    # Render checkboxes
    for idx, item in enumerate(st.session_state.goals):
        checked = st.checkbox(item["task"], value=item["done"], key=f"goal_{idx}")
        
        # When a student checks a goal off
        if checked and not item["done"]:
            st.session_state.goals[idx]["done"] = True
            st.balloons() # Shoot celebration balloons!
            
            # Show a cute celebratory message
            celebration_quote = random.choice(STUDENT_QUOTES)
            st.success(f"🎉 **Yay! You did it!** Keep that momentum going! \n\n {celebration_quote}")
            
        elif not checked and item["done"]:
            st.session_state.goals[idx]["done"] = False

# --- TAB 3: VENT & REFLECTION JOURNAL ---
with tab3:
    st.write("### 📝 Brain Dump & Vent Space")
    st.write("Stressed out? Frustrated? Type it all out here to leave it behind, or write down things you are grateful for today.")
    
    entry_text = st.text_area("Dump your thoughts here...", placeholder="Nobody can see this but you. Let it all out...", height=150)
    
    if st.button("🔒 Lock Entry Into Diary"):
        if entry_text.strip():
            st.session_state.journal.append(entry_text)
            st.toast("Saved safely! 🧸")
            st.rerun()
            
    # Display diary entries down below
    if st.session_state.journal:
        st.write("---")
        st.write("##### 📔 My Past Reflections")
        for entry in reversed(st.session_state.journal):
            st.warning(f"💭 {entry}")