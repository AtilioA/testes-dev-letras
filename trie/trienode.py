# Implementação adaptada da Wikipédia:
# https://en.wikipedia.org/wiki/Trie#Algorithms


# Para utilizar type hint com a classe Musica sem causar importação circular
# Também adiciona compatibilidade com versões de Python abaixo de 3.9 e acima de 3.7
from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from main import Musica


class TrieNode:
    def __init__(self) -> None:
        # Mapeia de str para TrieNode
        self.filhos: dict[str, TrieNode] = {}
        # Lista de músicas que possuem a palavra soletrada pelas arestas
        self.valor: list[Musica] = []

    def insere(self, chave: str, valor: Musica) -> None:
        """Insere chave:valor no node."""

        for char in chave:
            # Se não existir nó para o caractere da chave
            if char not in self.filhos:
                # Crie um novo nó
                self.filhos[char] = TrieNode()
            # Percorra pelo nó (se não existia antes, agora existe)
            self = self.filhos[char]

        # Após percorrer toda a árvore através dos caracteres da chave,
        # adicione o valor no último nó
        self.valor.append(valor)

    def busca(self, chave: str) -> list[Musica]:
        """Busca um valor pela sua chave no node."""

        # Procura por chave existente
        for char in chave:
            if char in self.filhos:
                # Se existir, percorra a árvore
                self = self.filhos[char]
            # Se não existir nó com caractere da chave, a chave não existe na árvore
            else:
                return None

        # Após percorrer toda a árvore através dos caracteres da chave,
        # retorn o valor do último nó
        return self.valor

    def popula_trie_musicas(self, musicas: list[Musica]) -> None:
        """Insere músicas de uma lista na árvore."""

        # Insere cada palavra de cada música na árvore
        for musica in musicas:
            for palavra in musica.titulo:
                self.insere(palavra, musica)

    def marca_feats(raizTrie: TrieNode) -> None:
        """Busca por músicas que contenham a palavra 'feat' e marca seus atributos."""

        musicasComFeat = raizTrie.busca("feat")
        if musicasComFeat:
            for musica in musicasComFeat:
                musica.set_feat(True)

    def __str__(self) -> str:
        return f"{self.valor};{self.filhos}"
