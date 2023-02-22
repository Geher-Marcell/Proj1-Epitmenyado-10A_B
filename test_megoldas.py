import filecmp
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
        for kulcs, ertek in self.mo.hazak_szama_adosavokban.items():
            if kulcs == 'A':
                self.assertEqual(kulcs, 'A')
                self.assertEqual(ertek, 165)
                self.assertEqual(self.mo.lekerdezett_adosav_adoja(kulcs), 20805600)
            if kulcs == 'B':
                self.assertEqual(kulcs, 'B')
                self.assertEqual(ertek, 144)
                self.assertEqual(self.mo.lekerdezett_adosav_adoja(kulcs), 13107000)
            if kulcs == 'C':
                self.assertEqual(kulcs, 'C')
                self.assertEqual(ertek, 234)
                self.assertEqual(self.mo.lekerdezett_adosav_adoja(kulcs), 3479600)

    def test_tobb_savba_sorolt_utcak(self) -> None:
        self.assertEqual(self.mo.felul_vizsgalandok, 'Besztercei\nGyurgyalag\nIcce\nKurta\nRezeda\nSzepesi\n')

    def test_fizetendo_hasonlitas(self):
        self.mo.fajl_kiiras('fizetendo.txt')
        self.assertTrue(filecmp.cmp('fizetendo.txt', 'fizetendo_OH.txt', shallow=False))
