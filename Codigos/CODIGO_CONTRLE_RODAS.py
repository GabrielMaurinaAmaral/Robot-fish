import RPi.GPIO as GPIO
<<<<<<< HEAD
from motor import Motor
=======
>>>>>>> e7d95f736f0ffb5c349e65636fb45fa266ab9fca
import time

pino_motor_1_E = 11
pino_motor_2_E = 12
pino_motor_1_D = 6
pino_motor_2_D = 7

<<<<<<< HEAD
=======
class Motor:
    def __init__(self, p1, p2):
        self.pino_1 = p1
        self.pino_2 = p2
        GPIO.setup(self.pino_1, GPIO.OUT)
        GPIO.setup(self.pino_2, GPIO.OUT)
        GPIO.output(self.pino_1, GPIO.LOW)
        GPIO.output(self.pino_2, GPIO.LOW)

    def frente(self):
        GPIO.output(self.pino_1, GPIO.HIGH)
        GPIO.output(self.pino_2, GPIO.LOW)

    def re(self):
        GPIO.output(self.pino_1, GPIO.LOW)
        GPIO.output(self.pino_2, GPIO.HIGH)

    def freiar(self):
        GPIO.output(self.pino_1, GPIO.HIGH)
        GPIO.output(self.pino_2, GPIO.HIGH)

    def parar(self):
        GPIO.output(self.pino_1, GPIO.LOW)
        GPIO.output(self.pino_2, GPIO.LOW)

>>>>>>> e7d95f736f0ffb5c349e65636fb45fa266ab9fca
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

<<<<<<< HEAD
=======
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

>>>>>>> e7d95f736f0ffb5c349e65636fb45fa266ab9fca
try:
    while True:
        Frente()
except KeyboardInterrupt:
    Parar()
    GPIO.cleanup()
