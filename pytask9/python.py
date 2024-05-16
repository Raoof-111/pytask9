
with open("text1.txt", "w") as file:
    file.write("bir cumle yazdimmmmmmmmmmmmmmm")

with open("text1.txt", "r") as file:
    frl = file.readline().upper()

with open("text2.txt", "w") as file:
    file.write(frl)