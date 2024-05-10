import numpy as np
import random
import pygame
import sys
import math

# Colors for the game
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

# Game settings
ROW_COUNT = 6
COLUMN_COUNT = 7
EMPTY = 0
ITERATIVE_DEEPENING_AI_PIECE = 1
MINIMAX_AI_PIECE = 2
WINDOW_LENGTH = 4

def create_board():
    return np.zeros((ROW_COUNT, COLUMN_COUNT))

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
    return False

def evaluate_window(window, piece):
    score = 0
    opponent_piece = ITERATIVE_DEEPENING_AI_PIECE if piece == MINIMAX_AI_PIECE else MINIMAX_AI_PIECE
    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2
    if window.count(opponent_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4
    return score

def score_position(board, piece):
    score = 0
    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r,:])]
        for c in range(COLUMN_COUNT - 3):
            window = row_array[c:c+WINDOW_LENGTH]
            score += evaluate_window(window, piece)
    for c in range(COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:,c])]
        for r in range(ROW_COUNT - 3):
            window = col_array[r:r+WINDOW_LENGTH]
            score += evaluate_window(window, piece)
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)
    return score

def minimax(board, depth, alpha, beta, maximizingPlayer):
    is_terminal = winning_move(board, ITERATIVE_DEEPENING_AI_PIECE) or winning_move(board, MINIMAX_AI_PIECE) or len(get_valid_locations(board)) == 0
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, MINIMAX_AI_PIECE):
                return (None, 100000000000000)
            elif winning_move(board, ITERATIVE_DEEPENING_AI_PIECE):
                return (None, -10000000000000)
            else:
                return (None, 0)
        else:
            return (None, score_position(board, MINIMAX_AI_PIECE if maximizingPlayer else ITERATIVE_DEEPENING_AI_PIECE))
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(get_valid_locations(board))
        for col in get_valid_locations(board):
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, MINIMAX_AI_PIECE)
            new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value
    else:
        value = math.inf
        column = random.choice(get_valid_locations(board))
        for col in get_valid_locations(board):
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, ITERATIVE_DEEPENING_AI_PIECE)
            new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if beta <= alpha:
                break
        return column, value

def iterative_deepening(board, max_depth):
    best_move = None
    best_score = -math.inf
    for depth in range(1, max_depth + 1):
        move, score = minimax(board, depth, -math.inf, math.inf, True)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations

def play_game():
    board = create_board()
    print_board(board)
    game_over = False
    turn = random.choice([ITERATIVE_DEEPENING_AI_PIECE, MINIMAX_AI_PIECE])  # Randomly decide who starts

    while not game_over:
        if turn == ITERATIVE_DEEPENING_AI_PIECE:
            col = iterative_deepening(board, 5)  # AI 1 plays with iterative deepening
        else:
            col, _ = minimax(board, 5, -math.inf, math.inf, True)  # AI 2 plays with fixed depth minimax

        if col is not None and is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, ITERATIVE_DEEPENING_AI_PIECE if turn == ITERATIVE_DEEPENING_AI_PIECE else MINIMAX_AI_PIECE)
            print_board(board)

            if winning_move(board, ITERATIVE_DEEPENING_AI_PIECE if turn == ITERATIVE_DEEPENING_AI_PIECE else MINIMAX_AI_PIECE):
                print(f"{'Iterative Deepening AI' if turn == ITERATIVE_DEEPENING_AI_PIECE else 'Minimax AI'} wins!")
                game_over = True

        turn = ITERATIVE_DEEPENING_AI_PIECE if turn == MINIMAX_AI_PIECE else MINIMAX_AI_PIECE

        if all(is_valid_location(board, col) == False for col in range(COLUMN_COUNT)):
            print("Game ends in a draw")
            break

if __name__ == "__main__":
    play_game()
