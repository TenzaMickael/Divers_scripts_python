# Extraire le texte des fichiers PDFS

from PyPDF2 import PdfFileWriter, PdfFileReader

f = open("/home/micka/Python_udemy/5_Parcours/1_Les_Scripts_d_Automatisation/3_PAGES_PDF/RESSOURCES/11_Recap.pdf", "rb")
reader = PdfFileReader(f)

page0 = reader.getPage(1)
texte = page0.extractText()

texte = texte.replace("Ò", "").replace("‘","è").replace("‹","à").replace("”","é").replace("Õ","'").replace("’","ê")
f.close()

print(texte)