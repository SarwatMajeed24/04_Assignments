import streamlit as st
import random
import time

# Function to reset the game
def reset_game():
    difficulty_settings = {
        "Easy (1-50)": (1, 50),
        "Medium (1-100)": (1, 100),
        "Hard (1-200)": (1, 200)
    }
    
    selected_difficulty = st.session_state.get('difficulty', "Medium (1-100)")
    min_val, max_val = difficulty_settings[selected_difficulty]

    st.session_state['random_number'] = random.randint(min_val, max_val)
    st.session_state['attempts'] = 0
    st.session_state['guess_history'] = []
    st.session_state['game_over'] = False
    st.session_state['message'] = f"🎯 Guess a number between {min_val} and {max_val}!"
    st.session_state['turn'] = 0  # Track player turns
    st.session_state['start_time'] = time.time()  # Start time tracking
    st.session_state['ai_guess'] = None  # AI opponent's guess

# Function for AI opponent guessing
def ai_guess_number(min_val, max_val):
    return random.randint(min_val, max_val)

# Initialize session state
if 'random_number' not in st.session_state:
    reset_game()

# Streamlit UI
st.title("🎲 Guess the Number Game")
st.write("Try to guess the number chosen by the computer!")

# Difficulty Selection
if st.session_state['attempts'] == 0:
    difficulty = st.selectbox("Select Difficulty:", ["Easy (1-50)", "Medium (1-100)", "Hard (1-200)"], index=1)
    st.session_state['difficulty'] = difficulty

# Multiplayer Mode
multiplayer = st.checkbox("👥 Enable Multiplayer Mode", value=False)
num_players = 1 if not multiplayer else st.slider("Number of Players:", 1, 4, 2)

# AI Opponent Mode
ai_opponent = st.checkbox("🤖 Enable AI Opponent", value=False)

# User input
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=200, step=1)

# Submit button
if st.button("Check Guess") and not st.session_state['game_over']:
    st.session_state['attempts'] += 1
    st.session_state['guess_history'].append(user_guess)

    correct_number = st.session_state['random_number']
    current_player = (st.session_state['turn'] % num_players) + 1  # Determine player turn

    if user_guess < correct_number:
        st.session_state['message'] = f"🔼 Too low! Player {current_player}, try a higher number."
    elif user_guess > correct_number:
        st.session_state['message'] = f"🔽 Too high! Player {current_player}, try a lower number."
    else:
        end_time = time.time()
        time_taken = round(end_time - st.session_state['start_time'], 2)
        score = max(100 - st.session_state['attempts'] * 5 - time_taken, 0)  # Score calculation
        st.session_state['message'] = f"🎉 Correct! Player {current_player} guessed it in {st.session_state['attempts']} attempts! 🏆 Score: {score}"
        st.session_state['game_over'] = True
        st.balloons()  # Celebrate with balloons!

        # Save to leaderboard
        if 'leaderboard' not in st.session_state:
            st.session_state['leaderboard'] = []
        st.session_state['leaderboard'].append({"player": current_player, "score": score, "attempts": st.session_state['attempts'], "time": time_taken})
        st.session_state['leaderboard'] = sorted(st.session_state['leaderboard'], key=lambda x: (-x['score'], x['attempts'], x['time']))

    # AI Opponent's Turn
    if ai_opponent and not st.session_state['game_over']:
        ai_guess = ai_guess_number(1, 200)
        st.session_state['ai_guess'] = ai_guess
        if ai_guess == correct_number:
            st.session_state['message'] = f"🤖 AI guessed the correct number **{ai_guess}**! AI wins!"
            st.session_state['game_over'] = True

    # Update turn for multiplayer
    st.session_state['turn'] += 1

# Display message
st.success(st.session_state['message'])

# Show AI Opponent's Guess
if ai_opponent and st.session_state['ai_guess']:
    st.write(f"🤖 AI guessed: **{st.session_state['ai_guess']}**")

# Show Guess History
if st.session_state['attempts'] > 0:
    st.write("📜 **Guess History:**", ", ".join(map(str, st.session_state['guess_history'])))

# Show Leaderboard
if 'leaderboard' in st.session_state and st.session_state['leaderboard']:
    st.subheader("🏆 Leaderboard")
    for idx, entry in enumerate(st.session_state['leaderboard']):
        st.write(f"**{idx + 1}. Player {entry['player']}** - Score: {entry['score']} | Attempts: {entry['attempts']} | Time: {entry['time']}s")

# Play sound effects (if game is won)
if st.session_state['game_over']:
    st.audio("https://www.soundjay.com/button/beep-07.wav", format="audio/wav")

# Reset button
if st.button("🔄 Play Again"):
    reset_game()



