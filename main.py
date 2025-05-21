''' 
Auteur(s)   : Elias Atlab et Marcos Vinicius de Castro de Facanha  
Librairie   : https://github.com/marcos-027/Labyrinthe  
Date        : 21 mai 2025  
Version     : 1.0  
Description : Résolution de labyrinthe en suivant le mur de droite  

   /''''^''''\
  /  L1 M R1  \
 |             |
 |L2         R2|  <- L2 = R2 (inversé dans la librairie)
o|.............|o
'''

from maprincess import *
from microbit import *
import utime

# Constantes
SPEED = 25
TURNING_SPEED = 50
WHITE = 0
BLACK = 1

# Initialisation
led_rgb(Color.WHITE)
display.on()

# Fonctions de virage
def tourner_gauche():
    led_rgb(Color.RED)
    display.show("G")
    
    # Tourne jusqu'à détecter une ligne
    while (line_sensor_data(LineSensor.R1) < 120 or
           line_sensor_data(LineSensor.L1) < 120 or
           line_sensor_data(LineSensor.M) < 120):
        motor_run(Motor.LEFT, TURNING_SPEED, 1)
        motor_run(Motor.RIGHT, TURNING_SPEED)
    

def tourner_droite():
    led_rgb(Color.GREEN)
    display.show("D")
    
    
    # Tourne jusqu'à retrouver la ligne à droite (capteur L2 = R2)
    while line_sensor_data(LineSensor.L2) > 200:
        motor_run(Motor.LEFT, TURNING_SPEED)
        motor_run(Motor.RIGHT, TURNING_SPEED, 1)
    

# Boucle principale
while True:
    r2 = line_sensor_data(LineSensor.L2)  # R2 (mal étiqueté dans la lib)
    r1 = line_sensor_data(LineSensor.R1)
    l1 = line_sensor_data(LineSensor.L1)
    m = line_sensor_data(LineSensor.M)

    # 2. Si un mur est en face, on tourne à gauche
    if r1 < 120 or l1 < 120 or m < 120:
        tourner_gauche()
        print("G")
    
    # 1. Si le mur de droite a disparu, on tourne à droite
    elif r2 > 200:
        tourner_droite()
        print("D")

    # 3. Sinon, on avance
    else:
        motor_run(Motor.ALL, SPEED)
        led_rgb(Color.WHITE)
        display.show("T")
        print("T")

    sleep(100)  # petite pause pour stabiliser les lectures
