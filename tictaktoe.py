import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x500")
        self.player = "X"
        self.buttons = [[None, None, None], [None, None, None], [None, None, None]]
        self.create_background()
        self.create_title()
        self.create_buttons()
        self.create_reset_button()
    
    def create_background(self):
        self.canvas = tk.Canvas(self.root, width=400, height=500)
        self.canvas.pack(fill="both", expand=True)
        self.bg_image = ImageTk.PhotoImage(Image.open("tic-tac-toe-strategy-game-criss-cross-leisure-recreation-concept-ECDXGK.jpg"))
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
    
    def create_title(self):
        self.title_label = tk.Label(self.root, text="TIC TAC TOE", font=("Helvetica", 24, "bold"), bg="sky blue", fg="black")
        self.title_window = self.canvas.create_window(100, 20, anchor="nw", window=self.title_label)
    
    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=("Helvetica", 20), height=3, width=6, 
                                               bg="#f2f2f2", command=lambda i=i, j=j: self.click(i, j))
                self.canvas.create_window(50 + j*100, 70 + i*100, anchor="nw", window=self.buttons[i][j])
    
    def create_reset_button(self):
        reset_button = tk.Button(self.root, text="Reset", font=("Helvetica", 15), height=2, width=10, bg="red", fg="white", command=self.reset)
        self.canvas.create_window(150, 400, anchor="nw", window=reset_button)
    
    def click(self, i, j):
        if self.buttons[i][j]["text"] == "" and self.check_winner() is False:
            self.buttons[i][j]["text"] = self.player
            self.buttons[i][j]["fg"] = "blue" if self.player == "X" else "green"
            if self.check_winner() is False:
                self.player = "O" if self.player == "X" else "X"
            elif self.check_winner() is True:
                messagebox.showinfo("Tic Tac Toe", f"Player {self.player} wins!")
            elif self.check_winner() == "Tie":
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
    
    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True
        for row in self.buttons:
            for button in row:
                if button["text"] == "":
                    return False
        return "Tie"
    
    def reset(self):
        self.player = "X"
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
                self.buttons[i][j]["fg"] = "black"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
