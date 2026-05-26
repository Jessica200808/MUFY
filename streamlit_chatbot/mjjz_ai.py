import streamlit as st
import random
from datetime import datetime


# =====================================================
# PAGE SETUP
# =====================================================

st.set_page_config(
    page_title="Life Companion Pro",
    page_icon="🌟",
    layout="wide"
)


# =====================================================
# SESSION STATE INIT
# =====================================================

if "journals" not in st.session_state:
    st.session_state.journals = []

if "goals" not in st.session_state:
    st.session_state.goals = []


# =====================================================
# MOTIVATIONAL QUOTES
# =====================================================

QUOTES = [
    "You are doing better than you think.",
    "Small steps every day lead to big results.",
    "Believe in your ability to grow.",
    "Consistency beats motivation.",
    "You can restart anytime.",
    "Progress, not perfection.",
    "Your future self will thank you."
]


# =====================================================
# SIDEBAR NAVIGATION
# =====================================================

st.sidebar.title("🌟 Life Companion Pro")

page = st.sidebar.radio(
    "Navigate",
    ["🏠 Dashboard", "📔 Journal", "🎯 Bucket List", "✨ Motivation"]
)


# =====================================================
# DASHBOARD
# =====================================================

if page == "🏠 Dashboard":

    st.title("🌟 Dashboard")

    st.write("Your personal growth overview")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📔 Journals", len(st.session_state.journals))

    with col2:
        completed = sum(1 for g in st.session_state.goals if g["done"])
        st.metric("🎯 Completed Goals", completed)

    st.divider()

    st.subheader("📊 Progress")

    total = len(st.session_state.goals)

    if total == 0:
        st.info("Add goals to see progress")
    else:
        progress = completed / total
        st.progress(progress)

        st.write(f"{completed}/{total} goals completed")


# =====================================================
# JOURNAL PAGE
# =====================================================

elif page == "📔 Journal":

    st.title("📔 Journal")

    mood = st.selectbox(
        "Mood",
        ["😊 Happy", "😐 Neutral", "😔 Sad", "😡 Angry", "🤯 Stressed"]
    )

    text = st.text_area("Write your thoughts")

    if st.button("Save Journal"):

        if text.strip():

            st.session_state.journals.append({
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "mood": mood,
                "text": text
            })

            st.success("Saved!")
        else:
            st.warning("Write something first")

    st.divider()

    st.subheader("Previous Entries")

    for j in reversed(st.session_state.journals):

        with st.container():
            st.write(f"**{j['mood']} | {j['date']}**")
            st.write(j["text"])
            st.divider()


# =====================================================
# BUCKET LIST PAGE
# =====================================================

elif page == "🎯 Bucket List":

    st.title("🎯 Bucket List")

    new_goal = st.text_input("Add a new goal")

    if st.button("Add Goal"):

        if new_goal.strip():

            st.session_state.goals.append({
                "goal": new_goal,
                "done": False
            })

            st.success("Goal added!")
        else:
            st.warning("Type a goal first")

    st.divider()

    st.subheader("Your Goals")

    for i, g in enumerate(st.session_state.goals):

        col1, col2 = st.columns([0.8, 0.2])

        with col1:
            done = st.checkbox(g["goal"], value=g["done"], key=i)

        with col2:
            if done and not g["done"]:
                st.balloons()
                st.success(random.choice(QUOTES))

        st.session_state.goals[i]["done"] = done


# =====================================================
# MOTIVATION PAGE
# =====================================================

elif page == "✨ Motivation":

    st.title("✨ Daily Motivation")

    st.write("Get a boost of positivity")

    if st.button("Generate Quote"):

        st.success(random.choice(QUOTES))

    st.divider()

    st.subheader("💡 Tip of the Day")

    tips = [
        "Drink water regularly",
        "Write your thoughts daily",
        "Take short breaks",
        "Focus on one task at a time",
        "Sleep at consistent times"
    ]

    st.info(random.choice(tips))