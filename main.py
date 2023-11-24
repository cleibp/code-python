import time
import calendar
import random
import speedtest
from time import sleep
import requests
import json
from random import randint

## Vai dar erro
# print(1+2+"3")

alfabeto = "abcdefghijklmnopqrstuvwxyz"
criptografia = "qwertyuiopasdfghjklzxcvbnm"
erro = "0"

def calc():
  cube = [1,2,3,4,5]
  cube[3] = 4 ** 3
  return  cube

def countdown(timer):
  while timer:
    print(timer)
    time.sleep(1)
    timer -= 1
  print("BANG")

def cal():
  number_month = range(1, 13,1)
  for n in number_month:
    print(calendar.month(2023,n))
    n +=1

def generator():
  lower = "abcdefghijklmnopqrstuvwxyz"
  upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  numbers = "0123456789"
  symbols = "[]{}()*;/,._-"
  all = lower + upper + numbers + symbols
  length = 16
  password = "".join(random.sample(all, length))
  print(password)

def meter():
  test = speedtest.Speedtest()
  download = test.download()
  upload = test.upload()
  print(f"Download speed: {download}")
  print(f"Upload speed: {upload}")

def temporizador(tempo):
  while tempo >= 0:
    print(tempo)
    sleep(1)
    tempo -= 1
  print("O tempo acabou")

def criptografar(mensagem):
    mensagem_criptografada = ""
    for letra in mensagem:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            mensagem_criptografada += criptografia[indice]
        else:
            mensagem_criptografada += erro # prédio

    return mensagem_criptografada

def descriptografar(mensagem):
    mensagem_normal = ""
    for letra in mensagem:
        if letra in criptografia:
            indice = criptografia.index(letra)
            mensagem_normal += alfabeto[indice]
        else:
            mensagem_normal += letra

    return mensagem_normal

def converter(valor, de, para):
    api = requests.get(f"https://economia.awesomeapi.com.br/{de}-{para}/")

    if api.status_code == 200:
        response = api.json()
        return float(response[0]['bid']) * valor
    else:
        return None

def ad():
  continua = True
  wins = 0
  loss = 0
  
  while continua:
      aleatorio = randint(1,5)
      tentativas = 3
      while tentativas > 0:
          escolha = int(input("Digite um número: "))
          if escolha == aleatorio:
              wins += 1
              print("Parabéns! Você acertou!")
              x = input("Deseja continuar para o próximo número? S/N: ")
              continua = True if x.upper() == "S" else False
              break
          else:
              tentativas -= 1
              if tentativas == 0:
                  loss += 1
                  x = input("Acabaram as tentativas, deseja continuar? S/N: ")
                  continua = True if x.upper() == "S" else False
              else:
                  print(f"Você errou :(. {tentativas} tentativas restantes")
      print(f"PLACAR = WINS: {wins} X LOSSES: {loss}")


def main():
  print("### Soma ###")
  a = '5'
  b = '5'
  print(a+b)

  print("### Cubo ###")
  print(calc())

  print("### Contador ###")
  countdown(10)
  
  print("### CALENDARIO ###")
  cal()

  print("### GERADOR DE SENHA ###")
  generator()

  print("### SPEED ###")
  meter()

  print("### TEMPORIZADOR ###")
  tempo = int(input("Tempo em segundos: "))
  temporizador(tempo)

  print("### CRIPTOGRAFIA / DESCRIPTOGRAFIA ###")
  print("O que deseja fazer?")
  print("1. Criptografar mensagem")
  print("2. Descriptografar mensagem")
  op = int(input("Escolha: "))
  if op == 1:
      criptografada = input("Mensagem para criptografar: ").lower()
      print(criptografar(criptografada))
  elif op == 2:
      descriptografada = input("Mensagem para descriptografar: ").lower()
      print(descriptografar(descriptografada))
  else:
      print("Opção inválida")

  print("### CONVERTER MOEDA ###")
  print("Principais moedas disponíveis: USD, BRL, EUR, JPY, BTC, ETH, DOGE, ETC.\n")
  valor = float(input("Valor: "))
  de = input("Converter de (código): ")
  para = input("Converter para (código): ")
  cotacao = converter(valor, de, para)
  if cotacao is not None:
      print(f"{valor} {de} é equivalente a {cotacao} {para}")
  else:
      print("Erro: moeda inválida.")

  print("### ADIVINHE O NÚMERO ###")
  ad()

if __name__ == "__main__":
  main()
