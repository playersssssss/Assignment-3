import yourguiapplication as tk


class YourGUIApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Your GUI Application")  # Set the title of the window

        self.label = tk.Label(master, text="Hello, tkinter!")  # Create a label widget
        self.label.pack()  # Pack the label into the window

        self.button = tk.Button(master, text="Click me", command=self.on_button_click)  # Create a button widget
        self.button.pack()  # Pack the button into the window

    def on_button_click(self):
        self.label.config(text="Button clicked!")  # Change the text of the label when the button is clicked


if __name__ == "__main__":
    root = tk.Tk()
    app = YourGUIApplication(root)
    root.mainloop()