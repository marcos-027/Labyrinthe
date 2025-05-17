''' Auteur(s)   : Elias Atlab et Marcos Vinicius de Castro de facanha
    Librairie   : https://github.com/GBSL-Informatik/maqueen-plus-v2-mpy/tree/main
    Date        : 14 mai 2025
    Version     : 1.0
    Description : labyrinthe

   /''''^''''\
  /  L1 M R1  \
 |             |
 |L2         R2|
o|.............|o

'''
from microbit import *
from maqueen import *
import time

# Constantes 
SPEED = 30
TURN_TIME = 2 
BLACK = 1

# Variables
turn_counter = 0  # Compteur de virages 

def avant():
    motor_run(Motor.LEFT, SPEED)
    motor_run(Motor.RIGHT, SPEED)

def stop():
    motor_stop()

def tourner_gauche():
    motor_run(Motor.LEFT, SPEED, 1)
    motor_run(Motor.RIGHT, SPEED)
    time.sleep(TURN_TIME)
    stop()
    global turn_counter
    turn_counter += 1  # +90°

def tourner_droite():
    motor_run(Motor.LEFT, SPEED)
    motor_run(Motor.RIGHT, SPEED, 1)
    time.sleep(TURN_TIME)
    stop()
    global turn_counter
    turn_counter -= 1  # -90°

def suivre_mur_droit():
    global turn_counter
    
    if line_sensor(LineSensor.R2) == BLACK:
        tourner_droite()
        if line_sensor(LineSensor.M) == BLACK:
            tourner_gauche()  
    
    if line_sensor(LineSensor.M) != BLACK:
        avant()
        time.sleep(2)
    
    else:
        tourner_gauche()
        if line_sensor(LineSensor.M) == BLACK:  
            tourner_gauche()
            tourner_gauche()

def resoudre_labyrinthe():
    global turn_counter
    while True:
        if turn_counter == 0 and line_sensor(LineSensor.M) != BLACK:
            avant()
            time.sleep(2)
        else:
            suivre_mur_droit()
        
        if button_a.is_pressed():
            break


display.show("P")
time.sleep(1)

resoudre_labyrinthe()

display.show("S")
stop()

