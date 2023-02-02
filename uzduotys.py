def ieskom():
    with open("gen_failui/generatoriui.txt", "r") as failas:
        while True:
            for eilute in failas:
                yield eilute

bandom = ieskom()

for rezultatas in bandom:
    print(rezultatas)