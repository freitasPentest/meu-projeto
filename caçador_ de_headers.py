import argparse
import requests

def fazer_requisiçoes(url, timeout):
    timeout = timeout if timeout is not None else 5
    try:
        requisiçoes = requests.head(url, timeout=timeout)
        if requisiçoes.status_code in (403, 401, 405):
            print('[#] METODO HEAD BLOQUEADO!, MUDANDO PARA METODO GET')
            requisiçoes = requests.get(url, timeout=timeout)
            
        if requisiçoes.status_code == 200:
            headersz = requisiçoes.headers
            header1 = headersz.get('Content-Type', 'NAO ENCONTRADO')
            header2 = headersz.get('X-Powered-By', 'NAO ENCONTRADO')
            print(f'[+] HEADER ALVO ENCONTRADO:  {header1}')
            print(f'[+] HEADER ALVO ENCONTRADO:  {header2}')
        else:
            print(f'[+] O SERVIDOR RESPONDEU COM STATUS CODE: {requisiçoes.status_code}')
            
    except Exception as e:
        print(f'[+] NAO FOI POSSIVEL FAZER A REQUISIÇAO, RESPOSTA DO SERVIDOR: {e}')

def argumentos_parser():
    parser = argparse.ArgumentParser(description="Descrição do Script")

    parser.add_argument('-u', '--url', required=True, help="digite sua URL alvo aqui! ex: http://alvo.com")
    parser.add_argument('-t', '--timeout', type=int, help="Explicação aqui")

    return parser

def main():
    try:
        parser = argumentos_parser()
        args = parser.parse_args()
        url_alvo = args.url
        timeout_alvo = args.timeout

        if not url_alvo.startswith(('http://', 'https://')):
            url_alvo = f'http://{url_alvo}'

        fazer_requisiçoes(url_alvo, timeout_alvo)
    except KeyboardInterrupt:
        print('[+] SCRIPT INTERROMPIDO POR COMANDO (CTRL + C)')

if __name__ == '__main__':
    main()
