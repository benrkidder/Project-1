from tkinter import *
from formulas import *
from typing import Optional, Literal


# TODO: Organize GUI __init__
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
        self.__memory = StringVar(name="memory", value="0")
        self.__moved = BooleanVar(name='moved', value=False)
        self.__operator = StringVar(name="operator", value="")
        self.__option = StringVar(name="menu", value="Options")
        self.__output = StringVar(name="output", value="0")
        self.__temp_output = StringVar(name="temp", value="0")
        self.__widget = StringVar(name="widget", value="")

        # Calculator Frame
        self.frame = Frame(self.window)
        self.frame.grid(column=0, columnspan=4)

        # Menu Popup
        self.options = OptionMenu(self.frame, self.__option, "Area", "Clear", command=lambda event: self.onMenu())
        self.options.grid(row=0, column=0, sticky="new")

        # Result/Entry output
        self.entry_output = Entry(self.frame,
                                  borderwidth=0,
                                  font=(self.font, 40),
                                  justify="right",
                                  highlightthickness=0,
                                  state="readonly",
                                  width=10,
                                  textvariable=self.__output)
        self.entry_output.grid(row=0, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

        # Keyboard Bindings
        self.window.bind("<KeyPress-1>", self.render)
        self.window.bind("<KeyPress-1>", lambda event: self.onPress("num", self.radio_1), add=True)
        self.window.bind("<KeyRelease-1>", lambda event: self.onRelease("num", self.radio_1))
        self.window.bind("<KeyPress-2>", self.render)
        self.window.bind("<KeyPress-2>", lambda event: self.onPress("num", self.radio_2), add=True)
        self.window.bind("<KeyRelease-2>", lambda event: self.onRelease("num", self.radio_2))
        self.window.bind("<KeyPress-3>", self.render)
        self.window.bind("<KeyPress-3>", lambda event: self.onPress("num", self.radio_3), add=True)
        self.window.bind("<KeyRelease-3>", lambda event: self.onRelease("num", self.radio_3))
        self.window.bind("<KeyPress-4>", self.render)
        self.window.bind("<KeyPress-4>", lambda event: self.onPress("num", self.radio_4), add=True)
        self.window.bind("<KeyRelease-4>", lambda event: self.onRelease("num", self.radio_4))
        self.window.bind("<KeyPress-5>", self.render)
        self.window.bind("<KeyPress-5>", lambda event: self.onPress("num", self.radio_5), add=True)
        self.window.bind("<KeyRelease-5>", lambda event: self.onRelease("num", self.radio_5))
        self.window.bind("<KeyPress-6>", self.render)
        self.window.bind("<KeyPress-6>", lambda event: self.onPress("num", self.radio_6), add=True)
        self.window.bind("<KeyRelease-6>", lambda event: self.onRelease("num", self.radio_6))
        self.window.bind("<KeyPress-7>", self.render)
        self.window.bind("<KeyPress-7>", lambda event: self.onPress("num", self.radio_7), add=True)
        self.window.bind("<KeyRelease-7>", lambda event: self.onRelease("num", self.radio_7))
        self.window.bind("<KeyPress-8>", self.render)
        self.window.bind("<KeyPress-8>", lambda event: self.onPress("num", self.radio_8), add=True)
        self.window.bind("<KeyRelease-8>", lambda event: self.onRelease("num", self.radio_8))
        self.window.bind("<KeyPress-9>", self.render)
        self.window.bind("<KeyPress-9>", lambda event: self.onPress("num", self.radio_9), add=True)
        self.window.bind("<KeyRelease-9>", lambda event: self.onRelease("num", self.radio_9))
        self.window.bind("<KeyPress-0>", self.render)
        self.window.bind("<KeyPress-0>", lambda event: self.onPress("num", self.radio_0), add=True)
        self.window.bind("<KeyRelease-0>", lambda event: self.onRelease("num", self.radio_0))
        self.window.bind("<KeyPress-BackSpace>", lambda event: self.onBackspace())

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
                                        command=lambda: self.onMemory("Clear"),
                                        fg=self.button_font_color,
                                        font=(self.button_font, self.button_font_size),
                                        indicatoron=False,
                                        text="mc")
        self.radio_mAdd = Radiobutton(self.frame,
                                      bg=self.mem_button_color,
                                      borderwidth=0,
                                      command=lambda: self.onMemory("Add"),
                                      fg=self.button_font_color,
                                      font=(self.button_font, self.button_font_size),
                                      indicatoron=False,
                                      text="m+")
        self.radio_mMinus = Radiobutton(self.frame,
                                        bg=self.mem_button_color,
                                        borderwidth=0,
                                        command=lambda: self.onMemory("Minus"),
                                        fg=self.button_font_color,
                                        font=(self.button_font, self.button_font_size),
                                        indicatoron=False,
                                        text="m-")
        self.radio_mRecall = Radiobutton(self.frame,
                                         bg=self.mem_button_color,
                                         borderwidth=0,
                                         command=lambda: self.onMemory("Recall"),
                                         fg=self.button_font_color,
                                         font=(self.button_font, self.button_font_size),
                                         indicatoron=False,
                                         text="mr")
        self.radio_mClear.grid(row=2, column=0, padx=(0, 1), pady=1, sticky="nsew")
        self.radio_mAdd.grid(row=2, column=1, padx=(0, 1), pady=1, sticky="nsew")
        self.radio_mMinus.grid(row=2, column=2, padx=(0, 1), pady=1, sticky="nsew")
        self.radio_mRecall.grid(row=2, column=3, pady=1, sticky="nsew")

        self.radio_mClear.bind("<ButtonPress-1>", lambda event: self.onPress("memory", self.radio_mClear))
        self.radio_mAdd.bind("<ButtonPress-1>", lambda event: self.onPress("memory", self.radio_mAdd))
        self.radio_mMinus.bind("<ButtonPress-1>", lambda event: self.onPress("memory", self.radio_mMinus))
        self.radio_mRecall.bind("<ButtonPress-1>", lambda event: self.onPress("memory", self.radio_mRecall))

        self.radio_mClear.bind("<ButtonRelease-1>", lambda event: self.onRelease("memory", self.radio_mClear))
        self.radio_mAdd.bind("<ButtonRelease-1>", lambda event: self.onRelease("memory", self.radio_mAdd))
        self.radio_mMinus.bind("<ButtonRelease-1>", lambda event: self.onRelease("memory", self.radio_mMinus))
        self.radio_mRecall.bind("<ButtonRelease-1>", lambda event: self.onRelease("memory", self.radio_mRecall))

        # Row with Clear, Percent, Mod and Div radios
        self.radio_clear = Radiobutton(self.frame,
                                       bg="#E00000",
                                       borderwidth=0,
                                       command=self.onClear,
                                       fg=self.op_font_color,
                                       font=(self.button_font, 18),
                                       indicatoron=False,
                                       text="AC")
        self.radio_percent = Radiobutton(self.frame,
                                         bg=self.op_button_color,
                                         borderwidth=0,
                                         command=lambda: self.onCalculate("Percent"),
                                         fg=self.op_font_color,
                                         font=(self.button_font, self.button_font_size),
                                         indicatoron=False,
                                         text="%")
        self.radio_mod = Radiobutton(self.frame,
                                     bg=self.op_button_color,
                                     borderwidth=0,
                                     command=lambda: self.onCalculate("Modulo"),
                                     fg=self.op_font_color,
                                     font=(self.button_font, self.button_font_size),
                                     indicatoron=False,
                                     text="mod")
        self.radio_div = Radiobutton(self.frame,
                                     bg=self.op_button_color,
                                     borderwidth=0,
                                     command=lambda: self.onCalculate("Divide"),
                                     fg=self.op_font_color,
                                     font=(self.button_font, self.op_font_size),
                                     indicatoron=False,
                                     text="\xf7")
        self.radio_clear.grid(row=3, column=0, padx=(0, 1), sticky="nsew")
        self.radio_percent.grid(row=3, column=1, padx=(0, 1), sticky="nsew")
        self.radio_mod.grid(row=3, column=2, padx=(0, 1), sticky="nsew")
        self.radio_div.grid(row=3, column=3, sticky="nsew")

        self.radio_clear.bind("<ButtonPress-1>", lambda event: self.onPress("clear", self.radio_clear))
        self.radio_percent.bind("<ButtonPress-1>", lambda event: self.onPress("operator", self.radio_percent))
        self.radio_mod.bind("<ButtonPress-1>", lambda event: self.onPress("operator", self.radio_mod))
        self.radio_div.bind("<ButtonPress-1>", lambda event: self.onPress("operator", self.radio_div))

        self.radio_clear.bind("<ButtonRelease-1>", lambda event: self.onRelease("clear", self.radio_clear))
        self.radio_percent.bind("<ButtonRelease-1>", lambda event: self.onRelease("operator", self.radio_percent))
        self.radio_mod.bind("<ButtonRelease-1>", lambda event: self.onRelease("operator", self.radio_mod))
        self.radio_div.bind("<ButtonRelease-1>", lambda event: self.onRelease("operator", self.radio_div))

        # First row of numbers and multiply radios
        self.radio_1 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   borderwidth=0,
                                   command=lambda: self.render(char="1"),
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="1")
        self.radio_2 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   borderwidth=0,
                                   command=lambda: self.render(char="2"),
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="2")
        self.radio_3 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   borderwidth=0,
                                   command=lambda: self.render(char="3"),
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="3")
        self.radio_mult = Radiobutton(self.frame,
                                      bg=self.op_button_color,
                                      borderwidth=0,
                                      command=lambda: self.onCalculate("Multiply"),
                                      fg=self.op_font_color,
                                      font=(self.button_font, self.op_font_size),
                                      indicatoron=False,
                                      text="\u00D7")
        self.radio_1.grid(row=6, column=0, padx=(0, 1), pady=1, sticky="nsew")
        self.radio_2.grid(row=6, column=1, padx=(0, 1), pady=1, sticky="nsew")
        self.radio_3.grid(row=6, column=2, padx=(0, 1), pady=1, sticky="nsew")
        self.radio_mult.grid(row=4, column=3, pady=1, sticky="nsew")

        self.radio_1.bind("<ButtonPress-1>", lambda event: self.onPress("num", self.radio_1))
        self.radio_2.bind("<ButtonPress-1>", lambda event: self.onPress("num", self.radio_2))
        self.radio_3.bind("<ButtonPress-1>", lambda event: self.onPress("num", self.radio_3))
        self.radio_mult.bind("<ButtonPress-1>", lambda event: self.onPress("operator", self.radio_mult))

        self.radio_1.bind("<ButtonRelease-1>", lambda event: self.onRelease("num", self.radio_1))
        self.radio_2.bind("<ButtonRelease-1>", lambda event: self.onRelease("num", self.radio_2))
        self.radio_3.bind("<ButtonRelease-1>", lambda event: self.onRelease("num", self.radio_3))
        self.radio_mult.bind("<ButtonRelease-1>", lambda event: self.onRelease("operator", self.radio_mult))

        # Second row of numbers and subtract radios
        self.radio_4 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   borderwidth=0,
                                   command=lambda: self.render(char="4"),
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="4")
        self.radio_5 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   borderwidth=0,
                                   command=lambda: self.render(char="5"),
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="5")
        self.radio_6 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   borderwidth=0,
                                   command=lambda: self.render(char="6"),
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="6")
        self.radio_sub = Radiobutton(self.frame,
                                     bg=self.op_button_color,
                                     borderwidth=0,
                                     command=lambda: self.onCalculate("Subtract"),
                                     fg=self.op_font_color,
                                     font=(self.button_font, self.op_font_size),
                                     indicatoron=False,
                                     text="\u2013")
        self.radio_4.grid(row=5, column=0, padx=(0, 1), sticky="nsew")
        self.radio_5.grid(row=5, column=1, padx=(0, 1), sticky="nsew")
        self.radio_6.grid(row=5, column=2, padx=(0, 1), sticky="nsew")
        self.radio_sub.grid(row=5, column=3, sticky="nsew")

        self.radio_4.bind("<ButtonPress-1>", lambda event: self.onPress("num", self.radio_4))
        self.radio_5.bind("<ButtonPress-1>", lambda event: self.onPress("num", self.radio_5))
        self.radio_6.bind("<ButtonPress-1>", lambda event: self.onPress("num", self.radio_6))
        self.radio_sub.bind("<ButtonPress-1>", lambda event: self.onPress("operator", self.radio_sub))

        self.radio_4.bind("<ButtonRelease-1>", lambda event: self.onRelease("num", self.radio_4))
        self.radio_5.bind("<ButtonRelease-1>", lambda event: self.onRelease("num", self.radio_5))
        self.radio_6.bind("<ButtonRelease-1>", lambda event: self.onRelease("num", self.radio_6))
        self.radio_sub.bind("<ButtonRelease-1>", lambda event: self.onRelease("operator", self.radio_sub))

        # Third row of numbers and add radios
        self.radio_7 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   borderwidth=0,
                                   command=lambda: self.render(char="7"),
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="7")
        self.radio_8 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   borderwidth=0,
                                   command=lambda: self.render(char="8"),
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="8")
        self.radio_9 = Radiobutton(self.frame,
                                   bg=self.button_color,
                                   borderwidth=0,
                                   command=lambda: self.render(char="9"),
                                   fg=self.button_font_color,
                                   font=(self.button_font, self.button_font_size),
                                   indicatoron=False,
                                   text="9")
        self.radio_add = Radiobutton(self.frame,
                                     bg=self.op_button_color,
                                     borderwidth=0,
                                     command=lambda: self.onCalculate("Add"),
                                     fg=self.op_font_color,
                                     font=(self.button_font, self.op_font_size),
                                     indicatoron=False,
                                     text="+")
        self.radio_7.grid(row=4, column=0, padx=(0, 1), pady=1, sticky="nsew")
        self.radio_8.grid(row=4, column=1, padx=(0, 1), pady=1, sticky="nsew")
        self.radio_9.grid(row=4, column=2, padx=(0, 1), pady=1, sticky="nsew")
        self.radio_add.grid(row=6, column=3, pady=1, sticky="nsew")

        self.radio_7.bind("<ButtonPress-1>", lambda event: self.onPress("num", self.radio_7))
        self.radio_8.bind("<ButtonPress-1>", lambda event: self.onPress("num", self.radio_8))
        self.radio_9.bind("<ButtonPress-1>", lambda event: self.onPress("num", self.radio_9))
        self.radio_add.bind("<ButtonPress-1>", lambda event: self.onPress("operator", self.radio_add))

        self.radio_7.bind("<ButtonRelease-1>", lambda event: self.onRelease("num", self.radio_7))
        self.radio_8.bind("<ButtonRelease-1>", lambda event: self.onRelease("num", self.radio_8))
        self.radio_9.bind("<ButtonRelease-1>", lambda event: self.onRelease("num", self.radio_9))
        self.radio_add.bind("<ButtonRelease-1>", lambda event: self.onRelease("operator", self.radio_add))

        # Row with Zero, Decimal, and Equal radios
        self.radio_sign = Radiobutton(self.frame,
                                      bg=self.modifier_button_color,
                                      borderwidth=0,
                                      command=lambda: self.onCalculate("Sign"),
                                      fg=self.button_font_color,
                                      font=(self.button_font, 22),
                                      indicatoron=False,
                                      text="\u00B1")
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
                                         command=lambda: self.render(char="Decimal"),
                                         fg=self.button_font_color,
                                         font=(self.button_font, self.button_font_size),
                                         indicatoron=False,
                                         text=".")
        self.radio_equal = Radiobutton(self.frame,
                                       bg=self.op_button_color,
                                       borderwidth=0,
                                       command=lambda: self.onCalculate("Equal"),
                                       fg=self.op_font_color,
                                       font=(self.button_font, self.op_font_size),
                                       indicatoron=False,
                                       text="=")
        self.radio_sign.grid(row=7, column=0, padx=(0, 1), sticky="nsew")
        self.radio_0.grid(row=7, column=1, padx=(0, 1), sticky="nsew")
        self.radio_decimal.grid(row=7, column=2, padx=(0, 1), sticky="nsew")
        self.radio_equal.grid(row=7, column=3, sticky="nsew")

        self.radio_sign.bind("<ButtonPress-1>", lambda event: self.onPress("mod", self.radio_sign))
        self.radio_0.bind("<ButtonPress-1>", lambda event: self.onPress("num", self.radio_0))
        self.radio_decimal.bind("<ButtonPress-1>", lambda event: self.onPress("mod", self.radio_decimal))
        self.radio_equal.bind("<ButtonPress-1>", lambda event: self.onPress("operator", self.radio_equal))
        self.window.bind("<KeyPress-Return>", lambda event: self.onPress("operator", self.radio_equal))
        self.window.bind("<KeyPress-Return>", lambda event: self.onCalculate("Equal"), True)
        self.window.bind("<KeyRelease-Return>", lambda event: self.onRelease("equal", self.radio_equal))

        self.radio_sign.bind("<ButtonRelease-1>", lambda event: self.onRelease("mod", self.radio_sign))
        self.radio_0.bind("<ButtonRelease-1>", lambda event: self.onRelease("num", self.radio_0))
        self.radio_decimal.bind("<ButtonRelease-1>", lambda event: self.onRelease("mod", self.radio_decimal))
        self.radio_equal.bind("<ButtonRelease-1>", lambda event: self.onRelease("equal", self.radio_equal))

        # Area Widget
        self.widget_frame = Frame(self.frame)

        self.label_area_dimension = Label(self.widget_frame,
                                          fg="#DDD",
                                          font=(self.font, 35),
                                          text='')
        self.label_operation = Label(self.widget_frame,
                                     anchor="w",
                                     fg="gray45",
                                     text="Shape:",
                                     font=(self.font, 20))
        self.circle_radio = Radiobutton(self.widget_frame,
                                        bg=self.button_color,
                                        borderwidth=0,
                                        command=lambda: self.onArea("Circle"),
                                        fg=self.button_font_color,
                                        font=(self.button_font, 20),
                                        indicatoron=False,
                                        text="Circle",
                                        value="Circle",
                                        variable=self.__widget)
        self.rectangle_radio = Radiobutton(self.widget_frame,
                                           bg=self.button_color,
                                           borderwidth=0,
                                           command=lambda: self.onArea("Rectangle"),
                                           fg=self.button_font_color,
                                           font=(self.button_font, 20),
                                           indicatoron=False,
                                           text="Rectangle",
                                           value="Rectangle",
                                           variable=self.__widget)
        self.square_radio = Radiobutton(self.widget_frame,
                                        bg=self.button_color,
                                        borderwidth=0,
                                        command=lambda: self.onArea("Square"),
                                        fg=self.button_font_color,
                                        font=(self.button_font, 20),
                                        indicatoron=False,
                                        text="Square",
                                        value="Square",
                                        variable=self.__widget)
        self.triangle_radio = Radiobutton(self.widget_frame,
                                          bg=self.button_color,
                                          borderwidth=0,
                                          command=lambda: self.onArea("Triangle"),
                                          fg=self.button_font_color,
                                          font=("Helvetica", 20),
                                          indicatoron=False,
                                          text="Triangle",
                                          value="Triangle",
                                          variable=self.__widget)
        self.label_formula = Label(self.widget_frame,
                                   fg="#DDD",
                                   text="",
                                   font=(self.font, 20))

        self.label_area_dimension.grid(row=0, column=0)
        self.label_operation.grid(row=1, column=0, sticky="ew")
        self.circle_radio.grid(row=2, column=0, padx=(1, 0), pady=1, sticky="nsew")
        self.rectangle_radio.grid(row=3, column=0, padx=(1, 0), sticky="nsew")
        self.square_radio.grid(row=4, column=0, padx=(1, 0), pady=1, sticky="nsew")
        self.triangle_radio.grid(row=5, column=0, padx=(1, 0), sticky="nsew")
        self.label_formula.grid(row=6, rowspan=2, padx=(1, 0), column=0)

        self.circle_radio.bind("<ButtonPress-1>", lambda event: self.onPress("widget", self.circle_radio))
        self.rectangle_radio.bind("<ButtonPress-1>", lambda event: self.onPress("widget", self.rectangle_radio))
        self.square_radio.bind("<ButtonPress-1>", lambda event: self.onPress("widget", self.square_radio))
        self.triangle_radio.bind("<ButtonPress-1>", lambda event: self.onPress("widget", self.triangle_radio))

        self.circle_radio.bind("<ButtonRelease-1>", lambda event: self.onRelease("widget", self.circle_radio))
        self.rectangle_radio.bind("<ButtonRelease-1>", lambda event: self.onRelease("widget", self.rectangle_radio))
        self.square_radio.bind("<ButtonRelease-1>", lambda event: self.onRelease("widget", self.square_radio))
        self.triangle_radio.bind("<ButtonRelease-1>", lambda event: self.onRelease("widget", self.triangle_radio))

        # Grid configuration
        self.frame.columnconfigure("all", weight=1, uniform="column", minsize=100)
        self.frame.rowconfigure(0, weight=2, uniform="row")
        self.frame.rowconfigure(1, weight=1, uniform="row")
        self.frame.rowconfigure(2, weight=2, uniform="row")
        self.frame.rowconfigure(3, weight=2, uniform="row")
        self.frame.rowconfigure(4, weight=2, uniform="row")
        self.frame.rowconfigure(5, weight=2, uniform="row")
        self.frame.rowconfigure(6, weight=2, uniform="row")
        self.frame.rowconfigure(7, weight=2, uniform="row")

    def onBackspace(self) -> None:
        """
        onBackspace handler for delete key interaction with entry output
        :return: None
        """
        # Reference Variable
        output = self.__output.get()

        # No value escape
        if output == "0":
            self.window.bell()
            return

        # Single digit modification
        elif len(output) == 1:
            self.__output.set("0")

        # Last position delete
        else:
            self.__output.set(output[:-1])

    def onCalculate(self, button: Literal["Equal",
                                          "Modulo",
                                          "Divide",
                                          "Multiply",
                                          "Subtract",
                                          "Add",
                                          "Sign",
                                          "Percent"]) -> None:
        """
        onCalculate is a handler method for the operation buttons.
        Makes calls to the imported the controller for computations.
        :param button: String identifier for operation type
        :return: None
        """
        # Initialize variables
        temp = self.__temp_output.get()
        output = self.__output.get()
        operator = self.__operator.get()
        widget = self.__widget.get()
        result: str

        # Set interrupter variable to modify input rendering
        self.__interrupter.set(True)

        # Button handler
        if button == "Equal" and not operator and output == "0" and temp == "0":
            return
        elif button == "Equal" and not operator and output == "0" and temp != "0":
            self.__output.set(temp)
            return
        elif button == "Equal" and not operator and output != "0":
            self.__temp_output.set(output)
            return
        elif button == "Equal" and widget != "":
            self.onArea(widget)
            return
        elif button == "Sign":
            result = multiply(output, "-1")
            self.__temp_output.set(result)
            self.__output.set(result)
            return
        elif button == "Percent":
            result = divide(output, "100")
            self.__temp_output.set(result)
            self.__output.set(result)
            return
        elif button not in ["Equal", "Sign", "Percent"]:
            self.__operator.set(button)

        # Save updated output to temp output variable
        self.__temp_output.set(output)

        # Calculation handler
        if operator == "Modulo":
            result = modulo(temp, output)
            self.__temp_output.set(output)
            self.__output.set(result)
        elif operator == "Divide":
            result = divide(temp, output)
            self.__temp_output.set(output)
            self.__output.set(result)
        elif operator == "Multiply":
            result = multiply(temp, output)
            self.__temp_output.set(output)
            self.__output.set(result)
        elif operator == "Subtract":
            result = subtract(temp, output)
            self.__temp_output.set(output)
            self.__output.set(result)
        elif operator == "Add":
            result = add(temp, output)
            self.__temp_output.set(output)
            self.__output.set(result)

    def onClear(self) -> None:
        """
        onClear handler method for Clear/AllClear button
        :return: None
        """
        # Reference variable
        temp = self.__temp_output.get()

        # Clear state
        if self.radio_clear["text"] == "C":
            self.radio_clear["text"] = "AC"
            if temp == "0":
                self.__operator.set("")

        elif self.radio_clear["text"] == "AC":
            self.__temp_output.set("0")
            self.__operator.set("")
            self.__output.set("0")

    def onMemory(self, button: Literal["Clear", "Add", "Minus", "Recall"]) -> None:
        """
        onMemory method to handle the memory buttons' function
        :param button: String identifier passed from button
        :return: None
        """
        # Clear Button
        if button == "Clear":
            self.__memory.set("0")
            return

        # Reference Variables
        memory = self.__memory.get()
        output = self.__output.get()

        # Add, Minus, and Recall Memory Buttons
        if button == "Add":
            self.__memory.set(add(memory, output))
        elif button == "Minus":
            self.__memory.set(subtract(memory, output))
        elif button == "Recall":
            self.radio_clear.config(text="C")
            self.__output.set(memory)

    def onMenu(self) -> None:
        """
        onMenu method renders the app when creating and clearing widgets
        :return: None
        """
        # Reference Variable
        option = self.__option.get()

        # Area Widget Render
        if option == "Area":
            self.__output.set("0")
            self.__temp_output.set("0")
            self.__operator.set("")
            min_column = self.window.winfo_width() / 4
            self.widget_frame.grid(row=0, rowspan=8, column=4, sticky="nsew")
            self.widget_frame.columnconfigure("all", weight=1, minsize=min_column, uniform="column")
            self.widget_frame.rowconfigure(0, weight=2, uniform="row")
            self.widget_frame.rowconfigure(1, weight=1, uniform="row")
            self.widget_frame.rowconfigure(2, weight=2, uniform="row")
            self.widget_frame.rowconfigure(3, weight=2, uniform="row")
            self.widget_frame.rowconfigure(4, weight=2, uniform="row")
            self.widget_frame.rowconfigure(5, weight=2, uniform="row")
            self.widget_frame.rowconfigure(6, weight=2, uniform="row")
            self.widget_frame.rowconfigure(7, weight=2, uniform="row")
            self.update("Area")

        # Clear Option Widget
        elif option == "Clear":
            self.__option.set("Options")
            self.circle_radio.configure(bg=self.button_color)
            self.rectangle_radio.configure(bg=self.button_color)
            self.square_radio.configure(bg=self.button_color)
            self.triangle_radio.configure(bg=self.button_color)
            self.label_area_dimension.configure(text="")
            self.label_formula.configure(text="")
            self.__widget.set("")
            self.widget_frame.grid_remove()
            self.update()

    def onPress(self, family: Literal["memory", "clear", "operator", "equal", "num", "mod", "widget"],
                widget: Optional[Radiobutton]) -> None:
        """
        onPress callback method acts as an animator for Button and Key Releases
        :param family: String indicating the family button style belongs to
        :param widget: Widget literal to apply the style
        :return: None
        """
        # Gives update appearance on entry output
        self.entry_output['fg'] = "#323232"

        # Button color shadow
        if family == "memory":
            widget['bg'] = "#999"
        elif family == "clear":
            widget['bg'] = "#FF1111"
        elif family == "operator":
            widget['bg'] = "#FFC03D"
        elif family == "equal":
            widget['bg'] = "#FFC03D"
        elif family == "num":
            widget['bg'] = "#888"
        elif family == "mod":
            widget['bg'] = self.button_color
        elif family == "widget":
            self.circle_radio['bg'] = self.button_color
            self.rectangle_radio['bg'] = self.button_color
            self.square_radio['bg'] = self.button_color
            self.triangle_radio['bg'] = self.button_color
            widget['bg'] = "#888"

    def onRelease(self, family: Literal["memory", "clear", "operator", "equal", "num", "mod", "widget"],
                  widget: Optional[Radiobutton]) -> None:
        """
        onRelease callback method acts as an animator for Button and Key Releases
        :param family: String indicating the family button style belongs to
        :param widget: Widget literal to apply the style
        :return: None
        """
        # Gives update appearance on entry output
        self.entry_output['fg'] = "white"

        # Button color reset
        if family == "memory":
            widget['bg'] = self.mem_button_color
        elif family == "clear":
            widget['bg'] = "#E00000"
        elif family == "operator":
            widget['bg'] = self.op_button_color
        elif family == "equal":
            widget['bg'] = self.op_button_color
        elif family == "num":
            widget['bg'] = self.button_color
        elif family == "mod":
            widget['bg'] = self.modifier_button_color

    def render(self, event: Optional[Event] = None, char: Optional[str] = None) -> None:
        """
        Render method renders clear button state and entry changes
        :param event: Class object passed from the bound listeners to buttons and keys or None
        :param char: String passed from command function indicating what button what pressed
        :return: None
        """
        key = char if char else event.keysym
        output = self.__output.get()
        interrupter = self.__interrupter.get()

        # Change All Clear to Clear
        if self.radio_clear["text"] == "AC":
            self.radio_clear["text"] = "C"

        if interrupter:
            self.__output.set("0")

        if char == "Decimal":
            if output.count(".") > 0:
                self.window.bell()
                return
            self.__output.set(output + ".")
            return

        if (output == "0" and key != "0") and output.count(".") == 0:
            self.__output.set(key)
            return
        elif interrupter:
            self.__output.set(key)
            self.__interrupter.set(False)
        else:
            self.__output.set(output + key)
            return

    def update(self, title: Optional[str] = None) -> None:
        """
        Update method refreshes the app when adding and removing widgets.
        :param title: String modifier from menu
        :return: None
        """
        if title == "Area":
            self.window.title("A Better Area Calculator")
        else:
            self.window.title("A Better Calculator")

        self.window.update()

        if not self.__moved.get():
            window_width = self.window.winfo_reqwidth()
            window_height = self.window.winfo_reqheight()
            screen_width = self.window.winfo_screenwidth()
            screen_height = self.window.winfo_screenheight()
            x_cord = int((screen_width / 2) - (window_width / 2))
            y_cord = int((screen_height / 2) - (window_height / 2))
            self.window.geometry(f'+{x_cord}+{y_cord}')

    def onArea(self, shape: Literal["Circle", "Rectangle", "Square", "Triangle"] | str) -> None:
        """
        Area calculating widget handler function. Renders widget state.
        :param shape: String modifier indicating shape formula to calculate.
        :return: None
        """
        temp = self.__temp_output.get()
        output = self.__output.get()
        operator = self.__operator.get()

        first_call = operator != shape
        second_call = operator == shape and (output != "0" and temp == "0")
        third_call = float(temp) > 0

        # Render the correct formulas
        if first_call:
            # Set Values
            self.__operator.set(shape)
            self.__output.set("0")
            self.__temp_output.set("0")

            if shape == "Circle":
                self.label_area_dimension.configure(text="r")
                self.label_formula.configure(text="A = \u03C0 r\u00B2")
            elif shape == "Rectangle":
                self.label_area_dimension.configure(text="s\u2081")
                self.label_formula.configure(text="A = s\u2081\u00D7s\u2082")
            elif shape == "Square":
                self.label_area_dimension.configure(text="s")
                self.label_formula.configure(text="A = s\u00B2")
            elif shape == "Triangle":
                self.label_area_dimension.configure(text="b")
                self.label_formula.configure(text="A = b \u00D7 h")
        elif second_call:
            if shape == "Circle":
                result = circle(output)
                self.label_area_dimension.configure(text="Area")
                self.__output.set(result)
                self.__temp_output.set(result)
                self.__operator.set("")
                self.circle_radio['bg'] = self.button_color
                self.__widget.set("")
            elif shape == "Rectangle":
                self.label_area_dimension.configure(text="s\u2082")
                self.__temp_output.set(output)
            elif shape == "Square":
                result = multiply(output, output)
                self.label_area_dimension.configure(text="Area")
                self.__output.set(result)
                self.__temp_output.set(result)
                self.__operator.set("")
                self.square_radio['bg'] = self.button_color
                self.__widget.set("")
            elif shape == "Triangle":
                self.label_area_dimension.configure(text="h")
                self.__temp_output.set(output)
        elif third_call:
            if shape == "Rectangle":
                self.label_area_dimension.configure(text="Area")
                result = multiply(temp, output)
                self.__output.set(result)
                self.__temp_output.set(result)
                self.__operator.set("")
                self.rectangle_radio['bg'] = self.button_color
                self.__widget.set("")
            elif shape == "Triangle":
                self.label_area_dimension.configure(text="Area")
                result = triangle(temp, output)
                self.__output.set(result)
                self.__temp_output.set(result)
                self.__operator.set("")
                self.triangle_radio['bg'] = self.button_color
                self.__widget.set("")


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
