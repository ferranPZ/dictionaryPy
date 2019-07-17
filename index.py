#Algoritmo que crea diccionario a partir de definiciones proporcinadas por el usuario
#Algorithm which creates a dictionary from definitions provided  by the user inputs

#define vars
diccionario={}
tupla = ("halfduplex","fullduplex","simplex","OSI model","TCP/IP model")
i=0


#it reads user input
def leer(i):
	print("Defina"+" "+tupla[i])
	definiciones(i,input())

#it assigns the user definitions to each key in the dictionary
def definiciones(i,palabra):
	diccionario[tupla[i]] = palabra
	
def main():
	#todo:i global
	for i in range(len(tupla)):
		leer(i)

	print(diccionario)

main()