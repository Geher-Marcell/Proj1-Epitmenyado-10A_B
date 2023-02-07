class haz:
    # 5-jegyű-adószám Utca-neve házszám adósáv alapterület
    _adószám: int
    _utca: str
    _házszám: str
    _adósáv: str
    _terület: int

    def __init__(self, line: str):
        line = line.strip(" ")
        self._adószám = int(line[0])
        self._utca = line[1]
        self._házszám = line[2]
        self._adósáv = line[3]
        self._terület = int(line[4])
