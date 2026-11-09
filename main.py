print("Hello, World!")

with open("krituliai.txt", "w") as f:
    f.write("Labas pasauli!")

with open("demofile.txt") as f:
    print(f.read())
