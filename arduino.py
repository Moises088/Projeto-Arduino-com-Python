from pyfirmata import Arduino, util, SERVO
from time import time, sleep

board = Arduino('COM3')

# Variavéis do semafóro
dig_semaforo_vermelho = 4
dig_semaforo_amarelo = 3
dig_semaforo_verde = 2

