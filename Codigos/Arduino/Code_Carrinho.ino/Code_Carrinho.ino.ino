#include <Arduino.h> 
#define pino_motor_1_E 11
#define pino_motor_2_E 12
#define pino_motor_1_D 6
#define pino_motor_2_D 7

class Motor{
public:
    int pino_1, pino_2;
    Motor(int p1, int p2) : pino_1(p1), pino_2(p2) {
        pinMode(pino_1, OUTPUT);
        pinMode(pino_2, OUTPUT);
        digitalWrite(pino_1, LOW); 
        digitalWrite(pino_2, LOW); 
    }
    void frente()
    {
        digitalWrite(pino_1, HIGH);
        digitalWrite(pino_2, LOW);
    }
    void re()
    {
        digitalWrite(pino_1, LOW);
        digitalWrite(pino_2, HIGH);
    }
    void freiar()
    {
        digitalWrite(pino_1, HIGH);
        digitalWrite(pino_2, HIGH);
    }
    void parar()
    {
        digitalWrite(pino_1, LOW);
        digitalWrite(pino_2, LOW);
    }
};

Motor *motor_direito = new Motor(pino_motor_1_D, pino_motor_2_D);
Motor *motor_esquerdo = new Motor(pino_motor_1_E, pino_motor_2_E);

<<<<<<< HEAD
void Direita()
{
    Serial.println("Virando para direita");
    motor_direito->frente();
    motor_esquerdo->parar();
}
void Esquerda()
{
    Serial.println("Virando para esquerda");
    motor_direito->parar();
=======
void Direita_vira()
{
    Serial.println("Virando para direita");
    motor_direito->frente();
    motor_esquerdo->re();
}
void Esquerda_vira()
{
    Serial.println("Virando para esquerda");
    motor_direito->re();
>>>>>>> e7d95f736f0ffb5c349e65636fb45fa266ab9fca
    motor_esquerdo->frente();
}
void Frente()
{
    Serial.println("Andando para frente");
    motor_direito->frente();
    motor_esquerdo->frente();
}
void Re()
{
    Serial.println("Dando re");
    motor_direito->re();
    motor_esquerdo->re();
}
void Parar()
{
    Serial.println("Parando");
    motor_direito->parar();
    motor_esquerdo->parar();
}
void Freiar()
{
    Serial.println("Freiando");
    motor_direito->freiar();
    motor_esquerdo->freiar();
}

void setup()
{
    Serial.begin(9600);      
}

void loop()
{
    Frente();
<<<<<<< HEAD
    delay(10000);
    Direita();
    delay(10000);
    Esquerda();
    delay(10000);
    Re();
    delay(10000);
    
=======
>>>>>>> e7d95f736f0ffb5c349e65636fb45fa266ab9fca
}
