# =====================================
# SIMPLE JOURNAL & BUCKET LIST APP
# Using Python + Streamlit
# =====================================

# Import libraries
import streamlit as st
import json
import random

# =====================================
# FILE NAMES
# =====================================

JOURNAL_FILE = "journals.json"
BUCKET_FILE = "bucket_list.json"

# =====================================
# POSITIVE QUOTES
# =====================================

quotes = [
    "Great job! Keep going!",
    "You are doing amazing!",
    "One step at a time!",
    "You can achieve your dreams!",
    "Success starts with small progress.",
    "Believe in yourself!"
]

# =====================================
# HELPER FUNCTIONS
# =====================================

def load_data(filename):
    """
    Load data from JSON file.
    If file does not exist, return empty list.
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


def add_journal(entry):
    """
    Add a journal entry.
    """

    journals = load_data(JOURNAL_FILE)

    journals.append(entry)

    save_data(JOURNAL_FILE, journals)


def add_goal(goal):
    """
    Add a bucket list goal.
    """

    goals = load_data(BUCKET_FILE)

    new_goal = {
        "task": goal,
        "completed": False
    }

    goals.append(new_goal)

    save_data(BUCKET_FILE, goals)


def complete_goal(index):
    """
    Mark goal as completed.
    """

    goals = load_data(BUCKET_FILE)

    goals[index]["completed"] = True

    save_data(BUCKET_FILE, goals)

    # Return random positive quote
    return random.choice(quotes)


# =====================================
# STREAMLIT APP
# =====================================

st.title("🌸 My Simple Journal App")

# =====================================
# JOURNAL SECTION
# =====================================

st.header("📖 Journal")

journal_text = st.text_area(
    "Write your journal:"
)

if st.button("Save Journal"):

    if journal_text != "":
        add_journal(journal_text)

        st.success("Journal saved!")

# Show previous journals
journals = load_data(JOURNAL_FILE)

if journals:

    st.subheader("Your Journal Entries")

    for entry in journals:
        st.write("•", entry)

# =====================================
# BUCKET LIST SECTION
# =====================================

st.header("🎯 Bucket List")

goal_text = st.text_input(
    "Add a goal:"
)

if st.button("Add Goal"):

    if goal_text != "":
        add_goal(goal_text)

        st.success("Goal added!")

# Show goals
goals = load_data(BUCKET_FILE)

if goals:

    st.subheader("Your Goals")

    for i, goal in enumerate(goals):

        checked = st.checkbox(
            goal["task"],
            value=goal["completed"],
            key=i
        )

        # If checked for first time
        if checked and goal["completed"] == False:

            quote = complete_goal(i)

            st.success("Goal completed!")
            st.info(quote)