# 1. Fidelius CLI
# https://github.com/mgrmtech/fidelius-cli/tree/main/src/main/java/com/mgrm/fidelius

# 2. Bouncy Castle Custom Curve
# https://github.com/bcgit/bc-java/blob/main/core/src/main/java/org/bouncycastle/crypto/ec/CustomNamedCurves.java#L77

# 3. fastecdsa Resource
# pip install fastecdsa
# https://github.com/AntonKueltz/fastecdsa#id8

# 4. ABDM Guidelines
# https://sandbox.abdm.gov.in/abdm-docs/EncryptionAndDecryptionData

# Considerations for format of keys
# 1. Note the format that Java uses for integers in the curve is Big endian (https://en.wikipedia.org/wiki/Endianness)
# 2. Public keys exported in X509 format should also be supported
# 3. Java Fidelius CLI returns output as base64 string for all methods (key material, encrypt and decrypt) as per ABDM guidelines.

# TODO Generate Curve Parameters using reference from Bouncy Castle

name = 'CustomCurve25519'
p = None
a = None
b = None
q = None
gx = None
gy = None
oid = None

# Create Custom Curve
from fastecdsa.curve import Curve
curve = Curve(
    name,  # (str): The name of the curve
    p,  # (long): The value of p in the curve equation.
    a,  # (long): The value of a in the curve equation.
    b,  # (long): The value of b in the curve equation.
    q,  # (long): The order of the base point of the curve.
    gx,  # (long): The x coordinate of the base point of the curve.
    gy,  # (long): The y coordinate of the base point of the curve.
    oid  # (str): The object identifier of the curve (optional).
)

# TODO Create keys using above curve
# TODO Encryption logic
# TODO Decryption logic
# TODO Use the test `test_python_custom_curve` for testing the logic



# Below is sample Interface that python util should support from the custom curve created in python

# For methods output, see corresponding function on fildelius_encryption_util for input and output params
# (Java Fidelius CLI returns output as base64 string for all methods)
class PythonCustomCurve25519:

    @staticmethod
    def get_key_material():
        raise NotImplementedError

    @staticmethod
    def encrypt_data(encryption_params):
        raise NotImplementedError

    @staticmethod
    def decrypt_data(decryption_params):
        raise NotImplementedError
