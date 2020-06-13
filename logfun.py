
"""
Angeles Quiros Cristian Gabriel
Gomar Salvador Juan Manuel 

	https://www.computrabajo.com.mx/ofertas-de-trabajo/oferta-de-trabajo-de-desarrollador-batch-exp-sistemas-abiertos-en-queretaro-601BC72F6CEBB0F761373E686DCF3405
	En una empresa solicitan Lic./Ing. en Sistemas, Computación o afín.
	con los siguientes requisitos:
	• Oracle BBDD

	• SQL y PL/SQL

	• Linux

	• Unix

	• Shell (Linux - Unix)

	• C++, Proc*C y Tuxedo V12 o anteriores

	• Visual Basic 6.0

	• Java (Frameworks) , Web Services y Micro Servicios APIs
	
	Realizar un programa que realice preguntas al usuario
	y que apartir de sus respuestas evalue si es cadidato o no
	
	(usen conjuntos)

"""

Requisitos = {
	"Oracle","SQL/PL","Linux","Unix","Shell","C++",
	"Proc*C","TuxedoV12", "VB6", "Java","WebServices","MicroServicios"
} 


print("¿Qué lenguajes de programacion maneja? ")

RequisitosUsuario = input()

X = RequisitosUsuario.replace(' ','')

R = X.split(',')

S = set(R)

Requisitos = Requisitos <= S

print("¿Es candidato?: ",Requisitos)

#Oracle, SQL/PL, Linux, Unix, Shell, C++, Proc*C, TuxedoV12, VB6, Java, WebServices, MicroServicios
