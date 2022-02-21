from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

PAGE_HEIGHT = A4[1]
PAGE_WIDTH = A4[0]

estilos = getSampleStyleSheet()
titulo = "Exemplo inicial"
pageinfo = "Exemplo platypus"

def primeriraPaxina (canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold', 16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-55, titulo)
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(mm, 2 * mm, "Paxina %d %s" % (doc.page, pageinfo))
    canvas.restoreState()

def paxinasPosteriores (canvas, doc):
    canvas.saveState()
    canvas.setFillGray(0.2, 0.5)
    canvas.setFont('Times-Bold', 32)
    canvas.drawCentredString(PAGE_WIDTH / 2.0, PAGE_HEIGHT/2, titulo)
    canvas.drawImage("/home/oracle/Imaxes/captura.png", 20, PAGE_HEIGHT-40, 500, 100)
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(mm, 2 * mm, "Paxina %d %s" % (doc.page, pageinfo))
    canvas.restoreState()

def contido():
    doc = SimpleDocTemplate("exemploPortadaDePaxina.pdf")
    elementos = [Spacer(2, 2 * mm)]
    estilo = estilos['Normal']
    for i in range (100):
        texto = ("Este é o parragrafo número %s. " % i) * 20
        parragrafo = Paragraph(texto, estilo)
        elementos.append(parragrafo)
        elementos.append(Spacer(2, 2 * mm))
    doc.build(elementos, onFirstPage=primeriraPaxina, onLaterPages=paxinasPosteriores)

contido()