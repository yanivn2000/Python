###
#pip install fpdf
#pip install python-barcode
#pip install barcode
#pip install python-barcode[images]
#http://www.fpdf.org

#create barcodes gif: https://barcode.tec-it.com/en/UPCA
#gif to jpeg https://cloudconvert.com/

import os
from fpdf import FPDF

import barcode
from barcode.writer import ImageWriter
from barcode import EAN13

# save FPDF() class into a
# variable pdf
pdf = FPDF()
# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size = 15)

marketplace=input("Please enter marketplace name:")
address=input("Please enter shipping address:")
fileName=input("Please enter the csv file:")
f = open(fileName, "r")
list = []
for line in f:
  list.append(line.replace("\n","").split(','))

barcodePath="/Volumes/GoogleDrive/My Drive/Brands/Gifffted/barcodes_jpeg"
#mockup barcode
eanStr = "859123007362"
EAN = barcode.get_barcode_class('ean13')
ean = EAN(eanStr)
# or sure, to an actual file:
barcodeFileName='./test.jpeg'

stickerNumber=0
for i in range(len(list)):
    carton = 0
    # Add a page
    if(i == 0):
        continue
    for j in range(len(list[i])):
        if(list[0][j] == "Carton"):
            carton = int(list[i][j])
            totalCartons = carton
        if(list[0][j] == "Barcode"):
            barcodeNumber = list[i][j]

        if(carton != 0):
            for c in range(carton):
                if(stickerNumber % 3 == 0):#insear 3 stickers in one page
                    pdf.add_page()
                stickerNumber+=1

                lineOutput = f"Address: {address}"
                pdf.cell(200, 11, txt=(f"{lineOutput}"), ln=0, align='L')
                lineOutput = f"Marketplace: {marketplace}"
                pdf.cell(100, 11, txt=(f"{lineOutput}"), ln=0, align='L')

                #linePrint = 1
                for cBack in range(len(list[i])): #read all from begining
                    if(list[0][cBack] == "Carton"):
                        break
                    elif (list[0][cBack] == "ASIN"):  # truncate the name that can be large
                        lineOutput = f"{list[0][cBack]}: {list[i][cBack]}"
                        pdf.cell(100, 11, txt=(f"{lineOutput}"), ln=1, align='L')
                    elif (list[0][cBack] == "SKU"):  # truncate the name that can be large
                        lineOutput = f"{list[0][cBack]}: {list[i][cBack]}"
                        pdf.cell(100, 11, txt=(f"{lineOutput}"), ln=0, align='L')
                    elif (list[0][cBack] == "Barcode"): # truncate the name that can be large
                        lineOutput = f"{list[0][cBack]}: {list[i][cBack]}"
                        pdf.cell(100, 11, txt=(f"{lineOutput}"), ln=1, align='L')
                    elif (list[0][cBack] == "Name"):  # truncate the name that can be large
                        lineOutput = f"{list[0][cBack]}: {list[i][cBack]}"
                        pdf.cell(200, 11, txt=(f"{lineOutput}"), ln=1, align='L')
                    elif (list[0][cBack] == "Number of Units"):  # truncate the name that can be large
                        lineOutput = f"{list[0][cBack]}: {list[i][cBack]}"
                        pdf.cell(100, 11, txt=(f"{lineOutput}"), ln=0, align='L')

                    #linePrint += 1
                pdf.cell(100, 11, txt=(f"Carton No.: {carton} of {totalCartons}"),ln=1, align='L')
                #inseart empty line
                pdf.cell(100, 3, txt="", ln=1, align='L')
                #inseart the barcode
                pdf.image(barcodePath+"/"+barcodeNumber+".jpg", x=None, y=None, w=50, h=0, type='', link='')
                #inseart empty line
                if(stickerNumber % 3 != 0):#insert 3 stickers in one page
                    pdf.cell(200, 26, txt=(f"{'-' * 100}"), ln=1, align='L')

                # add upc
                carton-=1
                if(carton == 0):
                    break

# save the pdf with name .pdf
#os.remove(f"{marketplace}.pdf")
pdf.output(f"{marketplace}.pdf")


