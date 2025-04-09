''' Auteur(s)   : Elias Atlab et Marcos Vinicius de Castro de facanha
    Librairie   : https://github.com/GBSL-Informatik/maqueen-plus-v2-mpy/tree/main
    Date        : 26 mars 2025
    Version     : 0.1
    Description : labyrinth

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

# line_sensor_data_all() renvoie valeur rgb 0;255

led_rgb(Color.BLUE)

def tourner_droite90():
    motor_stop()
    sleep(200)
    motor_run(Motor.LEFT, TURNING_SPEED, 1)
    motor_run(Motor.RIGHT, TURNING_SPEED)
    sleep(TimeToTurnRight) # temps mesuré pour faire 90 degré
    motor_stop()
    
def tourner_droite():
    motor_stop()
    sleep(200)
    while line_sensor(LineSensor.R2) == WHITE:
        motor_run(Motor.LEFT, TURNING_SPEED, 1)
        motor_run(Motor.RIGHT, TURNING_SPEED)
    motor_stop()
    
def tourner_gauche90():
    motor_stop()
    sleep(200)
    motor_run(Motor.LEFT, TURNING_SPEED)
    motor_run(Motor.RIGHT, TURNING_SPEED, 1)
    sleep(TimeToTurnLeft) # temps mesuré pour faire 90 degré
    motor_stop()

def tourner_gauche():
    motor_stop()
    sleep(200)
    while line_sensor(LineSensor.R2) == WHITE:
        motor_run(Motor.LEFT, TURNING_SPEED)
        motor_run(Motor.RIGHT, TURNING_SPEED,1)
        
    motor_stop()

while True:
    if line_sensor(LineSensor.R2) == BLACK :
        motor_run(Motor.ALL, SPEED)
        
        if line_sensor(LineSensor.L1) == BLACK or line_sensor(LineSensor.R1) == BLACK or line_sensor(LineSensor.M) == BLACK:
            tourner_droite()
            sleep(1000)
            
    if line_sensor(LineSensor.R2) == WHITE :
        tourner_gauche()
        sleep(1000)
    

