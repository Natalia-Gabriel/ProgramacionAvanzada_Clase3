class Linea:
    def __init__(self, x1,y1,x2,y2):
     
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
 
    def mover_derecha(self,d):
        return (self.x1+d,self.y1) , (self.x2+d,self.y2)
        
        

    def mover_izquierda(self,d):
        return (self.x1-d,self.y1) , (self.x2-d,self.y2)
        

    def mover_arriba(self,d):
        return (self.x1,self.y1+d) ,(self.x2,self.y2+d) 
              
    
    def mover_abajo(self,d):
        return (self.x1,self.y1-d), (self.x2,self.y2-d)
        


#Prueba

L1=Linea(2,5,-1,-3)
L1.mover_abajo(3)
