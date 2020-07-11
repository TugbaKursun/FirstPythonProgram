s = "AANNBGGHHTTKDKK"
unique = " "
for letter in s:
    if letter not in unique:
        unique += letter
print(unique)

names = ["Ayse", "Aysegul", "Tugba", "Ayse", "Husniye", "Tugba"]
non_dup = []
for name in names:
    if name not in non_dup:
        non_dup.append(name)

print(non_dup)