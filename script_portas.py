import socket
import argparse
import concurrent.futures




def conections(ip, porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    return s


def grep_banner(s):
    try:
        banner = s.recv(1024)
        return banner.decode('utf-8', errors='ignore').strip()
    except Exception as e:
        print(f'[#]------ ERRO NA CAPTURA DO BANNNER, ERRO:  {e}')


def pegar_serviço(porta):
   try:
     servico = socket.getservbyport(porta)
     print(f"A porta {porta} usa o serviço: {servico}")
   except OSError:
     print(f"Serviço desconhecido ou não padrão para a porta {porta}")


def scan_port(ip, porta):
    s = conections(ip, porta)
    try:
        s.connect((ip, porta))
        if s:
           print(f'[+] A PORTA {porta} ESTÁ ABERTA!')
           service = pegar_serviço(porta)
        else:
           print(f'[#] A PORTA {porta} ESTÁ FECHADA!')
           
        banner = grep_banner(s)
        if banner:
           print(f'[+] ENCONTRAMOS O BANNER DA PORTA {porta}: banner{banner}')
        

       
           
    except ConnectionRefusedError:
        print(f'[#] ConnectionRefusedError na porta {porta}')

    except socket.timeout:
        print(f'[#] TIMEOUT NA PORTA {porta}')

    except OSError:
        print(f'OsError na porta {porta}')
    finally:
        s.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Meu Scanner de Portas")
    parser.add_argument("-t", "--target", type=str, required=True, help="IP ou domínio alvo")
    parser.add_argument("-p", "--port", type=int, nargs='+', default=[80], help="Portas separadas por espaço")
    parser.add_argument("-v", "--verbose", action="store_true", help="Modo detalhado")

    args = parser.parse_args()

    ip_alvo = args.target
    portas = args.port

    print(f"[*] Iniciando scan no alvo: {ip_alvo}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(lambda p: scan_port(ip_alvo, p), portas)

    print("[*] Scan finalizado!")




