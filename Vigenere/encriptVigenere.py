# -*- coding: utf-8 -*-

# python encriptVigenere.py texto.txt

import sys
import string

### TUDO MINÚSCULO

texto = open(sys.argv[1], 'r').read()
chave = raw_input("Chave: ")
#chave = str(sys.argv[2])


alfabeto = 'abcdefghijklmnopqrstuvwxyz '

chavesConcatenadas = ''
count = 0
for position in range(len(texto)):
	if texto[position] == ' ':
		chavesConcatenadas = chavesConcatenadas + ' '
		count += 1
	else: 
		chavesConcatenadas = chavesConcatenadas + chave[((position - count))%len(chave)]	

mensagemCriptografada = ''
positionChavesConcatenadas = []
positionTexto = []
position = []
# Criando vetores com a posição de cada letra do texto e do alfabeto.
for caractere in chavesConcatenadas:
	positionChavesConcatenadas.append(alfabeto.find(caractere))

for caractere in texto:
	positionTexto.append(alfabeto.find(caractere))

for index in range(len(texto)):
	position = positionTexto[index] + positionChavesConcatenadas[index]
	if position >= len(alfabeto):
		position = position%len(alfabeto) + 1
	if position < 0:
		position = position + len(alfabeto)
	mensagemCriptografada = mensagemCriptografada + alfabeto[position]
print(texto)
print(chavesConcatenadas)
print(mensagemCriptografada)

