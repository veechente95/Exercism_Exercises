# Diffie-Hellman key exchange.

# Alice and Bob use Diffie-Hellman key exchange to share secrets. 
# They start with prime numbers, pick private keys, generate and share public keys, and then generate a shared secret key.

import random

def private_key(p):
    return random.randrange(2, p)

def public_key(p, g, private):
    return pow(g, private, p)

def secret(p, public, private):
    return pow(public, private, p)

