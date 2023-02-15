from haz import haz


class megoldas:
    _hazak: list[haz]

    @ property
    def felul_vizsgalandok(self):
        utcak: list[str] = []
        szoveg: str = ""
        for i in self._hazak:
            if i.utca not in utcak:
                utcak.append(i.utca)
        savok_szama: int = 0
        for i in utcak:
            for kulcs in self.keresett_utca_adosava(i):
                if self.keresett_utca_adosava(i)[kulcs] > 0:
                    savok_szama += 1
            if savok_szama > 1:
                szoveg += f'{i}\n'
            savok_szama = 0
        return szoveg if szoveg != "" else "Nincs ilyen utca."

    @ property
    def hazak_szama(self) -> int:
        return len(self._hazak)

    @ property
    def hazak_szama_adosavokban(self):
        adosavok_stat: dict[str, int] = {
            "A": 0,
            "B": 0,
            "C": 0
        }
        for h in self._hazak:
            adosavok_stat[h.adosav] += 1
        return adosavok_stat

    def fajl_kiiras(self, filenev: str):
        adok: dict[int, int] = {}
        for i in self._hazak:
            if i.adoszam not in adok:
                adok[i.adoszam] = 0
            adok[i.adoszam] += i.ado

        with open(filenev, "w", encoding="utf-8") as f:
            for kulcs, ertek in adok.items():
                f.write(f'{kulcs} {ertek}\n')

    def keresett_utca_adosava(self, utca: str) -> dict[str, int]:
        adosavok: dict[str, int] = {
            "A": 0,
            "B": 0,
            "C": 0
        }
        for i in self._hazak:
            if i.utca == utca:
                adosavok[i.adosav] += 1
        return adosavok

    def lekerdezett_adosav_adoja(self, adosav: str) -> int:
        adosav_ado: int = 0
        for i in self._hazak:
            if i.adosav == adosav:
                adosav_ado += i.ado
        return adosav_ado

    def keresett_telkek(self, adoszam: int) -> str:
        szoveg: str = ""
        for i in self._hazak:
            if i.adoszam == adoszam:
                szoveg += f'{i.utca} utca {i.hazszam}\n'

        return szoveg if szoveg != "" else "Nem szerepel az adatállományban."

    def __init__(self, file: str):
        self._hazak = []
        with open(file, "r", encoding="utf-8") as f:
            adosavok: list[str] = []
            for i, line in enumerate(f.read().splitlines()):
                if i == 0:
                    adosavok = line.split(" ")
                else:
                    self._hazak.append(haz(line))
            haz.adosavok = {
                "A": int(adosavok[0]),
                "B": int(adosavok[1]),
                "C": int(adosavok[2])
            }
            f.close()
