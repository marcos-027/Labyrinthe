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

# line_sensor_data_all() renvoie valeur rgb 0;255 ATTENTION L2 et R2 inversé dans la librairie

led_rgb(Color.WHITE)

def tourner_droite90():
    led_rgb(Color.GREEN)
    motor_stop()
    sleep(200)
    motor_run(Motor.LEFT, TURNING_SPEED, 1)
    motor_run(Motor.RIGHT, TURNING_SPEED)
    sleep(TimeToTurnRight) # temps mesuré pour faire 90 degré
    motor_stop()

def tourner_gauche90():
    led_rgb(Color.RED)
    motor_stop()
    sleep(200)
    motor_run(Motor.LEFT, TURNING_SPEED)
    motor_run(Motor.RIGHT, TURNING_SPEED, 1)
    sleep(TimeToTurnLeft) # temps mesuré pour faire 90 degré
    motor_stop()
    
def tourner_gauche():
    led_rgb(Color.RED)
    motor_stop()
    sleep(200)
    while line_sensor_data(LineSensor.R1) > 120 and line_sensor_data(LineSensor.L1) > 120 and line_sensor_data(LineSensor.M) > 120:
        motor_run(Motor.LEFT, TURNING_SPEED, 1)
        motor_run(Motor.RIGHT, TURNING_SPEED)
    motor_run(Motor.ALL, SPEED)
    
def tourner_droite():
    led_rgb(Color.GREEN)
    motor_stop()
    sleep(200)
    while line_sensor_data(LineSensor.R2) < 180: # R2 = L2 mal renseigné dans la librairie
        motor_run(Motor.LEFT, SPEED)
        motor_run(Motor.RIGHT, 0)
    motor_run(Motor.ALL, SPEED)

def tournerD():
    led_rgb(Color.GREEN)
    motor_stop()
    sleep(100)
    motor_run(Motor.LEFT, SPEED)
    motor_run(Motor.RIGHT, 0)
    sleep(500)
    
def tournerG():
    led_rgb(Color.RED)
    motor_stop()
    sleep(100)
    motor_run(Motor.LEFT, 0)
    motor_run(Motor.RIGHT, SPEED)
    sleep(500)



# while True:
#     if line_sensor(LineSensor.R2) == BLACK :
#         motor_run(Motor.ALL, SPEED)
#         led_rgb(Color.WHITE)
#         sleep(500)
#         
#     elif line_sensor(LineSensor.L1) == BLACK or line_sensor(LineSensor.R1) == BLACK or line_sensor(LineSensor.M) == BLACK :
#         tournerG()
#         
#             
#     elif line_sensor(LineSensor.R2) == WHITE :
#         tournerD()
while True:
    if line_sensor(LineSensor.R2) == BLACK :
        motor_run(Motor.ALL, SPEED)

        
    elif line_sensor(LineSensor.L1) == BLACK :
        motor_run(Motor.LEFT, 0)
        motor_run(Motor.RIGHT, SPEED)
    elif line_sensor(LineSensor.R1) == BLACK :
        motor_run(Motor.LEFT, 0)
        motor_run(Motor.RIGHT, SPEED)
    elif line_sensor(LineSensor.M) == BLACK :
        motor_run(Motor.LEFT, 0)
        motor_run(Motor.RIGHT, SPEED)
        
            
    elif line_sensor(LineSensor.R2) == WHITE :
        motor_run(Motor.LEFT, SPEED)
        motor_run(Motor.RIGHT, 0)
    sleep(100)
    motor_run(Motor.ALL, 0)
        

# while True :
#     print (line_sensor_data_all())


