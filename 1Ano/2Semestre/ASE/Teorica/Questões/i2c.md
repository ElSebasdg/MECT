# ASE
# Perguntas e Respostas sobre I2C

## Pergunta 1:
**O que é o protocolo I2C e para que serve?**

**Resposta:**
I2C (Inter-Integrated Circuit) é um protocolo de comunicação serial síncrona, desenvolvido pela Philips Semiconductor, que permite a comunicação entre múltiplos dispositivos num único barramento de dados. É amplamente utilizado para a comunicação entre microcontroladores e periféricos como sensores, EEPROMs, e displays.

## Pergunta 2:
**Quais são os principais sinais utilizados no protocolo I2C?**

**Resposta:**
Os principais sinais utilizados no protocolo I2C são:
- **SDA (Serial Data Line):** Linha de dados bidirecional utilizada para a transferência de dados.
- **SCL (Serial Clock Line):** Linha de relógio utilizada para sincronizar a transferência de dados através da linha SDA.

## Pergunta 3:
**Como funciona a estrutura de endereçamento no I2C?**

**Resposta:**
No protocolo I2C, cada dispositivo possui um endereço único de 7 ou 10 bits. Durante a comunicação, o dispositivo master envia um byte de endereço, seguido de um bit de leitura/escrita, para identificar o dispositivo slave com o qual deseja comunicar. O dispositivo slave com o endereço correspondente responde ao master.

## Pergunta 4:
**O que é uma condição de início e uma condição de paragem no protocolo I2C?**

**Resposta:**
- **Condição de início (Start Condition):** O master gera uma condição de início puxando a linha SDA de alta para baixa enquanto a linha SCL está alta. Isso indica o início de uma transmissão.
- **Condição de paragem (Stop Condition):** O master gera uma condição de paragem puxando a linha SDA de baixa para alta enquanto a linha SCL está alta. Isso indica o fim de uma transmissão.

## Pergunta 5:
**Explique a diferença entre um master e um slave no protocolo I2C.**

**Resposta:**
- **Master:** O dispositivo que inicia e controla a comunicação. Ele gera os sinais de clock e determina as condições de início e paragem.
- **Slave:** O dispositivo que responde ao master. Ele espera por comandos e responde quando o seu endereço é chamado pelo master.

## Pergunta 6:
**Como é realizada a comunicação de leitura no protocolo I2C?**

**Resposta:**
Na comunicação de leitura I2C, o master envia uma condição de início seguida pelo endereço do slave com o bit de leitura definido (1). O slave reconhece o endereço e começa a enviar os dados ao master, que os lê um byte de cada vez, enviando um ACK (acknowledge) após cada byte recebido. A comunicação termina quando o master envia uma condição de paragem.

## Pergunta 7:
**O que significa ACK e NACK no protocolo I2C?**

**Resposta:**
- **ACK (Acknowledge):** Um sinal enviado pelo receptor (master ou slave) após a recepção de um byte de dados, indicando que os dados foram recebidos com sucesso. A linha SDA é puxada para baixo durante o ciclo de clock ACK.
- **NACK (Not Acknowledge):** Um sinal enviado pelo receptor indicando que não conseguiu receber o byte de dados corretamente ou que não deseja receber mais dados. A linha SDA é deixada alta durante o ciclo de clock NACK.

## Pergunta 8:
**Descreva um cenário de comunicação entre um master e dois slaves no barramento I2C.**

**Resposta:**
1. O master inicia a comunicação enviando uma condição de início.
2. O master envia o endereço do primeiro slave com o bit de escrita.
3. O primeiro slave reconhece o endereço e responde com um ACK.
4. O master envia os dados para o primeiro slave.
5. Após a comunicação com o primeiro slave, o master pode enviar uma nova condição de início.
6. O master envia o endereço do segundo slave com o bit de leitura.
7. O segundo slave reconhece o endereço e responde com um ACK.
8. O slave envia os dados para o master.
9. O master termina a comunicação enviando uma condição de paragem.

## Pergunta 9:
**O que é uma condição de repetição de início (Repeated Start Condition) no protocolo I2C e quando é utilizada?**

**Resposta:**
Uma condição de repetição de início é gerada pelo master sem emitir uma condição de paragem anterior, permitindo que o master mantenha o controle do barramento e inicie uma nova comunicação sem liberar o barramento. É utilizada, por exemplo, quando o master deseja mudar a direção da comunicação (de escrita para leitura) sem perder o controle do barramento.

## Pergunta 10:
**Quais são as velocidades de comunicação padrão no protocolo I2C?**

**Resposta:**
As velocidades padrão no protocolo I2C são:
- **Standard Mode (Modo Padrão):** Até 100 kHz.
- **Fast Mode (Modo Rápido):** Até 400 kHz.
- **Fast Mode Plus (Modo Rápido Plus):** Até 1 MHz.
- **High-Speed Mode (Modo de Alta Velocidade):** Até 3.4 MHz.

