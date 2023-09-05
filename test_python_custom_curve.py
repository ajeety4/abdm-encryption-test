# This is a test code for python custom curve util (to be developed) that should generate keys similar to Fidelius CLI
# based on custom curve 25519 as used here
# https://github.com/mgrmtech/fidelius-cli/blob/main/src/main/java/com/mgrm/fidelius/keypairgen/KeyPairGenController.java#L36
import base64

import unittest
from fildelius_encryption_util import getEcdhKeyMaterial, decryptData, encryptData
from python_custom_curve import PythonCustomCurve25519


class TestPythonCustomCurve25519(unittest.TestCase):

    def test_public_key(self):
        key_material = PythonCustomCurve25519.get_key_material()
        public_key = key_material['publicKey']
        public_key_bytes = base64.b64decode(public_key.encode())
        assert len(public_key_bytes) == 65
        assert public_key_bytes[0] == 4

    def test_encryption(self):
        """Test by encrypting using python and decryption using fidelius cli"""
        string_to_encrypt = "This should be kept secret at all cost"

        # Requester is peer who shared his public key (Fidelius CLI)
        requester_key_material = getEcdhKeyMaterial()

        # Encrypt using Python Util
        sender_key_material = PythonCustomCurve25519.get_key_material()
        encryption_params = {
            "stringToEncrypt": string_to_encrypt,
            "senderNonce": sender_key_material["nonce"],
            "requesterNonce": requester_key_material["nonce"],
            "senderPrivateKey": sender_key_material["privateKey"],
            "requesterPublicKey": requester_key_material["publicKey"]
        }
        encrypted_data = PythonCustomCurve25519.encrypt_data(encryption_params)

        # Decrypt using Fidelius CLI
        decryption_params = {
            "encryptedData": encrypted_data,
            "requesterNonce": requester_key_material["nonce"],
            "senderNonce": sender_key_material["nonce"],
            "requesterPrivateKey": requester_key_material["privateKey"],
            "senderPublicKey": sender_key_material["publicKey"]
        }
        decrypted_data = decryptData(decryption_params)
        assert string_to_encrypt == decrypted_data

    def test_decryption(self):
        """Test by encrypting using fidelius cli and decryption using Python Util """
        string_to_encrypt = "This should be kept secret at all cost"

        # Requester is peer who shared his public key (Fidelius CLI)
        requester_key_material = PythonCustomCurve25519.get_key_material()

        # Encrypt using Python Util
        sender_key_material = getEcdhKeyMaterial()
        encryption_params = {
            "stringToEncrypt": string_to_encrypt,
            "senderNonce": sender_key_material["nonce"],
            "requesterNonce": requester_key_material["nonce"],
            "senderPrivateKey": sender_key_material["privateKey"],
            "requesterPublicKey": requester_key_material["publicKey"]
        }
        encrypted_data = encryptData(encryption_params)

        # Decrypt using Fidelius CLI
        decryption_params = {
            "encryptedData": encrypted_data,
            "requesterNonce": requester_key_material["nonce"],
            "senderNonce": sender_key_material["nonce"],
            "requesterPrivateKey": requester_key_material["privateKey"],
            "senderPublicKey": sender_key_material["publicKey"]
        }
        decrypted_data = PythonCustomCurve25519.decrypt_data(decryption_params)
        assert string_to_encrypt == decrypted_data

    def test_encryption_x509(self):
        """Test by encrypting using python and decryption using fidelius cli"""
        string_to_encrypt = "This should be kept secret at all cost"

        # Requester is peer who shared his public key (Fidelius CLI)
        requester_key_material = getEcdhKeyMaterial()

        # Encrypt using Python Util
        sender_key_material = PythonCustomCurve25519.get_key_material()
        encryption_params = {
            "stringToEncrypt": string_to_encrypt,
            "senderNonce": sender_key_material["nonce"],
            "requesterNonce": requester_key_material["nonce"],
            "senderPrivateKey": sender_key_material["privateKey"],
            "requesterPublicKey": requester_key_material["x509PublicKey"]
        }
        encrypted_data = PythonCustomCurve25519.encrypt_data(encryption_params)

        # Decrypt using Fidelius CLI
        decryption_params = {
            "encryptedData": encrypted_data,
            "requesterNonce": requester_key_material["nonce"],
            "senderNonce": sender_key_material["nonce"],
            "requesterPrivateKey": requester_key_material["privateKey"],
            "senderPublicKey": sender_key_material["x509PublicKey"]
        }
        decrypted_data = decryptData(decryption_params)
        assert string_to_encrypt == decrypted_data

    def test_decryption_x509(self):
        """Test by encrypting using fidelius cli and decryption using Python Util """
        string_to_encrypt = "This should be kept secret at all cost"

        # Requester is peer who shared his public key (Python util)
        requester_key_material = PythonCustomCurve25519.get_key_material()

        # Encrypt using Python Util
        sender_key_material = getEcdhKeyMaterial()
        encryption_params = {
            "stringToEncrypt": string_to_encrypt,
            "senderNonce": sender_key_material["nonce"],
            "requesterNonce": requester_key_material["nonce"],
            "senderPrivateKey": sender_key_material["privateKey"],
            "requesterPublicKey": requester_key_material["x509PublicKey"]
        }
        encrypted_data = encryptData(encryption_params)

        # Decrypt using Fidelius CLI
        decryption_params = {
            "encryptedData": encrypted_data,
            "requesterNonce": requester_key_material["nonce"],
            "senderNonce": sender_key_material["nonce"],
            "requesterPrivateKey": requester_key_material["privateKey"],
            "senderPublicKey": sender_key_material["x509PublicKey"]
        }
        decrypted_data = PythonCustomCurve25519.decrypt_data(decryption_params)
        assert string_to_encrypt == decrypted_data


if __name__ == "__main__":
    unittest.main()
