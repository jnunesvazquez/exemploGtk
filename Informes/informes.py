from reportlab.pdfgen import canvas

lenzo = canvas.Canvas("documento.pdf")
lenzo.drawString(0,0,"Posicion inicial=(0,0)")
lenzo.drawString(50,150,"Posicion inicial=(50,150)")
lenzo.drawString(200,50,"Posicion inicial=(200,50)")

lenzo.drawImage("/home/oracle/Imaxes/captura.png", 300, 300, 300, 150)

lenzo.showPage()
lenzo.save()