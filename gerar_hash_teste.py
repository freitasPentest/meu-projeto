import bcrypt
import time

def gerar_hash(senha):
    passowrd_encode = senha.encode()
    hash = bcrypt.hashpw(passowrd_encode, bcrypt.gensalt(12))
    print(f'SUA SENHA FOI CONVERTIDA EM HASH: {hash}, salvo em um arquivo mostrar_para_o_biel.txt"')
    with open('mostrar_para_o_biel.txt', 'wb') as file:
        write = file.write(hash)


def main():
    password ='testeparagerarhashfunçao'

    if password:
        print('INICIANDO PROCESSO DE GERAÇAO DO HASH!')
        time.sleep(3)
        gerar_hash(password)
    else:
        print('NAO FOI POSSIVEL CONCLUIR O OBJETIVO ')

if __name__ == "__main__":
    main()

        