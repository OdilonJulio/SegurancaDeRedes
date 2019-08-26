# -*- coding: utf-8 -*-


def mensagem_e_chave():
	texto = open(sys.argv[1], 'r').read()
	chave = open(sys.argv[2], 'r').read()

	chave_map = " "

	j = 0
	for i in range(len(texto)):
		if ord(texto[i]) == 32: # Por que 32?
			chave_map += " "
		else:
			if j < len(chave):
				chave_map += chave[j]
				j += 1
			else:
				j = 0
				chave_map += chave[j]
				j += 1
	# print(chave_map)
	return mensagem, chave_map

def criando_tabela_de_Vigenere():
	table = []
	for i in range(26):
		table.append([])
	for row in range(26):
		for column in range(26):
			if (row + 65) + column > 90:

				table[row].append(chr((row + 65) + column - 26))
			else:
				table[row].append(chr((row + 65) + column))
	for row in table:
		for column in row:
			print(column, end = ' ')
		print(end = "\n")

	return table

def mensagemCifrada( mensagemFinal, chave_mapeada ):
	table = criando_tabela_de_Vigenere()
	textoEncriptado = " "
	for i in range(len(mensagemFinal)):
		if mensagemFinal[i] == chr(32):

			textoEncriptado += " "
		else:
			row = ord(mensagemFinal[i] - 65)
			column = ord(chave_mapeada[i]) - 65
			textoEncriptado += table[row][column]

	print(" Mensagem Encriptada: []".format(textoEncriptado))

def itr_count(chave_mapeada, mensagemFinal):
	counter = 0
	result = " "
	

def mensagemDecifrada( mensagemFinal, chave_mapeada):
	table = criando_tabela_de_Vigenere()
	textoDecriptado = " "

	for i in range(len(mensagemFinal)):
		if mensagemFinal[i] == chr(32):

			textoDecriptado += " "
		else:
			textoDecriptado += chr(65 + itr_count(ord(chave_mapeada[i]), ord(mensagemFinal[i])))

	print(" Mensagem Decriptada: []".format(textoDecriptado))

def main():
	print("Chave e Mensagem podem apenas serem alfabéticas.")
	processo = int(input(" 1 - Encriptar.\n 2 - Decriptar.\n Escolha 1 ou 2."))
	if processo == 1:
		print(" --- Encriptação --- ")
		mensagemFinal, chaveFinal = mensagem_e_chave()
		mensagemCifrada( mensagemFinal, chave_mapeada )

	elif processo == 2:
		print(" --- Decriptação --- ")
		MensagemFinal, chaveFinal = mensagem_e_chave()
		mensagemDecifrada(mensagemFinal, chave_mapeada)

	else:
		print(" Escolha errada! ")

if __name__ == "__principal__":
	main()