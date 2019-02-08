import display
from random import randint
import time

target_cruising_range = randint(0, 300);
target_rpm = randint(0, 7000);

cruising_range = target_cruising_range + 10;
rpm = target_rpm;

def simulate():
    
    global target_cruising_range, target_rpm, rpm, cruising_range

    if (cruising_range == target_cruising_range):
        target_cruising_range = randint(0, 300);
    else:
        if (cruising_range > target_cruising_range): 
            cruising_range -= 1;
        else: 
            cruising_range += 1;

    if (rpm == target_rpm):
        target_rpm = randint(0, 7000);
    else:
        if (abs(rpm - target_rpm) < 50): 
            rpm -= 50;
        else: 
            rpm += 50;

    time.sleep(0.1);
    display.update_cruising_range(cruising_range);
    display.update_engine_rpm(rpm);

if __name__ == "__main__":
    simulate();