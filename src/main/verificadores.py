
def verificarnumero(prompt=">>>>"):
    while True:
        try:
            n = int(input(prompt))
            return n
        except:
            print("\033[31;1mDIGITE APENAS A OPÇÃO VALIDA !!!!!!!!\033[0m")
