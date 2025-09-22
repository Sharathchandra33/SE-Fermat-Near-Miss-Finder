"""
Fermat Near Miss Finder
A Pythonic implementation of Fermat's Near Miss Finder.
Usage:
    python fermat_near_miss.py <n> <k>
Example:
    python fermat_near_miss.py 6 30
"""

import math
import argparse

def find_best_near_miss(n: int, k: int):
    smallest_relative_miss = float("inf")
    best = None

    for x in range(10, k + 1):
        for y in range(10, k + 1):
            total = x ** n + y ** n
            z = round(total ** (1 / n))

            candidates = [(z, abs(total - z ** n)), (z + 1, abs(total - (z + 1) ** n))]
            chosen_z, miss = min(candidates, key=lambda item: item[1])

            relative_miss = miss / total
            print(f"x: {x}, y: {y}, z: {chosen_z}, Miss: {miss}, Relative Miss: {relative_miss:.7f}")

            if relative_miss < smallest_relative_miss:
                smallest_relative_miss = relative_miss
                best = (x, y, chosen_z, miss, relative_miss)

    return best

def main():
    parser = argparse.ArgumentParser(description="Fermat Near Miss Finder (Pythonic)")
    parser.add_argument("n", type=int, help="Exponent (3 <= n <= 11)")
    parser.add_argument("k", type=int, help="Upper bound for x and y (k > 10)")
    args = parser.parse_args()

    n, k = args.n, args.k

    if not (2 < n < 12):
        print("Invalid input. n must be between 3 and 11.")
        return

    if k <= 10:
        print("Invalid input. k must be greater than 10.")
        return

    best_x, best_y, best_z, miss, rel_miss = find_best_near_miss(n, k)
    print("\nSmallest Relative Miss:")
    print(f"x: {best_x}, y: {best_y}, z: {best_z}, Miss: {miss}, Relative Miss: {rel_miss:.7f}")

if __name__ == "__main__":
    main()
