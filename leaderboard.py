import sqlite3
import streamlit as st
import os
import time

# Database Path
DB_PATH = r"D:\VsCode\LSA\clinical_trials.db"

def check_database():
    """Check if the database file exists."""
    if not os.path.exists(DB_PATH):
        st.error(f"❌ Database not found at: {DB_PATH}")
        return False
    return True

def get_leaderboard():
    """Fetch top 10 players from the database based on scores."""
    if not check_database():
        return []
    
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT name, score FROM users ORDER BY score DESC LIMIT 10")
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        st.error(f"❌ Database error: {e}")
        return []

def leaderboard():
    """Streamlit UI for displaying the leaderboard with auto-refresh."""
    st.title("🏆 Leaderboard")

    rows = get_leaderboard()

    if rows:
        st.write("### 🔥 Top Players 🔥")
        for idx, (name, score) in enumerate(rows, start=1):
            st.write(f"**#{idx} {name}:** {score} points 🎖")
    else:
        st.info("No scores yet! Play the game to be the first on the leaderboard. 🏅")

    # Auto-refresh every 10 seconds
    time.sleep(10)
    st.rerun()

if __name__ == "__main__":
    leaderboard()
