class Cancion:
    def __init__(self,titulo,autor):
        self.titulo=titulo
        self.autor=autor
    
    
    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def set_titulo(self,escTitulo):
        self.escTitulo=escTitulo
    
    def set_autor(self,escAutor):
        self.escAutor=escAutor


#prueba 
tema1=Cancion("aaa","sinBanderas")
tema1.get_titulo()
tema1.get_autor()

