import numpy as np
import pygame
import sys
import math
import random

# Global Constants
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

PLAYER = 0
AI = 1

WINDOW_LENGTH = 4

EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2

ROW_COUNT = 6
COLUMN_COUNT = 7

SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

turn = random.randint(PLAYER, AI)


class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def create_board(self):
        board = np.zeros((self.rows, self.columns))
        return board

    def drop_piece(self, board, row, col, piece):
        board[row][col] = piece

    def is_valid_location(self, board, col):
        return board[ROW_COUNT-1][col] == 0

    def get_next_open_row(self, board, col):
        for r in range(ROW_COUNT):
            if board[r][col] == 0:
                return r

    def print_board(self, board):
        self.board = board
        print(np.flip(self.board, 0))

    def winning_move(self, board, piece):
        # Check horizontal locations for win
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT):
                if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT-3):
                if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                    return True

        # Check positively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT-3):
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                    return True

        # Check negatively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                    return True

    def evaluate_win(self, window, piece):
        score = 0
        opp_piece = PLAYER_PIECE
        if piece == PLAYER_PIECE:
            opp_piece = AI_PIECE

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(EMPTY) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(EMPTY) == 2:
            score += 2

        if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
            score -= 4

        return score

    def score_position(self, board, piece):
        score = 0
        # Center Score
        center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
        center_count = center_array.count(piece)
        score += center_count * 3
        
        ## Horizontal Score
        for r in range(ROW_COUNT):
            row_array = [int(i) for i in list(board[r,:])]
            for c in range(COLUMN_COUNT-3):
                window = row_array[c:c+WINDOW_LENGTH]
                score += self.evaluate_win(window, piece)

        ## Vertical Score
        for c in range(COLUMN_COUNT):
            col_array = [int(i) for i in list(board[:,c])]
            for r in range(ROW_COUNT-3):
                window = col_array[r:r+WINDOW_LENGTH]
                score += self.evaluate_win(window, piece)

        ## Diagonal Score
        for r in range(ROW_COUNT-3):
            for c in range(COLUMN_COUNT-3):
                window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_win(window, piece)

        for r in range(ROW_COUNT-3):
            for c in range(COLUMN_COUNT-3):
                window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_win(window, piece)

        return score

    def is_terminal_node(self, board):
        return self.winning_move(board, PLAYER_PIECE) or self.winning_move(board, AI_PIECE) or len(self.get_valid_locations(board)) == 0

    def minimax(self, board, depth, alpha, beta, maximizingPlayer):
        valid_locations = self.get_valid_locations(board)
        is_terminal = self.is_terminal_node(board)
        if depth ==0 or is_terminal:
            if is_terminal:
                if self.winning_move(board, AI_PIECE):
                    return (None, 1000000000000000000000)
                elif self.winning_move(board, PLAYER_PIECE):
                    return (None, -1000000000000000000000)
                else: #GAme Over 
                    return (None, 0)
            else: #Zero Depth
                return (None, self.score_position(board, AI_PIECE))
        if maximizingPlayer:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = self.get_next_open_row(board, col)
                b_copy = board.copy()
                self.drop_piece(b_copy, row, col, AI_PIECE)
                new_score = self.minimax(b_copy, depth-1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value

        else:
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = self.get_next_open_row(board, col)
                b_copy = board.copy()
                self.drop_piece(b_copy, row, col, PLAYER_PIECE)
                new_score = self.minimax(b_copy, depth-1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value

    def get_valid_locations(self, board):
        valid_locations = []
        for col in range(COLUMN_COUNT):
            if self.is_valid_location(board, col):
                valid_locations.append(col)
        return valid_locations

    def pick_best_move(self, board, piece):
        valid_locations = self.get_valid_locations(board)
        best_score = -10000
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = self.get_next_open_row(board, col)
            temp_board = board.copy()
            self.drop_piece(temp_board, row, col, piece)
            score = self.score_position(temp_board, piece)
            if score > best_score:
                best_score = score
                best_col = col

        return best_col
                

    def draw_board(self, board):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(
                    screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(screen, BLACK, (int(
                    c*SQUARESIZE + SQUARESIZE/2), int(r*SQUARESIZE + SQUARESIZE+SQUARESIZE/2)), RADIUS)

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if board[r][c] == PLAYER_PIECE:
                    pygame.draw.circle(screen, RED, (int(
                        c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                elif board[r][c] == AI_PIECE:
                    pygame.draw.circle(screen, YELLOW, (int(
                        c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)

        pygame.display.update()


if __name__ == "__main__":
    board = Board(ROW_COUNT, COLUMN_COUNT)
    game_over = False
    game = board.create_board()
    board.print_board(game)

    pygame.init()

    screen = pygame.display.set_mode(size)
    myFont = pygame.font.SysFont("monopsace", 75)
    board.draw_board(game)
    pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == PLAYER:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                print(event.pos)

                #Ask For Player 1
                if turn == PLAYER:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if board.is_valid_location(game, col):
                        row = board.get_next_open_row(game, col)
                        board.drop_piece(game, row, col, PLAYER_PIECE)

                        if board.winning_move(game, PLAYER_PIECE):
                            label = myFont.render("Player 1 Wins !!", 1, RED)
                            screen.blit(label, (40,10))
                            game_over = True

                        turn += 1
                        turn = turn%2

                        board.print_board(game)
                        board.draw_board(game)

        #Ask for Player 2
        if turn == AI and not game_over:
            
            col, minimax_score = board.minimax(game, 6, -math.inf, math.inf, True)

            if board.is_valid_location(game, col):
                """ pygame.time.wait(500) """
                row = board.get_next_open_row(game, col)
                board.drop_piece(game, row, col, AI_PIECE)

                if board.winning_move(game, AI_PIECE):
                    label = myFont.render("Player 2 Wins !!", 1, YELLOW)
                    screen.blit(label, (40,10))
                    game_over = True

                board.print_board(game)
                board.draw_board(game)

                turn += 1
                turn = turn % 2

        if game_over:
            pygame.time.wait(3000)