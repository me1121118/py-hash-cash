# py-hash-cash

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](https://pypi.org/project/py-hash-cash/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

Zero-dependency Proof-of-Work (Hashcash) challenge generator and validator for bot protection and rate-limiting defense in pure Python.

---

## 🚀 Features

- 🛡️ **Anti-Bot Defense**: Force bot scripts to compute proof-of-work before accepting forms or emails.
- 🪶 **Zero Dependencies**: Pure Python standard library (`hashlib`, `secrets`).
- ⚡ **Tunable Difficulty**: Configurable leading zero bits difficulty level.

---

## 📦 Installation

```bash
pip install py-hash-cash
```

---

## 🛠️ Quickstart

```python
from py_hash_cash import generate_challenge, solve_challenge, verify_solution

# 1. Server generates challenge
challenge = generate_challenge(difficulty=16)

# 2. Client computes solution
nonce = solve_challenge(challenge)

# 3. Server verifies in O(1) time
is_valid = verify_solution(challenge, nonce)
print(is_valid)  # True
```

---

## ☕ Support My Studies / Buy Me a Coffee

I am an independent developer and student building open-source developer productivity tools. If this proof-of-work challenge protected your APIs from scraping, please consider supporting my studies:

- ☕ **Buy Me a Coffee:** [ko-fi.com/me1121118](https://ko-fi.com/)
- ⭐ **Star this repository** on GitHub!

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
