import hashlib

# text = "Hello World!"
# hash_object = hashlib.sha256(text.encode())
# hash_digest = hash_object.hexdigest()
# print("SHA Hash of", text, "is", hash_digest)

def hash_file(file_path):
    hash = hashlib.new("sha256")
    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(1024)
            if chunk == b"":
                break
            hash.update(chunk)
    return hash.hexdigest()

if __name__ == "__main__":
    print("SHA Hash of file is: ", hash_file(r"sample_files\sample.txt"))