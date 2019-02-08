# Main file for the Python GUI
# Initializes the main window, and is the file responsible for coordinating all subtasks

from Tkinter import *
import time;
import display
import simulator

def main():
    w = Tk();
    display.init_window(w, w.winfo_screenwidth()/2, w.winfo_screenheight()/2);

if __name__ == "__main__":
    main()