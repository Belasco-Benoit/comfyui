fichier = open("prompts2.json", "w")

p = "unicolor shirt, cotton, portrait, illustration, digital art, soft colors, green background"
p1 = ["man, short hair", "woman, long hair"]
p2 = ["brown hair", "blond hair", "red hair"]
p3 = ["blue eyes", "brown eyes"]
p4 = ["no hat", "red hat", "blue hat"]
p5 = ["no flowers", "holding white flowers", "holding red flowers"]

prompts = []

n = len(p1) *len(p2) *len(p3) *len(p4) *len(p5)
print(n, "prompts générés")
for e1 in p1:
    for e2 in p2:
        for e3 in p3:
            for e4 in p4:
                for e5 in p5:
                    prompt = e1 +', ' +e2 +', ' +e3 +', ' +e4 +', ' +e5 +' ,' +p
                    prompts.append(prompt)

prompts = str(prompts).replace("'", '"')
print(prompts)
fichier.write(prompts)
fichier.close()
print(n, "prompts générés")