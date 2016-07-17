import datetime

t = datetime.time(1, 2, 3, 234)
hora = t.hour
minuto = t.minute
segundo = t.second
microsegundo = t.microsecond
#------------------------------------------
#Sumatoria de Días
hoy = datetime.date.today()
dia = datetime.timedelta(days=1)
ayer = hoy - dia
mañana = hoy + dia
#------------------------------------------
now = datetime.datetime(2014, 12, 14, 13, 8, 32)
año = now.year
mes = now.month
dia = now.day
hora = now.hour
minuto = now.minute
segundo = now.second

now.ctime() #Sun Dec 14 13:09:19 2014
dia = datetime.date(2005, 04, 24)
hora = datetime.time(12, 04, 12, 234)
#------------------------------------------
import calendar 
cal = calendar.month(2014, 12)
#------------------------------------------
now = datetime.datetime.now()
fecha = now.strftime("%y-%m-%d %H:%M:%S") # 15-01-12 12:47:38
año = now.strftime("%Y") # 2015
añoAbreviado = now.strftime("%y") # 15
mes = now.strftime("%B") # January
mesAbreviado = now.strftime("%b") # Jan
mesNumero = now.strftime("%m") # 1
dia = now.strftime("%A") # Monday
diaAbreviado = now.strftime("%a") # Mon
diaMes = now.strftime("%d") # 12
diaAño = now.strftime("%j") # 12
diaSemana = now.strftime("%w") # 1
semanaAño = now.strftime("%U") # 2
#------------------------------------------
#Modificar el idioma
import locale
locale.setlocale(locale.LC_TIME, 'es_ES')


