from reportlab.pdfgen import canvas

frase = ["El patio de mi casa", "es particular", "cuando llueve se moja", "como los demas"]

documento = canvas.Canvas("documentoTexto.pdf")

obxTexto = documento.beginText()
obxTexto.setTextOrigin(20, 600)
obxTexto.setFont("Courier", 14)
for linea in frase:
    obxTexto.textLine(linea)

obxTexto.setFillGray(0.5)
lineasTexto = '''
Este es un texto multilinea
que va en un comentario y
lo vamos a escribir con Python y
Reportlab
'''

obxTexto.textLines(lineasTexto)

for tipoLetra in documento.getAvailableFonts():
    obxTexto.setFont(tipoLetra, 12)
    obxTexto.textLine(tipoLetra + ": " + frase[2])

obxTexto.setFont("Helvetica", 14)

for linea in frase:
    obxTexto.textOut(linea)
    obxTexto.moveCursor(20, 15)

obxTexto.setWordSpace(8)
obxTexto.textLines(lineasTexto)

espazo = 0
for n, linea in enumerate(frase):
    obxTexto.setCharSpace(espazo)
    obxTexto.textLine(linea)
    espazo = n + 1

documento.drawText(obxTexto)
documento.showPage()
documento.save()