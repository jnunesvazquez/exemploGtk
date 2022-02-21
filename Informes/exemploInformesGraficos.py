from reportlab.platypus import SimpleDocTemplate
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

guion = []

d = Drawing(100, 100)
etiqueta = Label()
etiqueta.fontName = 'Helvetica'
etiqueta.setOrigin(100, 90)
etiqueta.angle = 45
etiqueta.dx = 500
etiqueta.dy = -20
etiqueta.boxStrokeColor = colors.green
etiqueta.setText ('unha \n etiqueta\n Multiliña')
d.add (etiqueta)
d = Drawing (400, 200)

datos = [(23,14,10,9,19,21,25,4),
         (2,7,9,16,14,19,20,24)]

bg = VerticalBarChart()
bg.data = datos
bg.x = 50
bg.y = 50
bg.height = 125
bg.width = 300
bg.strokeColor = colors.black
bg.valueAxis.valueMin = 0
bg.valueAxis.valueMax = 30
bg.valueAxis. valueStep = 10
bg.categoryAxis.labels.boxAnchor = 'ne' #north east
bg.categoryAxis.labels.dx = 8
bg.categoryAxis.labels.dy = -2
bg.categoryAxis.labels.angle = 30
bg.categoryAxis.categoryNames = ['Xan-21', 'Feb-21', 'Mar-21', 'Abr-21', 'Mai-21', 'Xun-21', 'Xul-21', 'Ago-21']
bg.groupSpacing = 10
bg.barSpacing = 5
d.add(bg)
guion.append(d)

d = Drawing(300, 200)
tarta = Pie()
tarta.data = [3, 12, 20, 50, 30]
tarta.labels = ['Non Prensetados', 'Suspensos', 'Aprobados', 'Notables', 'Sobresalientes']
tarta.x = 65
tarta.y = 15
tarta.width = 180
tarta.height = 180
tarta.slices.strokeWidth = 0.5
tarta.slices[2].popout = 10
tarta.slices[3].strokeWidth = 2
tarta.slices[3].strokeDashArray = [5, 2]
tarta.slices[3].labelRadius = 1.75
tarta.slices[3].fontColor = colors.red
tarta.sideLabels = 1

d.add(tarta)

lenda = Legend()
lenda.x = 370
lenda.y = 0
lenda.dx = 8
lenda.dy = 8
lenda.fontName = 'Helvetica'
lenda.fontSize = 7
lenda.boxAnchor = 'n'
lenda.columnMaximum = 10
lenda.strokeWidth = 1
lenda.strokeColor = colors.black
lenda.autoXPadding = 5
lenda.yGap = 0
lenda.dxTextSpace = 5
lenda.alignment = 'right'
lenda.dividerLines = 1 | 2 | 3 | 4
lenda.dividerOffsY = 4.5
lenda.subCols.rpad = 30
lenda.deltax = 75
lenda.deltay = 10

colores = [colors.pink, colors.red, colors.green, colors.blue, colors.yellow]
for i , color in enumerate (colores):
    tarta.slices[i].fillColor = color

lenda.colorNamePairs = [(tarta.slices[i].fillColor,
                              (tarta.labels[i][0:20], '%0.2f' % tarta.data[i])
                               ) for i in range (len(tarta.data))]

d.add(lenda)

guion.append(d)
doc = SimpleDocTemplate("informeGraficos.pdf", pagesize=A4)

doc.build(guion)