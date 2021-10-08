import unittest

import utils.string_utils as str_utils
import main


class TestMainFunctions(unittest.TestCase):
    def test_busca_musicas(self):
        sE = "21"
        sM = str_utils.stringsBanco
        musicas = main.busca_musicas(sE, sM)
        musicas.sort(key=lambda musica: musica.score, reverse=True)

        self.assertEqual(musicas[0].score, 7)
        self.assertEqual(musicas[0].tituloOriginal, "Rockstar feat 21 Savage")

        sE = "Vai malandr"
        musicas = main.busca_musicas(sE, sM)
        musicas.sort(key=lambda musica: musica.score, reverse=True)

        self.assertEqual(musicas[0].score, 31)
        self.assertEqual(
            musicas[0].tituloOriginal,
            "Vai Malandra (part. MC Zaac, Maejor, Tropkillaz e DJ Yuri Martins)",
        )
        self.assertEqual(musicas[1].score, 17)
        self.assertEqual(musicas[1].tituloOriginal, "Você Vai Entender")
        self.assertEqual(musicas[2].score, 14)
        self.assertEqual(musicas[2].tituloOriginal, "O Que Tiver Que Ser Vai Ser")
        self.assertEqual(musicas[3].score, 8)
        self.assertEqual(musicas[3].tituloOriginal, "Fica (part. Matheus e Kauan)")
        self.assertEqual(musicas[4].score, 7)
        self.assertEqual(musicas[4].tituloOriginal, "Pesadão (part. Marcelo Falcão)")
        self.assertEqual(musicas[5].score, 6)
        self.assertEqual(
            musicas[5].tituloOriginal,
            "Quero Conhecer Jesus (O Meu Amado é o Mais Belo)",
        )
        self.assertEqual(musicas[6].score, 6)
        self.assertEqual(musicas[6].tituloOriginal, "Bom Rapaz (part. Jorge e Mateus)")
        self.assertEqual(musicas[7].score, 6)
        self.assertEqual(musicas[7].tituloOriginal, "Vidinha de Balada")
        self.assertEqual(musicas[8].score, 6)
        self.assertEqual(musicas[8].tituloOriginal, "A Música Mais Triste do Ano")
        self.assertEqual(musicas[9].score, 6)
        self.assertEqual(musicas[9].tituloOriginal, "Paraíso (part. Pabllo Vittar)")

        sE = "Havana"
        musicas = main.busca_musicas(sE, sM)
        musicas.sort(key=lambda musica: musica.score, reverse=True)

        self.assertEqual(musicas[0].score, 16)
        self.assertEqual(musicas[0].tituloOriginal, "Havana")
        self.assertEqual(musicas[1].score, 11)
        self.assertEqual(musicas[1].tituloOriginal, "Havana feat Young Thug")
        self.assertEqual(musicas[2].score, 7)
        self.assertEqual(
            musicas[2].tituloOriginal,
            "Vai Malandra (part. MC Zaac, Maejor, Tropkillaz e DJ Yuri Martins)",
        )
        self.assertEqual(musicas[3].score, 5)
        self.assertEqual(musicas[3].tituloOriginal, "Fica (part. Matheus e Kauan)")
        self.assertEqual(musicas[4].score, 4)
        self.assertEqual(musicas[4].tituloOriginal, "Me Leva Pra Casa")
        self.assertEqual(musicas[5].score, 4)
        self.assertEqual(musicas[5].tituloOriginal, "Vidinha de Balada")
        self.assertEqual(musicas[6].score, 3)
        self.assertEqual(musicas[6].tituloOriginal, "Amor da Sua Cama")
        self.assertEqual(musicas[7].score, 3)
        self.assertEqual(musicas[7].tituloOriginal, "Pesadão (part. Marcelo Falcão)")
        self.assertEqual(musicas[8].score, 3)
        self.assertEqual(musicas[8].tituloOriginal, "Tem Café (part. MC Hariel)")

        sE = "feat"
        sM = "Featuring (feat)"
        musicas = main.busca_musicas(sE, sM)
        musicas.sort(key=lambda musica: musica.score, reverse=True)

        self.assertEqual(musicas[0].score, 4)
        self.assertEqual(musicas[0].tituloOriginal, "Featuring (feat)")


if __name__ == "__main__":
    unittest.main()
