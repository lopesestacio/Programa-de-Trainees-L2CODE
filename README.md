# Programa-de-Trainees-L2CODE

Repositorio destinado para o programa de trainnes da L2CODE com as resoluções da avaliação técnica da 1° fase do programa.


# 🚀 Começando

Cada questão possui uma pasta com suas respectivas resoluções.

- **[Question1](#-question-1)** - Aspirador Inteligente
- **[Question2](#-question-2)** - Desenvolvimento Web
- **[Question3](#-question-3)** - Consulta / Banco de Dados


📋 Question 1
------------

Arquivo: resolution.py - Escrito na linguagem Python.

Função
------------
Criamos uma função chamada new_position()

new_position() possui os seguintes parâmetros:
- width (int): Largura - default: 0
- length (int): Comprimento - default: 0
- actions (str): Ações - default: str vazio
- position (dict): Dicionario contendo posição inicial - default: {'x':0, 'y':0, 'o':'N'}
- info (bool): inicia o metodo input(), solicitando as entradas dos valores de width, length e actions. - default: True

A função pode ser usada sem passar nenhum dos parâmetros, ao iniciar será solicitado as seguintes entradas ao usuário:
- 1° entrada: width length -----> (A largura e o comprimento separadas por espaço. Ex: 5 5)
- 2° entrada: actions ----> (Uma sequencia de carecteres que correnspodem as ações do aspirador. Ex: FDFEFDFEFDFEFDF)

```
new_position()
#input
10 10
FFFFFFFFFDFFFFFFFFFDFFFFFFFFFDFFFFFFFFF
#output
O 0 0 

```
Também podemos passar os valores diretamente nos argumentos da função.
```
new_position(width=5, length=5, actions="FDFEFDFEFDFEFDF", info=False)
#output
O 0 0
```
📋 Question 2
------------

Uma série de exemplos passo-a-passo que informam o que você deve executar para ter um ambiente de desenvolvimento em execução.

Diga como essa etapa será:

```
Dar exemplos
```
📋 Question 3
------------

```
Dar exemplos
```
