import streamlit as st
import random

# Step 1: Define your word pairs (Spanish to English)
words = {
    "gato": "cat",
    "perro": "dog",
    "casa": "house",
    "libro": "book",
    "amigo": "friend",
    "comida": "food",
    "sol": "sun",
    "cielo": "sky",
    "agua": "water",
    "tierra": "earth"
}

# Step 2: Choose a random word
if "current_word" not in st.session_state:
    st.session_state.current_word = random.choice(list(words.keys()))
    st.session_state.attempts = 0

# Display the Spanish word
st.title("Spanish Word Memorization Game")
st.write(f"Translate the word: **{st.session_state.current_word}**")

# Input field for the user’s answer
user_answer = st.text_input("Your answer:")

if st.button("Submit"):
    # Increment attempts
    st.session_state.attempts += 1
    
    # Check the answer
    if user_answer.lower() == words[st.session_state.current_word].lower():
        st.success("Correct! 🎉")
        # Reset the game with a new word
        st.session_state.current_word = random.choice(list(words.keys()))
        st.session_state.attempts = 0
    elif st.session_state.attempts < 3:
        st.warning(f"Try again! You have {3 - st.session_state.attempts} attempts left.")
    else:
        st.error(f"Out of attempts! The correct answer was: {words[st.session_state.current_word]}")
        # Reset the game with a new word
        st.session_state.current_word = random.choice(list(words.keys()))
        st.session_state.attempts = 0
