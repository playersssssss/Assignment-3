import yourguiapplication


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("My First GUI")
        self.label = tkinter.Label(self.main_window, text='my text')
        self.label1 = tkinter.Label(self.main_window, text='This is my program.')
        self.label.pack(side='left')
        self.label1.pack(side='left')
        self.button = tkinter.Button(self.main_window, text="Click me", command=self.pm_button_click)
        self.button.pack()
        tkinter.mainloop()

    def pm_button_click(self):
        self.label1.config(text="Thanks for clicking the button")


if __name__ == '__main__':
    my_gui = MyGUI()
