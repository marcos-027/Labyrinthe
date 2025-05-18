from microbit import *
import maqueen
import time

# Constantes 
SPEED = 15
TURNING_SPEED = 30
TURN_TIME = 2000  
WHITE = 0
BLACK = 1

# Variables de l'algorithme
turn_counter = 0       # Compteur de virages pour Pledge
suivre_mur = False # Mode suivi de mur

def avant():
    motor_run(Motor.LEFT, TURNING_SPEED)
    motor_run(Motor.RIGHT, TURNING_SPEED)

def stop():
    motor_stop()

def gauche():
    motor_run(Motor.LEFT, TURNING_SPEED, 1)
    motor_run(Motor.RIGHT, TURNING_SPEED)
    sleep(TURN_TIME)
    stop()

def droite():
    motor_run(Motor.LEFT, TURNING_SPEED)
    motor_run(Motor.RIGHT, TURNING_SPEED, 1)
    sleep(TURN_TIME)
    stop()

def suivre():
    global turn_counter
    
    if not line_sensor(LineSensor.M) == BLACK :
        avant()
        sleep(300)
        stop()
    else:
        gauche()
        turn_counter += 1  # +90°
        
        if line_sensor(LineSensor.M) == BLACK :
            gauche()
            turn_counter += 1  # +90°
            
            if line_sensor(LineSensor.M) == BLACK :
                gauche()
                turn_counter += 1  # +90°

def solve_maze():
    global turn_counter, suivre_mur
    
    while True:
        if not suivre and not line_sensor(LineSensor.M) == BLACK:
            # Mode exploration libre
            move_forward()
            sleep(300)
            stop()
        else:
            # Activer le suivi de mur
            suivre_mur = True
            
            if turn_counter == 0 and not line_sensor(LineSensor.M) == BLACK :
                # Réinitialiser si compteur à 0 et pas d'obstacle
                suivre_mur = False
                avant()
                sleep(300)
                stop()
            else:
                suivre()
        
        # Condition de sortie (à adapter)
        if button_a.is_pressed():
            break

# Programme principal
display.show("P")  # P pour Pledge
sleep(1000)

solve_maze()

display.show("S")  # S pour Sortie
stop()