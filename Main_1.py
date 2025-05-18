''' Auteur(s)   : Elias Atlab et Marcos Vinicius de Castro de facanha
    Librairie   : https://github.com/marcos-027/Labyrinthe
    Date        : 18 mai 2025
    Version     : 0.5
    Description : résolution de labyrinth en suivant le mur de droit

   /''''^''''\
  /  L1 M R1  \
 |             |
 |L2         R2|
o|.............|o

'''
from maprincess import *
from microbit import *
import utime

WHITE = 0
BLACK = 1


SPEED = 15
TimeToTurnRight = 2000
TimeToTurnLeft = 2000
TURNING_SPEED= 30

# line_sensor_data_all() renvoie valeur rgb 0;255 ATTENTION L2 et R2 inversé dans la librairie

led_rgb(Color.WHITE)
microbit.display.on()
    
def tourner_gauche():
    led_rgb(Color.RED)
    microbit.display.show("G")
    motor_stop()
    sleep(200)
    while line_sensor_data(LineSensor.R1) < 120 and line_sensor_data(LineSensor.L1) < 120 and line_sensor_data(LineSensor.M) < 120:
        motor_run(Motor.LEFT, TURNING_SPEED, 1)
        motor_run(Motor.RIGHT, TURNING_SPEED)
    motor_stop()
    
def tourner_droite():
    led_rgb(Color.GREEN)
    microbit.display.show("D")
    motor_stop()
    sleep(200)
    while line_sensor_data(LineSensor.R2) < 180:  # R2 = L2 mal défini dans la librairie
        motor_run(Motor.LEFT, SPEED)
        motor_run(Motor.RIGHT, 0)
    motor_stop()

while True:
    if line_sensor_data(LineSensor.L2) < 120:  # L2 = R2 mal défini dans la librairie
        motor_run(Motor.ALL, SPEED)
        microbit.display.show("T")
        print("T")

    if line_sensor_data(LineSensor.R1) < 120 or line_sensor_data(LineSensor.L1) < 120 or line_sensor_data(LineSensor.M) < 120:
        tourner_gauche()
        print("G")
        
    if line_sensor_data(LineSensor.L2) > 180:
        tourner_droite()
        print("D")
