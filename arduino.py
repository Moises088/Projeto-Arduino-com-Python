from pyfirmata import Arduino, util, SERVO
from time import time, sleep

board = Arduino('COM3')

# Variavéis do semafóro (leds)
dig_semaforo_vermelho = 4
dig_semaforo_amarelo = 3
dig_semaforo_verde = 2

# Portas e matriz correspondente ao display de 7 segmentos
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

# Porta PWM do servo motor
servo_pin = board.get_pin('d:5:p')
servo_pin.mode = SERVO

# Função para exibir o número no display
def getDisplayNumber(board, display_pinos, display_digitos, number):
    for i in range(8):
        board.digital[display_pinos[i]].write(display_digitos[number][i])

# Função para "abrir" o servo motor (rotacionar aproximadamente 90 graus)
def rotateServoOpen(servo_pin):
    for i in range(11):
        servo_pin.write(9.2 * i)
        sleep(0.5 / (i + 0.2))

# Função para "fechar" o servo motor (rotacionar aproximadamente 0 graus)
def rotateServoClose(servo_pin):
    for i in range(10):
        servo_pin.write(90 - (i * 10))
        sleep(0.5 / (i + 0.2))


# Iniciando a lógica
print ("Inicio...")

index = 0 # Variável de repetição do código 
rotateServoClose(servo_pin) # Iniciar com o servo a 0 graus "fechado"

while index < 10:
    board.digital[dig_semaforo_vermelho].write(1) # Inciar com o led vermelho ligado

    for i in range(10): # Contar até 10 (de 0 a 9)
        getDisplayNumber(board, display_pinos, display_digitos, i)
        sleep(1)
    
    getDisplayNumber(board, display_pinos, display_digitos, 0) # Zerar o display
    board.digital[dig_semaforo_vermelho].write(0) # Apagar led vermelho
    board.digital[dig_semaforo_amarelo].write(1) # Ligar led amarelo
    rotateServoOpen(servo_pin) # "Abrir" servo enquanto o led está amarelo
    sleep(0.8)
    board.digital[dig_semaforo_amarelo].write(0) # Após abrir o servo apagar o led amarelo
    board.digital[dig_semaforo_verde].write(1) # Ligar led verde

    for i in range(10): # Contar até 10 (de 0 a 9)
        getDisplayNumber(board, display_pinos, display_digitos, i)
        sleep(1)

    rotateServoClose(servo_pin) # "Fechar" o servo
    board.digital[dig_semaforo_verde].write(0) # Apagar led verde
    getDisplayNumber(board, display_pinos, display_digitos, 0) # Zerar o display
    
    index = index + 1

print ("Fim...")


