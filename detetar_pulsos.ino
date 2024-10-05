const int pin_sensor = 2;
volatile int count = 0;
float contagem_total = 0;
const float constante_uSv = 0.2; // Constante de conversão para uSv/h
unsigned long inicio_contagem = 0;
volatile unsigned long tempo_pulso = 0;
float tempo = 60 * 60000; // Tempo em minutos que se quer medir
volatile float pulso_minutos = 0.00;

void setup()
{
  Serial.begin(9600);
  pinMode(pin_sensor, INPUT);
  attachInterrupt(digitalPinToInterrupt(pin_sensor), contador_pulsos, RISING);
}

void loop()
{
  if (Serial.available())
  {
    char texto_escrito = Serial.read();
    if (texto_escrito == 'S') 
    {
      inicio_contagem = micros();
      radiacao();
    }
  }
}

void radiacao() 
{
  

  Serial.println("- Vai comecar a contagem -");
  
  Serial.println("Tempo em que se deu o pulso, desde o início da contagem, em minutos: ");
  // Reinicia o contador e espera 60 segundos
  
  delay(tempo);

  Serial.println("A medição acabou");
}

void contador_pulsos() 
{
  tempo_pulso = micros();
  Serial.println(tempo_pulso);

}

