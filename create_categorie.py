fichier = open("prompts3.json", "w")

p = "unicolor shirt, cotton, portrait, illustration, digital art, soft colors, green background"
p1 = ["smiling young man short hair", "smiling young woman long hair"]
p2 = [" with brown hair", " with blond hair", " with red hair"]
p3 = [" and big blue eyes", " and big brown eyes"]
p4 = ["", " wearin big hat",]
p5 = ["", " holding one big white flower", " holding one big red flower"]

prompts = []

n = len(p1) *len(p2) *len(p3) *len(p4) *len(p5)
print(n, "prompts générés")
for e1 in p1:
    for e2 in p2:
        for e3 in p3:
            for e4 in p4:
                for e5 in p5:
                    prompt = e1 +e2 +e3 +e4 +e5 +' ,' +p
                    prompts.append(prompt)

prompts = str(prompts).replace("'", '"').replace('", "', '",\n"')
#print(prompts)
fichier.write(prompts)
fichier.close()
print(n, "prompts générés")