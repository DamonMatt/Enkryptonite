from des import DES
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("method", type=str, help="Specify the encryption algorithm")
parser.add_argument("-k", "--key", help="Specify the hex key used for encryption")
parser.add_argument("-m", "--message", type=str, help="Specify the clear text message")
parser.add_argument("-c", "--cipher", type=str, help="Specify the cipher message")
parser.add_argument("-d", "--decrypt", action="store_true", help="Encrypt/Decrypt")

args = parser.parse_args()

if args.method == "des":
    encryptor = DES(args.key)
    if encryptor.key:
        if args.decrypt:
            if args.cipher:
                encryptor.Decrypt(args.cipher)
                print("[+] Decrypted Message:",encryptor.text)
            else:
                print("[!] ERROR: No Cipher Specified!")
        else:
            if args.message:
                encryptor.Encrypt(args.message)
                print("[+] Encrypted Message:",encryptor.cipher)
            else:
                print("[!] ERROR: No Message Specified!")
    else:
        print("[!] ERROR: Key Format Invalid!")
else:
    print("[!] ERROR: Wrong Method")