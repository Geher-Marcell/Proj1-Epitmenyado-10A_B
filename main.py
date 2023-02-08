from megoldas import megoldas


def main() -> None:
    # 1. feladat
    m = megoldas("utca.txt")

    # 2. feladat
    print(f'2. feladat. A mintában {m.hazak_szama} telek szerepel')

    # 3. feladat
    try:
        keresendo_adoszam: int = int(input("3. feladat. Egy tulajdonos adószáma: "))
    except ValueError:
        print("Hibás típus!")
        return

    print(m.keresett_telkek(keresendo_adoszam))

    print('5. feladat')
    for key, value in m.hazak_adosavokban.items():
        print(f'\t{key} sávba {value} telek esik, az adó {m.lekerdezett_adosav_adoja(key)} Ft')

    print('6. feladat')
    print(m.felul_vizsgalandok)


if __name__ == "__main__":
    main()
 
