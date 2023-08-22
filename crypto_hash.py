import hashlib

def crypto_hash(data):
    """
    Returns a SHA256 hash of the given data
    """
    return hashlib.sha256(data.encode('utf-8'))

def main():
    print(f'Hash of Data(Hatake)- {crypto_hash("Hatake")}' )

if __name__ == "__main__":
    main()