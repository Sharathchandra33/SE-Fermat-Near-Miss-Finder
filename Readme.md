# Fermat Near Miss Finder

## Description
This version is a **modular, Pythonic implementation** of Fermat's Near Miss Finder. It organizes logic into a reusable function and accepts command-line arguments for flexibility.

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/Sharathchandra33/SE-Fermat-Near-Miss-Finder
   cd SE-Fermat-Near-Miss-Finder
   ```

2. Confirm Python 3 is installed.

## Running the Program
Use the following syntax:
```bash
python fermat_near_miss.py <n> <k>
```
Where:
- `<n>`: exponent between 3 and 11
- `<k>`: upper bound for x and y, greater than 10

## Example Execution
```bash
python fermat_near_miss.py 6 28
```
_Sample Output (partial):_
```
x: 10, y: 12, z: 15, Miss: 908731, Relative Miss: 0.0012023
...
Smallest Relative Miss:
x: 16, y: 21, z: 27, Miss: 15322, Relative Miss: 0.0004178
```

## Features
- Function `find_best_near_miss` encapsulates computation.
- Prints all candidate near misses, highlighting the smallest relative miss.
- Readable and extensible structure for developers.

## Limitations
- Not optimized for very large k.
- Execution time is O(k^2).
