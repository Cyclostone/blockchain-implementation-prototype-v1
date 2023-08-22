import hashlib
import json

# def stringify(data):
#     return json.dumps(data)

def crypto_hash(*args):
    """
    Returns a SHA256 hash of the given data
    """
    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    #print(f'stringified_args: {stringified_args}')

    joined_data = "".join(stringified_args)
    #print(joined_data)
    #stringified_data = json.dumps(args)
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f'Hash of Data([7], 1, Eight)- {crypto_hash([7], 1, "Eight")}' )
    print(f'Hash of Data(Eight, [7], 1)- {crypto_hash("Eight", [7], 1)}' )

if __name__ == "__main__":
    main()