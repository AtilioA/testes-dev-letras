import string
import unicodedata

# from pprint import pprint
from enum import Enum


def compara_strings_ingenuo(string1, string2):
    correspondencias = 0
    lenString1 = len(string1)
    for i in range(lenString1):
        if string1[i] == string2[i]:
            correspondencias += 1

    if correspondencias == lenString1:
        correspondencias += 10

    return correspondencias


class EnumScore(Enum):
    FULL_MATCH = 10
    MATCH = 1
    FEAT = -5


class Musica:
    def __init__(self, titulo: list[str], indiceOriginal: int):
        self.titulo = titulo
        self.indiceOriginal = indiceOriginal
        self.score = 0
        self.feat = None

    def __str__(self):
        return f"m:{self.titulo}|i:{self.indiceOriginal}|{self.score} pontos"

    def subtrai_score(self, delta):
        return self.score - delta

    def adiciona_score(self, delta):
        return self.score + delta

    def get_titulo(self):
        return self.titulo

    def get_feat(self):
        return self.feat


class EspacoBusca:
    def __init__(self, musicasOriginais, musicasTratadas=[]):
        self.musicasOriginais = musicasOriginais
        self.musicasTratadas = []

    def adiciona_musica(self, musica: Musica):
        self.musicasTratadas.append(musica)

        pass


def verifica_feat_ingenuo(musicaBusca: Musica, musicasFixas: list[Musica]):
    for musicaFixa in musicasFixas:
        if musicaFixa.get_titulo() in "feat" and musicaBusca.get_titulo() in "feat":
            musicaFixa.subtrai_score(EnumScore["FEAT"].value)  # Use enum


def comparador_ingenuo(string, stringsFixas):
    lenString = len(string)

    #  Compara string com cada string fixa
    for stringFixa in stringsFixas:
        for char in stringFixa[:lenString]:
            pass


def divide_string_por_espaco(string):
    return string.split(" ")


# Remove caracteres especiais de letras (sinais diacríticos) e torna-as minúsculas
def trata_string(string: str) -> str:
    # Normaliza string, separando caracteres especiais das letras
    stringNormalizada = unicodedata.normalize("NFKD", string)
    # Codifica em ASCII para remover caracteres especiais (fora do ASCII), agora separados, e ignora erros
    stringASCII = stringNormalizada.encode("ASCII", "ignore")
    # Decodifica de ASCII para a codificação padrão de str
    stringTratada = stringASCII.decode("ASCII")
    # Retorna a string com apenas minúsculas
    return stringTratada.lower()


if __name__ == "__main__":
    stringsFixas = [
        "Que Tiro Foi Esse",
        "Deixe-me Ir",
        "Sobre Nós (Poesia Acústica #2)",
        "Apelido Carinhoso",
        "Tô Com Moral No Céu",
        "Lugar Secreto",
        "Jó",
        "Perfect",
        "Fica Tranquilo",
        "Capricorniana (Poesia Acústica #3)",
        "Amor da Sua Cama",
        "Nessas Horas",
        "Downtown (part. J Balvin)",
        "Você Vai Entender",
        "Aquieta Minh'alma",
        "Havana",
        "Havana feat Young Thug",
        "Vai Malandra (part. MC Zaac, Maejor, Tropkillaz e DJ Yuri Martins)",
        "Prioridade",
        "Trevo (Tu) (part. Tiago Iorc)",
        "Machika (part. Anitta y Jeon)",
        "Trem Bala",
        "Moça do Espelho",
        "Safadômetro",
        "Eu Cuido de Ti",
        "Too Good At Goodbyes",
        "Duro Igual Concreto",
        "Aquela Pessoa",
        "Rap Lord (part. Jonas Bento)",
        "Contrato",
        "IDGAF",
        "De Quem É a Culpa?",
        "Não Troco",
        "Quase",
        "Deus É Deus",
        "Anti-Amor",
        "Eu Era",
        "Cerveja de Garrafa (Fumaça Que Eu Faço)",
        "Não Deixo Não",
        "Rockstar feat 21 Savage",
        "New Rules",
        "Photograph",
        "Eu Juro",
        "Ninguém Explica Deus (part. Gabriela Rocha)",
        "Lindo És",
        "Bengala e Crochê",
        "Pirata e Tesouro",
        "A Libertina",
        "Pesadão (part. Marcelo Falcão)",
        "Aleluia (part. Michely Manuely)",
        "Eu Cuido de Ti",
        "Oi",
        "Céu Azul",
        "Never Be The Same",
        "My Life Is Going On",
        "Imaturo",
        "Gucci Gang",
        "Cuidado",
        "K.O.",
        "Échame La Culpa",
        "Échame La Culpa feat Luis Fonsi",
        "Tem Café (part. MC Hariel)",
        "Raridade",
        "Te Vi Na Rua Ontem",
        "Dona Maria (feat Jorge)",
        "Fica (part. Matheus e Kauan)",
        "9 Meses (Oração do Bebê)",
        "Muleque de Vila",
        "A Vitória Chegou",
        "Ar Condicionado No 15",
        "Vida Loka Também Ama",
        "Pegada Que Desgrama",
        "Transplante (part. Bruno & Marrone)",
        "Na Conta da Loucura",
        "Tem Café (part. Gaab)",
        "Apelido Carinhoso",
        "Perfect Duet",
        "Perfect Duet feat Beyoncé",
        "Coração de Aço",
        "Minha Morada",
        "Amar, Amei",
        "Regime Fechado",
        "O Escudo",
        "Minha Namorada",
        "Quero Conhecer Jesus (O Meu Amado é o Mais Belo)",
        "Me Leva Pra Casa",
        "Como é Que Faz? (part. Rob Nunes)",
        "The Scientist",
        "Bella Ciao",
        "O Que Tiver Que Ser Vai Ser",
        "Corpo Sensual (part. Mateus Carrilho)",
        "Cor de Marte",
        "Bom Rapaz (part. Jorge e Mateus)",
        "Vidinha de Balada",
        "Não Era Você",
        "Em Teus Braços",
        "De Trás Pra Frente",
        "All Of Me",
        "Believer",
        "A Música Mais Triste do Ano",
        "Rabiola",
        "Paraíso (part. Pabllo Vittar)",
        "Vem Pra Minha Vida",
    ] * 1

    inputString = trata_string(str(input().strip()))

    # espacoBusca = EspacoBusca(stringsFixas)
    objsMusicas = []
    musicasTratadas = []

    stringsFixasTratadas = map(trata_string, stringsFixas)
    stringsFixasDivididas = list(map(divide_string_por_espaco, stringsFixasTratadas))
    inputStringDividida = inputString.split()

    for indice, titulo in enumerate(stringsFixasDivididas):
        objMusica = Musica(titulo, indice)
        print(objMusica)
        musicasTratadas.append(objMusica)
        for palavra in titulo:
            musicasTratadas.append(objMusica)

    # print(inputString)
    # search(inputString)

    # print(stringsFixasDivididas, inputStringDividida)
