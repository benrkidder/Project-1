from tkinter import *
from formulas import *


class GUI:
    def __init__(self, window):
        self.window = window

        # Widget styles
        self.font = "Helvetica Light"
        self.button_color = "#5F5F5F"
        self.button_font = "Helvetica"
        self.button_font_color = "#DDD"
        self.button_font_size = 20
        self.mem_button_color = "#777"
        self.modifier_button_color = "#444"
        self.op_button_color = "#FF9F0D"
        self.op_font_color = "White"
        self.op_font_size = 25

        # Variables
        self.__interrupter = BooleanVar(name="interrupter")
        self.__memory = IntVar(name="mem")
        self.__moved = BooleanVar(name='moved')
        self.__operator = StringVar(name="operator", value="")
        self.__option = StringVar(name="option", value="Options")
        self.__output = IntVar(name="output")
        self.__temp_output = IntVar(name="temp")
        self.__widget = StringVar(name="widget")

        # Calculator Frame
        self.frame = Frame(self.window)
        self.frame.grid(column=0, columnspan=4)

        # Menu Popup
        self.options = OptionMenu(self.window, self.__option, "Area", "Clear", command=lambda event: self.menu())
        self.options.grid(row=0, column=0, sticky="nw")

        # Result/Entry output
        self.entry_output = Entry(self.frame,
                                  borderwidth=0,
                                  font=(self.font, 40),
                                  justify="right",
                                  highlightthickness=0,
                                  state="readonly",
                                  textvariable=self.__output)
        self.entry_output.grid(row=0, column=0, columnspan=4, padx=10, pady=5, sticky="ew")
        self.entry_output.bind("<KeyPress-1>", self.render)
        self.entry_output.bind("<KeyPress-2>", self.render)
        self.entry_output.bind("<KeyPress-3>", self.render)
        self.entry_output.bind("<KeyPress-4>", self.render)
        self.entry_output.bind("<KeyPress-5>", self.render)
        self.entry_output.bind("<KeyPress-6>", self.render)
        self.entry_output.bind("<KeyPress-7>", self.render)
        self.entry_output.bind("<KeyPress-8>", self.render)
        self.entry_output.bind("<KeyPress-9>", self.render)
        self.entry_output.bind("<KeyPress-0>", self.render)
        self.entry_output.bind("<KeyPress-BackSpace>", lambda event: self.onBackspace)
        self.entry_output.focus_set()

        # Memory output
        self.label_mem_val = Label(self.frame,
                                   anchor="w",
                                   foreground="gray45",
                                   font=(self.font, 20),
                                   textvariable=self.__memory)
        self.label_mem_val.grid(row=1, column=0, columnspan=4, padx=5, sticky="ew")

        # Row with Memory radios
        self.radio_mClear = Radiobutton(self.frame,
                                        bg=self.mem_button_color,
                                        borderwidth=0,
                                        command=lambda: self.mem("Clear"),
                                        fg=self.button_font_color,
                                        font=(self.button_font, self.button_font_size),
                                        indicatoron=False,
                                        text="mc")
        self.radio_mAdd = Radiobutton(self.frame,
                                      bg=self.mem_button_color,
                                      borderwidth=0,
                                      command=lambda: self.mem("Add"),
                                      fg=self.button_font_color,
                                      font=(self.button_font, self.button_font_size),
                                      indicatoron=False,
                                      text="m+")
        self.radio_mMinus = Radiobutton(self.frame,
                                        bg=self.mem_button_color,
                                        borderwidth=0,
                                        command=lambda: self.mem("Minus"),
                                        fg=self.button_font_color,
                                        font=(self.button_font, self.button_font_size),
                                        indicatoron=False,
                                        text="m-")
        self.radio_mRecall = Radiobutton(self.frame,
                                         bg=self.mem_button_color,
                                         borderwidth=0,
                                         command=lambda: self.mem("Recall"),
                                         fg=self.button_font_color,
                                         font=(self.button_font, self.button_font_size),
                                         indicatoron=False,
                                         text="mr")
        self.radio_mClear.grid(row=2, column=0, padx=(0, 1), pady=1, sticky="nsew")
        self.radio_mAdd.grid(row=2, column=1, padx=(0, 1), pady=1, sticky="nsew")
        self.radio_mMinus.grid(row=2, column=2, padx=(0, 1), pady=1, sticky="nsew")
        self.radio_mRecall.grid(row=2, column=3, padx=0, pady=1, sticky="nsew")

        self.radio_mClear.bind("<ButtonPress-1>", lambda event: self.press("memory", self.radio_mClear))
        self.radio_mAdd.bind("<ButtonPress-1>", lambda event: self.press("memory", self.radio_mAdd))
        self.radio_mMinus.bind("<ButtonPress-1>", lambda event: self.press("memory", self.radio_mMinus))
        self.radio_mRecall.bind("<ButtonPress-1>", lambda event: self.press("memory", self.radio_mRecall))

        self.radio_mClear.bind("<ButtonRelease-1>", lambda event: self.release("memory", self.radio_mClear))
        self.radio_mAdd.bind("<ButtonRelease-1>", lambda event: self.release("memory", self.radio_mAdd))
        self.radio_mMinus.bind("<ButtonRelease-1>", lambda event: self.release("memory", self.radio_mMinus))
        self.radio_mRecall.bind("<ButtonRelease-1>", lambda event: self.release("memory", self.radio_mRecall))

        # Row with Clear, Percent, Mod and Div radios
        self.radio_clear = Radiobutton(self.frame,
                                       bg="#E00000",
                                       borderwidth=0,
                                       command=self.clear,
                                       fg=self.op_font_color,
                                       font=(self.button_font, 18),
                                       indicatoron=False,
                                       text="AC")
        self.radio_percent = Radiobutton(self.frame,
                                         bg=self.op_button_color,
                                         borderwidth=0,
                                         command=lambda: self.calculate("Percent"),
                                         fg=self.op_font_color,
                                         font=(self.button_font, self.button_font_size),
                                         indicatoron=False,
                                         text="%")
        self.radio_mod = Radiobutton(self.frame,
                                     bg=self.op_button_color,
                                     borderwidth=0,
                                     command=lambda: self.calculate("Modulo"),
                                     fg=self.op_font_color,
                                     font=(self.button_font, self.button_font_size),
                                     indicatoron=False,
                                     text="mod")
        self.radio_div = Radiobutton(self.frame,
                                     bg=self.op_button_color,
                                     borderwidth=0,
                                     command=lambda: self.calculate("Divide"),
                                     fg=self.op_font_color,
                                     font=(self.button_font, self.op_font_size),
                                     indicatoron=False,
                                     text="\xf7")
        self.radio_clear.grid(row=3, column=0, padx=(0, 1), sticky="nsew")
        self.radio_percent.grid(row=3, column=1, padx=(0, 1), sticky="nsew")
        self.radio_mod.grid(row=3, column=2, padx=(0, 1), sticky="nsew")
        self.radio_div.grid(row=3, column=3, padx=0, sticky="nsew")

        self.radio_clear.bind("<ButtonPress-1>", lambda event: self.press("clear", self.radio_clear))
        self.radio_percent.bind("<ButtonPress-1>", lambda event: self.press("operator", self.radio_percent))
        self.radio_mod.bind("<ButtonPress-1>", lambda event: self.press("operator", self.radio_mod))
        self.radio_div.bind("<ButtonPress-1>", lambda event: self.press("operator", self.radio_div))

        self.radio_clear.bind("<ButtonRelease-1>", lambda event: self.release("clear", self.radio_clear))
        self.radio_percent.bind("<ButtonRelease-1>", lambda event: self.release("operator", self.radio_percent))
        self.radio_mod.bind("<ButtonRelease-1>", lambda event: self.release("operator", self.radio_mod))
        self.radio_div.bind("<ButtonRelease-1>", lambda event: self.release("operator", self.radio_div))

        # First row of numbers and multiply radios
        self.radio_1 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   borderwidth=0,
                                   command=lambda: self.render(char=1),
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="1")
        self.radio_2 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   borderwidth=0,
                                   command=lambda: self.render(char=2),
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="2")
        self.radio_3 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   borderwidth=0,
                                   command=lambda: self.render(char=3),
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="3")
        self.radio_mult = Radiobutton(self.frame,
                                      bg=self.op_button_color,
                                      borderwidth=0,
                                      command=lambda: self.calculate("Multiply"),
                                      fg=self.op_font_color,
                                      font=(self.button_font, self.op_font_size),
                                      indicatoron=False,
                                      text="\xd7")
        self.radio_1.grid(row=4, column=0, padx=(0, 1), pady=1, sticky="nsew")
        self.radio_2.grid(row=4, column=1, padx=(0, 1), pady=1, sticky="nsew")
        self.radio_3.grid(row=4, column=2, padx=(0, 1), pady=1, sticky="nsew")
        self.radio_mult.grid(row=4, column=3, padx=0, pady=1, sticky="nsew")

        self.radio_1.bind("<ButtonPress-1>", lambda event: self.press("num", self.radio_1))
        self.radio_2.bind("<ButtonPress-1>", lambda event: self.press("num", self.radio_2))
        self.radio_3.bind("<ButtonPress-1>", lambda event: self.press("num", self.radio_3))
        self.radio_mult.bind("<ButtonPress-1>", lambda event: self.press("operator", self.radio_mult))

        self.radio_1.bind("<ButtonRelease-1>", lambda event: self.release("num", self.radio_1))
        self.radio_2.bind("<ButtonRelease-1>", lambda event: self.release("num", self.radio_2))
        self.radio_3.bind("<ButtonRelease-1>", lambda event: self.release("num", self.radio_3))
        self.radio_mult.bind("<ButtonRelease-1>", lambda event: self.release("operator", self.radio_mult))

        # Second row of numbers and subtract radios
        self.radio_4 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   borderwidth=0,
                                   command=lambda: self.render(char=4),
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="4")
        self.radio_5 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   borderwidth=0,
                                   command=lambda: self.render(char=5),
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="5")
        self.radio_6 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   borderwidth=0,
                                   command=lambda: self.render(char=6),
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="6")
        self.radio_sub = Radiobutton(self.frame,
                                     bg=self.op_button_color,
                                     borderwidth=0,
                                     command=lambda: self.calculate("Subtract"),
                                     fg=self.op_font_color,
                                     font=(self.button_font, self.op_font_size),
                                     indicatoron=False,
                                     text="\u2013")
        self.radio_4.grid(row=5, column=0, padx=(0, 1), sticky="nsew")
        self.radio_5.grid(row=5, column=1, padx=(0, 1), sticky="nsew")
        self.radio_6.grid(row=5, column=2, padx=(0, 1), sticky="nsew")
        self.radio_sub.grid(row=5, column=3, padx=0, sticky="nsew")

        self.radio_4.bind("<ButtonPress-1>", lambda event: self.press("num", self.radio_4))
        self.radio_5.bind("<ButtonPress-1>", lambda event: self.press("num", self.radio_5))
        self.radio_6.bind("<ButtonPress-1>", lambda event: self.press("num", self.radio_6))
        self.radio_sub.bind("<ButtonPress-1>", lambda event: self.press("operator", self.radio_sub))

        self.radio_4.bind("<ButtonRelease-1>", lambda event: self.release("num", self.radio_4))
        self.radio_5.bind("<ButtonRelease-1>", lambda event: self.release("num", self.radio_5))
        self.radio_6.bind("<ButtonRelease-1>", lambda event: self.release("num", self.radio_6))
        self.radio_sub.bind("<ButtonRelease-1>", lambda event: self.release("operator", self.radio_sub))

        # Third row of numbers and add radios
        self.radio_7 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   borderwidth=0,
                                   command=lambda: self.render(char=7),
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="7")
        self.radio_8 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   borderwidth=0,
                                   command=lambda: self.render(char=8),
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="8")
        self.radio_9 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   borderwidth=0,
                                   command=lambda: self.render(char=9),
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="9")
        self.radio_add = Radiobutton(self.frame,
                                     bg=self.op_button_color,
                                     borderwidth=0,
                                     command=lambda: self.calculate("Add"),
                                     fg=self.op_font_color,
                                     font=(self.button_font, self.op_font_size),
                                     indicatoron=False,
                                     text="+")
        self.radio_7.grid(row=6, column=0, padx=(0, 1), pady=1, sticky="nsew")
        self.radio_8.grid(row=6, column=1, padx=(0, 1), pady=1, sticky="nsew")
        self.radio_9.grid(row=6, column=2, padx=(0, 1), pady=1, sticky="nsew")
        self.radio_add.grid(row=6, column=3, padx=0, pady=1, sticky="nsew")

        self.radio_7.bind("<ButtonPress-1>", lambda event: self.press("num", self.radio_7))
        self.radio_8.bind("<ButtonPress-1>", lambda event: self.press("num", self.radio_8))
        self.radio_9.bind("<ButtonPress-1>", lambda event: self.press("num", self.radio_9))
        self.radio_add.bind("<ButtonPress-1>", lambda event: self.press("operator", self.radio_add))

        self.radio_7.bind("<ButtonRelease-1>", lambda event: self.release("num", self.radio_7))
        self.radio_8.bind("<ButtonRelease-1>", lambda event: self.release("num", self.radio_8))
        self.radio_9.bind("<ButtonRelease-1>", lambda event: self.release("num", self.radio_9))
        self.radio_add.bind("<ButtonRelease-1>", lambda event: self.release("operator", self.radio_add))

        # Row with Zero, Decimal, and Equal radios
        self.radio_sign = Radiobutton(self.frame,
                                      bg=self.modifier_button_color,
                                      borderwidth=0,
                                      command=lambda: self.render(char="sign"),
                                      fg=self.button_font_color,
                                      font=(self.button_font, 22),
                                      indicatoron=False,
                                      text="\xb1")
        self.radio_0 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   borderwidth=0,
                                   command=lambda: self.render(char="0"),
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="0")
        self.radio_decimal = Radiobutton(self.frame,
                                         bg=self.modifier_button_color,
                                         borderwidth=0,
                                         command=lambda: self.render(char="."),
                                         fg=self.button_font_color,
                                         font=(self.button_font, self.button_font_size),
                                         indicatoron=False,
                                         text=".")
        self.radio_equal = Radiobutton(self.frame,
                                       bg=self.op_button_color,
                                       borderwidth=0,
                                       command=lambda: self.calculate("Equal"),
                                       fg=self.op_font_color,
                                       font=(self.button_font, self.op_font_size),
                                       indicatoron=False,
                                       text="=")
        self.radio_sign.grid(row=7, column=0, padx=(0, 1), sticky="nsew")
        self.radio_0.grid(row=7, column=1, padx=(0, 1), sticky="nsew")
        self.radio_decimal.grid(row=7, column=2, padx=(0, 1), sticky="nsew")
        self.radio_equal.grid(row=7, column=3, padx=0, sticky="nsew")

        self.radio_sign.bind("<ButtonPress-1>", lambda event: self.press("mod", self.radio_sign))
        self.radio_0.bind("<ButtonPress-1>", lambda event: self.press("num", self.radio_0))
        self.radio_decimal.bind("<ButtonPress-1>", lambda event: self.press("mod", self.radio_decimal))
        self.radio_equal.bind("<ButtonPress-1>", lambda event: self.press("operator", self.radio_equal))

        self.radio_sign.bind("<ButtonRelease-1>", lambda event: self.release("mod", self.radio_sign))
        self.radio_0.bind("<ButtonRelease-1>", lambda event: self.release("num", self.radio_0))
        self.radio_decimal.bind("<ButtonRelease-1>", lambda event: self.release("mod", self.radio_decimal))
        self.radio_equal.bind("<ButtonRelease-1>", lambda event: self.release("operator", self.radio_equal))

        # Area widget
        self.__shape = StringVar(name="shape", value="Shapes:")

        # Area Frame
        self.widget_frame = Frame(self.frame)

        self.label_operation = Label(self.widget_frame,
                                     anchor="n",
                                     fg="#DDD",
                                     font=("Helvetica Light", 40),
                                     text='Shape:')
        self.circle_radio = Radiobutton(self.widget_frame,
                                        bg="#5F5F5F",
                                        borderwidth=0,
                                        command=lambda: self.render("Circle"),
                                        fg="#DDD",
                                        font=("Helvetica", 20),
                                        indicatoron=False,
                                        text="Circle")
        self.rectangle_radio = Radiobutton(self.widget_frame,
                                           bg="#5F5F5F",
                                           borderwidth=0,
                                           command=lambda: self.render("Rectangle"),
                                           fg="#DDD",
                                           font=("Helvetica", 20),
                                           indicatoron=False,
                                           text="Rectangle")
        self.square_radio = Radiobutton(self.widget_frame,
                                        bg="#5F5F5F",
                                        borderwidth=0,
                                        command=lambda: self.render("Square"),
                                        fg="#DDD",
                                        font=("Helvetica", 20),
                                        indicatoron=False,
                                        text="Square")
        self.triangle_radio = Radiobutton(self.widget_frame,
                                          bg="#5F5F5F",
                                          borderwidth=0,
                                          command=lambda: self.render("Triangle"),
                                          fg="#DDD",
                                          font=("Helvetica", 20),
                                          indicatoron=False,
                                          text="Triangle")

        self.label_operation.grid(row=0, rowspan=1, column=0, pady=5, sticky="nsew")
        self.circle_radio.grid(row=2, column=0, padx=(1, 0), pady=1, sticky="nsew")
        self.rectangle_radio.grid(row=3, column=0, padx=(1, 0), pady=(0, 1), sticky="nsew")
        self.square_radio.grid(row=4, column=0, padx=(1, 0), pady=(0, 1), sticky="nsew")
        self.triangle_radio.grid(row=5, column=0, padx=(1, 0), sticky="nsew")

        self.circle_radio.bind("<ButtonPress-1>", lambda event: self.press("num", self.circle_radio))
        self.rectangle_radio.bind("<ButtonPress-1>", lambda event: self.press("num", self.rectangle_radio))
        self.square_radio.bind("<ButtonPress-1>", lambda event: self.press("num", self.square_radio))
        self.triangle_radio.bind("<ButtonPress-1>", lambda event: self.press("num", self.triangle_radio))

        self.circle_radio.bind("<ButtonRelease-1>", lambda event: self.release("num", self.circle_radio))
        self.rectangle_radio.bind("<ButtonRelease-1>", lambda event: self.release("num", self.rectangle_radio))
        self.square_radio.bind("<ButtonRelease-1>", lambda event: self.release("num", self.square_radio))
        self.triangle_radio.bind("<ButtonRelease-1>", lambda event: self.release("num", self.triangle_radio))

        self.frame.columnconfigure("all", weight=1, uniform="column")
        self.frame.rowconfigure(0, weight=2, uniform="row")
        self.frame.rowconfigure(1, weight=1, uniform="row")
        self.frame.rowconfigure(2, weight=2, uniform="row")
        self.frame.rowconfigure(3, weight=2, uniform="row")
        self.frame.rowconfigure(4, weight=2, uniform="row")
        self.frame.rowconfigure(5, weight=2, uniform="row")
        self.frame.rowconfigure(6, weight=2, uniform="row")
        self.frame.rowconfigure(7, weight=2, uniform="row")

        self.widget_frame.columnconfigure("all", uniform="column")
        self.widget_frame.rowconfigure(0, weight=2, uniform="row")
        self.widget_frame.rowconfigure(1, weight=1, uniform="row")
        self.widget_frame.rowconfigure(2, weight=2, uniform="row")
        self.widget_frame.rowconfigure(3, weight=2, uniform="row")
        self.widget_frame.rowconfigure(4, weight=2, uniform="row")
        self.widget_frame.rowconfigure(5, weight=2, uniform="row")
        self.widget_frame.rowconfigure(6, weight=2, uniform="row")
        self.widget_frame.rowconfigure(7, weight=2, uniform="row")

    def calculate(self, button):
        widget = self.__widget.get()
        formula = ""

        if widget == "Area":
            print(formula)

        if formula == "Circle":
            area = circle(self.__temp_output.get())
            self.__temp_output.set(area)

        if self.__operator.get() == "":
            self.__operator.set(button)
        elif button == "Add":
            val1 = self.__temp_output.get()
            val2 = self.__output.get()
            output = add(val1, val2)
            self.__output.set(output)
            self.__temp_output.set(output)

    def clear(self):
        if self.radio_clear["text"] == "C":
            self.__temp_output.set(0)
            self.radio_clear["text"] = "AC"
        elif self.radio_clear["text"] == "AC" and self.__temp_output.get() == 0:
            self.__temp_output.set(0)
            self.__output.set(0)
            self.entry_output.configure(textvariable=self.__output)

    def mem(self, button):
        if button == "Clear":
            self.__memory.set(0)
            return

        self.__interrupter.set(True)
        memory = self.__memory.get()
        output = self.__temp_output.get()

        if button == "Add":
            self.__memory.set(add(memory, output))
        elif button == "Minus":
            self.__memory.set(subtract(memory, output))
        elif button == "Recall":
            self.__temp_output.set(memory)
            self.entry_output.configure(textvariable=self.__temp_output)

    def menu(self):
        self.widget_frame.grid_configure(row=0, rowspan=8, column=4, sticky="ew")
        option = self.__option.get()
        if option == "Area":
            self.__widget.set(option)
            self.update("Area")
        elif option == "Clear":
            self.__option.set("Options")
            self.__widget.set("")
            self.update()

    def onBackspace(self):
        self.__temp_output.set(5)
        self.update()
        if self.entry_output["textvariable"] == "temp" and self.__temp_output.get() > 0:
            value = self.__temp_output.get()
            value //= 10
            self.__temp_output.set(value)
        else:
            self.window.bell()

    def press(self, family, widget):
        if family == "memory":
            widget['bg'] = "#999"
        elif family == "clear":
            widget['bg'] = "#FF1111"
        elif family == "operator":
            widget['bg'] = "#FFC03D"
        elif family == "num":
            widget['bg'] = "#888"
        elif family == "mod":
            widget['bg'] = self.button_color

    def release(self, family, widget):
        if family == "memory":
            widget['bg'] = self.mem_button_color
        elif family == "clear":
            widget['bg'] = "#E00000"
        elif family == "operator":
            widget['bg'] = self.op_button_color
        elif family == "num":
            widget['bg'] = self.button_color
        elif family == "mod":
            widget['bg'] = self.modifier_button_color

    def render(self, event=None, char=None):
        key = 0

        # Change all clear button to clear
        if self.radio_clear["text"] == "AC":
            self.radio_clear["text"] = "C"

        if char == ".":
            return
        elif char == "sign":
            return

        # Determine event listener or command
        if event:
            key = int(event.keysym)
        elif char:
            key = int(char)

        temp = self.__temp_output.get()

        # Update after first input
        if self.entry_output["textvariable"] == "output" and self.__output.get() == 0:
            self.__output.set(key)
            self.__temp_output.set(key)
            self.entry_output.configure(textvariable=self.__temp_output)
        # Update cleared temp
        elif self.entry_output["textvariable"] == "temp" and temp == 0:
            self.__temp_output.set(key)
        # Update temp interrupt
        elif self.__operator.get() == "memory":
            self.__temp_output.set(key)
        # Update more input
        elif len(str(temp)) < 20:
            temp = (temp * 10) + key
            self.__temp_output.set(temp)
        else:
            self.window.bell()
            return

    def update(self, title=None):
        if title == "Area":
            self.window.title("A Better Calculator - Areas")
        else:
            self.window.title("A Better Calculator")

        self.window.update()
        window_width = self.window.winfo_reqwidth()
        window_height = self.window.winfo_reqheight()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x_cord = int((screen_width / 2) - (window_width / 2))
        y_cord = int((screen_height / 2) - (window_height / 2))
        self.window.geometry(f'+{x_cord}+{y_cord}')


if __name__ == "__main__":
    win = Tk()
    win.title("A Better Calculator")

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
