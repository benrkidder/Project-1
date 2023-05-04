from tkinter import *
from formulas import *


class GUI:
    def __init__(self, window):
        self.window = window

        # Widget styles
        self.font = "Helvetica Light"
        self.button_font = "Helvetica"
        self.button_font_color = "#DDD"
        self.button_color = "#323232"
        self.modifier_button_color = "#444"
        self.mem_button_color = "#5F5F5F"
        self.op_button_color = "#F3A23C"
        self.op_font_color = "White"
        self.button_font_size = 20

        # Result output
        self.frame = Frame(self.window)
        self.frame.grid(column=0, columnspan=4)
        self.frame.columnconfigure(0, weight=1, uniform="column")
        self.frame.columnconfigure(1, weight=1, uniform="column")
        self.frame.columnconfigure(2, weight=1, uniform="column")
        self.frame.columnconfigure(3, weight=1, uniform="column")
        self.frame.rowconfigure(0, weight=2, uniform="row")
        self.frame.rowconfigure(1, weight=1, uniform="row")
        self.frame.rowconfigure(2, weight=2, uniform="row")
        self.frame.rowconfigure(3, weight=2, uniform="row")
        self.frame.rowconfigure(4, weight=2, uniform="row")
        self.frame.rowconfigure(5, weight=2, uniform="row")
        self.frame.rowconfigure(6, weight=2, uniform="row")
        self.frame.rowconfigure(7, weight=2, uniform="row")

        self.__output = IntVar()
        self.__output.set(0)
        self.__temp_output = IntVar()
        self.__temp_output.set(0)

        self.entry_output = Entry(self.frame,
                                  font=(self.font, 40),
                                  insertwidth=0,
                                  justify="right",
                                  textvariable=self.__output)
        self.entry_output.grid(column=0, row=0, columnspan=4, sticky="ew")
        self.entry_output.focus_set()
        self.entry_output.icursor(1)

        # Memory output
        self.label_memory = Label(self.frame,
                                  anchor="w",
                                  font=(self.font, 20),
                                  foreground="gray45",
                                  text="Memory:")
        self.__memory = IntVar()
        self.__memory.set(0)
        self.label_mem_val = Label(self.frame,
                                   anchor="w",
                                   foreground="gray45",
                                   font=(self.font, 20),
                                   textvariable=self.__output)
        self.label_memory.grid(row=1, column=0, sticky="ew")
        self.label_mem_val.grid(row=1, column=1, columnspan=3, sticky="ew")

        # Row with Memory radios
        self.radio_mClear = Radiobutton(self.frame,
                                        bg=self.mem_button_color,
                                        command=lambda: self.mem("Clear"),
                                        fg=self.button_font_color,
                                        font=(self.button_font, self.button_font_size),
                                        indicatoron=False,
                                        text="mc")
        self.radio_mAdd = Radiobutton(self.frame,
                                      bg=self.mem_button_color,
                                      command=lambda: self.mem("Add"),
                                      fg=self.button_font_color,
                                      font=(self.button_font, self.button_font_size),
                                      indicatoron=False,
                                      text="m+")
        self.radio_mMinus = Radiobutton(self.frame,
                                        bg=self.mem_button_color,
                                        command=lambda: self.mem("Minus"),
                                        fg=self.button_font_color,
                                        font=(self.button_font, self.button_font_size),
                                        indicatoron=False,
                                        text="m-")
        self.radio_mRecall = Radiobutton(self.frame,
                                         bg=self.mem_button_color,
                                         command=lambda: self.mem("Recall"),
                                         fg=self.button_font_color,
                                         font=(self.button_font, self.button_font_size),
                                         indicatoron=False,
                                         text="mr")
        self.radio_mClear.grid(row=2, column=0, sticky="nsew")
        self.radio_mAdd.grid(row=2, column=1, sticky="nsew")
        self.radio_mMinus.grid(row=2, column=2, sticky="nsew")
        self.radio_mRecall.grid(row=2, column=3, sticky="nsew")

        # Row with Clear, Percent, Mod and Div radios
        self.radio_clear = Radiobutton(self.frame,
                                       bg="red",
                                       command=self.clear,
                                       fg=self.op_font_color,
                                       font=(self.button_font, self.button_font_size),
                                       indicatoron=False,
                                       text="AC")
        self.radio_percent = Radiobutton(self.frame,
                                         bg=self.op_button_color,
                                         command=self.percent,
                                         fg=self.button_font_color,
                                         font=(self.button_font, self.button_font_size),
                                         indicatoron=False,
                                         text="%")
        self.radio_mod = Radiobutton(self.frame,
                                     bg=self.op_button_color,
                                     command=self.modulo,
                                     fg=self.op_font_color,
                                     font=(self.button_font, self.button_font_size),
                                     indicatoron=False,
                                     text="mod")
        self.radio_div = Radiobutton(self.frame,
                                     bg=self.op_button_color,
                                     command=self.divide,
                                     fg=self.op_font_color,
                                     font=(self.button_font, self.button_font_size),
                                     indicatoron=False,
                                     text="\xf7")
        self.radio_clear.grid(row=3, column=0, sticky="nsew")
        self.radio_percent.grid(row=3, column=1, sticky="nsew")
        self.radio_mod.grid(row=3, column=2, sticky="nsew")
        self.radio_div.grid(row=3, column=3, sticky="nsew")

        # First row of numbers and multiply radios
        self.radio_1 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   command=self.update,
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="1")
        self.radio_2 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   command=self.update,
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="2")
        self.radio_3 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   command=self.update,
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="3")
        self.radio_mult = Radiobutton(self.frame,
                                      bg=self.op_button_color,
                                      command=self.multiply,
                                      fg=self.op_font_color,
                                      font=(self.button_font, self.button_font_size),
                                      indicatoron=False,
                                      text="x")
        self.radio_1.grid(row=4, column=0, sticky="nsew")
        self.radio_2.grid(row=4, column=1, sticky="nsew")
        self.radio_3.grid(row=4, column=2, sticky="nsew")
        self.radio_mult.grid(row=4, column=3, sticky="nsew")

        # Second row of numbers and subtract radios
        self.radio_4 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   command=self.update,
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="4")
        self.radio_5 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   command=self.update,
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="5")
        self.radio_6 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   command=self.update,
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="6")
        self.radio_sub = Radiobutton(self.frame,
                                     bg=self.op_button_color,
                                     command=self.subtract,
                                     fg=self.op_font_color,
                                     font=(self.button_font, self.button_font_size),
                                     indicatoron=False,
                                     text="-")
        self.radio_4.grid(row=5, column=0, sticky="nsew")
        self.radio_5.grid(row=5, column=1, sticky="nsew")
        self.radio_6.grid(row=5, column=2, sticky="nsew")
        self.radio_sub.grid(row=5, column=3, sticky="nsew")

        # Third row of numbers and add radios
        self.radio_7 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   command=self.update,
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="7")
        self.radio_8 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   command=self.update,
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="8")
        self.radio_9 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   command=self.update,
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="9")
        self.radio_add = Radiobutton(self.frame,
                                     bg=self.op_button_color,
                                     command=self.add,
                                     fg=self.op_font_color,
                                     font=(self.button_font, self.button_font_size),
                                     indicatoron=False,
                                     text="+")
        self.radio_7.grid(row=6, column=0, sticky="nsew")
        self.radio_8.grid(row=6, column=1, sticky="nsew")
        self.radio_9.grid(row=6, column=2, sticky="nsew")
        self.radio_add.grid(row=6, column=3, sticky="nsew")

        # Row with Zero, Decimal, and Equal radios
        self.radio_sign = Radiobutton(self.frame,
                                      bg=self.modifier_button_color,
                                      command=self.update,
                                      fg=self.button_font_color,
                                      font=(self.button_font, self.button_font_size),
                                      indicatoron=False,
                                      text="+ / -")
        self.radio_0 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   command=self.update,
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="0")
        self.radio_decimal = Radiobutton(self.frame,
                                         bg=self.modifier_button_color,
                                         command=self.update,
                                         fg=self.button_font_color,
                                         font=(self.button_font, self.button_font_size),
                                         indicatoron=False,
                                         text=".")
        self.radio_equal = Radiobutton(self.frame,
                                       bg=self.op_button_color,
                                       command=self.update,
                                       fg=self.op_font_color,
                                       font=(self.button_font, self.button_font_size),
                                       indicatoron=False,
                                       text="=")
        self.radio_sign.grid(row=7, column=0, sticky="nsew")
        self.radio_0.grid(row=7, column=1, sticky="nsew")
        self.radio_decimal.grid(row=7, column=2, sticky="nsew")
        self.radio_equal.grid(row=7, column=3, sticky="nsew")

    def update(self):
        pass

    def mem(self, button):
        pass

    def clear(self):
        pass

    def percent(self):
        pass

    def modulo(self):
        pass

    def divide(self):
        pass

    def multiply(self):
        pass

    def add(self):
        pass

    def subtract(self):
        pass


if __name__ == "__main__":
    win = Tk()
    win.title('A Better Calculator')

    GUI(win)

    win.update()
    win_width = win.winfo_reqwidth()
    win_height = win.winfo_reqheight()
    scr_width = win.winfo_screenwidth()
    scr_height = win.winfo_screenheight()
    x = int((scr_width / 2) - (win_width / 2))
    y = int((scr_height / 2) - (win_height / 2))
    win.geometry(f'+{x}+{y}')
    win.resizable(False, False)

    win.mainloop()
