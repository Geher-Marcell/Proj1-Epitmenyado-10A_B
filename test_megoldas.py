from unittest import TestCase
from megoldas import Megoldas


class TestMegoldas(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.mo: Megoldas = Megoldas('utca.txt')

    def test_hazak_szama(self) -> None:
        self.assertEqual(self.mo.hazak_szama, 543)

    def test_keresett_telkek(self) -> None:
        self.assertEqual(self.mo.keresett_telkek(68396), 'Harmat utca 22\nSzepesi utca 17\n')

    def test_osszesitett_ado(self) -> None:
        i = 0
        for kulcs, ertek in self.mo.hazak_szama_adosavokban.items():
            self.assertEqual(kulcs, self.mo.abc[i])
            self.assertEqual(ertek, ertek)
            self.assertEqual(self.mo.lekerdezett_adosav_adoja(kulcs), self.mo.lekerdezett_adosav_adoja(kulcs))
            i += 1
