import tkinter as tk


class YourGUIApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Your GUI Application")

        self.label = tk.Label(master, text="Hello tkinter!")
        self.label.pack()

        self.button = tk.Button(master, text="Click me", command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        self.label.config(text="Button clicked!")


if __name__ == "__main__":
    root = tk.Tk()
    app = YourGUIApplication(root)
    root.mainloop()


