# automated_report_python
An easy way to generate automated report with Python. Create spreadsheet and email them.
This is a proposal of how you can do the automated report. It will necessary that modified the example acord your need. Everything is described in the article link below.

## Instalation

You will need:

- Python
- mysql.connector
    You can install throw pip:
    pip install mysql.connector
- xlwt
    pip install xlwt

- User and password of your database.  

## How to use

1. On reporteSemanal.py you need to modify the credential, and the sql query acord what you need to show. Also the list of the destinataries whom you need to send the report.
2. On Movimiento.py, map the columns of the query to one object, you need to rename according to your query.
3. On ManejoMail.py, need to change the credential of your SMTP server.

Finaly configure cron/scheduled tasks to run reporteSemanal.py when you need.