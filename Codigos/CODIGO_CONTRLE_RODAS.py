import RPi.GPIO as GPIO
from motor import Motor
import time

pino_motor_1_E = 11
pino_motor_2_E = 12
pino_motor_1_D = 6
pino_motor_2_D = 7

motor_direito = Motor(pino_motor_1_D, pino_motor_2_D)
motor_esquerdo = Motor(pino_motor_1_E, pino_motor_2_E)

def Direita_vira():
    print("Virando para direita")
    motor_direito.frente()
    motor_esquerdo.re()

def Esquerda_vira():
    print("Virando para esquerda")
    motor_direito.re()
    motor_esquerdo.frente()

def Frente():
    print("Andando para frente")
    motor_direito.frente()
    motor_esquerdo.frente()

def Re():
    print("Dando re")
    motor_direito.re()
    motor_esquerdo.re()

def Parar():
    print("Parando")
    motor_direito.parar()
    motor_esquerdo.parar()

def Freiar():
    print("Freiando")
    motor_direito.freiar()
    motor_esquerdo.freiar()

try:
    while True:
        Frente()
except KeyboardInterrupt:
    Parar()
    GPIO.cleanup()
