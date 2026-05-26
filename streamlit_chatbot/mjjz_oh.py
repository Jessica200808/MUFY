# =========================================
# CUTE JOURNAL & BUCKET LIST APP 🌸
# Beginner Friendly Streamlit App
# =========================================

import streamlit as st
import random

# =========================================
# PAGE SETTINGS
# =========================================

st.set_page_config(
    page_title="My Happy Space 🌸",
    page_icon="🌸"
)

# =========================================
# SESSION STORAGE
# =========================================

# Create empty journal list if not exist
if "journals" not in st.session_state:
    st.session_state.journals = []

# Create empty goals list if not exist
if "goals" not in st.session_state:
    st.session_state.goals = []

# =========================================
# MOTIVATIONAL QUOTES
# =========================================

quotes = [
    "🌸 You are doing amazing!",
    "💖 Keep believing in yourself!",
    "✨ Small progress is still progress.",
    "🌈 Better days are coming.",
    "☀️ Keep shining!",
    "🦋 You can do it!"
]

# =========================================
# TITLE
# =========================================

st.title("🌸 My Happy Space")

st.write("A cute place for your thoughts and dreams 💖")

# =========================================
# DAILY MOTIVATION
# =========================================

st.header("✨ Daily Motivation")

st.info(random.choice(quotes))

# =========================================
# JOURNAL SECTION
# =========================================

st.header("📖 Journal")

journal_text = st.text_area(
    "Write about your day 🌷"
)

if st.button("💾 Save Journal"):

    if journal_text != "":

        st.session_state.journals.append(journal_text)

        st.success("Journal saved 💖")

# =========================================
# SHOW JOURNALS
# =========================================

if st.session_state.journals:

    st.subheader("🌸 Previous Journal Entries")

    for entry in reversed(st.session_state.journals):

        st.write("💌", entry)

# =========================================
# BUCKET LIST SECTION
# =========================================

st.header("🎯 Bucket List")

goal_text = st.text_input(
    "Add your dream or goal 🌈"
)

if st.button("➕ Add Goal"):

    if goal_text != "":

        st.session_state.goals.append({
            "task": goal_text,
            "done": False
        })

        st.success("Goal added 🌟")

# =========================================
# SHOW GOALS
# =========================================

if st.session_state.goals:

    st.subheader("💖 My Goals")

    for i, goal in enumerate(st.session_state.goals):

        checked = st.checkbox(
            goal["task"],
            value=goal["done"],
            key=i
        )

        # If completed
        if checked and goal["done"] == False:

            st.session_state.goals[i]["done"] = True

            st.balloons()

            st.success("🎉 Goal completed!")

            st.info(random.choice(quotes))

# =========================================
# FOOTER
# =========================================

st.write("---")

st.caption(
    "🌷 Remember: You are enough just as you are 💖"
)