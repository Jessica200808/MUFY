# =====================================================
# CUTE JOURNAL & BUCKET LIST APP 🌸
# Python + Streamlit
# Beginner Friendly Version
# =====================================================

# Import libraries
import streamlit as st
import json
import random
from datetime import datetime

# =====================================================
# PAGE SETTINGS
# =====================================================

st.set_page_config(
    page_title="My Happy Space 🌸",
    page_icon="🌸",
    layout="centered"
)

# =====================================================
# FILE NAMES
# =====================================================

JOURNAL_FILE = "journals.json"
GOAL_FILE = "goals.json"

# =====================================================
# MOTIVATIONAL QUOTES
# =====================================================

quotes = [
    "🌷 You are doing better than you think.",
    "✨ Small progress is still progress.",
    "💖 Your dreams matter.",
    "🌈 Every day is a fresh start.",
    "🦋 Believe in yourself.",
    "🌸 You are growing beautifully.",
    "☀️ Keep shining!",
    "💪 You can do hard things.",
    "🌟 One step at a time.",
    "💕 Be proud of yourself."
]

# =====================================================
# MOOD MESSAGES
# =====================================================

mood_messages = {
    "😊 Happy":
        "Keep spreading your happiness 🌞",

    "😴 Tired":
        "Rest is important too 💖",

    "😢 Sad":
        "Bad days don't last forever 🌈",

    "😡 Angry":
        "Take a deep breath 🌸",

    "😰 Stressed":
        "You are stronger than your stress 💪"
}

# =====================================================
# HELPER FUNCTIONS
# =====================================================

def load_data(filename):
    """
    Load data from JSON file.
    If file doesn't exist, return empty list.
    """

    try:
        with open(filename, "r") as file:
            return json.load(file)

    except:
        return []


def save_data(filename, data):
    """
    Save data into JSON file.
    """

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def add_journal(text, mood):
    """
    Add journal entry into file.
    """

    journals = load_data(JOURNAL_FILE)

    entry = {
        "date": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "mood": mood,
        "text": text
    }

    journals.append(entry)

    save_data(JOURNAL_FILE, journals)


def add_goal(goal):
    """
    Add a bucket list goal.
    """

    goals = load_data(GOAL_FILE)

    new_goal = {
        "task": goal,
        "completed": False
    }

    goals.append(new_goal)

    save_data(GOAL_FILE, goals)


def complete_goal(index):
    """
    Mark goal as completed.
    Return motivational quote.
    """

    goals = load_data(GOAL_FILE)

    goals[index]["completed"] = True

    save_data(GOAL_FILE, goals)

    return random.choice(quotes)


# =====================================================
# APP TITLE
# =====================================================

st.title("🌸 My Happy Space")
st.write("Your safe place for journaling, dreams, and motivation 💖")

# =====================================================
# DAILY MOTIVATION
# =====================================================

st.header("🌟 Daily Motivation")

daily_quote = random.choice(quotes)

st.info(daily_quote)

# =====================================================
# MOOD CHECK-IN
# =====================================================

st.header("💭 How Are You Feeling Today?")

selected_mood = st.selectbox(
    "Choose your mood:",
    [
        "😊 Happy",
        "😴 Tired",
        "😢 Sad",
        "😡 Angry",
        "😰 Stressed"
    ]
)

st.success(mood_messages[selected_mood])

# =====================================================
# JOURNAL SECTION
# =====================================================

st.header("📖 My Journal")

journal_text = st.text_area(
    "Write about your day 🌷"
)

if st.button("💾 Save Journal"):

    if journal_text.strip() != "":

        add_journal(journal_text, selected_mood)

        st.success("Journal saved successfully 💖")

# =====================================================
# SHOW JOURNALS
# =====================================================

journals = load_data(JOURNAL_FILE)

if journals:

    st.subheader("🌸 Previous Journal Entries")

    for entry in reversed(journals):

        st.markdown(f"""
        💕 **Date:** {entry["date"]}

        😊 **Mood:** {entry["mood"]}

        ✨ {entry["text"]}

        ---
        """)

# =====================================================
# BUCKET LIST SECTION
# =====================================================

st.header("🎯 My Bucket List")

goal_text = st.text_input(
    "Add your dream or goal 🌈"
)

if st.button("➕ Add Goal"):

    if goal_text.strip() != "":

        add_goal(goal_text)

        st.success("Goal added 🌟")

# =====================================================
# SHOW GOALS
# =====================================================

goals = load_data(GOAL_FILE)

if goals:

    st.subheader("💖 My Goals")

    completed_count = 0

    for i, goal in enumerate(goals):

        checked = st.checkbox(
            goal["task"],
            value=goal["completed"],
            key=i
        )

        if checked:
            completed_count += 1

        # First time completed
        if checked and goal["completed"] == False:

            quote = complete_goal(i)

            st.balloons()

            st.success("🎉 Goal completed!")

            st.info(quote)

# =====================================================
# PROGRESS SECTION
# =====================================================

st.header("📊 Progress Tracker")

total_goals = len(goals)

if total_goals > 0:

    progress = completed_count / total_goals

    st.progress(progress)

    st.write(
        f"✨ You completed {completed_count} out of {total_goals} goals!"
    )

else:
    st.write("No goals yet 🌸")

# =====================================================
# CUTE FOOTER
# =====================================================

st.write("---")

st.caption(
    "🌷 Remember: You don't need to be perfect to make progress 💖"
)