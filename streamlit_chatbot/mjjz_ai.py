import streamlit as st
import random
from datetime import datetime


# ======================================
# PAGE SETTINGS
# ======================================

st.set_page_config(
    page_title="My Life App",
    page_icon="🌟"
)


# ======================================
# APP TITLE
# ======================================

st.title("🌟 My Life App")

st.write(
    "Write journals, track goals, "
    "and stay motivated!"
)


# ======================================
# SESSION STORAGE
# ======================================

# Create journal list if it doesn't exist
if "journals" not in st.session_state:
    st.session_state.journals = []

# Create bucket list if it doesn't exist
if "goals" not in st.session_state:
    st.session_state.goals = []


# ======================================
# POSITIVE QUOTES
# ======================================

quotes = [

    "You are amazing.",

    "Keep going.",

    "Small progress matters.",

    "Believe in yourself.",

    "You can do hard things.",

    "Every day is a fresh start."
]


# ======================================
# CREATE TABS
# ======================================

tab1, tab2 = st.tabs([
    "📔 Journal",
    "🎯 Bucket List"
])


# ======================================
# JOURNAL TAB
# ======================================

with tab1:

    st.header("Daily Journal")

    # User writes journal
    journal_text = st.text_area(
        "Write about your day"
    )

    # Mood dropdown
    mood = st.selectbox(
        "Choose your mood",
        [
            "😊 Happy",
            "😐 Okay",
            "😔 Sad",
            "😡 Angry"
        ]
    )

    # Save journal button
    if st.button("Save Journal"):

        st.session_state.journals.append({

            "date": str(datetime.now()),

            "mood": mood,

            "text": journal_text
        })

        st.success("Journal saved!")


    # Show previous journals
    st.subheader("Previous Entries")

    for entry in reversed(st.session_state.journals):

        st.markdown(f"### 📅 {entry['date']}")

        st.write(entry["mood"])

        st.write(entry["text"])

        st.divider()


# ======================================
# BUCKET LIST TAB
# ======================================

with tab2:

    st.header("Bucket List")

    # Goal input
    goal = st.text_input(
        "Enter a new goal"
    )

    # Add goal button
    if st.button("Add Goal"):

        st.session_state.goals.append({

            "goal": goal,

            "completed": False
        })

        st.success("Goal added!")


    # Show goals
    st.subheader("Your Goals")

    for i, item in enumerate(st.session_state.goals):

        checked = st.checkbox(
            item["goal"],
            value=item["completed"],
            key=i
        )

        # If goal completed
        if checked and not item["completed"]:

            st.balloons()

            quote = random.choice(quotes)

            st.success(
                f"🎉 Goal completed!\n\n✨ {quote}"
            )

        # Update status
        st.session_state.goals[i]["completed"] = checked