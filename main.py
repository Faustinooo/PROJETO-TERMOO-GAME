termo = "olhos"
tentativas = 0
while True:
    letras_certas = str("")
    tentativas += 1
    tentativa = str(input("Escreva Uma Palavra: ").strip())
    if len(tentativa) > len(termo):
        print(f"A PALAVRA TEM {len(termo)} Letras")
        continue
    if len(tentativa) < len(termo):
        print(f"A PALAVRA TEM {len(termo)} Letras")
        continue
    n = 0
    for letras1 in tentativa:
        letras_certas += tentativa[n]
        n += 1

    palavra_formada = ""
    num = 0
    for letras in letras_certas:
        if letras in termo and termo.find(letras) == tentativa.find(letras):
            palavra_formada += f"\033[34m{letras}\033[m"
        if letras in termo and termo.find(letras) != tentativa.find(letras):
            palavra_formada += f"\033[32m{letras}\033[m"
        if letras not in termo:
            palavra_formada += f"\033[31m{tentativa[num]}\033[m"
        num += 1
    print(palavra_formada)
    if tentativa == termo:
        break
print(f"\033[31mPARABÉNS VOCÊ DESCOBRIU! A PALAVRA ERA\033[m {termo.upper()}!")
