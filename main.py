# Adiciona compatibilidade com versões de Python abaixo de 3.9 e ao menos 3.7
from __future__ import annotations

from enum import Enum


import trie.trienode as trie


class EnumScore(Enum):
    """Enum que armazena os diferentes valores de pontuação."""

    FULL_MATCH = 10
    MATCH = 1
    WANT_FEAT = 0
    NO_FEAT = 0
    DONT_WANT_FEAT = -5


import utils.string_utils as str_utils


class Musica:
    """Classe que abstrai uma música do banco de músicas."""

    def __init__(self, titulo: list[str], tituloOriginal: str) -> None:
        # Título da música, tratado e divido em uma lista de strings
        self.titulo: list[str] = titulo
        # Título original da música
        self.tituloOriginal: str = tituloOriginal
        # Pontuação da música para a busca atual
        self.score: int = 0
        # Booleano representando caso a música tenha feat
        self.temFeat: bool = None

    def pontua_feat(self, stringsBusca: list[str]) -> None:
        """Checa se strings de busca possuem feat e altera pontuação de acordo com lógica estabelecida pelo desafio para a string buscada."""

        if self.tem_feat():
            if "feat" in stringsBusca:
                # Usuário está procurando feat, não desconte ponto
                self.adiciona_score(EnumScore["WANT_FEAT"].value)
            else:
                # Usuário não está procurando feat mas música possui 'feat', desconte ponto
                self.adiciona_score(EnumScore["DONT_WANT_FEAT"].value)
        else:
            # Não há feat, não desconte ponto
            self.adiciona_score(EnumScore["NO_FEAT"].value)

    def __str__(self) -> str:
        """Representação em string do objeto Música, imprimindo título, índice e score."""
        return f"{self.tituloOriginal}|{self.score} pontos"

    def adiciona_score(self, delta: int) -> None:
        """Soma um valor ao score de um objeto Musica."""
        self.score += delta

    def subtrai_score(self, delta: int) -> None:
        """Subtrai um valor do score de um objeto Musica."""
        self.score -= delta

    def set_feat(self, temFeat: bool) -> None:
        """Atribui um valor ao atributo temFeat de um objeto Musica."""
        self.temFeat = temFeat

    def get_titulo(self) -> list[str]:
        """Retorna o título de uma música, sendo uma lista de strings de cada palavra."""
        return self.titulo

    def tem_feat(self) -> bool:
        """Retorna se uma música tem feat ou não."""
        return self.temFeat


def cria_objs_musica(stringsMusicasDivididas: list[list[str]], stringsBanco: list[str]):
    """Cria um objeto Musica para cada lista de string da lista dada como entrada"""
    # Cria objeto Musica para cada música, salvando o título original do vetor de strings do banco
    # Aqui deve-se haver cuidado para não realizar cópia e utilizar memória descenessariamente
    # Como strings são imutáveis em Python e não pretendemos alterar esta string, o seguinte custa pouca memória:

    objsMusicas = []

    for indice, titulo in enumerate(stringsMusicasDivididas):
        objMusica = Musica(titulo, stringsBanco[indice])
        objsMusicas.append(objMusica)

    return objsMusicas


def busca_musicas(stringsBusca: list[str], musicas: list[Musica]) -> list[Musica]:
    # Percorre todas as músicas do banco de músicas
    for i, musica in enumerate(musicas):
        # Compara cada palavra de busca
        for palavraBusca in stringsBusca:
            # Com cada palavra do objeto Musica recém criado
            for palavraMusica in musica.get_titulo():
                # Adiciona pontos de acordo com as correspondências
                musicas[i].adiciona_score(
                    str_utils.compara_strings_ingenuo(palavraBusca, palavraMusica)
                )

        # Retira pontos caso apenas a música possua a palavra 'feat'
        musicas[i].pontua_feat(palavraBusca)

    return musicas


if __name__ == "__main__":
    # Número de músicas a serem exibidas no ranking
    TOP_N_MUSICAS = 10

    # Lê string de busca da entrada
    stringEntrada = input("# Digite sua busca: ")
    # Trata string de busca para ignorar capitalização e acentos
    stringEntrada = str_utils.trata_string(stringEntrada).strip()
    # Divide string de busca para comparar palavra por palavra
    stringEntradaDividida: list[str] = stringEntrada.split()

    # Lista com títulos das músicas separados por espaço (i.e., dividos em lista de strings)
    stringsBancoDivididas: list[list[str]] = str_utils.trata_e_divide_strings_banco(
        str_utils.stringsBanco
    )

    # Lista de objetos Musica para armazenar objetos com o score devidamente computado
    musicas: list[Musica] = cria_objs_musica(
        stringsBancoDivididas, str_utils.stringsBanco
    )

    # Monta árvore trie para buscar por músicas com palavra 'feat'
    raizTrie = trie.TrieNode()
    raizTrie.popula_trie_musicas(musicas)
    raizTrie.marca_feats()

    # Faz comparação ingênua
    musicas = busca_musicas(stringEntradaDividida, musicas)

    # Ordena músicas por score (decrescente, desempate não importa)
    musicas.sort(key=lambda musica: musica.score, reverse=True)

    print("#")
    print("# Resultados:")
    # Percorre imprimindo até TOP_N_MUSICAS, neste caso 10
    for musica in musicas[:TOP_N_MUSICAS]:
        print(f"# {musica.score} pontos, {musica.tituloOriginal}")
    print("#")
    print("# {}".format("-" * 37))
