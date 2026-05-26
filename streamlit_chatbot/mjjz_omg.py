import random
import streamlit as st

# -----------------------------------------------------------------------------
# 1. APP CONFIGURATION & PRE-MADE QUOTES
# -----------------------------------------------------------------------------

# Set up the title of the browser tab and page layout
st.set_page_config(page_title="My Daily Space", page_icon="🌱")

# A list of positive quotes to reward you when completing a goal
POSITIVE_QUOTES = [
    "“The future belongs to those who believe in the beauty of their dreams.” – Eleanor Roosevelt",
    "“Every accomplishment starts with the decision to try.” – John F. Kennedy",
    "“Don't count the days, make the days count.” – Muhammad Ali",
    "“You are never too old to set another goal or to dream a new dream.” – C.S. Lewis",
    "“Believe you can and you're halfway there.” – Theodore Roosevelt",
    "“Cheers to a new achievement! Keep chasing what sets your soul on fire.” ✨"
]

# -----------------------------------------------------------------------------
# 2. APPLICATION MEMORY (Session State)
# -----------------------------------------------------------------------------
# Streamlit re-runs the code from top to bottom every time you click something.
# We use st.session_state so the app "remembers" your data and doesn't erase it.

if "journal_entries" not in st.session_state:
    st.session_state.journal_entries = []
    
if "bucket_list" not in st.session_state:
    # Starting with two example items already in your list
    st.session_state.bucket_list = [
        {"task": "Learn Python", "completed": False},
        {"task": "Build my first web app", "completed": False}
    ]

# -----------------------------------------------------------------------------
# 3. MAIN APP INTERFACE
# -----------------------------------------------------------------------------

st.title("🌱 My Daily Space")
st.write("Welcome! Use this space to log your thoughts and track your goals.")

# Create two simple tabs at the top of the page
tab1, tab2 = st.tabs(["📝 Journal", "🎯 Bucket List"])

# --- TAB 1: JOURNAL ---
with tab1:
    st.subheader("Personal Journal")
    
    # 1. Input: Box for typing your entry
    user_entry = st.text_area("What's on your mind today?", placeholder="Start writing here...", height=150)
    
    # 2. Action: Save button
    if st.button("Save Entry", type="primary"):
        if user_entry.strip() != "":  # Make sure they actually typed something
            st.session_state.journal_entries.append(user_entry)
            st.success("Saved successfully!")
        else:
            st.warning("Please write something before saving.")
            
    # 3. Output: Display past entries if there are any
    if st.session_state.journal_entries:
        st.write("### Past Entries")
        # We use reversed() so the newest entries show up at the very top
        for entry in reversed(st.session_state.journal_entries):
            st.info(entry)


# --- TAB 2: BUCKET LIST ---
with tab2:
    st.subheader("My Bucket List")
    
    # 1. Input: Box to type a new goal
    new_goal = st.text_input("Add a new goal:", placeholder="e.g., Skydiving, Learn to cook...")
    
    if st.button("Add to List"):
        if new_goal.strip() != "":
            st.session_state.bucket_list.append({"task": new_goal, "completed": False})
            st.rerun() # Refresh the page immediately to show the new goal
            
    st.write("### Check off your achievements:")
    
    # 2. Output & Logic: Display checkboxes for each goal
    for idx, item in enumerate(st.session_state.bucket_list):
        
        # Display the checkbox. Its checked status comes from our memory (item["completed"])
        checked = st.checkbox(item["task"], value=item["completed"], key=f"goal_{idx}")
        
        # If the user clicks a checkbox that WAS NOT completed yet:
        if checked and not item["completed"]:
            st.session_state.bucket_list[idx]["completed"] = True
            
            # Pick a random quote and show a big celebration banner!
            celebration_quote = random.choice(POSITIVE_QUOTES)
            st.balloons() # Shoots visual balloons up the screen!
            st.success(f"🎉 **Goal Completed!** Here is your quote:\n\n{celebration_quote}")
            
        # If the user unchecks a box, mark it as incomplete again
        elif not checked and item["completed"]:
            st.session_state.bucket_list[idx]["completed"] = False