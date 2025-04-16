<!-- app.py:

Imports: Imports streamlit for the UI and random (though not strictly needed in this minimax implementation, it's good practice to include if you might add random elements later).
CSS Injection: Reads the style.css file and injects the CSS into the Streamlit app using st.markdown and <style>.
Game State: Uses st.session_state to manage the game's state:
board: A list representing the Tic-Tac-Toe board (9 elements, ' ' for empty, 'X' or 'O').
player_turn: Keeps track of whose turn it is ('X' for the human player, 'O' for the AI).
game_over: A boolean indicating if the game has ended.
winner: Stores the winner ('X', 'O', or 'Tie').
Helper Functions:
check_winner(board): Checks if there's a winner or a tie.
make_move(board, position, player): Creates a new board with the given move.
get_available_moves(board): Returns a list of empty cell indices.
AI Logic (Minimax):
minimax(board, depth, maximizing_player): Implements the minimax algorithm with alpha-beta pruning (implicitly, as we're just returning the best score).
Base Cases: If there's a winner or a tie, return a score.
Recursive Calls:
If it's the maximizing player ('O' - AI), try all possible moves and recursively call minimax to find the move with the highest score.
If it's the minimizing player ('X' - Human), try all possible moves and recursively call minimax to find the move with the lowest score.
find_best_move(board): Calls minimax to determine the best move for the AI.
Game Interface:
st.title(): Sets the title of the app.
handle_click(index): This function is called when a player clicks on a cell.
It checks if the move is valid.
Updates the board and switches turns.
Checks for a winner or a tie after the player's move.
If the game is not over, it triggers the AI's turn.
Board Rendering: Uses st.markdown and st.button to create the Tic-Tac-Toe grid. The buttons are dynamically created based on the st.session_state.board. The disabled attribute prevents clicking on already filled cells or after the game is over.
Game Over Messages: Displays messages indicating the winner or a tie.
"Play Again" Button: Resets the game state when clicked.
style.css:

.board: Styles the container for the Tic-Tac-Toe grid using Flexbox to center the board.
.row: Styles each row of the grid using Flexbox to arrange the buttons horizontally.
button: Styles the individual cells (buttons):
Sets width and height.
Increases font size.
Centers the text.
Adds margin, border, and rounded corners.
Sets the cursor to indicate interactivity.
button:disabled: Styles the disabled buttons to indicate they cannot be clicked.
h1, h2, etc.: Centers the text for headings and subheadings.
How to Run:

Save the files: Create the tic_tac_toe_ai directory and save app.py and style.css inside it.
Install Streamlit: If you haven't already, install Streamlit:
Bash

pip install streamlit
Run the app: Open your terminal, navigate to the tic_tac_toe_ai directory, and run:
Bash

streamlit run app.py
This will open the Tic-Tac-Toe AI application in your web browser.

Further Enhancements (Optional):

Difficulty Levels: Implement different AI difficulty levels (e.g., random moves for easy, a simpler evaluation function for medium).
Visual Improvements: Add more sophisticated CSS for animations or a more visually appealing design.
User Choice of Symbol: Allow the user to choose to play as 'O' instead of 'X'.
Error Handling: Add more robust error handling (though Streamlit handles some of this automatically).
Code Refactoring: For larger projects, consider breaking down the code into more modular functions and classes.
Deployment: Deploy your Streamlit app online using platforms like Streamlit Sharing, Heroku, or AWS. -->


# Tic-Tac-Toe AI

This is a simple Tic-Tac-Toe game where you can play against an AI that uses the Minimax algorithm to make optimal moves.

## Features
- You play as "X", and the AI plays as "O".
- The game checks for a winner after each move.
- It uses Streamlit for the web interface.

## Run the App

1. Clone this repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Run the app with `streamlit run app.py`.
4. Open the app in your browser and play!

## Customization
You can modify the CSS in the `assets/styles.css` file to change the appearance of the game.
