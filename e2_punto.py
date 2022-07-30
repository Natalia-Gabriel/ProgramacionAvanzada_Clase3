#Ejercicio 2

class Punto:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def eje_x(self):
        return self.x

    def eje_y(self):
        return self.y
    
    def opuesto(self):
        return (-self.x,-self.y)
    
    def set_eje_x(self,x):
        self.x=x

    def set_eje_y(self,y):
        self.y=y


#instanciar
puntoA = Punto(2,-3)
puntoA.eje_x()
puntoA.eje_y()
puntoA.opuesto()


puntoB = Punto(-1,-6)
puntoB.eje_x()
puntoB.eje_y()
puntoB.opuesto()

 
