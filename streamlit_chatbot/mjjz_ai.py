import streamlit as st
import random
from datetime import datetime


# ==============================
# PAGE SETUP
# ==============================

st.set_page_config(
    page_title="Life App",
    page_icon="🌟",
    layout="centered"
)

st.title("🌟 My Life App")
st.write("Journal • Goals • Motivation")


# ==============================
# SESSION STORAGE (IMPORTANT)
# ==============================

if "journals" not in st.session_state:
    st.session_state.journals = []

if "goals" not in st.session_state:
    st.session_state.goals = []


# ==============================
# QUOTES
# ==============================

quotes = [
    "You are doing better than you think.",
    "Small steps matter.",
    "Keep going, don’t give up.",
    "You are stronger than yesterday.",
    "Progress takes time.",
    "Believe in yourself."
]


# ==============================
# TABS
# ==============================

tab1, tab2, tab3 = st.tabs([
    "📔 Journal",
    "🎯 Bucket List",
    "✨ Motivation"
])


# ==============================
# JOURNAL TAB
# ==============================

with tab1:

    st.subheader("Write your journal")

    mood = st.selectbox(
        "Mood",
        ["😊 Happy", "😐 Okay", "😔 Sad", "😡 Angry"]
    )

    text = st.text_area("What happened today?")

    if st.button("Save Journal"):

        if text.strip() != "":

            st.session_state.journals.append({
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "mood": mood,
                "text": text
            })

            st.success("Saved!")
        else:
            st.warning("Write something first!")

    st.divider()

    st.subheader("Past Journals")

    for j in reversed(st.session_state.journals):

        st.write(f"**{j['mood']} | {j['date']}**")
        st.write(j["text"])
        st.divider()


# ==============================
# BUCKET LIST TAB
# ==============================

with tab2:

    st.subheader("Add your goals")

    goal = st.text_input("New goal")

    if st.button("Add Goal"):

        if goal.strip() != "":

            st.session_state.goals.append({
                "goal": goal,
                "done": False
            })

            st.success("Goal added!")
        else:
            st.warning("Write a goal first!")

    st.divider()

    st.subheader("Your Goals")

    for i, g in enumerate(st.session_state.goals):

        checked = st.checkbox(
            g["goal"],
            value=g["done"],
            key=i
        )

        if checked and not g["done"]:
            st.balloons()
            st.success(random.choice(quotes))

        st.session_state.goals[i]["done"] = checked


# ==============================
# MOTIVATION TAB
# ==============================

with tab3:

    st.subheader("Daily Motivation")

    if st.button("Get Quote"):

        st.success(random.choice(quotes))

    st.info("Stay consistent. You are improving every day.")