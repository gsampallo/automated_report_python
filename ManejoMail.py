import smtplib

from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.MIMEBase import MIMEBase
from email import Encoders
from Mensaje import Mensaje

import json
import io

class ManejoMail(object):

	def __init__(self):

		self.destinatarios = []
		self.parametros = json.load(open("config.json", "r"))


	def enviarCorreo(self,mensaje,archivo):

		smtp = smtplib.SMTP(self.parametros["smtp"])
		smtp.login(self.parametros["mail"], self.parametros["password"])

		correo = MIMEMultipart()
		
		correo['Subject'] = mensaje.subject
		correo['From'] = self.parametros["mail"]
		
		texto = MIMEText(mensaje.getMensaje(), 'html')
		correo.attach(texto)

		part = MIMEBase('application', "octet-stream")
		part.set_payload(open(archivo, "rb").read())
		Encoders.encode_base64(part)

		part.add_header('Content-Disposition', 'attachment; filename="'+archivo+'"')
		correo.attach(part)

		for destino in self.destinatarios:
			print ("Enviando correo a ",destino)
			correo['To'] = destino
			smtp.sendmail(self.parametros["mail"], destino, correo.as_string())

		

		smtp.quit()    