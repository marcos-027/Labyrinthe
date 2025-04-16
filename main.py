import radio
import random
from microbit import display, Image, button_a, sleep
from maqueen import Maqueen
robot = Maqueen()

radio.on()
radio.config(group=45)
while True:
    incoming = radio.receive()
    if incoming == "right":
        robot.motor_left(100)
        robot.motor_right(70, 1)

    if incoming == "left":
        robot.motor_left(70,1)
        robot.motor_right(100)

    if incoming == "up":
        robot.motor_left(100)
        robot.motor_right(110)

    if incoming == "down":
        robot.motor_left(70, 1)
        robot.motor_right(70, 1)
        
    if incoming == "stop":
        robot.motor_left(0)
        robot.motor_right(0)