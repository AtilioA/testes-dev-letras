import unittest

import utils.string_utils as str_utils
import main
import trie.trienode as trie


class TestMainFunctions(unittest.TestCase):
    def test_busca_musicas(self):
        stringEntrada = "21"
        # Trata string de busca para ignorar capitalização e acentos
        stringEntrada = str_utils.trata_string(stringEntrada).strip()
        # Divide string de busca para comparar palavra por palavra
        stringEntradaDivida: list[str] = stringEntrada.split()

        stringsMusicas = str_utils.trata_e_divide_strings_banco(str_utils.stringsBanco)
        stringsMusicas = main.cria_objs_musica(stringsMusicas, str_utils.stringsBanco)

        raizTrie = trie.TrieNode()
        raizTrie.popula_trie_musicas(stringsMusicas)
        raizTrie.marca_feats()

        musicas = main.busca_musicas(stringEntradaDivida, stringsMusicas)

        self.assertEqual(musicas[0].score, 7)
        self.assertEqual(musicas[0].tituloOriginal, "Rockstar feat 21 Savage")

        stringEntrada = "Vai malandr"
        # Trata string de busca para ignorar capitalização e acentos
        stringEntrada = str_utils.trata_string(stringEntrada).strip()
        # Divide string de busca para comparar palavra por palavra
        stringEntradaDivida: list[str] = stringEntrada.split()
        musicas = main.busca_musicas(stringEntradaDivida, stringsMusicas)

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

        # Reinicia pontuação de músicas
        for i, musica in enumerate(musicas):
            musicas[i].score = 0

        stringEntrada = "Havana"
        # Trata string de busca para ignorar capitalização e acentos
        stringEntrada = str_utils.trata_string(stringEntrada).strip()
        # Divide string de busca para comparar palavra por palavra
        stringEntradaDivida: list[str] = stringEntrada.split()
        musicas = main.busca_musicas(stringEntradaDivida, stringsMusicas)

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
        self.assertEqual(musicas[4].tituloOriginal, "Vidinha de Balada")
        self.assertEqual(musicas[5].score, 4)
        self.assertEqual(musicas[5].tituloOriginal, "Me Leva Pra Casa")
        self.assertEqual(musicas[6].score, 3)
        self.assertEqual(musicas[6].tituloOriginal, "Pesadão (part. Marcelo Falcão)")
        self.assertEqual(musicas[7].score, 3)
        self.assertEqual(musicas[7].tituloOriginal, "Bom Rapaz (part. Jorge e Mateus)")
        self.assertEqual(musicas[8].score, 3)
        self.assertEqual(musicas[8].tituloOriginal, "Paraíso (part. Pabllo Vittar)")

        stringEntrada = "feat"
        # Trata string de busca para ignorar capitalização e acentos
        stringEntrada = str_utils.trata_string(stringEntrada).strip()
        # Divide string de busca para comparar palavra por palavra
        stringEntradaDivida: list[str] = stringEntrada.split()

        stringsMusicasOriginal = ["Featuring (feat)"]
        stringsMusicas = str_utils.trata_e_divide_strings_banco(stringsMusicasOriginal)
        stringsMusicas = main.cria_objs_musica(stringsMusicas, stringsMusicasOriginal)

        raizTrie = trie.TrieNode()
        raizTrie.popula_trie_musicas(stringsMusicas)
        raizTrie.marca_feats()

        musicas = main.busca_musicas(stringEntradaDivida, stringsMusicas)

        self.assertEqual(musicas[0].score, 4)
        self.assertEqual(musicas[0].tituloOriginal, "Featuring (feat)")


if __name__ == "__main__":
    unittest.main()
