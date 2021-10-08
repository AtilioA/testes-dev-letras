import sys
import unittest


import utils.string_utils as str_utils
from main import EnumScore


class TestStringMethods(unittest.TestCase):
    # def test_remove_acentos_string(self):
    #     s1 = "1 - áéíóúÂÊÎÔÛãõÃÕ."
    #     self.assertEqual(str_utils.remove_acentos_string(s1), "1 - aeiouAEIOUãõÃÕ.")

    def test_compara_strings_ingenuo(self):
        s1 = "havana"
        s2 = "havana"
        self.assertEqual(str_utils.compara_strings_ingenuo(s1, s2), EnumScore['MATCH'].value * len(s1) + EnumScore['FULL_MATCH'].value)

        s3 = "malandr"
        s4 = "malandra"
        self.assertEqual(str_utils.compara_strings_ingenuo(s3, s4), EnumScore['MATCH'].value * len(s3))

        s5 = "part"
        s6 = "(part."
        self.assertEqual(str_utils.compara_strings_ingenuo(s5, s6), 0)

        s7 = "Fala"
        s8 = "Fica"
        self.assertEqual(str_utils.compara_strings_ingenuo(s7, s8), EnumScore['MATCH'].value * 2)

        s9 = "Fala"
        s10 = "Tranquilo"
        self.assertEqual(str_utils.compara_strings_ingenuo(s9, s10), 0)

        s11 = "Fala"
        s12 = "Tranquilo"
        self.assertEqual(str_utils.compara_strings_ingenuo(s11, s12), 0)

        s13 = "Feat"
        s14 = "Featuring"
        self.assertEqual(str_utils.compara_strings_ingenuo(s13, s14), EnumScore['MATCH'].value * 4)

        s15 = "feat"
        s16 = "(feat)"
        self.assertEqual(str_utils.compara_strings_ingenuo(s15, s16), 0)

        s15 = "Havana"
        s16 = "feat"
        self.assertEqual(str_utils.compara_strings_ingenuo(s15, s16), 0)

        s17 = "Era"
        s18 = "Eu"
        self.assertEqual(str_utils.compara_strings_ingenuo(s17, s18), EnumScore['MATCH'].value * 1)

        s19 = "era"
        s20 = "era"
        self.assertEqual(str_utils.compara_strings_ingenuo(s19, s20), EnumScore['MATCH'].value * 3 + EnumScore['FULL_MATCH'].value)

    def test_divide_string_por_espaco(self):
        s1 = ""
        self.assertEqual(str_utils.divide_string_por_espaco(s1), [''])
        s2 = "a"
        self.assertEqual(str_utils.divide_string_por_espaco(s2), ['a'])
        s3 = "a bc def"
        self.assertEqual(str_utils.divide_string_por_espaco(s3), ['a', 'bc', 'def'])

    def test_verifica_feat_strings(self):
        s1E = "feat"
        s2M = "feat"
        self.assertEqual(str_utils.verifica_feat_strings(s1E, s2M), EnumScore["WANT_FEAT"].value)
        s3E = ""
        s4M = "feat"
        self.assertEqual(str_utils.verifica_feat_strings(s3E, s4M), EnumScore["DONT_WANT_FEAT"].value)
        s5E = ""
        s6M = ""
        self.assertEqual(str_utils.verifica_feat_strings(s5E, s6M), EnumScore["NO_FEAT"].value)
        s7E = "e"
        s8M = "feat"
        self.assertEqual(str_utils.verifica_feat_strings(s7E, s8M), EnumScore["DONT_WANT_FEAT"].value)
        s9E = "e"
        s10M = "e"
        self.assertEqual(str_utils.verifica_feat_strings(s9E, s10M), EnumScore["NO_FEAT"].value)


if __name__ == "__main__":
    unittest.main()
