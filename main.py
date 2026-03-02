from util.calcule import (
    citeste_vectori_din_fisier,
    distanta_manhattan_manual,
    distanta_manhattan_cityblock,
)


def main() -> None:
    x, y = citeste_vectori_din_fisier("input.txt")

    d1 = distanta_manhattan_manual(x, y)
    d2 = distanta_manhattan_cityblock(x, y)

    print("X =", x)
    print("Y =", y)
    print(f"Distanța Manhattan (manual) = {d1}")
    print(f"Distanța Manhattan (cityblock) = {d2}")

    if abs(d1 - d2) < 1e-9:
        print("OK: rezultatele coincid.")
    else:
        print("ATENȚIE: rezultatele diferă.")


if __name__ == "__main__":
    main()