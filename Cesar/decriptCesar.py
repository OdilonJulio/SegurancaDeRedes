# -*- coding: utf-8 -*-
import sys
import string


texto = open(sys.argv[1], 'r').read()

alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ?,'

arquivo = open('mensagens.txt', 'w')

for chave in range(len(alfabeto)):
  arquivo.writelines('Chave %d' % chave)
  arquivo.writelines("\n\n\n")
  mensagemConvertida = ''
  for caractere in texto:
    if caractere in alfabeto:
      position = alfabeto.find(caractere)
      position = position + chave
      if position >= len(alfabeto):
        position = position - len(alfabeto)
      elif position < 0:
        position = position + len(alfabeto)
      mensagemConvertida = mensagemConvertida + alfabeto[position] 
    else:
      mensagemConvertida = mensagemConvertida + caractere
  arquivo.writelines(mensagemConvertida)
  arquivo.writelines("\n\n\n")

arquivo.close()
