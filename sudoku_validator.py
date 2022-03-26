def valid_solution(board):
    board1 = []
    for i in range(len(board)):
        for j in range(len(board)):
            board1.append(board[j][i])
        if len(set(board1)) < 9 or 0 in board1:
            return False
        board1 = []
    board1 = []
    board2 = []
    board3 = []
    for i in board:
        if len(set(i)) < 9 or 0 in i:
            return False
    for i in range(3):
        for j in range(3):
            for k in range(3):
                board1.append(board[k][j])
                board2.append(board[k+3][j+3])
                board3.append(board[k+6][j+6])
        if len(set(board1)) < 9 or len(set(board2)) < 9 or len(set(board3)) < 9 or 0 in board1 or 0 in board2 or 0 in board3:
            return False
        board1 = board2 = board3 = []
    return True
