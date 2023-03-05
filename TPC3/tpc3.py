import re

processos = {}

with open('processos.txt', 'r') as f:
    for line in f:
        match = re.search(r'(\d+)::(\d{4})-\d{2}-\d{2}::(.+?)(?:::(.+?))?::(?:(.+?))?::(?:(.+))?::(?:(.+))?$', line)
        if not match:
            continue
        pasta, data, nome, pai, mae, obs = match.group(1), match.group(2), match.group(3), match.group(4) or '', match.group(5) or '', match.group(6) or ''
        processos[pasta] = {'Data': data, 'Nome': nome, 'Pai': pai.strip() or None, 'Mãe': mae.strip() or None, 'Observações': obs.strip().lower() or None}

for pasta, dados in processos.items():
    print(f'Pasta: {pasta}, Data: {dados["Data"]}, Nome: {dados["Nome"]}, Pai: {dados["Pai"]}, Mãe: {dados["Mãe"]}, Observações: {dados["Observações"]}')

print("|Frequência : Parentesco|")
parentesco_freq = {}

for pasta, dados in processos.items():
    obs = dados["Observações"]
    if obs is None:  # ignorar processos sem observações
        continue
    parentescos = re.findall(r"([Mm]ãe|[Pp]ai|[Ii]rm[aã]o|[Aa]vô|[Aa]vó|[Tt]io|[Tt]ia|[Pp]rimo|[Pp]rima|[Ss]obrinh[oa])", obs)
    for parentesco in parentescos:
        if parentesco in parentesco_freq:
            parentesco_freq[parentesco] += 1
        else:
            parentesco_freq[parentesco] = 1

for parentesco, freq in parentesco_freq.items():
    print(f"{parentesco}: {freq}")

ano_freq = {}


print("|Frequência : Data|")
for pasta, dados in processos.items():
    ano = dados["Data"][:4]
    
    if ano in ano_freq:
        ano_freq[ano] += 1
    else:
        ano_freq[ano] = 1

for ano, freq in ano_freq.items():
    print(f"Ano {ano}: Frequência {freq}")


nome_freq = {}
apelido_freq = {}

for pasta, dados in processos.items():
    nome_completo = dados["Nome"]
    partes_nome = nome_completo.split()
    

    primeiro_nome = partes_nome[0]
    if primeiro_nome in nome_freq:
        nome_freq[primeiro_nome] += 1
    else:
        nome_freq[primeiro_nome] = 1
    

    apelido = partes_nome[-1]
    if apelido in apelido_freq:
        apelido_freq[apelido] += 1
    else:
        apelido_freq[apelido] = 1


print("Os 5 nomes próprios mais usados:")
for nome, freq in sorted(nome_freq.items(), key=lambda item: item[1], reverse=True)[:5]:
    print(f"{nome}: {freq}")


print("\nOs 5 apelidos mais usados:")
for apelido, freq in sorted(apelido_freq.items(), key=lambda item: item[1], reverse=True)[:5]:
    print(f"{apelido}: {freq}")

processos_20 = {k: v for k, v in processos.items() if int(k) <= 20}

json_str = str(processos_20).replace("'", "\"")
json_str = re.sub(r"(\w+):", r'"\1":', json_str)

with open('output.json', 'w') as f:
    f.write(json_str)