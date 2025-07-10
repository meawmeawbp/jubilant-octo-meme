import base64
import base58
import base32_crockford

from itertools import permutations

msg = "SFcUFnKydQ9L1q6jfZXKvbZVY3uQPyENV2g4WveejUrptAkcru4pRbMP8ceGxhe9DMoptJen43SwYrDi5mBDMFN1wadt439ZjbNS6QbtBBPvuCTH4Vp5A8h1b4zbgnaMUV4"

def decode_chain(message, chain):
    for enc in chain:
        if isinstance(message, str):
            message = message.encode()
        if enc == 'base64':
            message = base64.b64decode(message)
        elif enc == 'base58':
            message = base58.b58decode(message)
        elif enc == 'base32_crockford':
            message = base32_crockford.decode(message.decode())
    return message

encodings = ['base64', 'base58', 'base32_crockford']
for chain in permutations(encodings):
    try:
        result = decode_chain(msg, chain)
        decoded = result.decode(errors='ignore')
        print(f"[{chain}] → {decoded[:80]}...")  # print first 80 characters only
    except Exception as e:
        print(f"[{chain}] → ❌ Error: {e}")
