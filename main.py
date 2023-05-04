from view import *


# Run Program
def main():
    window = Tk()
    window.title('A Better Calculator')

    GUI(window)

    window.update()
    window_width = window.winfo_reqwidth()
    window_height = window.winfo_reqheight()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_cord = int((screen_width / 2) - (window_width / 2))
    y_cord = int((screen_height / 2) - (window_height / 2))
    window.geometry(f'+{x_cord}+{y_cord}')
    window.resizable(False, False)

    window.mainloop()


# Init Program
if __name__ == "__main__":
    main()
