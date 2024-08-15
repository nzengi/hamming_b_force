# Hamming Brute-Force Bitcoin Key Search

**Hamming Brute-Force Bitcoin Key Search** is a Python library that calculates Hamming distances to find the closest private keys to target Bitcoin addresses. This library utilizes parallel processing and SIMD optimizations to search large key ranges efficiently and help locate the closest private key to a target Bitcoin address.

## Features

- **Parallel Search:** Accelerates the search process by performing parallel operations across a range of keys.
- **SIMD Optimization:** Speeds up Hamming distance calculations using the Numba library.
- **Target Address Search:** Finds the closest private keys to a target Bitcoin address within a specified Hamming distance.

## Installation

Clone the project to your local machine:

```bash
git clone https://github.com/yourusername/hamming_brute_force.git
cd hamming_brute_force

