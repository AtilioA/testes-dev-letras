import sys
import re
import unicodedata

from main import EnumScore


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


def verifica_feat_strings(stringEntrada: str, stringMusica: str) -> int:
    # print(stringMusica, stringMusica in "feat")
    if stringMusica == "feat":
        if stringEntrada == "feat":
            return EnumScore["NO_FEAT"].value
        else:
            return EnumScore["FEAT"].value
    else:
        return EnumScore["NO_FEAT"].value


# Compara duas strings e calcula pontuação de acordo com regras do teste
def compara_strings_ingenuo(s1: str, s2: str) -> int:
    score = 0
    lenComp = min(len(s1), len(s2))

    for i in range(lenComp):
        if s1[i] == s2[i]:
            # print(s1[:i], s1[i], s2[:i], s2[i])
            score += EnumScore["MATCH"].value

    if score == len(s2):  # Conseguimos corresponder toda a s2
        score += EnumScore["FULL_MATCH"].value

    return score


def divide_string_por_espaco(string: str) -> list[str]:
    return string.split(" ")


# Remove acentos de uma string e torna-a minúscula
def trata_string(string: str) -> str:
    string = remove_acentos_string(string)
    return string.lower()


# Remove apenas acentos de uma string (por ex.: não remove til)
def remove_acentos_string(string: str) -> str:
    # Normaliza string, separando caracteres especiais das letras
    stringNormalizada = unicodedata.normalize("NFKD", string)
    # Codifica em ASCII para remover caracteres especiais (fora do ASCII), agora separados, e ignora erros
    stringASCII = stringNormalizada.encode("ASCII", "ignore")
    # Decodifica de ASCII para a codificação padrão de str
    stringTratada = stringASCII.decode("ASCII")
    # Retorna a string, com todas as letras minúsculas
    # stringSemAcentos = re.sub(r'[áéíóúÁÉÍÓÚâêîôÂÊÎÔçÇ]', '', string)
    return stringTratada.lower()
