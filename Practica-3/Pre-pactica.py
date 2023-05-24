class Vehiculo(): 

    def __init__(self,marca:str,ruedas:int,color:str):#esto es un constructor
      self.marca = marca
      self.ruedas = ruedas
      self.color = color
      self.EnMarcha = False

    def arrancar(self):
        self.EnMarcha= True
       
    def mostrar(self):
        print(self.ruedas)
        print(self.marca)
        print(self.color)
        print(self.EnMarcha)  

    def tipoVehiculo(self):
        if self.ruedas == 4 :
            print("Es un automovil")
        elif self.ruedas == 2:
           print("Es una motocicleta")   
    
miAuto=Vehiculo("Ford", 2 ,"Rojo")
miAuto.arrancar()
miAuto.tipoVehiculo()
miAuto.mostrar()

