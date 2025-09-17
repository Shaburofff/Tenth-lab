import tkinter as tk

# Главное окно
root = tk.Tk()
root.title("Крестики-нолики")
root.geometry("500x500")
root.resizable(False, False)

current_player = 'X'
board = [['' for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

def check_winner():

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return True

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != '':
            return True

    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False

# Клик по кнопке
def on_click(row, col):
    global current_player
    if board[row][col] == '':
        buttons[row][col].config(text=current_player)
        board[row][col] = current_player
        if check_winner():
            winner_label.config(text=f"Победил игрок {current_player}")
            current_player = None
        else:
            current_player = 'X' if current_player == 'O' else 'O'

# Кнопки
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text='', font=("Arial", 30), width=5, height=2,
                                  command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i, column=j)

turn_label = tk.Label(root, text="Ход X", font=("Arial", 18))
turn_label.grid(row=3, columnspan=3)

winner_label = tk.Label(root, text="", font=("Arial", 18))
winner_label.grid(row=4, columnspan=3)

root.mainloop()
