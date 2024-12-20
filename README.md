# **Easy SQL: SQL em Português e Simplificado**

## **Equipe**

- Lucas Gonçalves Rodrigues  
- Arthur Marcelino Batista da Silva  
- Humberto Matheus  

---

## **Objetivo**

O projeto visa criar uma versão simplificada do SQL, com os principais comandos da linguagem original traduzidos para o português. A ideia é trazer uma versão mais simples e intuitiva do SQL que pode ser aprendida e utilizada por qualquer pessoa, idepndentemente de sua experiência com programação, podendo ser alguém totalmente leigo ou experiente na área.

O funcionamento do código consiste na escrita de comandos SQL mais simples e em português, que serão analisados e traduzidos para a linguagem SQL original.

Dentre as facilitações trazidas pelo Easy SQL, destacamos:

1) Utilização de comandos simplificados e intuitivos em português, para facilitar o aprendizado e a utilização da linguagem por pessoas que nunca programaram antes.
2) Tradução de agregadores padrões do SQL, como "AVG", "SUM" e "COUNT", que também foram traduzidos para "MEDIA", "SOMA" e "CONTAR", respectivamente. Além de trazer comandos intuitivos para somar à linguagem original, como a possibilidade de se utilizar "TUDO", como alternativa par "*", que seleciona todos os itens de uma tabela no SQL.

---

## **Como executar o projeto**

### 1. Criar um ambiente virtual:     
```
python -m venv venv
```

### 2. Ativar o ambiente virtual:

venv\Scripts\activate

### 3. Instalar o ANTLR:

```
wget https://www.antlr.org/download/antlr-4.13.2-complete.jar 
pip install antlr4-python3-runtime
```

### 4. Rodar a gramática:

```
java -jar antlr.jar -Dlanguage=Python3 EasySQL.g4
```

### 5. Rodar o códiog:

```
python main.py
```

### 6. Interagir com o Easy SQL:

Após rodar o código, digite os comandos desejados. Para encerrar a execução, pressione apenas a tecla Enter (deixe a entrada vazia).

---

## **Exemplo de código:**

### 1. Tabela Com Produtos de Uma Loja

```
CRIAR TABELA produtos (nome VARCHAR(50),marca VARCHAR(100), preco FLOAT);

INSERIR EM produtos VALORES ('Notebook','DELL', 3500.00); 
INSERIR EM produtos VALORES ('Notebook','Lenovo', 2500.00), ('Mouse','Multilaser', 14.99), ('Monitor','Philips', 2000.00);

MOSTRAR SOMA(preco) DE produtos;

ATUALIZAR produtos DEFINIR preco = 20 ONDE marca = 'Multilaser';

MOSTRAR TUDO DE produtos;

REMOVER DE produtos ONDE preco > 3000;

DELETAR TABELA produtos;
```

### 2. Tabela com Informação de Atletas

```
CRIAR TABELA atletas (nome VARCHAR(50),esporte VARCHAR(100),idade INT, aposentado BOOLEAN);

INSERIR EM atletas VALORES ('Cristiano Ronaldo','Futebol', 39, False), ('Chris Bumstead','Fisiculturismo', 29, False),('Mike Tyson','Boxe', 59, True), ('Tiger Woods','Golf', 48, True), ('LeBron James','Basquete', 39, False);

MOSTRAR MEDIA(idade) DE atletas;

ATUALIZAR atletas DEFINIR aposentado = True ONDE nome = 'Chris Bumstead';

MOSTRAR TUDO DE atletas ONDE aposentado = True;

REMOVER DE atletas ONDE esporte = 'Golf';

DELETAR TABELA atletas;
```
