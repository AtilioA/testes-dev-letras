import unittest

import sys

# Para poder importar módulos
sys.path.append(sys.path[0] + "/../")

import main
import utils.string_utils as str_utils


class TestStringFunctions(unittest.TestCase):
    def test_compara_strings_ingenuo(self):
        s1 = "havana"
        s2 = "havana"
        self.assertEqual(
            str_utils.compara_strings_ingenuo(s1, s2),
            main.EnumScore["MATCH"].value * len(s1)
            + main.EnumScore["FULL_MATCH"].value,
        )

        s3 = "malandr"
        s4 = "malandra"
        self.assertEqual(
            str_utils.compara_strings_ingenuo(s3, s4),
            main.EnumScore["MATCH"].value * len(s3),
        )

        s5 = "part"
        s6 = "(part."
        self.assertEqual(str_utils.compara_strings_ingenuo(s5, s6), 0)

        s7 = "Fala"
        s8 = "Fica"
        self.assertEqual(
            str_utils.compara_strings_ingenuo(s7, s8), main.EnumScore["MATCH"].value * 2
        )

        s9 = "Fala"
        s10 = "Tranquilo"
        self.assertEqual(str_utils.compara_strings_ingenuo(s9, s10), 0)

        s11 = "Fala"
        s12 = "Tranquilo"
        self.assertEqual(str_utils.compara_strings_ingenuo(s11, s12), 0)

        s13 = "Feat"
        s14 = "Featuring"
        self.assertEqual(
            str_utils.compara_strings_ingenuo(s13, s14),
            main.EnumScore["MATCH"].value * 4,
        )

        s15 = "feat"
        s16 = "(feat)"
        self.assertEqual(str_utils.compara_strings_ingenuo(s15, s16), 0)

        s15 = "Havana"
        s16 = "feat"
        self.assertEqual(str_utils.compara_strings_ingenuo(s15, s16), 0)

        s17 = "Era"
        s18 = "Eu"
        self.assertEqual(
            str_utils.compara_strings_ingenuo(s17, s18),
            main.EnumScore["MATCH"].value * 1,
        )

        s19 = "era"
        s20 = "era"
        self.assertEqual(
            str_utils.compara_strings_ingenuo(s19, s20),
            main.EnumScore["MATCH"].value * 3 + main.EnumScore["FULL_MATCH"].value,
        )

        s21 = ""
        s22 = ""
        self.assertEqual(str_utils.compara_strings_ingenuo(s21, s22), 0)

    def test_divide_string_por_espaco(self):
        s1 = ""
        self.assertEqual(str_utils.divide_string_por_espaco(s1), [""])
        s2 = "a"
        self.assertEqual(str_utils.divide_string_por_espaco(s2), ["a"])
        s3 = "a bc def"
        self.assertEqual(str_utils.divide_string_por_espaco(s3), ["a", "bc", "def"])

    def test_trata_string(self):
        s1 = "Pesadão"
        self.assertEqual(str_utils.trata_string(s1), "pesadão")

        s2 = "Café"
        self.assertEqual(str_utils.trata_string(s2), "cafe")

        s3 = "Acústica"
        self.assertEqual(str_utils.trata_string(s3), "acustica")

        s4 = "#2"
        self.assertEqual(str_utils.trata_string(s4), "#2")

        s5 = "'\"1234567890#_,.;[]{{}}()"
        self.assertEqual(str_utils.trata_string(s5), "'\"1234567890#_,.;[]{{}}()")

        s6 = "Moça"
        self.assertEqual(str_utils.trata_string(s6), "moça")

        s7 = "Oração"
        self.assertEqual(str_utils.trata_string(s7), "oração")

        s8 = "aAàÀáÁâÂeEèÈéÉêÊiIìÌíÍîÎoOòÒóÓôÔuUùÙúÚûÛ"
        self.assertEqual(
            str_utils.trata_string(s8), "aaaaaaaaeeeeeeeeiiiiiiiioooooooouuuuuuuu"
        )

        s9 = ""
        self.assertEqual(str_utils.trata_string(s9), "")


if __name__ == "__main__":
    unittest.main()
