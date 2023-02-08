from haz import haz


class megoldas:
    _hazak: list[haz]

    def adosavok_utcaban(self, utca: str) -> dict[str, int]:
        adosavok: dict[str, int] = {
            "A": 0,
            "B": 0,
            "C": 0
        }
        for i in self._hazak:
            if i.utca == utca:
                adosavok[i.adosav] += 1
        return adosavok

    @property
    def felul_vizsgalandok(self):
        utcak: list[str] = []
        szoveg: str = ""
        for i in self._hazak:
            if i.utca not in utcak:
                utcak.append(i.utca)

        savok_szama: int = 0
        for i in utcak:
            for key in self.adosavok_utcaban(i).keys():
                if self.adosavok_utcaban(i)[key] > 0:
                    savok_szama += 1
            if savok_szama > 1:
                szoveg += f'\t{i}\n'
            savok_szama = 0
        return szoveg if szoveg != "" else "\tNincs ilyen utca."

    @property
    def hazak_szama(self) -> int:
        return len(self._hazak)

    def ado(self, adosav: str, alapterulet: int) -> int:
        fizetendo_ado = 0
        adosavok: dict[str, int] = {
            "A": 800,
            "B": 600,
            "C": 100
        }
        for i, e in adosavok.items():
            if i == adosav:
                fizetendo_ado = alapterulet * e
        return fizetendo_ado

    def lekerdezett_adosav_adoja(self, adosav: str) -> int:
        adosav_ado: int = 0
        for i in self._hazak:
            if i.adosav == adosav:
                if self.ado(i.adosav, i.terulet) < 10000:
                    continue
                adosav_ado += self.ado(i.adosav, i.terulet)
        return adosav_ado

    @property
    def hazak_adosavokban(self):
        adosavok_stat: dict[str, int] = {
            "A": 0,
            "B": 0,
            "C": 0
        }
        for h in self._hazak:
            adosavok_stat[h.adosav] += 1
        return adosavok_stat

    def keresett_telkek(self, adoszam: int) -> str:
        szoveg: str = ""
        for i in self._hazak:
            if i.adoszam == adoszam:
                szoveg += f'\t{i.utca} utca {i.hazszam}\n'

        return szoveg if szoveg != "" else "\tNem szerepel az adatállományban."

    def __init__(self, file: str):
        self._hazak = []
        with open(file, "r", encoding="utf-8") as f:
            for line in f.read().splitlines()[1:]:
                self._hazak.append(haz(line))
