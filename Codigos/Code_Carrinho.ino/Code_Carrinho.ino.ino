<<<<<<< HEAD
#define pino_motor_1_E 6
#define pino_motor_2_E 7
#define pino_motor_1_D 12
#define pino_motor_2_D 13
int velocidade;
=======
#define pino_motor_1_E 5
#define pino_motor_2_E 6
#define pino_motor_1_D 9
#define pino_motor_2_D 10
>>>>>>> 482244f9570f7f4cf0499a30fdec42099bb4f95a

class Motor{
public:
    int pino_1, pino_2;
    Motor(int p1, int p2)
    {
        this->pino_1 = p1;
        this->pino_2 = p2;

        pinMode(pino_1, OUTPUT);
        pinMode(pino_2, OUTPUT);

        digitalWrite(pino_1, LOW); 
        digitalWrite(pino_2, LOW); 
    }
    void frente()
    {
        analogWrite(pino_1, HIGH);
        digitalWrite(pino_2, LOW);
    }
    void re()
    {
        digitalWrite(pino_1, LOW);
        analogWrite(pino_2, HIGH);
    }
    void freiar()
    {
        analogWrite(pino_1, HIGH);
        analogWrite(pino_2, HIGH);
    }
    void parar()
    {
        digitalWrite(pino_1, LOW);
        digitalWrite(pino_2, LOW);
    }
};

Motor *motor_direito = new Motor(pino_motor_1_D, pino_motor_2_D);
Motor *motor_esquerdo = new Motor(pino_motor_1_E, pino_motor_2_E);

void Direita_vira()
{
    Serial.println("Virando para direita");
    motor_direito->frente();
    motor_esquerdo->re();
}
void Esquerda_vira(int v)
{
    Serial.println("Virando para esquerda");
    motor_direito->re();
    motor_esquerdo->frente();
}
void Frente(int v)
{
    Serial.println("Andando para frente");
    motor_direito->frente();
    motor_esquerdo->frente();
}
void Re(int v)
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
void Freiar(int v)
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
    delay(5000);
    Esquerda_vira();
    delay(5000);
    Direita_vira();
    delay(5000);
    Freiar();
    delay(5000);
    Re();
    delay(5000);
    Parar();
}
