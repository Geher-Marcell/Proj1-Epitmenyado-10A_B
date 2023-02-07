class haz:
    # 5-jegyű-adószám Utca-neve házszám adósáv alapterület
    _adoszam: int
    _utca: str
    _hazszam: str
    _adosav: str
    _terulet: int

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
