import hashlib
import secrets
from typing import NamedTuple

class Challenge(NamedTuple):
    resource: str
    salt: str
    difficulty: int

def generate_challenge(resource: str = "api_request", difficulty: int = 12) -> Challenge:
    """Generate a proof-of-work challenge with random salt and specified difficulty in bits."""
    salt = secrets.token_hex(8)
    return Challenge(resource=resource, salt=salt, difficulty=difficulty)

def verify_solution(challenge: Challenge, nonce: int) -> bool:
    """Verify proof-of-work solution in O(1) time."""
    payload = f"{challenge.resource}:{challenge.salt}:{nonce}".encode("utf-8")
    digest = hashlib.sha256(payload).hexdigest()
    num = int(digest, 16)
    # Check leading zero bits (SHA-256 is 256 bits)
    return (num >> (256 - challenge.difficulty)) == 0

def solve_challenge(challenge: Challenge, max_iterations: int = 1000000) -> int:
    """Client-side solver: search for a nonce that satisfies the difficulty."""
    for nonce in range(max_iterations):
        if verify_solution(challenge, nonce):
            return nonce
    raise RuntimeError("Failed to solve challenge within max iterations")
