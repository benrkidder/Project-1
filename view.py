from tkinter import *
from formulas import *


class GUI:
    def __init__(self, window):
        self.window = window
        # Result Window
        self.frame_output = Frame(self.window)
        self.__output = IntVar()
        self.__output.set(0)
        self.entry_output = Entry(self.frame_output, justify="right", textvariable=self.__output)
        self.entry_output.pack(side="left", fill="both", padx=5)
        self.frame_output.pack(anchor="center")

        # Row with Memory radios
        self.frame_memory = Frame(self.window)
        self.__memory = IntVar()
        self.__memory.set(0)
        self.radio_mClear = Radiobutton(self.frame_memory, text="MC", indicatoron=False, command=self.memSub)
        self.radio_mAdd = Radiobutton(self.frame_memory, text="M+", indicatoron=False, command=self.memAdd)
        self.radio_mMinus = Radiobutton(self.frame_memory, text="M-", indicatoron=False, command=self.memSub)
        self.radio_mRecall = Radiobutton(self.frame_memory, text="MR", indicatoron=False, textvariable=self.__memory, command=self.update)
        self.radio_mClear.pack(side="left")
        self.radio_mAdd.pack(side="left")
        self.radio_mMinus.pack(side="left")
        self.radio_mRecall.pack(side="left")
        self.frame_memory.pack(anchor="center")

        # Row with Clear, Percent, Mod and Div radios
        self.frame_ops = Frame(self.window)
        self.radio_clear = Radiobutton(self.frame_ops, text="AC", indicatoron=False, command=self.clear)
        self.radio_percent = Radiobutton(self.frame_ops, text="%", indicatoron=False, command=self.percent)
        self.radio_mod = Radiobutton(self.frame_ops, text="mod", indicatoron=False, command=self.mod)
        self.radio_div = Radiobutton(self.frame_ops, text="/", indicatoron=False, command=self.div)
        self.radio_clear.pack(side="left")
        self.radio_percent.pack(side="left")
        self.radio_mod.pack(side="left")
        self.radio_div.pack(side="left")
        self.frame_ops.pack(anchor="center")

        # First row of numbers and multiply radios
        self.frame_num1 = Frame(self.window)
        self.radio_1 = Radiobutton(self.frame_num1, text="1", indicatoron=False, command=self.update)
        self.radio_2 = Radiobutton(self.frame_num1, text="2", indicatoron=False, command=self.update)
        self.radio_3 = Radiobutton(self.frame_num1, text="3", indicatoron=False, command=self.update)
        self.radio_mult = Radiobutton(self.frame_num1, text="*", indicatoron=False, command=self.mult)
        self.radio_1.pack(side="left")
        self.radio_2.pack(side="left")
        self.radio_3.pack(side="left")
        self.radio_mult.pack(side="left")
        self.frame_num1.pack(anchor="center")

        # Second row of numbers and subtract radios
        self.frame_num2 = Frame(self.window)
        self.radio_4 = Radiobutton(self.frame_num2, text="4", indicatoron=False, command=self.update)
        self.radio_5 = Radiobutton(self.frame_num2, text="5", indicatoron=False, command=self.update)
        self.radio_6 = Radiobutton(self.frame_num2, text="6", indicatoron=False, command=self.update)
        self.radio_sub = Radiobutton(self.frame_num2, text="-", indicatoron=False, command=self.sub)
        self.radio_4.pack(side="left")
        self.radio_5.pack(side="left")
        self.radio_6.pack(side="left")
        self.radio_sub.pack(side="left")
        self.frame_num2.pack(anchor="center")

        # Third row of numbers and add radios
        self.frame_num3 = Frame(self.window)
        self.radio_7 = Radiobutton(self.frame_num3, text="7", indicatoron=False, command=self.update)
        self.radio_8 = Radiobutton(self.frame_num3, text="8", indicatoron=False, command=self.update)
        self.radio_9 = Radiobutton(self.frame_num3, text="9", indicatoron=False, command=self.update)
        self.radio_add = Radiobutton(self.frame_num3, text="+", indicatoron=False, command=self.add)
        self.radio_7.pack(side="left")
        self.radio_8.pack(side="left")
        self.radio_9.pack(side="left")
        self.radio_add.pack(side="left")
        self.frame_num3.pack(anchor="center")

        # Row with Zero, Decimal, and Equal radios
        self.frame_num4 = Frame(self.window)
        self.radio_0 = Radiobutton(self.frame_num4, text="0", indicatoron=False, command=self.update)
        self.radio_decimal = Radiobutton(self.frame_num4, indicatoron=False, text=".")
        self.radio_equal = Radiobutton(self.frame_num4, indicatoron=False, text="=")
        self.radio_0.pack(side="left", padx=(0, 10))
        self.radio_decimal.pack(side="left")
        self.radio_equal.pack(side="left")
        self.frame_num4.pack(anchor="center")

    def update(self):
        pass

    def memAdd(self):
        pass

    def memSub(self):
        pass

    def clear(self):
        pass

    def percent(self):
        pass

    def mod(self):
        pass

    def div(self):
        pass

    def mult(self):
        pass

    def add(self):
        pass

    def sub(self):
        pass
