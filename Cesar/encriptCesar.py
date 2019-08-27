# -*- coding: utf-8 -*-

## Digite no termilal
# python encriptCesar.py texto.txt <chave numérica>

import sys
import string


texto = open(sys.argv[1], 'r').read()
chave = int(sys.argv[2])

alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ?,'

arquivo = open('mensagens.txt', 'w')

mensagemConvertida = ''
for caractere in texto:
  if caractere in alfabeto:
    position = alfabeto.find(caractere)
    position = position - chave
    if position >= len(alfabeto):
      position = position - len(alfabeto)
    elif position < 0:
      position = position + len(alfabeto)
    mensagemConvertida = mensagemConvertida + alfabeto[position] 
  else:
    mensagemConvertida = mensagemConvertida + caractere
arquivo.writelines(mensagemConvertida)
arquivo.close()
