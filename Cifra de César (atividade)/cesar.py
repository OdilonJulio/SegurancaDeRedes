# -*- coding: utf-8 -*-


import sys
import string



texto = open(sys.argv[1], 'r').read()

# chave = int(sys.argv[2])

alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ?,'

mensagemConvertida = ''
range(alfabeto)
'''
#for chave in range(alfabeto):
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



arquivo = open('mensagens.txt', 'w')
arquivo.writelines(mensagemConvertida)
arquivo.close()













'''
modo = input('Escolha E para encriptar ou D para decriptar o texto: ')

for caractere in texto:
  if caractere in CARACTERES:

    num = CARACTERES.find(caractere)
 
    if modo == 'E':
      num = num + chave
    elif modo == 'D':
      num = num - chave
 
  if num >= len(CARACTERES):
    num = num - len(CARACTERES)
  elif num < 0:
    num = num + len(CARACTERES)

    mensagemConvertida = mensagemConvertida + CARACTERES[num] 
  else:
 
    mensagemConvertida = mensagemConvertida + caractere

if modo == 'E':
  print('O texto criptografado é ', mensagemConvertida)
if modo == 'D':
  print('O texto decriptado é ', mensagemConvertida)
'''
