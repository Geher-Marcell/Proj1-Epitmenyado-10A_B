from haz import haz


class megoldas:
    _hazak: list[haz]

    def __init__(self, file: str):
        self._hazak = []
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                self._hazak.append(haz(line))
