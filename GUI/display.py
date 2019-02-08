
import Tkinter as tk
import math
import simulator

cruising_range = 200;
gas_level = 75.0;
eco_mode = False;
outside_temp = 65;
tire_pressure = (33, 32, 33, 34) # front left, front right, back left, back right
engine_rpm = 2000.0;

window = None;

cruising_range_bar = -1;
rpm_needle = -1;

def update_cruising_range(new_cruising_range):
    global cruising_range;
    cruising_range = new_cruising_range;

def update_gas_level(new_gas_level):
    global gas_level;
    gas_level = new_gas_level;

def update_engine_rpm(new_engine_rpm):
    global engine_rpm;
    engine_rpm = new_engine_rpm;

def update_tire_pressures(new_tire_pressures):
    global tire_pressure;
    tire_pressure = new_tire_pressures;

def update_outside_temp(new_outside_temp):
    global outside_temp;
    outside_temp = new_outside_temp;

def draw_loop(canvas, width, height):
    global window, cruising_range, gas_level, eco_mode, outside_temp, tire_pressure, engine_rpm;
    global cruising_range_bar, rpm_needle

    canvas.delete(cruising_range_bar);
    canvas.delete(rpm_needle)

    # cruising range bounding box
    # determine top left and bottom right
    crbb_tlx = width / 8.0;
    crbb_tly = height / 8;
    crbb_brx = crbb_tlx + width / 8.0;
    crbb_bry = crbb_tly + height * 3 / 4;
    canvas.create_rectangle(crbb_tlx, crbb_tly, crbb_brx, crbb_bry);

    # cruising range bar
    cr_tlx = width / 8;
    cr_tly = height / 8;
    cr_brx = cr_tlx + width / 8;
    cr_bry = cr_tly + height * 3 / 4;
    cr_tly = cr_bry - (cruising_range * (height * 3 / 4)/300);
    cruising_range_bar = canvas.create_rectangle(cr_tlx, cr_tly, cr_brx, cr_bry, outline=None, fill="green");

    # engine RPM
    rpmbb_tlx = width * 3/8;
    rpmbb_tly = height * 5/8;
    rpmbb_brx = rpmbb_tlx + width/4;
    rpmbb_bry = rpmbb_tly + height/4;
    canvas.create_rectangle(rpmbb_tlx, rpmbb_tly, rpmbb_brx, rpmbb_bry);

    # engine RPM needle
    ndl_center_x = (rpmbb_tlx + rpmbb_brx) / 2;
    ndl_center_y = rpmbb_bry;
    ndl_rad = (rpmbb_bry - rpmbb_tly) * 3/4;
    ndl_th = math.pi - math.pi*engine_rpm/7000;

    ndl_pt_x = ndl_rad*math.cos(ndl_th) + ndl_center_x;
    ndl_pt_y = ndl_center_y - ndl_rad*math.sin(ndl_th);

    ndl_base_th = math.pi / 2 - ndl_th;
    ndl_base_rad = ndl_rad/10;

    ndl_base_pt_x1 = ndl_center_x + ndl_base_rad*math.cos(ndl_base_th);
    ndl_base_pt_y1 = ndl_center_y + ndl_base_rad*math.sin(ndl_base_th);
    ndl_base_pt_x2 = ndl_center_x + ndl_base_rad*math.cos(math.pi + ndl_base_th);
    ndl_base_pt_y2 = ndl_center_y + ndl_base_rad*math.sin(math.pi + ndl_base_th);

    rpm_needle = canvas.create_polygon(ndl_pt_x, ndl_pt_y, ndl_base_pt_x1, ndl_base_pt_y1, ndl_base_pt_x2, ndl_base_pt_y2, fill="red", outline="black");

    # draw the text box for outside temperature


    # draw the tire pressure boxes and numbers


    # draw the eco mode gauge and needle


    # schedule the next update
    window.after(100, draw_loop, canvas, width, height);
    window.after(10, simulator.simulate);
    pass

def init_window(in_window, width, height):
    global window, cruising_range, gas_level, eco_mode, outside_temp, tire_pressure, engine_rpm;

    window = in_window;

    window.geometry("{0}x{1}+0+0".format(width, height));
    
    canvas = tk.Canvas(window, width=width, height=height);

    draw_loop(canvas, width, height);

    canvas.pack();

    window.mainloop();
    
if __name__ == "__main__":
    init_window(tk.Tk(), 800, 450);
    # window.winfo_screenwidth(), window.winfo_screenheight()