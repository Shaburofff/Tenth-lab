import tkinter as tk
from random import choice

root = tk.Tk()
root.title("Tic-Tac Toe♥")
board = [""] * 9
buttons = []

def minimax(board, player):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] != "":
            return 1 if board[w[0]] == "O" else -1
    if "" not in board:
        return 0
    scores = []
    for i in range(9):
        if board[i] == "":
            board[i] = player
            s = minimax(board, "X" if player == "O" else "O")
            board[i] = ""
            scores.append(s)
    if not scores:
        return 0
    return max(scores) if player == "O" else min(scores)

def bot_move():
    if board[4] == "":
        return 4
    moves = [i for i in range(9) if board[i] == ""]
    scored = [(minimax(board[:i] + ["O"] + board[i+1:], "X"), i) for i in moves]
    best_score = max(scored, key=lambda x: x[0])[0]
    best_moves = [m for s, m in scored if s == best_score]
    return choice(best_moves)

def click(i):
    if board[i] == "":
        board[i] = "X"
        buttons[i].config(text="X", state="disabled")
        if check_win():
            return
        if "" in board:
            b = bot_move()
            board[b] = "O"
            buttons[b].config(text="O", state="disabled")
            check_win()

def check_win():
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] != "":
            for i in w:
                buttons[i].config(bg="lightgreen")
            return True
    if "" not in board:
        for b in buttons:
            b.config(bg="lightyellow")
        return True
    return False

for i in range(9):
    b = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                  command=lambda i=i: click(i))
    b.grid(row=i//3, column=i%3)
    buttons.append(b)

def new_game():
    for b in buttons:
        b.config(text="", state="normal", bg="SystemButtonFace")
    for i in range(9):
        board[i] = ""

tk.Button(root, text="New Game", command=new_game).grid(row=3, column=0, columnspan=3)

root.mainloop()
