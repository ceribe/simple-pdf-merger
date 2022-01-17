from PyPDF2 import PdfFileMerger
import os
from pathlib import Path

#Get all files in current dir
files = Path(".").iterdir()

#Sorting by date modified
#files = sorted(files, key=os.path.getmtime)

#Sorting by name
files = sorted(files, key=os.path.basename)

#Change paths to strings
files = map(os.path.basename, files)

#Filter out non-pdf files
pdfs = filter(lambda n : n.endswith(".pdf"), files)

#Merge pdfs
merger = PdfFileMerger()
for pdf in pdfs:
    merger.append(pdf)
merger.write("Merged.pdf")
merger.close()
