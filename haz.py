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

    def __init__(self, line: str):
        a, u, h, a2, t = line.split(" ")
        self._adoszam = int(a)
        self._utca = u
        self._hazszam = h
        self._adosav = a2
        self._terulet = int(t)
