# import streamlit as st
# import sqlite3
# import time
# import google.generativeai as genai

# # Initialize Gemini API
# genai.configure(api_key="AIzaSyByLOZAmBso2PXKwA-rt9t0bs3YOBJyxY4")

# def generate_gemini_question(prompt):
#     model = genai.GenerativeModel("gemini-1.5-pro-latest")
#     response = model.generate_content(prompt)
#     return response.text if hasattr(response, "text") else "No response generated"

# # Initialize Database
# def init_db():
#     conn = sqlite3.connect("clinical_trials.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT UNIQUE,
#             score INTEGER DEFAULT 0
#         )
#     """)
#     conn.commit()
#     conn.close()

# # Function to update score
# def update_score(name, points):
#     conn = sqlite3.connect("clinical_trials.db")
#     cursor = conn.cursor()
    
#     cursor.execute("SELECT score FROM users WHERE name = ?", (name,))
#     existing_score = cursor.fetchone()
    
#     if existing_score:
#         new_score = existing_score[0] + points
#         cursor.execute("UPDATE users SET score = ? WHERE name = ?", (new_score, name))
#     else:
#         cursor.execute("INSERT INTO users (name, score) VALUES (?, ?)", (name, points))
    
#     conn.commit()
#     conn.close()

# # Welcome Screen
# def welcome():
#     st.title("🧪 Welcome to Clinical Trials Adventure!")
#     st.write("""
#     Imagine you're a scientist testing a **new superhero medicine**!
#     Your job is to **test it step by step** to make sure it's safe for everyone.
    
#     Are you ready to begin your adventure? 🚀
#     """)
    
#     name = st.text_input("Enter your name:")
#     if st.button("Start Game") and name:
#         st.session_state["name"] = name
#         st.session_state["score"] = 0
#         st.session_state["page"] = "phase1"
#         st.rerun()

# # Function to display progress bar
# def show_progress():
#     phases = ["phase1", "phase2", "phase3", "phase4", "phase5", "phase6"]
#     progress = (phases.index(st.session_state["page"]) + 1) / len(phases)
#     st.progress(progress)

# # Function to handle phases
# def phase(number, description, question, options, correct_option, next_phase):
#     show_progress()
#     st.title(f"🧪 Clinical Trials - Phase {number}")
#     st.write(description)
    
#     answer = st.radio("Choose the correct answer:", options, index=None)
    
#     if st.button("Submit Answer") and answer:
#         if answer == correct_option:
#             st.success("Correct! 🎉")
#             update_score(st.session_state["name"], 10)
#         else:
#             st.error("Oops! Try again.")
        
#         time.sleep(1)
#         st.session_state["page"] = next_phase
#         st.rerun()

# # Define all phases
# def phase1():
#     phase(1, "**Scenario:** You are in a lab testing a new medicine on **healthy volunteers**. Your goal is to check if it’s safe.",
#           "What is the main goal of Phase 1 trials?",
#           ["To find out if the medicine works", "To test if the medicine is safe", "To sell the medicine in stores"],
#           "To test if the medicine is safe", "phase2")

# def phase2():
#     phase(2, "**Scenario:** The medicine is safe! Now, you must test it on a larger group of **patients** to check if it works.",
#           "What is the primary goal of Phase 2 trials?",
#           ["To test if the medicine is safe", "To check how well the medicine works", "To distribute the medicine worldwide"],
#           "To check how well the medicine works", "phase3")

# def phase3():
#     phase(3, "**Scenario:** Now, it’s time to test the medicine on **thousands of people** to confirm its effectiveness and safety.",
#           "What is a key aspect of Phase 3 trials?",
#           ["To confirm the medicine’s effectiveness on a large scale", "To test on a few people", "To stop testing and sell the medicine"],
#           "To confirm the medicine’s effectiveness on a large scale", "phase4")

# def phase4():
#     phase(4, "**Scenario:** The medicine is approved! Now, you must **monitor** it in real-world conditions.",
#           "What is the purpose of Phase 4 trials?",
#           ["To test if the medicine is safe", "To monitor long-term effects and safety", "To stop research and move on"],
#           "To monitor long-term effects and safety", "phase5")

# def phase5():
#     generated_question = generate_gemini_question("Generate a clinical trial-related question for Phase 5 testing.")
#     phase(5, "**Scenario:** You are investigating rare side effects that might show up years later.",
#           generated_question,
#           ["To check for side effects", "To distribute worldwide", "To stop monitoring"],
#           "To check for side effects", "phase6")

# def phase6():
#     generated_question = generate_gemini_question("Generate a clinical trial-related question for Phase 6 real-world impact.")
#     phase(6, "**Scenario:** You are evaluating real-world patient outcomes years after approval.",
#           generated_question,
#           ["To improve future medicine", "To stop trials", "To focus only on profits"],
#           "To improve future medicine", "leaderboard")

# # Leaderboard
# def leaderboard():
#     st.title("🏆 Leaderboard")
#     conn = sqlite3.connect("clinical_trials.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT name, score FROM users ORDER BY score DESC LIMIT 10")
#     rows = cursor.fetchall()
#     conn.close()
    
#     for name, score in rows:
#         st.write(f"{name}: {score} points")

# # Main function
# def main():
#     init_db()
#     if "page" not in st.session_state:
#         welcome()
#     else:
#         globals()[st.session_state["page"]]()

# if __name__ == "__main__":
#     main()

import streamlit as st
import sqlite3
import time

# Initialize Database
def init_db():
    conn = sqlite3.connect("clinical_trials.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            score INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

# Function to update score
def update_score(name, points):
    conn = sqlite3.connect("clinical_trials.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT score FROM users WHERE name = ?", (name,))
    existing_score = cursor.fetchone()
    
    if existing_score:
        new_score = existing_score[0] + points
        cursor.execute("UPDATE users SET score = ? WHERE name = ?", (new_score, name))
    else:
        cursor.execute("INSERT INTO users (name, score) VALUES (?, ?)", (name, points))
    
    conn.commit()
    conn.close()

# Welcome Screen
def welcome():
    st.title("🧪 Welcome to Clinical Trials Adventure!")
    st.write("""
    Imagine you're a scientist testing a **new superhero medicine**!
    Your job is to **test it step by step** to make sure it's safe for everyone.
    
    Are you ready to begin your adventure? 🚀
    """)
    
    name = st.text_input("Enter your name:")
    if st.button("Start Game") and name:
        st.session_state["name"] = name
        st.session_state["score"] = 0
        st.session_state["page"] = "phase1"
        st.rerun()

# Function to display progress bar
def show_progress():
    phases = ["phase1", "phase2", "phase3", "phase4"]
    progress = (phases.index(st.session_state["page"]) + 1) / len(phases)
    st.progress(progress)

# Phase 1
def phase1():
    show_progress()
    st.title("🔬 Clinical Trials - Phase 1")
    st.write("""
    **Scenario:**
    You have just discovered a new medicine that could help people with a rare disease. 
    Before giving it to sick people, you need to test it on a small group of **healthy volunteers** 
    to see if it is **safe** for human use. 
    
    **Your Challenge:**
    What is the **main goal** of Phase 1 trials?
    """)
    
    answer = st.radio("Choose the correct answer:", [
        "To find out if the medicine works",
        "To test if the medicine is safe",
        "To sell the medicine in stores"
    ], index=None)
    
    if st.button("Submit Answer") and answer:
        if answer == "To test if the medicine is safe":
            st.success("Correct! 🎉 Safety first!")
            update_score(st.session_state["name"], 10)
        else:
            st.error("Oops! The main goal is to test safety first.")
        
        time.sleep(1)
        st.session_state["page"] = "phase2"
        st.rerun()

# Phase 2
def phase2():
    show_progress()
    st.title("🧪 Clinical Trials - Phase 2")
    st.write("""
    **Scenario:**
    Your medicine passed the safety test! Now, you must test it on **a larger group of patients** 
    who actually have the disease. This helps you understand if the medicine **works** and what dosage is best.
    
    **Your Challenge:**
    What is the primary goal of Phase 2 trials?
    """)
    
    answer = st.radio("Choose the correct answer:", [
        "To test if the medicine is safe",
        "To check how well the medicine works",
        "To distribute the medicine worldwide"
    ], index=None)
    
    if st.button("Submit Answer") and answer:
        if answer == "To check how well the medicine works":
            st.success("Correct! 🎯 Effectiveness is key in Phase 2.")
            update_score(st.session_state["name"], 10)
        else:
            st.error("Not quite! Phase 2 focuses on effectiveness.")
        
        time.sleep(1)
        st.session_state["page"] = "phase3"
        st.rerun()

# Phase 3
def phase3():
    show_progress()
    st.title("🧪 Clinical Trials - Phase 3")
    st.write("""
    **Scenario:**
    Your medicine is showing promise! Now, you need to **test it on thousands of patients** across different locations. 
    This helps confirm its effectiveness and detect any rare side effects.
    
    **Your Challenge:**
    What is a key aspect of Phase 3 trials?
    """)
    
    answer = st.radio("Choose the correct answer:", [
        "To confirm the medicine’s effectiveness on a large scale",
        "To test on a few people",
        "To stop testing and sell the medicine"
    ], index=None)
    
    if st.button("Submit Answer") and answer:
        if answer == "To confirm the medicine’s effectiveness on a large scale":
            st.success("Correct! ✅ Large-scale testing is crucial.")
            update_score(st.session_state["name"], 10)
        else:
            st.error("Try again! Phase 3 is about large-scale confirmation.")
        
        time.sleep(1)
        st.session_state["page"] = "phase4"
        st.rerun()

# Phase 4
def phase4():
    show_progress()
    st.title("🚀 Clinical Trials - Phase 4")
    st.write("""
    **Scenario:**
    Congratulations! Your medicine has been approved. But your work is not over.
    Now, you need to keep monitoring patients who take the medicine in real life 
    to detect any long-term side effects.
    
    **Your Challenge:**
    What is the purpose of Phase 4 trials?
    """)
    
    answer = st.radio("Choose the correct answer:", [
        "To test if the medicine is safe",
        "To monitor long-term effects and safety",
        "To stop research and move on"
    ], index=None)
    
    if st.button("Submit Answer") and answer:
        if answer == "To monitor long-term effects and safety":
            st.success("Correct! 📊 Monitoring is essential.")
            update_score(st.session_state["name"], 10)
        else:
            st.error("Phase 4 is all about long-term monitoring!")
        
        time.sleep(1)
        st.session_state["page"] = "leaderboard"
        st.rerun()

# Leaderboard
def leaderboard():
    st.title("🏆 Leaderboard")
    conn = sqlite3.connect("clinical_trials.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, score FROM users ORDER BY score DESC LIMIT 10")
    rows = cursor.fetchall()
    conn.close()
    
    for name, score in rows:
        st.write(f"{name}: {score} points")

# Main function
def main():
    init_db()
    if "page" not in st.session_state:
        welcome()
    elif st.session_state["page"] == "phase1":
        phase1()
    elif st.session_state["page"] == "phase2":
        phase2()
    elif st.session_state["page"] == "phase3":
        phase3()
    elif st.session_state["page"] == "phase4":
        phase4()
    elif st.session_state["page"] == "leaderboard":
        leaderboard()

if __name__ == "__main__":
    main()
