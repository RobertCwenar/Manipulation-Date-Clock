import tkinter as tk

root = tk.Tk()
root.title("Moja pierwsza aplikacja GUI")
root.geometry("400x300")

label = tk.Label(root, text="Witaj w aplikacji GUI!")
label.pack(pady=30)

root.mainloop()