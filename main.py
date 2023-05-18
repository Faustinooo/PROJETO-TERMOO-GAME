from decoração import *
linha(33)
cabeçalho(f"TERMOO")
print('''\033[32mCERTO\033[m
\033[33mLUGAR ERRADO\033[m
\033[31mERRADO\033[m''')
linha(34)
termo = str("olhos").upper()
tentativas = 0
while True:
    letras_certas = ""
    tentativas += 1
    print(f"DICA: A PALAVRA POSSUI {len(termo)} LETRAS")
    tentativa = str(input("Escreva Uma Palavra: ").strip().upper())
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
            palavra_formada += f"\033[32m{letras}\033[m"
        if letras in termo and termo.find(letras) != tentativa.find(letras):
            palavra_formada += f"\033[33m{letras}\033[m"
        if letras not in termo:
            palavra_formada += f"\033[31m{tentativa[num]}\033[m"
        num += 1
    linha(0)
    print(palavra_formada)
    linha(0)
    if tentativa == termo:
        break
print(f"\033[32mPARABÉNS VOCÊ DESCOBRIU! A PALAVRA ERA\033[m {termo.upper()}!")