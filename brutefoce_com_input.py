encontrada = False
def bruteforce(wordlist, senha):
    contador = 0

    with open(wordlist, 'r') as file:
      for linha in file:
          contador += 1
          linha_limpa = linha.strip()
          if linha_limpa == senha:
             print(f'senha encontrda: {linha_limpa}')
             global encontrada
             encontrada = True
             break

    if not encontrada:
       print('senha inexistente!!!!!')
       print(f'numero de tentativas: {contador}')



def main():
   password = input('digite sua palavra chave desejada: ')
   if password:
      entrada = input('digite sua wordlist aqui: ')
      bruteforce(entrada, password)
   else:
      print('nao foi possivel fazer a verificaçao')


if __name__ == "__main__":
   main()

