from megoldas import megoldas


def main() -> None:
    # 1. feladat
    m = megoldas("utca.txt")

    # 2. feladat
    print(f'2. feladat. A mintában {m.hazak_szama} telek szerepel')


if __name__ == "__main__":
    main()
