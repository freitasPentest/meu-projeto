def bruteforce(password, wordlist):
  with open(wordlist, 'r') as file:
        for i in file:
           conteudo_limpo = i.strip()
           if conteudo_limpo == password:
            print(f'senha encontrada:  {conteudo_limpo}')
            encontrado = True
            break

  if not encontrado:
       print(f'Não foi possivel encontrar a senha em {wordlist}')





def main():
   entrada = input('DIGITE SUA SENHA: ')
   wordlistss = 'bruteforce.txt'
   if entrada:
      print('Inicializando varredura!!!!')
      bruteforce(entrada, wordlistss)
   else:
      print('Não foi possivel inicializar o script')
    
      

if __name__ == "__main__":
   main()

       
           

   