Meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
DiasPorMes = [31,28,31,30,31,30,31,31,30,31,30,31]

for i in range (0,12):
  print '%s tiene %d dias.' % (Meses[i], DiasPorMes[i])
