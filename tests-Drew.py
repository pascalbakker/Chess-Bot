import chess
import random

def startGame():
    # clear_stack
    return chess.Board()

def displayBoard(board):
    print board

def randomAI(board): #Selects one of the legal moves randomly and returns it
    moves = []
    for move in board.legal_moves:
        moves.append(move)
    move = random.choice(moves)
    while not chess.Move.from_uci(str(move)) in board.legal_moves:
        move = random.choice(moves)

    return chess.Move.from_uci(str(move))

def pascalTest():
    board = chess.Board()
    color = True #True=White Black=false
    num = 0 #Number of moves

    #Runs the chess game until win, draw, or stalemate
    while(True):
        board.push(randomAI(board))
        num=num+1
        print board
        print "=============================="
        if board.is_stalemate() or board.is_insufficient_material() or board.can_claim_threefold_repetition() or board.can_claim_fifty_moves() or board.can_claim_draw():
            print "Stalemate or Draw"
            print "Number of Moves: ",num
            break;
        if board.is_game_over() or board.is_checkmate():
            if color:
                print "White Won"
            else:
                print "Black Won"
            print "Number of Moves: ",num
            break;
        color!=color

def drewTest():
    turn = 0       # turn counter
    stillPlaying = True     # outer loop boolean
    player_white = True     # white = true, black = false

    init_board = startGame()
    displayBoard(init_board)

    while stillPlaying:

        if player_white:
            print "white moves"

        else:
            print "black moves"

def main():
    pascalTest()

main()
