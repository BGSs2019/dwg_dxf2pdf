# The following code sample demonstrates how to convert a DWG file to a PDF document using Python.
import aspose.cad as cad
import os
from pypdf import PdfMerger

# Initialize and specify CAD options
rasterizationOptions = cad.imageoptions.CadRasterizationOptions()
#rasterizationOptions.page_width = 297
#rasterizationOptions.page_height = 210
rasterizationOptions.layouts = ["Model"]

# Specify PDF Options
pdfOptions = cad.imageoptions.PdfOptions()
pdfOptions.vector_rasterization_options = rasterizationOptions

target = "C:/Users/BobrovGS/Downloads/dwg2pdf/target/"
result = "C:/Users/BobrovGS/Downloads/dwg2pdf/result/"

#PDF creation
file_names = []
file_paths = []
for file in os.listdir(target):
    file_names.append(file.split(" ")[0])
    file_paths.append(target + file)

for i, file_path in enumerate(file_paths):
    image = cad.Image.load(file_path)
    res_file = result+file_names[i]+".pdf"
    image.save(res_file, pdfOptions)
    print(res_file)
    print("PDF ready " + str(i+1) + "/" + str(len(file_names)))

print("PDFs creation completed!")

#PDF merging

pdf_names = []
numeric_names = []
pdf_paths = []
merger = PdfMerger()
res_pdf_file = result+"output"+".pdf"

for pdf in os.listdir(result):
    pdf_names.append(pdf.split(" ")[0])

for name in pdf_names:
    numeric_names.append(int(name.split(".")[0]))

numeric_names = sorted(numeric_names)

for name in numeric_names:
    pdf_paths.append(result + str(name) + ".pdf")
print(pdf_paths)

for i, pdf_path in enumerate(pdf_paths):
    print(pdf_path)
    merger.append(pdf_path)
    print("ready " + str(i+1) + "/" + str(len(pdf_names)))

merger.write(res_pdf_file)
merger.close()