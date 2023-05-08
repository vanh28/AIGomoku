from AI import *
import utils as utils
import gomoku
import copy

board = [['X','X',' ',' ',' '],
         ['O','X','X','X','X'],
         ['O','X','O','O',' '],
         ['O','O','X',' ',' '],
         ['O',' ',' ','X',' ']]
board1 = [[' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' ']]
ai = GomokuAI()
ai.turn = -1
# if (ai.turn == 1):
#     ai.firstMove()
#     print(ai.firstMove())
#     ai.turn *= -1
print(ai.turn)
ai.boardMap = copy.deepcopy(board)
ai.setBoard()
print(ai.boardMap)
ai.setAllState()
print(ai.boardMap)
# for i in range(5):
#     for j in range(5):
#         if (board[i][j] != board1[i][j]):
#             print(j+1, i+1)

move_i, move_j = gomoku.ai_move(ai)
# print("Alpha" + int(move_i))
# print("Alpha j" + int(move_j))
#                 # Make the move and update zobrist hash
ai.setState(move_i, move_j, 1)
ai.rollingHash ^= ai.zobristTable[move_i][move_j][0]
ai.emptyCells -= 1
print(ai.boardMap)
print(ai.emptyCells)

#     result = ai.checkResult()
# for i in range(5):
#     for j in range(5):
#         if (board[i][j] != board1[i][j]):
#             print(i+1, j+1)
# while  end:
turn = ai.turn
    # print(turn)
#     move_i, move_j = gomoku.ai_move(ai)
#     print("Alpha" + move_i)
#     print("Alpha j" + move_j)
#                 # Make the move and update zobrist hash
#     ai.setState(move_i, move_j, turn)
#     ai.rollingHash ^= ai.zobristTable[move_i][move_j][0]
#     ai.emptyCells -= 1

#     result = ai.checkResult()
#     ai.turn *= -1
#     for i in range(5):
#         for j in range(5):
#             if (board[i][j] != board1[i][j]):
#                 move_i = i
#                 move_j = j
#     print(move_i)
#     print(move_j)
#     if ai.isValid(move_i, move_j):
#         ai.boardValue = ai.evaluate(move_i, move_j, ai.boardValue, -1, ai.nextBound)
#         ai.updateBound(move_i, move_j, ai.nextBound)
#         ai.currentI, ai.currentJ = move_i, move_j
#                         # Make the move and update zobrist hash
#         ai.setState(move_i, move_j, turn)
#         ai.rollingHash ^= ai.zobristTable[move_i][move_j][1]
#         ai.emptyCells -= 1
#         result =  ai.checkResult()
#         ai.turn *= -1

    # if result != None:
    #     end = True
