import ezdxf
from ezdxf.addons.drawing import Frontend, RenderContext
from ezdxf.addons.drawing import layout, pymupdf
import os
from pypdf import PdfMerger

from ezdxf.addons.drawing import layout, svg

target = "D:/py/dwg2pdf/target/"
result = "D:/py/dwg2pdf/result/"

ezdxf.addons.drawing.properties.MODEL_SPACE_BG_COLOR = "#FFFFFF"

#PDF creation
file_names = []
file_paths = []
for file in os.listdir(target):
    file_names.append(file.split(" ")[0])
    file_paths.append(target + file)

for i, file_path in enumerate(file_paths):
    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()
    backend = pymupdf.PyMuPdfBackend()
    Frontend(RenderContext(doc), backend).draw_layout(msp)
    res_file = result+file_names[i]+".pdf"
    with open(res_file, "wb") as fp:
        fp.write(backend.get_pdf_bytes(layout.Page(0, 0)))
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