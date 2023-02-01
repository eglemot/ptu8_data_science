def skaiciuojam_iki(iki):
    count = 1
    while count <= iki:
        yield count
        count +=1

counter = skaiciuojam_iki(5)

sarasas = list(counter)
print(sarasas)
for i in counter:
    print(i)

