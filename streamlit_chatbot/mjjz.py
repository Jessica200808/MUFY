# ============================================
# LIFE COMPANION APP (NO AI VERSION)
# Python + Streamlit
#
# FEATURES:
# 1. Journal
# 2. Bucket List
# 3. Positive Quotes
#
# ============================================
# HOW TO RUN
#
# 1. Install Streamlit:
#    pip install streamlit
#
# 2. Create this folder structure:
#
#    life_app/
#    ├── app.py
#    └── data/
#         ├── journal.json
#         └── bucket_list.json
#
# 3. Put [] inside BOTH json files
#
# 4. Run app:
#    streamlit run app.py
#
# ============================================


# ============================================
# IMPORTS
# ============================================

import streamlit as st
import json
import random
from datetime import datetime


# ============================================
# FILE PATHS
# ============================================

JOURNAL_FILE = "data/journal.json"

BUCKET_FILE = "data/bucket_list.json"


# ============================================
# LOAD DATA FUNCTION
# ============================================

def load_data(file_path):
    """
    Load data from JSON file.
    """

    try:

        with open(file_path, "r") as file:

            return json.load(file)

    except:

        return []


# ============================================
# SAVE DATA FUNCTION
# ============================================

def save_data(file_path, data):
    """
    Save data into JSON file.
    """

    with open(file_path, "w") as file:

        json.dump(data, file, indent=4)


# ============================================
# POSITIVE QUOTES FUNCTION
# ============================================

def get_positive_quote():
    """
    Return random motivational quote.
    """

    quotes = [

        "You are stronger than you think.",

        "Small progress is still progress.",

        "Believe in yourself.",

        "Every day is a fresh start.",

        "Your future self will thank you.",

        "You can do hard things.",

        "Keep going. You are improving.",

        "Success begins with consistency."
    ]

    return random.choice(quotes)


# ============================================
# STREAMLIT PAGE SETTINGS
# ============================================

st.set_page_config(

    page_title="Life Companion App",

    page_icon="🌟",

    layout="centered"
)


# ============================================
# APP TITLE
# ============================================

st.title("🌟 Life Companion App")

st.write(
    "Write your journal, track your goals, "
    "and stay motivated."
)


# ============================================
# CREATE TABS
# ============================================

tab1, tab2 = st.tabs([
    "📔 Journal",
    "🎯 Bucket List"
])


# ====================================================
# JOURNAL TAB
# ====================================================

with tab1:

    st.header("Daily Journal")

    # Journal input
    journal_text = st.text_area(
        "Write about your day"
    )

    # Mood selection
    mood = st.selectbox(
        "Choose your mood",
        [
            "😊 Happy",
            "😐 Okay",
            "😔 Sad",
            "😡 Angry"
        ]
    )

    # Save button
    if st.button("Save Journal"):

        # Load old journal entries
        journal_entries = load_data(JOURNAL_FILE)

        # Add new journal entry
        journal_entries.append({

            "date": str(datetime.now()),

            "mood": mood,

            "text": journal_text
        })

        # Save updated entries
        save_data(JOURNAL_FILE, journal_entries)

        st.success("Journal saved successfully!")


    # ============================================
    # SHOW PREVIOUS ENTRIES
    # ============================================

    st.subheader("Previous Entries")

    journal_entries = load_data(JOURNAL_FILE)

    # Show newest entries first
    for entry in reversed(journal_entries):

        st.markdown(f"### 📅 {entry['date']}")

        st.write(entry["mood"])

        st.write(entry["text"])

        st.divider()


# ====================================================
# BUCKET LIST TAB
# ====================================================

with tab2:

    st.header("Bucket List")

    # Goal input
    new_goal = st.text_input(
        "Enter a new goal"
    )

    # Add goal button
    if st.button("Add Goal"):

        goals = load_data(BUCKET_FILE)

        # Add new goal
        goals.append({

            "goal": new_goal,

            "completed": False
        })

        # Save goals
        save_data(BUCKET_FILE, goals)

        st.success("Goal added!")


    # ============================================
    # SHOW GOALS
    # ============================================

    st.subheader("Your Goals")

    goals = load_data(BUCKET_FILE)

    # Loop through goals
    for i, goal in enumerate(goals):

        completed = st.checkbox(

            goal["goal"],

            value=goal["completed"],

            key=i
        )

        # If user completes goal
        if completed and not goal["completed"]:

            st.balloons()

            quote = get_positive_quote()

            st.success(
                f"🎉 Goal completed!\n\n✨ {quote}"
            )

        # Update completed status
        goals[i]["completed"] = completed


    # Save updated goals
    save_data(BUCKET_FILE, goals)