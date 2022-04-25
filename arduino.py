from pyfirmata import Arduino, util, SERVO
from time import time, sleep

board = Arduino('COM3')

# Variavéis do semafóro (leds)
dig_semaforo_vermelho = 4
dig_semaforo_amarelo = 3
dig_semaforo_verde = 2

# matriz do display
display_pinos = [10, 12, 7, 8, 9, 13, 11, 6]
display_digitos = [
    [1,1,1,1,1,1,0,0],
    [0,1,1,0,0,0,0,0],
    [1,1,0,1,1,0,1,0],
    [1,1,1,1,0,0,1,0],
    [0,1,1,0,0,1,1,0],
    [1,0,1,1,0,1,1,0],
    [1,0,1,1,1,1,1,0],
    [1,1,1,0,0,0,0,0],
    [1,1,1,1,1,1,1,0],
    [1,1,1,0,0,1,1,0]
]

# servo motor
servo_pin = board.get_pin('d:5:p')
servo_pin.mode = SERVO




