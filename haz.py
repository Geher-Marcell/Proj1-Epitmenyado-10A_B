class Haz:
    # 5-jegyű-adószám Utca-neve házszám adósáv alapterület
    _adoszam: int
    _utca: str
    _hazszam: str
    _adosav: str
    _terulet: int
    adosavok: dict[str, int]

    @property
    def ado(self) -> int:
        fizetendo_ado = 0
        adosavok: dict[str, int] = Haz.adosavok
        for i, e in adosavok.items():
            if i == self._adosav:
                fizetendo_ado = self.terulet * e
                if fizetendo_ado < 10000:
                    fizetendo_ado = 0
        return fizetendo_ado

    @property
    def adoszam(self) -> int:
        return self._adoszam

    @property
    def utca(self) -> str:
        return self._utca

    @property
    def hazszam(self) -> str:
        return self._hazszam

    @property
    def adosav(self) -> str:
        return self._adosav

    @property
    def terulet(self) -> int:
        return self._terulet

    def __init__(self, line: str):
        adoszam, utca, hazszam, adosav, terulet = line.split(" ")
        self._adoszam = int(adoszam)
        self._utca = utca
        self._hazszam = hazszam
        self._adosav = adosav
        self._terulet = int(terulet)
