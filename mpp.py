
"""
# Programación  Lógica
#Angeles Quiros Cristian Gabriel
#Gomar Salvador Juan Manuel 


# Modus ponendo ponens

"el modo que, al afirmar, afirma"

P → Q. P ∴ Q


Se puede encadenar usando algunas variables

P → Q. 
Q → S. 
S → T. P ∴ T

Ejercicio 
Defina una funcion que resuelva con verdadero o falso segun corresponada

Laura esta en Queretaro
Alena esta en Paris
Claudia esta en San Francisco
Queretaro esta en Mexico
Paris esta en Francia
San Francisco esta en EUA
Mexico esta en America
Francia esta en Europa
EUA esta en America
"""
Base = [
	["Laura","Queretaro"],
	["Alena","Paris"],
	["Claudia","San Francisco"],
	["Queretaro","Mexico"],
	["Paris","Francia"],
	["San Francisco","EUA"],
	["Mexico","America"],
	["Francia","Europa"],
	["EUA","America"]
]

def estaB(base,B):
	if not base:
		return []
	if len(base):
		if B == base[0][0]:
			return base[0][1]
		else:
			return estaB(base[1:], B)

def esta(E1,E2):
	B = estaB(Base,E1)
	L = estaB(Base, B)
	if L == E2 or B == E2:
		return True
	S = estaB(Base, L)
	if S == E2:
		return True
	else:
		return False


print(esta("Alena","Europa"))
# true

print(esta("Laura","America"))
# true

print(esta("Laura","Europa"))
# false



