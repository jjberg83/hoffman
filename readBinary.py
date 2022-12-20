f = open("input.txt", "rb")
content = f.read()
print("hei")
print(content)
f.close()

# Finne ascii verdi for bokstav
print(ord("a"))

# Finne binærverdi av desimaltall (kommer ut som string)
print(bin(97).replace("0b", ""))
