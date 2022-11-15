# Programa-de-Trainees-L2CODE

Repositorio destinado para o programa de trainnes da L2CODE com as resoluções da avaliação técnica da 1° fase do programa.


# 🚀 Começando

Cada questão possui uma pasta com suas respectivas resoluções.

- **[Question1](#-question-1)** - Aspirador Inteligente
- **[Question2](#-question-2)** - Desenvolvimento Web
- **[Question3](#-question-3)** - Consulta / Banco de Dados


📋 Question 1
------------

Arquivo: `resolution.py` ---> Arquivo contendo a resolução da questão 1 escrito na linguagem Python.

Função
------------
Criamos uma função chamada `new_position(width=0, length=0, actions="", position={'x':0, 'y':0, 'o':'N'}, info=True)`

Parâmetros:
- `width` (int): Largura - default: 0
- `length` (int): Comprimento - default: 0
- `actions` (str): Ações - default: str vazio
- `position` (dict): Dicionario contendo posição inicial - default: {'x':0, 'y':0, 'o':'N'}
- `info` (bool): Parâmento que permite solicitar as entradas dos valores de width, length e actions. - default: True

Return: 
- `position_final`(str): Contendo a orientação e posição final do aspirador separados por espaço.

A função pode ser usada sem passar nenhum argumento, ao iniciar será solicitado as seguintes entradas ao usuário:
- 1° entrada: width length -----> (A largura e o comprimento separadas por espaço. Ex: 5 5)
- 2° entrada: actions ----> (Uma sequencia de carecteres que correspodem as ações do aspirador. Ex: FDFEFDFEFDFEFDF)
```
new_position()
#input
10 10
FFFFFFFFFDFFFFFFFFFDFFFFFFFFFDFFFFFFFFF
#output
O 0 0 

```
Também podemos passar os valores diretamente como argumentos da função, para isto devemos definir info=False.
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
Arquivos:
- `resolution.ipynb`---> Jupyter notebook contendo a resolução da questão 3.
- `dados.db`---> Arquivo de dados usado no sqlite contendo as tabelas pessoas, contratos e pagamentos.
- `inadimplemntes.sql`---> Arquivo sql contendo a consulta para selecionar as pessoas inadimplementes.
- `pagamento_completo.sql` ---> Arquivo sql contendo a consulta para selecionar as pessoas com pagamento completo.
- `tabelas.pdf` ---> Arquivo pdf contendo as tabelas tiradas do pdf da avaliação técnica disponibilizado pela L2CODE.

Geramos arquivos csv para as tabelas pessoas, contratos e pagamentos, que permitiu importar as tabelas para o sqlite, sem a necessidade de cria-las do zero.
- `pessoas.csv` ---> Tabela pessoas em formato csv.
- `contratos.csv` ---> Tabela contrato em formato csv.
- `pagamentos.csv` ---> Tabela pagamentos em formato csv.

Para a resolução da questão 3 existem duas resoluções no `resolution.ipynb` usando ferramentas diferentes.

- 1º Resolução: Utilizando as bibliotecas `tabula` para extração das tabelas no pdf e do `pandas` para realizar as consultas solicitadas.
- 2° Resolução: Utilizando consultas `SQL` com sqlite para realizar as consultas solicitadas.

Link útil

- https://sqliteonline.com/ : Site sqlite online, podemos exportar os arquivo de dados `dados.db` e as consultas `inadimplemntes.sql` e `pagamento_completo.sql`, para avaliar as respostas, sem precisar ter o sqlite ou qualquer banco de dados SQL instalados localmente.
