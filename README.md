# DIY_Car_Info_Screen
CMU Roboclub SHRG project for Spring 2019
This project is funded by the Carnegie Mellon Robotics Club


This project aims to create a vehicle information display that shows the driver pertinent information about their vehicle. This is accomplished by establishing a link via a car's OBD-II port (more info [here](https://www.geotab.com/blog/obd-ii/)), translating the messages into software, and then feeding them to a Python application which displays the information.

The operating system is (Raspian | Ubuntu | Win10 IoT | FreeRTOS), and the features / todo list is as follows:

- [*] setup a raspberry pi and screen
- [] Flash FreeRTOS and evaluate its potential
- [] Create Python GUI for displaying vehicle information
- [] Connect OBD link to vehicle and evaluate what information can be gathered
- [] write Linux driver for the OBD-II port and connect it to the GUI
- [] Design and print a case for the enclosure
- [] Integrate the GPS into the system, and add a map tab to the GUI
- [] add Spotify support into the Python GUI for centralized media playback
- [] (if possible) add a "controls" tab to control interal features of the vehicle
