
def verificarnumero(prompt=">>>>"):
    while True:
        try:
            n = int(input(prompt))
            return n
        except:
            print("Digite apenas numeros")