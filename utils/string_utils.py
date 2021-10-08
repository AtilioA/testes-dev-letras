# Importa enum com valores de crédito/débito de pontuação de acordo com correspondências em strings
from main import EnumScore


# Strings de músicas fornecidas pelo desafio
stringsBanco = [
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
]


# Tabela de 'tradução' para remover acentos.
# Como cedilha (e também trema) não são acentos (apenas sinais diacríticos), não os incluí aqui
__accents_translation_table = str.maketrans(
    "áéíóúýàèìòùỳâêîôûŷÁÉÍÓÚÝÀÈÌÒÙỲÂÊÎÔÛŶ", "aeiouyaeiouyaeiouyAEIOUYAEIOUYAEIOUY"
)


def compara_strings_ingenuo(s1: str, s2: str) -> int:
    """Compara duas strings e calcula pontuação de acordo com regras do teste."""

    score = 0
    # Comparamos até alguma das duas strings acabar
    lenComp = min(len(s1), len(s2))

    if s1 and s2:
        for i in range(lenComp):
            # Se alguma das duas tiver caractere igual na mesma posição
            if s1[i] == s2[i]:
                # Incrementa score com crédito de MATCH (no nosso caso específico, 1)
                score += EnumScore["MATCH"].value

        # Se conseguirmos corresponder toda a s2
        if score == len(s2):
            # Incrementa score com crédito de FULL_MATCH (no nosso caso específico, 10)
            score += EnumScore["FULL_MATCH"].value

    return score


def divide_string_por_espaco(string: str) -> list[str]:
    """Divide uma string em seus espaços em branco, retornando lista de strings."""

    return string.split(" ")


def trata_string(string: str) -> str:
    """Torna string minúscula e remove acentos."""

    string = remove_acentos_string(string.lower())
    return string


def remove_acentos_string(string: str) -> str:
    """Remove apenas acentos de uma string (por ex.: não remove til)."""

    return string.translate(__accents_translation_table)
