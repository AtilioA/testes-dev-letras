import unittest

import sys

# Para poder importar módulos
sys.path.append(sys.path[0] + "/../../")

import main
import trie.trienode as trie
import utils.string_utils as str_utils


class TestTrieMethods(unittest.TestCase):
    def test_insere(self):
        m1 = main.Musica("titulo", "tituloOriginal")
        raiz = trie.TrieNode()
        raiz.insere(m1.titulo, m1)

        # Cada filho deve apontar para o próximo caractere de 'titulo'
        self.assertTrue(raiz.filhos["t"])
        self.assertTrue(raiz.filhos["t"].filhos["i"])
        self.assertTrue(raiz.filhos["t"].filhos["i"].filhos["t"])
        self.assertTrue(raiz.filhos["t"].filhos["i"].filhos["t"].filhos["u"])
        self.assertTrue(
            raiz.filhos["t"].filhos["i"].filhos["t"].filhos["u"].filhos["l"]
        )
        self.assertTrue(
            raiz.filhos["t"].filhos["i"].filhos["t"].filhos["u"].filhos["l"].filhos["o"]
        )
        # O último caractere na árvore deve conter um valor
        self.assertTrue(
            raiz.filhos["t"]
            .filhos["i"]
            .filhos["t"]
            .filhos["u"]
            .filhos["l"]
            .filhos["o"]
            .valor
        )

        # Nós intermediários devem estar vazios
        self.assertFalse(raiz.filhos["t"].valor)
        self.assertFalse(raiz.filhos["t"].filhos["i"].valor)
        self.assertFalse(raiz.filhos["t"].filhos["i"].filhos["t"].valor)
        self.assertFalse(raiz.filhos["t"].filhos["i"].filhos["t"].filhos["u"].valor)
        self.assertFalse(
            raiz.filhos["t"].filhos["i"].filhos["t"].filhos["u"].filhos["l"].valor
        )

    def test_busca(self):
        titulo1 = str_utils.divide_string_por_espaco(
            str_utils.trata_string("ceci n'est pas une pipe")
        )
        m1 = main.Musica(titulo1, "tituloOriginal")
        raiz = trie.TrieNode()
        for palavra in titulo1:
            raiz.insere(palavra, m1)

        self.assertEqual(raiz.busca("ceci"), [m1])
        self.assertEqual(raiz.busca("n'est"), [m1])
        self.assertEqual(raiz.busca("une")[0], m1)
        self.assertEqual(raiz.busca("pipe")[0], m1)

        titulo2 = str_utils.divide_string_por_espaco(
            str_utils.trata_string("ceci est une pipe")
        )
        m2 = main.Musica(titulo2, "tituloOriginal2")
        for palavra in titulo2:
            raiz.insere(palavra, m2)

        # Busca por uma palavra deve retornar todas as músicas com esta palavra presente no título
        self.assertEqual(raiz.busca("ceci"), [m1, m2])
        self.assertEqual(raiz.busca("une"), [m1, m2])
        self.assertEqual(raiz.busca("pipe"), [m1, m2])
        self.assertNotEqual(raiz.busca("est"), [m1, m2])
        self.assertNotEqual(raiz.busca("n'est"), [m1, m2])

    def test_popula_trie_musicas(self):
        raiz = trie.TrieNode()
        musicas = []

        titulo = str_utils.divide_string_por_espaco(
            str_utils.trata_string("ceci n'est pas une pipe")
        )
        musicas.append(main.Musica(titulo, "tituloOriginal"))
        titulo = str_utils.divide_string_por_espaco(
            str_utils.trata_string("ceci est une pipe")
        )
        musicas.append(main.Musica(titulo, "tituloOriginal"))
        titulo = str_utils.divide_string_por_espaco(
            str_utils.trata_string("celine dion | my heart will go on")
        )
        musicas.append(main.Musica(titulo, "tituloOriginal"))

        raiz.popula_trie_musicas(musicas)
        self.assertEqual(raiz.busca("ceci"), [musicas[0], musicas[1]])
        self.assertEqual(raiz.busca("celine"), [musicas[2]])

    def test_marca_feats(self):
        musicas = []
        titulo1 = str_utils.divide_string_por_espaco(
            str_utils.trata_string("featuring (feat)")
        )
        musicas.append(main.Musica(titulo1, "tituloOriginal"))
        titulo2 = str_utils.divide_string_por_espaco(
            str_utils.trata_string("rockstar feat 21")
        )
        musicas.append(main.Musica(titulo2, "tituloOriginal"))
        titulo3 = str_utils.divide_string_por_espaco(
            str_utils.trata_string("featuring")
        )
        musicas.append(main.Musica(titulo3, "tituloOriginal"))
        titulo4 = str_utils.divide_string_por_espaco(str_utils.trata_string("f"))
        musicas.append(main.Musica(titulo4, "tituloOriginal"))
        titulo5 = str_utils.divide_string_por_espaco(str_utils.trata_string("fe"))
        musicas.append(main.Musica(titulo5, "tituloOriginal"))
        titulo6 = str_utils.divide_string_por_espaco(str_utils.trata_string("fea"))
        musicas.append(main.Musica(titulo6, "tituloOriginal"))
        titulo7 = str_utils.divide_string_por_espaco(str_utils.trata_string("feat"))
        musicas.append(main.Musica(titulo7, "tituloOriginal"))

        raiz = trie.TrieNode()
        raiz.popula_trie_musicas(musicas)
        raiz.marca_feats()

        self.assertFalse(musicas[0].tem_feat())
        self.assertTrue(musicas[1].tem_feat())
        self.assertFalse(musicas[2].tem_feat())
        self.assertFalse(musicas[3].tem_feat())
        self.assertFalse(musicas[4].tem_feat())
        self.assertFalse(musicas[5].tem_feat())
        self.assertTrue(musicas[6].tem_feat())


if __name__ == "__main__":
    unittest.main()
