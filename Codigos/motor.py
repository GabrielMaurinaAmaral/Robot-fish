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