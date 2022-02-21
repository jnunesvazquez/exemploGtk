import os.path
from reportlab.platypus import Paragraph,Image, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

elementos = []
follaEstilo = getSampleStyleSheet()

cabeceira = follaEstilo['Heading4']
cabeceira.pageBreakBefore = 0
cabeceira.keepWithNext = 0
cabeceira.backColor = colors.cornsilk

parragrafo = Paragraph("CABECEIRA DO DOCUMENTO", cabeceira)
elementos.append(parragrafo)

cadea = "Exemplo de utilización de ReportLab con Platypus. " * 500
corpo = follaEstilo['BodyText']
parragrafo2 = Paragraph(cadea, corpo)
elementos.append(parragrafo2)
elementos.append(Spacer(0, 20))

miImagen = Image(os.path.relpath("/home/oracle/Imaxes/captura.png"), width=325, height=223)
elementos.append(miImagen)

doc = SimpleDocTemplate("exemploPlatypus.pdf", pagesize=A4, showBoundary=0, author="Joel")
doc.build(elementos)