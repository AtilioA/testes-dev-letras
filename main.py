from enum import Enum

import utils.string_utils as str_utils


class EnumScore(Enum):
    """Enum que armazena os diferentes valores de pontuação."""

    FULL_MATCH = 10
    MATCH = 1
    WANT_FEAT = 0
    NO_FEAT = 0
    DONT_WANT_FEAT = -5


class Musica:
    """Classe que abstrai uma música do banco de músicas."""

    def __init__(self, titulo: list[str], tituloOriginal: str) -> None:
        # Título da música
        self.titulo: list[str] = titulo
        # Índice no vetor original de músicas
        self.tituloOriginal: str = tituloOriginal
        # Pontuação da música para a busca atual
        self.score: int = 0
        # Booleano representando caso a música tenha feat
        self.temFeat: bool = None
        self.verifica_feat()  # Atualiza self.temFeat

    def verifica_feat(self) -> None:
        """Determina se strings de entrada possuem 'feat' e retorna pontuação de acordo com lógica estabelecida pelo desafio."""

        for palavra in self.get_titulo():
            if palavra == "feat":
                return self.set_feat(True)
        # Caso nenhuma palavra da música seja 'feat'
        return self.set_feat(False)

    def pontua_feat(self, stringBusca) -> None:
        """Determina se string de entrada possui 'feat' e retorna pontuação de acordo com lógica estabelecida pelo desafio para a música em questão."""

        if self.tem_feat():
            if stringEntrada == "feat":
                # Usuário está procurando feat, não desconte ponto
                return self.adiciona_score(EnumScore["WANT_FEAT"].value)
            else:
                # Usuário não está procurando feat (mas música possui 'feat'), desconte ponto
                return self.adiciona_score(EnumScore["DONT_WANT_FEAT"].value)
        else:
            # Não há feat, não desconte ponto
            return self.adiciona_score(EnumScore["NO_FEAT"].value)

    def __str__(self) -> str:
        """Representação em string do objeto Música, imprimindo título, índice e score."""
        return f"m:{self.titulo}|i:{self.indiceOriginal}|{self.score} pontos"

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


if __name__ == "__main__":
    # Número de músicas a serem exibidas no ranking
    TOP_N_MUSICAS = 10

    # Lê da entrada e trata string para ignorar capitalização e acentos
    stringEntrada = str_utils.trata_string(str(input("# Digite sua busca: ").strip()))
    print("#")

    # Divide string de entrada para comparar palavra por palavra
    stringEntradaDividida: list[str] = stringEntrada.split()

    musicas: list[Musica] = []

    # Trata strings do banco de músicas da mesma forma que a da entrada
    stringsBancoTratadas = map(str_utils.trata_string, str_utils.stringsBanco)
    # Divide títulos das músicas por espaços para comparar palavra por palavra
    stringsBancoDivididas: list[list[str]] = list(
        map(str_utils.divide_string_por_espaco, stringsBancoTratadas)
    )

    # Percorre todas as músicas do banco de músicas
    for indice, titulo in enumerate(stringsBancoDivididas):
        # Cria objeto Musica para cada música, salvando o título original do vetor de strings do banco
        # Aqui deve-se haver cuidado para não realizar cópia e utilizar memória descenessariamente
        # Como strings são imutáveis em Python e não pretendemos alterar esta string, o seguinte custa pouca memória:
        objMusica = Musica(titulo, str_utils.stringsBanco[indice])

        # Compara cada palavra de entrada
        for palavraEntrada in stringEntradaDividida:
            # Com cada palavra do objeto Musica recém criado
            for palavraMusica in objMusica.get_titulo():
                # Adiciona pontos de acordo com as correspondências
                objMusica.adiciona_score(
                    str_utils.compara_strings_ingenuo(palavraEntrada, palavraMusica)
                )

            # Retira pontos caso apenas a música possua a palavra 'feat'
            objMusica.pontua_feat(palavraEntrada)

        # Adiciona o objeto Musica, agora com pontuação correta, a um vetor
        musicas.append(objMusica)

    print("# Resultados:")

    # Ordena músicas por score (decrescente, desempate não importa)
    musicas.sort(key=lambda musica: musica.score, reverse=True)

    # Percorre imprimindo até TOP_N_MUSICAS, neste caso 10
    for musica in musicas[:TOP_N_MUSICAS]:
        print(f"# {musica.score} pontos, {musica.tituloOriginal}")
    print("#")
    print("# {}".format("-" * 37))
