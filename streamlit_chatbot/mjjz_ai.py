import streamlit as st
import random
from datetime import datetime


# =========================================
# PAGE SETTINGS
# =========================================

st.set_page_config(
    page_title="Life Companion",
    page_icon="🌟",
    layout="centered"
)


# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

.main {
    background-color: #0f172a;
    color: white;
}

h1, h2, h3 {
    color: #f8fafc;
}

.stButton button {
    background-color: #8b5cf6;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px;
    font-weight: bold;
}

.stTextArea textarea {
    border-radius: 10px;
}

.stTextInput input {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# =========================================
# SESSION STORAGE
# =========================================

if "journals" not in st.session_state:
    st.session_state.journals = []

if "goals" not in st.session_state:
    st.session_state.goals = []


# =========================================
# POSITIVE QUOTES
# =========================================

quotes = [

    "You are capable of amazing things.",

    "Small progress is still progress.",

    "Believe in yourself.",

    "Your future is bright.",

    "Every day is a second chance.",

    "You can do difficult things.",

    "Keep showing up for yourself.",

    "Growth takes time."
]


# =========================================
# SIDEBAR
# =========================================

st.sidebar.title("🌟 Navigation")

page = st.sidebar.radio(

    "Go to:",

    [
        "🏠 Home",
        "📔 Journal",
        "🎯 Bucket List",
        "✨ Motivation"
    ]
)


# =========================================
# HOME PAGE
# =========================================

if page == "🏠 Home":

    st.title("🌟 Life Companion")

    st.write(
        "A self-care app to help you track goals, "
        "write journals, and stay motivated."
    )

    st.image(
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
        use_container_width=True
    )

    st.subheader("📊 Your Progress")

    total_goals = len(st.session_state.goals)

    completed_goals = 0

    for goal in st.session_state.goals:

        if goal["completed"]:
            completed_goals += 1

    # Prevent division error
    if total_goals > 0:

        progress = completed_goals / total_goals

        st.progress(progress)

        st.write(
            f"{completed_goals} out of "
            f"{total_goals} goals completed"
        )

    else:
        st.write("No goals added yet.")


# =========================================
# JOURNAL PAGE
# =========================================

elif page == "📔 Journal":

    st.title("📔 Daily Journal")

    mood = st.select_slider(

        "How are you feeling today?",

        options=[
            "😔",
            "😐",
            "😊",
            "😁"
        ]
    )

    journal_text = st.text_area(
        "Write your thoughts"
    )

    if st.button("Save Journal"):

        st.session_state.journals.append({

            "date": str(datetime.now()),

            "mood": mood,

            "text": journal_text
        })

        st.success("Journal saved successfully!")


    st.subheader("📚 Previous Entries")

    for entry in reversed(st.session_state.journals):

        st.markdown(
            f"### {entry['mood']} {entry['date']}"
        )

        st.write(entry["text"])

        st.divider()


# =========================================
# BUCKET LIST PAGE
# =========================================

elif page == "🎯 Bucket List":

    st.title("🎯 Bucket List")

    new_goal = st.text_input(
        "Add a new goal"
    )

    if st.button("Add Goal"):

        st.session_state.goals.append({

            "goal": new_goal,

            "completed": False
        })

        st.success("Goal added!")


    st.subheader("Your Goals")

    for i, goal in enumerate(st.session_state.goals):

        checked = st.checkbox(

            goal["goal"],

            value=goal["completed"],

            key=i
        )

        # Goal completed
        if checked and not goal["completed"]:

            st.balloons()

            quote = random.choice(quotes)

            st.success(
                f"🎉 Goal completed!\n\n✨ {quote}"
            )

        st.session_state.goals[i]["completed"] = checked


# =========================================
# MOTIVATION PAGE
# =========================================

elif page == "✨ Motivation":

    st.title("✨ Daily Motivation")

    st.write(
        "Click the button for a positive quote."
    )

    if st.button("Generate Quote"):

        quote = random.choice(quotes)

        st.success(f"💜 {quote}")

    st.image(
        "https://images.unsplash.com/photo-1490750967868-88aa4486c946",
        use_container_width=True
    )