from datetime import datetime, timedelta
import mysql.connector
from mysql.connector import errorcode
from Movimiento import Movimiento
from MovimientosToExcel import MovimientosToExcel

config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'stock',
        'raise_on_warnings': True,

      }

cursor = 0
try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    query = "SELECT \
                DATE_FORMAT(movimientos.fecha,'%d-%m-%Y') as fecha, \
                productos.producto_id, \
                productos.descripcion, \
                movimientos.tipo_movimiento, \
                movimientos.cantidad \
                FROM \
                movimientos \
                INNER JOIN productos ON movimientos.producto_id = productos.producto_id \
                WHERE WEEKOFYEAR(movimientos.fecha) = (WEEKOFYEAR(curdate())-1) \
                ORDER BY productos.descripcion,movimientos.fecha"

    cursor.execute(query)
    m2e = MovimientosToExcel('Weekly Report')

    for fila in cursor:
        print(fila)
        movimiento = Movimiento(fila)
        movimiento.listar()

        m2e.agregarItem(movimiento)

    m2e.guardarPlanilla("reporte_semanal.xls")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
  cnx.close()

