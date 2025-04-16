# import streamlit as st

# # Load custom CSS
# try:
#     with open('styles.css') as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# except FileNotFoundError:
#     st.warning("styles.css file not found! Default styles will be used.")

# # Initialize the board
# def initialize_game():
#     return [[" " for _ in range(3)] for _ in range(3)]

# # Function to check if there is a winner and return the winning cells
# def check_winner(board, player):
#     winning_cells = []
#     # Check rows and columns
#     for i in range(3):
#         if all([board[i][j] == player for j in range(3)]):  # row check
#             winning_cells.extend([(i, j) for j in range(3)])
#         if all([board[j][i] == player for j in range(3)]):  # column check
#             winning_cells.extend([(j, i) for j in range(3)])
    
#     # Check diagonals
#     if all([board[i][i] == player for i in range(3)]):  # left-to-right diagonal
#         winning_cells.extend([(i, i) for i in range(3)])
#     if all([board[i][2 - i] == player for i in range(3)]):  # right-to-left diagonal
#         winning_cells.extend([(i, 2 - i) for i in range(3)])

#     return winning_cells if winning_cells else None

# # Function to check if the board is full (draw)
# def is_full(board):
#     for row in board:
#         if " " in row:
#             return False
#     return True

# # Function to handle the game state
# def make_move(i, j):
#     if st.session_state.board[i][j] == " " and not st.session_state.game_over:
#         st.session_state.board[i][j] = "X" if st.session_state.turn == "Player 1 (X)" else "O"
#         if check_winner(st.session_state.board, "X"):
#             st.session_state.game_over = True
#         elif check_winner(st.session_state.board, "O"):
#             st.session_state.game_over = True
#         elif is_full(st.session_state.board):
#             st.session_state.game_over = True
#         # Toggle turn
#         st.session_state.turn = "Player 2 (O)" if st.session_state.turn == "Player 1 (X)" else "Player 1 (X)"

# # Restart the game
# def restart_game():
#     st.session_state.board = initialize_game()
#     st.session_state.game_over = False
#     st.session_state.turn = "Player 1 (X)"

# # Streamlit interface
# def main():
#     # Page title
#     st.title("Tic-Tac-Toe (2 Player Game)")

#     # Create columns for layout
#     col1, col2, col3 = st.columns([1, 3, 1])

#     with col2:
#         # Initialize the game state
#         if "board" not in st.session_state:
#             st.session_state.board = initialize_game()

#         if "game_over" not in st.session_state:
#             st.session_state.game_over = False

#         if "turn" not in st.session_state:
#             st.session_state.turn = "Player 1 (X)"

#         # Display the current player's turn
#         st.write(f"**It's {st.session_state.turn}'s turn**", unsafe_allow_html=True)

#         # Check if the game is over
#         winning_cells_x = check_winner(st.session_state.board, "X")
#         winning_cells_o = check_winner(st.session_state.board, "O")

#         # Conditional styling for the subheader based on winner
#         if st.session_state.game_over:
#             winner = "Player 1" if winning_cells_x else "Player 2" if winning_cells_o else "It's a draw!"
#             # Apply blinking or shining effect based on the winner
#             if winning_cells_x:
#                 winner_class = "subheader-shining"  # Player 1 (X) wins, shining effect
#             elif winning_cells_o:
#                 winner_class = "subheader-blinking"  # Player 2 (O) wins, blinking effect
#             else:
#                 winner_class = "subheader-drawAnimation"  # Draw, blinking effect

#             st.markdown(f'<h2 class="{winner_class}">Game Over! {winner} wins!</h2>', unsafe_allow_html=True)

#         # Create buttons for the board cells with larger size and show X or O
#         for i in range(3):
#             cols = st.columns(3)  # Three columns per row for the board cells
#             for j in range(3):
#                 with cols[j]:
#                     # Set background color based on "X" or "O"
#                     cell_value = st.session_state.board[i][j]
#                     if cell_value == "X":
#                         button_color = "#FF5733"  # Red for X
#                     elif cell_value == "O":
#                         button_color = "#33C1FF"  # Blue for O
#                     else:
#                         button_color = "#F4F4F9"  # Default white for empty cell

#                     # Check if the cell is a winning cell and apply animation if it is
#                     is_winning_cell = (i, j) in (winning_cells_x or []) + (winning_cells_o or [])

#                     # Add the button with on_click functionality and unique key
#                     button = st.button(f"", key=f"cell_{i}_{j}", use_container_width=True, on_click=make_move, args=(i, j), help=f"Click to place {st.session_state.turn}")
#                     if button:
#                         make_move(i, j)  # Trigger move logic if button clicked
                    
#                     # Apply animation to the winning cells
#                     if is_winning_cell:
#                         animation = "shining"  # You can change this to "blinking" if preferred
#                         # Adding HTML for styling winning cells
#                         st.markdown(f"""
#                             <style>
#                                 .cell_{i}_{j} {{
#                                     background-color: {button_color};
#                                     animation: {animation} 1s infinite;
#                                 }}
#                             </style>
#                         """, unsafe_allow_html=True)

#                     # Show the current "X" or "O" in the cell
#                     st.markdown(f"### {cell_value}", unsafe_allow_html=True)

#         # **Always Display the Restart Game Button**
#         if st.button("Restart Game", key="restart_button"):
#             restart_game()

# # Main function to run the game
# if __name__ == "__main__":
#     main()


import streamlit as st
import random

# Load custom CSS
try:
    with open('styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("styles.css file not found! Default styles will be used.")

# Initialize the board
def initialize_game():
    return [[" " for _ in range(3)] for _ in range(3)]

# Function to check if there is a winner and return the winning cells
def check_winner(board, player):
    winning_cells = []
    # Check rows and columns
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):  # row check
            winning_cells.extend([(i, j) for j in range(3)])
        if all([board[j][i] == player for j in range(3)]):  # column check
            winning_cells.extend([(j, i) for j in range(3)])
    
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]):  # left-to-right diagonal
        winning_cells.extend([(i, i) for i in range(3)])
    if all([board[i][2 - i] == player for i in range(3)]):  # right-to-left diagonal
        winning_cells.extend([(i, 2 - i) for i in range(3)])

    return winning_cells if winning_cells else None

# Function to check if the board is full (draw)
def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Function to make a random AI move (for simplicity)
def ai_move():
    available_moves = [(i, j) for i in range(3) for j in range(3) if st.session_state.board[i][j] == " "]
    return random.choice(available_moves)

# Function to handle the game state
def make_move(i, j):
    if st.session_state.board[i][j] == " " and not st.session_state.game_over:
        # Player (X) move
        st.session_state.board[i][j] = "X"
        if check_winner(st.session_state.board, "X"):
            st.session_state.game_over = True
        elif is_full(st.session_state.board):
            st.session_state.game_over = True
        else:
            # AI (O) move
            ai_i, ai_j = ai_move()
            st.session_state.board[ai_i][ai_j] = "O"
            if check_winner(st.session_state.board, "O"):
                st.session_state.game_over = True
            elif is_full(st.session_state.board):
                st.session_state.game_over = True

# Restart the game
def restart_game():
    st.session_state.board = initialize_game()
    st.session_state.game_over = False

# Streamlit interface
def main():
    # Page title
    st.title("Tic-Tac-Toe (Player vs AI)")

    # Create columns for layout
    col1, col2, col3 = st.columns([1, 3, 1])

    with col2:
        # Initialize the game state
        if "board" not in st.session_state:
            st.session_state.board = initialize_game()

        if "game_over" not in st.session_state:
            st.session_state.game_over = False

        # Always initialize winning cells variables
        winning_cells_x = check_winner(st.session_state.board, "X") or []
        winning_cells_o = check_winner(st.session_state.board, "O") or []

        # Display the current player's turn
        if not st.session_state.game_over:
            st.write("**It's your turn (X)**", unsafe_allow_html=True)
        else:
            # Check if game is over and display the result
            if winning_cells_x:
                winner = "You win!"  # Player wins
                winner_class = "subheader-shining"  # Shining effect for Player (X)
            elif winning_cells_o:
                winner = "AI wins!"  # AI wins
                winner_class = "subheader-blinking"  # Blinking effect for AI (O)
            else:
                winner = "It's a draw!"  # Draw
                winner_class = "subheader-drawAnimation"  # Draw with animation

            st.markdown(f'<h2 class="{winner_class}">Game Over! {winner}</h2>', unsafe_allow_html=True)

        # Create buttons for the board cells with larger size and show X or O
        for i in range(3):
            cols = st.columns(3)  # Three columns per row for the board cells
            for j in range(3):
                with cols[j]:
                    # Set background color based on "X" or "O"
                    cell_value = st.session_state.board[i][j]
                    if cell_value == "X":
                        button_color = "#FF5733"  # Red for X
                    elif cell_value == "O":
                        button_color = "#33C1FF"  # Blue for O
                    else:
                        button_color = "#F4F4F9"  # Default white for empty cell

                    # Check if the cell is a winning cell and apply animation if it is
                    is_winning_cell = (i, j) in winning_cells_x + winning_cells_o

                    # Add the button with on_click functionality and unique key
                    button = st.button(f"", key=f"cell_{i}_{j}", use_container_width=True, on_click=make_move, args=(i, j), help="Click to place your X")
                    if button:
                        make_move(i, j)  # Trigger move logic if button clicked
                    
                    # Apply animation to the winning cells
                    if is_winning_cell:
                        animation = "shining"  # You can change this to "blinking" if preferred
                        # Adding HTML for styling winning cells
                        st.markdown(f"""
                            <style>
                                .cell_{i}_{j} {{
                                    background-color: {button_color};
                                    animation: {animation} 1s infinite;
                                }}
                            </style>
                        """, unsafe_allow_html=True)

                    # Show the current "X" or "O" in the cell
                    st.markdown(f"### {cell_value}", unsafe_allow_html=True)

        # **Always Display the Restart Game Button**
        if st.button("Restart Game", key="restart_button"):
            restart_game()

# Main function to run the game
if __name__ == "__main__":
    main()
