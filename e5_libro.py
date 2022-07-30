from e5_persona import Persona

class Libro(Persona):
	def __init__(self,titulo,autor,isbn,pag,edicion,lugar,fecha_ed):
		self.titulo=titulo
		self.autor=autor
		self.isbn=isbn
		self.pag=pag
		self.edicion=edicion
		self.lugar=lugar
		self.fecha_ed=fecha_ed
		
	def get_titulo(self):
		return self.titulo
		
	def set_titulo(self,titulo):
		self.titulo=titulo
		
	def get_autor(self):
		return self.autor
		
	def set_autor(self,autor):
		self.autor=autor
		
	def get_isbn(self):
		return self.isbn
		
	def set_isbn(self,isbn):
		self.isbn=isbn
		
	def get_pag(self):
		return self.pag
	
	def set_pag(self,pag):
		self.pag=pag	
	
	def get_edicion(self):
		return self.edicion
		
	def set_edicion(self,edicion):
		self.edicion=edicion
		
	def get_lugar(self):
		return self.lugar
		
	def set_lugar(self,lugar):
		self.lugar=lugar
		
	def get_fecha_ed(self):
		return self.fecha_lug
		
	def set_fecha_ed(self,fecha_ed):
		self.fecha_ed=fecha_ed
		
	def mostrar_info(self):
		print((f'''
Titulo: {self.titulo} 
Autor: {self.autor()}
ISBN: {self.isbn} 
{self.ed}, {self.lugar}
{self.fecha_ed}	
{self.pag} '''))


