from __future__ import annotations
from typing import List, Sequence, Tuple
from scipy.spatial.distance import cityblock

def citeste_vectori_din_fisier(cale: str) -> Tuple[List[float], List[float]]:
 
    with open(cale, "r", encoding="utf-8") as f:
        linii = [ln.strip() for ln in f.readlines() if ln.strip()]

    if len(linii) < 2:
        raise ValueError("Fișierul trebuie să conțină cel puțin 2 linii (X și Y).")

    def parse_line(line: str) -> List[float]:
        line = line.replace(",", " ")
        parts = [p for p in line.split() if p]
        return [float(p) for p in parts]

    x = parse_line(linii[0])
    y = parse_line(linii[1])

    if len(x) != len(y):
        raise ValueError(f"Vectorii trebuie să aibă aceeași dimensiune: {len(x)} vs {len(y)}")

    return x, y


def distanta_manhattan_manual(x: Sequence[float], y: Sequence[float]) -> float:
    
    if len(x) != len(y):
        raise ValueError("Vectorii trebuie să aibă aceeași dimensiune.")

    s = 0.0
    for xi, yi in zip(x, y):
        s += abs(xi - yi)
    return s


def distanta_manhattan_cityblock(x: Sequence[float], y: Sequence[float]) -> float:
   
    if len(x) != len(y):
        raise ValueError("Vectorii trebuie să aibă aceeași dimensiune.")

    return float(cityblock(x, y))