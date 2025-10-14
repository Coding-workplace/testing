with open("my_file.txt", "r+") as f:
    print(f.read())
    f.seek(0)
    print(f.fileno())
    f.truncate(2)
    f.seek(0)
    print(f.read())
    f.flush()
print("End")
