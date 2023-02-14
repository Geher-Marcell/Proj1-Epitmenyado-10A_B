from megoldas import megoldas


def main() -> None:
    # 1. feladat
    m = megoldas("utca.txt")

    # 2. feladat
    print(f'2. feladat. A mintában {m.hazak_szama} telek szerepel.')

    # 3. feladat
    try:
        keresendo_adoszam: int = int(
            input("3. feladat. Egy tulajdonos adószáma: "))
    except ValueError:
        print("Hibás input!")
        return

    print(m.keresett_telkek(keresendo_adoszam))

    # 5. feladat
    print('5. feladat')
    for kulcs, ertek in m.hazak_szama_adosavokban.items():
        print(
            f'{kulcs} sávba {ertek} telek esik, az adó {m.lekerdezett_adosav_adoja(kulcs)} Ft.')

    # 6. feladat
    print('6. feladat. A több sávba sorolt utcák:')
    print(m.felul_vizsgalandok)

    # 7. feladat
    m.fajl_kiiras("fizetendo.txt")


if __name__ == "__main__":
    main()
