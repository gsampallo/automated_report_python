import xlwt
from datetime import datetime

class MovimientosToExcel:

	def __init__(self,name):
		self.wb = xlwt.Workbook()
		self.ws = self.wb.add_sheet(name,cell_overwrite_ok=True)

		self.ws.write(0, 0, name)

		columnas = ["Fecha",
					"Producto ID",
					"Producto",
					"Tipo Movimiento",
					"Cantidad"]

		c = 0
		for columna in columnas:
			self.ws.write(1, c, columna)
			c = c + 1

		self.fila = 2

	def agregarItem(self,item):
		self.ws.write(self.fila, 0, item.fecha)
		self.ws.write(self.fila, 1, item.producto_id)
		self.ws.write(self.fila, 2, item.producto)
		self.ws.write(self.fila, 3, item.tipo_movimiento)
		self.ws.write(self.fila, 4, item.cantidad)

		self.fila = self.fila + 1

	def guardarPlanilla(self,archivo):
		self.wb.save(archivo)
		print ("Generado")

