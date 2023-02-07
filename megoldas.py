from haz import haz


class megoldas:
    _hazak: list[haz]

    @property
    def hazak_szama(self) -> int:
        return len(self._hazak)

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
