from haz import haz


class megoldas:
    _hazak: list[haz]

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

    def hazak_utani_adok(self):
        A_adosav: haz = []
        B_adosav: haz = []
        C_adosav: haz = []
        for i in self._hazak:
            akt_ado = 0
            if i.adosav == "A":
                akt_ado = self.ado(i.adosav, i.terulet)
        return A_adosav
            
                


    @property
    def hazak_adosavokban(self):
        adosavok_stat: dict[str, int] = {}
        for h in self._hazak:
            if h.adosav in adosavok_stat:
                adosavok_stat[h.adosav] += 1
            else:
                adosavok_stat[h.adosav] = 1
        return adosavok_stat

    # 3. feladat rossz, b része nincs kész
    def keresett_telkek(self, adoszam: int) -> str:
        szoveg: str = ""
        for i in self._hazak:
            if i.adoszam == adoszam:
                szoveg += f'\t{i.utca} utca {i.hazszam}\n'
        return szoveg

    def __init__(self, file: str):
        self._hazak = []
        with open(file, "r", encoding="utf-8") as f:
            for line in f.read().splitlines()[1:]:
                self._hazak.append(haz(line))
