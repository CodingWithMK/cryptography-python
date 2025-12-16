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

def verify_integrity(file1, file2):
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)
    print("\nChecking integrity between", file1, " and", file2)
    if hash1 == hash2:
        return "File is intact. No modifications have been made."
    return "File has been modified. Possibly corrupted or unsafe."

if __name__ == "__main__":
    print("SHA Hash of file is: ", hash_file(r"sample_files\sample.txt"))
    print(verify_integrity(r"sample_files\test1.txt", r"sample_files\test2.txt"))
    print(verify_integrity(r"sample_files\test1.txt", r"sample_files\test3.txt"))