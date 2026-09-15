import pytest
from py_hash_cash import generate_challenge, solve_challenge, verify_solution

def test_hashcash_pow():
    # Difficulty 10 is fast to solve in tests
    ch = generate_challenge(resource="test_login", difficulty=10)
    nonce = solve_challenge(ch)
    assert verify_solution(ch, nonce) is True
    assert verify_solution(ch, nonce + 999999) is False
