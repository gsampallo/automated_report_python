class Mensaje(object):

    def __init__(self,inicio,fin):

        self.subject = "Reporte semanal de descansos "+inicio+" al "+fin

        self.head = "<html><h2><b>Reporte de Periodo "+inicio+" - "+fin+"</b></h2>"
        self.body = "<p>Se adjunta los datos de la semana.</p>"
            

        self.tail = '<p>Para datos especificos por favor referirse a la pagina <a href=\"#\">web</a>.</p></html>'

    def getMensaje(self):
        return self.head+self.body+self.tail
    

    def agregarContenido(self,data):
        self.body = self.body + data
    
     