from ManejoMail import ManejoMail
from Mensaje import Mensaje

msg = Mensaje('01-06-2019','07-06-2019')
#Agregamos contenido al mensaje en formato html
msg.agregarContenido("<p>Agregamos un detalle al mensaje</p>")

#Agregamos una imagen al mensaje
msg.agregarContenido("<p><img src=\"http://www.gsampallo.com/blog/wp-content/uploads/2019/07/logo-gs_logo-fondo-negro.jpg\" height=\"15%\"	width=\"15%\"></p>")

mMail = ManejoMail()

mMail.destinatarios.append("destinatario1@demo.com")
mMail.destinatarios.append("destinatario2@demo.com")
mMail.destinatarios.append("destinatario3@demo.com")

mMail.enviarCorreo(msg,"ejemplo.xls")
