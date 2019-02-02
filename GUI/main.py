# Main file for the Python GUI
# Initializes the main window, and is the file responsible for coordinating all subtasks

from Tkinter import *
import time;

def main():
    main_window = Tk();
    main_window.title("RX 350 Info Screen");

    top_label = Label(main_window, text="RX 350 Info Screen");
    top_label.grid(column=1, row=0);

    main_window.geometry("{0}x{1}+0+0".format(main_window.winfo_screenwidth(), main_window.winfo_screenheight()));
    main_window.state("zoomed");

    main_window.mainloop();

def anim_test():
    gui = Tk()
    var=IntVar()
    gui.geometry("800x800")
    c = Canvas(gui ,width=800 ,height=800)
    c.pack()
    oval = c.create_oval(5,5,60,60,fill='pink')
    a = 5
    b = 5
    for x in range(0 ,100):
        c.move(oval,a,b)
        gui.update()
        time.sleep(.01)
    gui.title("First title")
    gui.mainloop()

if __name__ == "__main__":
    # main();
    anim_test();