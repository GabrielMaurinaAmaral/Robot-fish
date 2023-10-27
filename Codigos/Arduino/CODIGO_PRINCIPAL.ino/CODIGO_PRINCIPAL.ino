#define pino1_motor_E 5
#define pino2_motor_E 6
#define pino1_motor_D 9
#define pino2_motor_D 10

int velocidade;

class Motor{
public:
    int pino_1, pino_2;

    Motor(int p1, int p2) : pino_1(p1), pino_2(p2) {
        pinMode(pino_1, OUTPUT);
        pinMode(pino_2, OUTPUT);;
        digitalWrite(pino_1, LOW); 
        digitalWrite(pino_2, LOW); 
    }

    // Funções do motor:
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
    void parar()
    {
        digitalWrite(pino_1, LOW);
        digitalWrite(pino_2, LOW);
    }
    void freiar(int v)
    {
        analogWrite(pino_2, v/4);
        analogWrite(pino_2, v/4);
    }
};

Motor *motor_direito = new Motor(pino1_motor_D, pino2_motor_D);
Motor *motor_esquerdo = new Motor(pino1_motor_E, pino2_motor_E);

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
    motor_direito->freiar(v);
    motor_esquerdo->freiar(v);
}

void setup()
{
    velocidade = 150;
    Serial.begin(9600);      
}

void loop()
{

}
