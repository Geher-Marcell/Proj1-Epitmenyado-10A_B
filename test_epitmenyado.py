from unittest import TestCase
from haz import Haz


class TestEpitmenyek(TestCase):
    # 5-jegyű-adószám Utca-neve házszám adósáv alapterület
    @classmethod
    def setUpClass(cls):
        cls.sor6: Haz = Haz('49812 Aradi 5 C 154')
        cls.sor53: Haz = Haz('58059 Egyenes 15 B 96')
        cls.sor175: Haz = Haz('51755 Icce 17 B 248')
        cls.sor241: Haz = Haz('10962 Kossuth 25C C 120')
        cls.sor384: Haz = Haz('19339 Pesti 23 C 273')

    def test_adoszam(self):
        self.assertEqual(self.sor6.adoszam, 49812)
        self.assertEqual(self.sor53.adoszam, 58059)
        self.assertEqual(self.sor175.adoszam, 51755)
        self.assertEqual(self.sor241.adoszam, 10962)
        self.assertEqual(self.sor384.adoszam, 19339)

    def test_utca(self):
        self.assertEqual(self.sor6.utca, 'Aradi')
        self.assertEqual(self.sor53.utca, 'Egyenes')
        self.assertEqual(self.sor175.utca, 'Icce')
        self.assertEqual(self.sor241.utca, 'Kossuth')
        self.assertEqual(self.sor384.utca, 'Pesti')

    def test_hazszam(self):
        self.assertEqual(self.sor6.hazszam, '5')
        self.assertEqual(self.sor53.hazszam, '15')
        self.assertEqual(self.sor175.hazszam, '17')
        self.assertEqual(self.sor241.hazszam, '25C')
        self.assertEqual(self.sor384.hazszam, '23')

    def test_adosav(self):
        self.assertEqual(self.sor6.adosav, 'C')
        self.assertEqual(self.sor53.adosav, 'B')
        self.assertEqual(self.sor175.adosav, 'B')
        self.assertEqual(self.sor241.adosav, 'C')
        self.assertEqual(self.sor384.adosav, 'C')

    def test_terulet(self):
        self.assertEqual(self.sor6.terulet, 154)
        self.assertEqual(self.sor53.terulet, 96)
        self.assertEqual(self.sor175.terulet, 248)
        self.assertEqual(self.sor241.terulet, 120)
        self.assertEqual(self.sor384.terulet, 273)
