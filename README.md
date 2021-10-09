<h1 align="center">
  Desafio Prático - Estágio Mobile Letras - 09/2021</a>
</h1>

<h4 align="center"> Códigos desenvolvidos durante o processo seletivo da Letras (Mobile) </h4>

<h5 align="center">

![License: Unlicense](https://img.shields.io/badge/License-Unlicense-White.svg)

</h5>

## ℹ Sobre:

Para a etapa do desafio prático, desenvolvi uma solução em Python utilizando árvore trie parcialmente.
A árvore foi utilizada para encontrar ocorrências da palavra 'feat' tanto na string de busca quanto nas strings do banco de músicas. Para encontrar correspondências entre esses dois, foi utilizado um algoritmo de busca ingênuo. Apesar da adição de uma árvore trie neste contexto não reduzir a complexidade do algoritmo de busca completo, é capaz de reduzir o tempo de pior caso para a checagem por feats.

Utilizei type hinting do Python para aproximar o código o máximo possível de uma linguagem estaticamente tipada, como Kotlin. Também modularizei o código para tentar separar as responsabilidades de cada trecho de código, tornar as funções mais puras e, assim, viabilizar testes mais unitários.


## ▶️ Executando a aplicação:

Para executar a aplicação, basta chamar o seguinte comando no diretório raiz do projeto, isto é, a pasta que contém o arquivo `main.py`:

```python3 main.py```

Por conta de utilizar sintaxe mais moderna de type hints, **o projeto requer Python ao menos 3.7 ou superior**; você também pode utilizar `py` ou `python` se eles invocarem Python de uma versão igual ou superior à 3.7, mas note que o projeto foi desenvolvido usando Python 3.9.1, sendo 3.9 ou superior a versão recomendada.

## 🧪 Rodando testes com `unittest`:
Análogo à seção anterior, execute o seguinte comando na pasta raiz:

```python3 -m unittest -v```
