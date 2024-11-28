## Easy SQL: SQL em Português e Simplificado

## Equipe

Lucas Gonçalves Rodrigues
Arthur Marcelino
Humberto Matheus

## Objetivo

O projeto visa criar uma versão simplificada do SQL, com os principais comandos da linguagem original traduzidos para o português. A ideia é trazer uma versão mais simples e intuitiva do SQL que pode ser aprendida e utilizada por qualquer pessoa, idepndentemente de sua experiência com programação, podendo ser alguém totalmente leigo ou experiente na área.

O funcionamento do código consiste na escrita de comandos SQL mais simples e em português, que serão analisados e traduzidos para a linguagem SQL original.

Dentre as facilitações trazidas pelo Easy SQL, destacamos:

1) Utilização de comandos simplificados e intuitivos em português, para facilitar o aprendizado e a utilização da linguagem por pessoas que nunca programaram antes.
2) Tradução de agregadores padrões do SQL, como "AVG", "SUM" e "COUNT", que também foram traduzidos para "MEDIA", "SOMA" e "CONTAR", respectivamente. Além de trazer comandos intuitivos para somar à linguagem original, como a possibilidade de se utilizar "TUDO", como alternativa par "*", que seleciona todos os itens de uma tabela no SQL.

## Como executar:

1) Criar um ambiente virtual: 

python -m venv venv 

2) Ativar o ambiente virtual:

venv\Scripts\activate

3) Instalar o ANTLR:

wget https://www.antlr.org/download/antlr-4.13.2-complete.jar 
pip install antlr4-python3-runtime

4) Rodar a gramática:

java -jar antlr.jar -Dlanguage=Python3 EasySQL.g4

5) Rodar o códiog:

python main.py


6) Após rodar o código, digite os comandos que desejar. A execução se encerrará quando for nada for passado para consulta (pressionar apenas a tecla "enter").

## Exemplo de código:


CRIAR TABELA produtos (nome VARCHAR(50),marca VARCHAR(100), preco FLOAT);

INSERIR EM produtos VALORES ('Notebook','DELL', 3500.00); \
INSERIR EM produtos VALORES ('Notebook','Lenovo', 2500.00); \
INSERIR EM produtos VALORES ('Mouse','Multilaser', 15.00); \
INSERIR EM produtos VALORES ('Monitor','Philips', 2000.00); \

MOSTRAR SOMA(preco) DE produtos;

ATUALIZAR preco DEFINIR 20 ONDE nome = 'Multilaser';

MOSTRAR TUDO DE produtos;

REMOVER DE produtos ONDE preco > 3000;

DELETAR TABELA produtos;