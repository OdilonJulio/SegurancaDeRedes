# -*- coding: utf-8 -*-

## Digite no termilal
# python steganography.py . mensagem.txt

import sys
from PIL import Image
import HYP_Utils
import HYP_Texture
import HYP_Material

def cifrar(retratoBinario, mensagemBinaria):
	count = 0
	for byte in mensagem :
		for bit in list(byte):
			retratoBinario[count] = str(retratoBinario[count])[:-1] + bit
			count += 1
	for slot in '00000011':
		retratoBinario[count] = str(retratoBinario[count])[:-1] + slot
		count += 1
	return retratoBinario

def decifrar(retratoCifrado):
	count = 0
	arrayTemporaria = str()
	mensagemDecifrada = str()
	for pixel in range(len(retratoCifrado)):
		for bit in range(8):
			arrayTemporaria += str(retratoCifrado[count])[-1]
			count += 1
		caractere = chr(int(arrayTemporaria, 2))
		if arrayTemporaria != '00000011':
			mensagemDecifrada += caractere
			arrayTemporaria = str()
		else:
			break
	print(mensagemDecifrada)

def salvarImagem(retrato, caminho, tamanho):
	arquivo = list()
	for pixel in retrato:
		arquivo.append(tuple(pixel))
	novaImagem = Image.new('RGB', tamanho)
	novaImagem.putdata(arquivo)
	novaImagem.save('modificado '+caminho)

def retratoNormal(retratoBinario):
	count = 0
	retratoRGB = list()
	RGBs = list()
	for pixel in range(0, len(retratoBinario)):
		RGBs.insert(count, int(retratoBinario[pixel], 2))
		count = (count + 1) % 3
		if (pixel + 1) % 3 == 0 and pixel != 0:
			retratoRGB.insert(pixel, RGBs)
			RGBs = list()
	return retratoRGB

def binDaMensagem(mensagem):
	mensagemEmListaBinaria = list()
	for caractere in mensagem:
		mensagemEmListaBinaria.append(bin(ord[i])[2:].zfill(8))
	return mensagemEmListaBinaria

def binDaImagem(retrato):
	retratoEmListaBinaria = list()
	for pixel in list(retrato.getdata()):
		retratoEmListaBinaria.append(bin(pixel[0])[2:].zfill(8))
		retratoEmListaBinaria.append(bin(pixel[1])[2:].zfill(8))
		retratoEmListaBinaria.append(bin(pixel[2])[2:].zfill(8))
	return retratoEmListaBinaria

mensagemParaCifrar = open(sys.argv[2], 'r').read()
modo = raw_input("Digite 1 para ENCRIPTAR e 2 para DECRIPTAR: ")

if modo == 1:
	try:
		imagem = Image.open(sys.argv[1])
	except IOError as erro:
		print('Houve um erro ao tentar abrir a imagem.')
	if len(sys.argv[1])*8 < len(imagem.getdata()*3):
		salvarImagem(retratoNormal(cifrar(binDaImagem(imagem), binDaMensagem(mensagemParaCifrar))), sys.argv[1], imagem.size())
	else:
		print('A mensagem não cabe na imagem.')
elif modo == 2:
	imagem = Image.open('encriptada:::' + sys.argv[1])
	decifrar(binDaImagem(imagem))