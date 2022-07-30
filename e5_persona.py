class Persona:
	def __init__(self, nombre, apellido):
		self.nombre=nombre
		self.apellido=apellido
		
	def datos(self):
		return self.apellido+", "+self.nombre



#prueba
persona1=Persona("Natalia","Gabriel")
persona1.datos()

