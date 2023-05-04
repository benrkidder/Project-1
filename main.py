from view import *


# Run Program
def main():
    window = Tk()
    window.title('A Better Calculator')
    width = 400
    height = 500
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_cord = int((screen_width / 2) - (width / 2))
    y_cord = int((screen_height / 2) - (height / 2))
    window.geometry(f'{width}x{height}+{x_cord}+{y_cord}')
    window.resizable(False, False)

    GUI(window)
    window.mainloop()


# Init Program
if __name__ == "__main__":
    main()
