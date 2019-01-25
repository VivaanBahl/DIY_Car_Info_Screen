# Main file for the Python GUI
# Initializes the main window, and is the file responsible for coordinating all subtasks

from Tkinter import *

def main():
    main_window = Tk();
    main_window.title("RX 350 Info Screen");

    top_label = Label(main_window, text="RX 350 Info Screen");
    top_label.grid(column=1, row=0);

    main_window.geometry("{0}x{1}+0+0".format(main_window.winfo_screenwidth(), main_window.winfo_screenheight()));

    main_window.mainloop();

if __name__ == "__main__":
    main();