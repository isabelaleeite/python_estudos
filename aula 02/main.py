# Exemplo que causa TypeError

"""nome = "Isabela"

try:
    resultado = len(2)
    print(resultado)
except TypeError as e:
   print(e)
else:
    print('Tudo ocorreu bem')
finally: 
    print('Independente de tudo ele roda')
    """
try: 
        
    numero = int(input("Insira um numero: "))

    if isinstance(numero, int):
        print("A variável é um inteiro.")
    else:
        print("A variável não é um inteiro")

except ValueError: 
    print ("Por favor, insira um númerico")
    
