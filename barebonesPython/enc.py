import binascii, base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat, load_pem_public_key
from cryptography.hazmat.primitives.kdf.x963kdf import X963KDF
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.hmac import HMAC
from colorama import Fore, Back, Style

backend = default_backend()

message = 'The Magic Words are still Squeamish Ossifrage'

# It's Bob's world and we're all living in it!

bob_pem = '''
-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHiG0sllsW2K9uX/Ey1nxJsv4u/1z
28JgocZcuFcmE/BuKXZ1w5CB35VxrYqF6RKUucnaauk4VfjSAfYr6gC+GA==
-----END PUBLIC KEY-----'''

bob_pem = bytes(bob_pem, 'utf-8')
bob_public = load_pem_public_key(bob_pem, backend)
bob_pub_bytes = bob_public.public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)[-65:]

#print(Fore.RED)
#print(type(bob_public))
#print(Fore.WHITE)

#print("Bob's public key (PEM format):")
#print("{}".format(bob_pem))

print(Fore.BLUE)
print("Bob's public key in bytes: {}".format(binascii.b2a_hex(bob_pub_bytes)))

# Alice enters the picture

alice_priv = ec.generate_private_key(ec.SECP256R1(), backend)

alice_pub_bytes = alice_priv.public_key().public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)[-65:]

print(Fore.GREEN)
print("Alice's public key in bytes: {}".format(binascii.b2a_hex(alice_pub_bytes)))

shared_key = alice_priv.exchange(ec.ECDH(), bob_public)

print(Fore.RED)
print("Shared key in bytes: {}".format(binascii.b2a_hex(shared_key)))

xkdf = X963KDF(algorithm=hashes.SHA256(), length=16, sharedinfo=alice_pub_bytes, backend=backend)

key_enc = xkdf.derive(shared_key)

print(Fore.YELLOW)
print("AES encryption key in bytes: {}".format(binascii.b2a_hex(key_enc)))

IV = binascii.a2b_hex('00000000000000000000000000000000')


