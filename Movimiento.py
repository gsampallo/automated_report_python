class Movimiento(object):
    
	def __init__(self,lista):
        
		self.fecha = lista[0]
		self.producto_id = lista[1]
		self.producto = lista[2]
		self.tipo_movimiento = lista[3]
		self.cantidad = str(lista[4])


	def listar(self):
		print (self.fecha,self.producto_id,self.producto,self.tipo_movimiento,self.cantidad)