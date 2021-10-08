# from pprint import pprint
from enum import Enum

import utils.string_utils as str_utils


class EnumScore(Enum):
    # Enum que armazena os diferentes valores de pontuação
    FULL_MATCH = 10
    MATCH = 1
    NO_FEAT = 0
    FEAT = -5


class Musica:
    def __init__(self, titulo: list[str], indiceOriginal: int):
        # Título da música
        self.titulo = titulo
        # Índice no vetor original de músicas
        self.indiceOriginal = indiceOriginal
        # Pontuação da música para a busca atual
        self.score = 0
        # Booleano representando caso a música tenha feat
        self.temFeat = None

    def __str__(self):
        # Representação em string do objeto Música, imprimindo título, índice e score
        return f"m:{self.titulo}|i:{self.indiceOriginal}|{self.score} pontos"

    def subtrai_score(self, delta):
        self.score -= delta

    def adiciona_score(self, delta):
        self.score += delta

    def get_titulo(self):
        return self.titulo

    def get_feat(self):
        return self.feat


if __name__ == "__main__":
    TOP_N_MUSICAS = 10

    # Lê da entrada e trata string para ignorar capitalização e acentos
    stringEntrada = str_utils.remove_acentos_string(
        str(input("# Digite sua busca: ").strip())
    )
    print("#")
    # Divide string de entrada para comparar palavra por palavra
    stringEntradaDividida = stringEntrada.split()

    # espacoBusca = EspacoBusca(str_utils.stringsFixas)
    objsMusicas = []
    musicasTratadas = []

    # Trata strings do fixas/banco de dados da mesma forma que a da entrada
    str_utils.stringsFixasTratadas = map(
        str_utils.remove_acentos_string, str_utils.stringsFixas
    )
    # Divide títulos das músicas por espaços para comparar palavra por palavra
    str_utils.stringsFixasDivididas = list(
        map(str_utils.divide_string_por_espaco, str_utils.stringsFixasTratadas)
    )

    for indice, titulo in enumerate(str_utils.stringsFixasDivididas):
        objMusica = Musica(titulo, indice)
        for palavraEntrada in stringEntradaDividida:
            for palavraMusica in objMusica.get_titulo():
                # print(palavraMusica)
                objMusica.adiciona_score(
                    str_utils.compara_strings_ingenuo(palavraEntrada, palavraMusica)
                )
                objMusica.adiciona_score(
                    str_utils.verifica_feat_strings(palavraEntrada, palavraMusica)
                )
        musicasTratadas.append(objMusica)

    print("# Resultados:")
    # Top músicas por score (decrescente, desempate não importa)
    musicasTratadas.sort(key=lambda x: x.score, reverse=True)
    for musica in musicasTratadas[: TOP_N_MUSICAS]:
        print(
            f"# {musica.score} pontos, {str_utils.stringsFixas[musica.indiceOriginal]}"
        )
    print("#")
    print("# {}".format("-" * 37))
