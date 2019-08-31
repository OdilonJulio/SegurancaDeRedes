# -*- coding: utf-8 -*-




## Como encriptar: python3 esteganografia.py arquivoTextoClaro.txt image.bmp
# Digitar "1" no input

## Como decriptar: python3 esteganografia.py arquivoTextoDecifrado.txt encriptada_image.bmp
# Digitar "2" no input
 
import sys
from PIL import Image

modo = input("Digite 1 para ENCRIPTAR e 2 para DECRIPTAR: ")

if modo == '1':
	#Tratamento de exceção, caso não abra a imagem.
	try:
		retrato = Image.open(sys.argv[2])
	except IOError as erro:
		print('Houve um erro ao tentar abrir a imagem.')
	#Tratando, caso a imagem não tenho espaço para a mensagem.
	mensagem = open(sys.argv[1], 'r').read()
	if len(mensagem)*8 < len(retrato.getdata())*3:

		## Transformando a mensagem em Lista Binária.
		mensagemEmListaBinaria = list()

		for caractere in mensagem:
			mensagemEmListaBinaria.append(bin(ord(caractere))[2:].zfill(8))

		# Transformando a imagem em Lista Binária.
		retratoEmListaBinaria = list()
		retrato = Image.open(sys.argv[2])

		for pixel in list(retrato.getdata()):
			
			retratoEmListaBinaria.append(bin(pixel[0])[2:].zfill(8))
			retratoEmListaBinaria.append(bin(pixel[1])[2:].zfill(8))
			retratoEmListaBinaria.append(bin(pixel[2])[2:].zfill(8))

		# Cifrando a mensagem(binária) na imagem(binária).
		count = 0
		for byte in mensagemEmListaBinaria:	
			for bit in list(byte):
				retratoEmListaBinaria[count] = str(retratoEmListaBinaria[count])[:-1] + bit
				count += 1
		count2 = count
		for slot in '00000011':
			retratoEmListaBinaria[count2] = str(retratoEmListaBinaria[count2])[:-1] + slot
			count2 += 1

		#Transformando a imagem binária (com a mensagem) em imagem normal.
		count3 = 0
		retratoRGB = list()
		RGBs = list()

		for pixel in range(0, len(retratoEmListaBinaria)):
			RGBs.insert(count, int(retratoEmListaBinaria[pixel], 2))
			count3 = (count3 + 1) % 3
			
			if (pixel + 1) % 3 == 0 and pixel != 0:
				retratoRGB.insert(pixel, RGBs)
				RGBs = list()

		#Salvando o arquivo da imagem normal já com a mensagem criptografada.
		arquivo = list()
		for pixel in retratoRGB:
			arquivo.append(tuple(pixel))

		novaImagem = Image.new('RGB', retrato.size)
		novaImagem.putdata(arquivo)
		novaImagem.save('encriptada_'+sys.argv[2])
		print('Mensagem codificada na imagem com sucesso!')
elif modo == '2':
	retratoComMensagemCifrada = Image.open(sys.argv[2])
	# Transformando a imagem com cifra em Lista Binária.
	retratoComMensagemEmListaBinaria = list()
	for pixel in list(retratoComMensagemCifrada.getdata()):
		
		retratoComMensagemEmListaBinaria.append(bin(pixel[0])[2:].zfill(8))
		retratoComMensagemEmListaBinaria.append(bin(pixel[1])[2:].zfill(8))
		retratoComMensagemEmListaBinaria.append(bin(pixel[2])[2:].zfill(8))
	count = 0
	arrayTemporaria = str()
	mensagemDecifrada = str()
	for pixel in range(len(retratoComMensagemEmListaBinaria)):
		for bit in range(8):
			arrayTemporaria += str(retratoComMensagemEmListaBinaria[count])[-1]
			count += 1
		caractere = chr(int(arrayTemporaria, 2))
		if arrayTemporaria != '00000011':
			mensagemDecifrada += caractere
			arrayTemporaria = str()
		else:
			break
	print(mensagemDecifrada)
	arquivoTextoDecifrado = open(sys.argv[1], 'w')
	arquivoTextoDecifrado.writelines(mensagemDecifrada)
	arquivoTextoDecifrado.close()
else:
	print('Escolha incorreta!')