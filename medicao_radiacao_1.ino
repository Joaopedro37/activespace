const int pin_sensor = 2;
volatile int count = 0;
float contagem_total = 0;
const float constante_uSv = 0.2; // Constante de conversão para uSv/h
unsigned long inicio_contagem = 0;
volatile unsigned long tempo_pulso = 0;
volatile float pulso = 0.00;
volatile float pulso_anterior = 0.00;
float tempo = 3 * 60000; // Tempo em minutos que se quer medir
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
      inicio_contagem = millis();
      radiacao();
    }
  }
}

void radiacao() 
{

  Serial.println("- Vai comecar a contagem -");
  
  Serial.println("Tempo em que se deu o pulso, desde o início da contagem, em minutos: ");
  // Reinicia o contador e espera 60 segundos
  count = 0;
  delay(tempo);
  
  contagem_total = count;

  // Imprime o valor total de pulsos
  Serial.println("Total de pulsos: ");
  Serial.println(contagem_total);
}

void contador_pulsos() 
{
  tempo_pulso = millis();
  
  pulso_anterior = pulso;

  pulso = (tempo_pulso - inicio_contagem)/1000; // Arredonda o pulso às unidades, aos segundos
  pulso_minutos = pulso/60; // Tempo em que se deu o pulso, desde o inicio da contagem em minutos

  if(pulso != pulso_anterior)
  {
   count++; // Incrementa o contador quando um pulso é detectado
   
   Serial.println(pulso_minutos);
  }
  else{}
}

