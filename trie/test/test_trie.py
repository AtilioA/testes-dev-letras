import unittest

import sys

sys.path.append(sys.path[0] + "/../../")
import main
import trie.trienode as trie


class TestStringMethods(unittest.TestCase):
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
        titulo = "ceci n'est une pipe".split()
        m1 = main.Musica(titulo, "tituloOriginal")
        raiz = trie.TrieNode()
        for palavra in titulo:
            raiz.insere(palavra, m1)

        self.assertEqual(raiz.busca("ceci"), [m1])
        self.assertEqual(raiz.busca("n'est"), [m1])
        self.assertEqual(raiz.busca("une")[0], m1)
        self.assertEqual(raiz.busca("pipe")[0], m1)

        titulo2 = "ceci est une pipe".split()
        m2 = main.Musica(titulo2, "tituloOriginal2")
        for palavra in titulo2:
            raiz.insere(palavra, m2)

        # Busca por uma palavra deve retornar todas as músicas com esta palavra presente no título
        self.assertEqual(raiz.busca("ceci"), [m1, m2])
        self.assertEqual(raiz.busca("une"), [m1, m2])
        self.assertEqual(raiz.busca("pipe"), [m1, m2])
        self.assertNotEqual(raiz.busca("est"), [m1, m2])
        self.assertNotEqual(raiz.busca("n'est"), [m1, m2])


if __name__ == "__main__":
    unittest.main()
