from haz import haz


class megoldas:
    _hazak: list[haz]

    @property
    def hazak_szama(self) -> int:
        return len(self._hazak)

    def __init__(self, file: str):
        self._hazak = []
        with open(file, "r", encoding="utf-8") as f:
            for line in f.read().splitlines()[1:]:
                self._hazak.append(haz(line))
