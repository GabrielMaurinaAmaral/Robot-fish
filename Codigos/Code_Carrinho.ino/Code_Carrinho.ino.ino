#define pino_motor_1_E 6
#define pino_motor_2_E 7
#define pino_motor_1_D 12
#define pino_motor_2_D 13
int velocidade;

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
    void frente(int v)
    {
        analogWrite(pino_1, v);
        digitalWrite(pino_2, LOW);
    }
    void re(int v)
    {
        digitalWrite(pino_1, LOW);
        analogWrite(pino_2, v);
    }
    void freiar(int v)
    {
        analogWrite(pino_1, v/2);
        analogWrite(pino_2, v/2);
    }
    void parar()
    {
        digitalWrite(pino_1, LOW);
        digitalWrite(pino_2, LOW);
    }
};

Motor *motor_direito = new Motor(pino_motor_1_D, pino_motor_2_D);
Motor *motor_esquerdo = new Motor(pino_motor_1_E, pino_motor_2_E);

void Direita_vira(int v)
{
    Serial.println("Virando para direita");
    motor_direito->frente(v);
    motor_esquerdo->re(v);
}
void Esquerda_vira(int v)
{
    Serial.println("Virando para esquerda");
    motor_direito->re(v);
    motor_esquerdo->frente(v);
}
void Frente(int v)
{
    Serial.println("Andando para frente");
    motor_direito->frente(v);
    motor_esquerdo->frente(v);
}
void Re(int v)
{
    Serial.println("Dando re");
    motor_direito->re(v);
    motor_esquerdo->re(v);
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
    motor_direito->freiar(v/2);
    motor_esquerdo->freiar(v/2);
}

void setup()
{
    velocidade = 150;
    Serial.begin(9600);      
}

void loop()
{
    Frente(velocidade);
    delay(5000);
    Esquerda_vira(velocidade);
    delay(5000);
    Direita_vira(velocidade);
    delay(5000);
    Freiar(velocidade);
    delay(5000);
    Re(velocidade);
    delay(5000);
    Parar();
}
