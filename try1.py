import os
import PyPDF2

from fpdf import FPDF
  
  
# save FPDF() class into a 
# variable pdf
pdf = FPDF()

# Add a page
pdf.add_page()

pdf.set_font("Arial", size = 15)

pdf.image("poza1.jpg",x=20,y=60,w=100,h=80)

pdf.cell(200, 10, txt = "Bine ai venit la targ", 
         ln = 1, align = 'C')
body1 = ["Cum te numesti?","Easy to use",
"It allows page format and margin","It allows to manage page header and footer"]
for sentence in body1:
    pdf.cell(200, 10, txt = sentence,
         ln = 2, align = 'A')
pdf.output("targ.pdf")   