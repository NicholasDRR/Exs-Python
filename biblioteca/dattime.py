from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import mdays

setlocale(LC_ALL, 'pt_BR.utf-8')

atual = datetime.now()
mesatual = int(atual.strftime('%m'))
data = datetime(2022, 8, 12, 0, 53, 20)
print(atual.strftime('%A-%d de %B %Y'))
print(atual.strftime('%d-%m-%Y %H:%M:%S'))
print(mesatual, mdays[mesatual])
##################################################################
#timestamp = data.timestamp()
#print(data.strftime('%d-%m-%Y %H:%M:%S'))
#data2 = datetime.fromtimestamp(timestamp)
#print(data2)
#data3 = datetime.strptime('12-08-2022 01:01:00', '%d-%m-%Y %H:%M:%S')
#print(data3 + timedelta(days=5, seconds=20, hours=1, minutes=21))
#dif = data3 - data
#print(dif)
#
#print(dif.days)
#print(dif.seconds)
