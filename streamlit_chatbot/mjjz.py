# ============================================
# LIFE COMPANION APP
# Python + Streamlit
#
# Features:
# 1. Journal
# 2. Bucket List
# 3. Positive Quotes
# 4. AI Support Chat
#
# HOW TO RUN:
#
# 1. Install libraries:
#    pip install streamlit openai
#
# 2. Create folders/files:
#
#    life_app/
#    ├── app.py
#    └── data/
#         ├── journal.json
#         └── bucket_list.json
#
# 3. Put [] inside both json files
#
# 4. Run:
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
from openai import OpenAI


# ============================================
# OPENAI API KEY
# ============================================

# Replace with your own API key
# Get API key from:
# https://platform.openai.com/

client = OpenAI(
    api_key="YOUR_API_KEY_HERE"
)


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
# RANDOM POSITIVE QUOTE
# ============================================

def get_positive_quote():
    """
    Return random motivational quote.
    """

    quotes = [

        "You are stronger than you think.",

        "Small progress is still progress.",

        "Believe in yourself.",

        "You can do hard things.",

        "Every day is a new beginning.",

        "Your future self will thank you.",

        "Keep going. You are improving.",

        "Success starts with consistency."
    ]

    return random.choice(quotes)


# ============================================
# AI CHAT FUNCTION
# ============================================

def ask_ai(user_message):
    """
    Send user message to AI.
    """

    try:

        response = client.chat.completions.create(

            model="gpt-4.1-mini",

            messages=[

                {
                    "role": "system",
                    "content": (
                        "You are a kind and supportive AI friend. "
                        "Help users with motivation, emotional support, "
                        "stress, productivity, and encouragement."
                    )
                },

                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"


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
    "Journal your thoughts, complete goals, "
    "and talk to AI for support."
)


# ============================================
# TABS
# ============================================

tab1, tab2, tab3 = st.tabs([
    "📔 Journal",
    "🎯 Bucket List",
    "🤖 AI Support"
])


# =====================================================
# JOURNAL TAB
# =====================================================

with tab1:

    st.header("Daily Journal")

    # User writes journal
    journal_text = st.text_area(
        "Write about your day"
    )

    # User mood
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

        # Load old entries
        journal_entries = load_data(JOURNAL_FILE)

        # Add new entry
        journal_entries.append({

            "date": str(datetime.now()),

            "mood": mood,

            "text": journal_text
        })

        # Save back to file
        save_data(JOURNAL_FILE, journal_entries)

        st.success("Journal saved!")


    # Show previous journal entries
    st.subheader("Previous Entries")

    journal_entries = load_data(JOURNAL_FILE)

    # Show newest first
    for entry in reversed(journal_entries):

        st.markdown(f"### 📅 {entry['date']}")

        st.write(entry["mood"])

        st.write(entry["text"])

        st.divider()


# =====================================================
# BUCKET LIST TAB
# =====================================================

with tab2:

    st.header("Bucket List")

    # Input new goal
    new_goal = st.text_input(
        "Enter a new goal"
    )

    # Add goal button
    if st.button("Add Goal"):

        goals = load_data(BUCKET_FILE)

        goals.append({

            "goal": new_goal,

            "completed": False
        })

        save_data(BUCKET_FILE, goals)

        st.success("Goal added!")


    # Show goals
    st.subheader("Your Goals")

    goals = load_data(BUCKET_FILE)

    # Loop through goals
    for i, goal in enumerate(goals):

        completed = st.checkbox(

            goal["goal"],

            value=goal["completed"],

            key=i
        )

        # If newly completed
        if completed and not goal["completed"]:

            st.balloons()

            quote = get_positive_quote()

            st.success(
                f"🎉 Goal completed!\n\n✨ {quote}"
            )

        # Update completion status
        goals[i]["completed"] = completed

    # Save updated goals
    save_data(BUCKET_FILE, goals)


# =====================================================
# AI SUPPORT TAB
# =====================================================

with tab3:

    st.header("Talk to AI")

    st.write(
        "Share your problems or feelings."
    )

    # User message
    user_problem = st.text_area(
        "What do you want help with?"
    )

    # AI button
    if st.button("Ask AI"):

        if user_problem.strip() != "":

            with st.spinner("AI is thinking..."):

                ai_response = ask_ai(user_problem)

            st.markdown("### 🤖 AI Response")

            st.write(ai_response)

        else:

            st.warning("Please type something.")