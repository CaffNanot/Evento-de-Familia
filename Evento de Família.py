ano = int(input("Digite um Ano: "))

if (ano%400==0 and not ano%100==0) or (ano%4==0): #validando se o ano possui múltiplos de 4 e 400 e se não é multiplo de 100
    print('Bissexto')
else:
    print('Não é bissexto')
    
