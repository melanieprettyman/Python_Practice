import PyPDF2
import sys

# Open pdf
with open('dummy.pdf', 'rb') as pdf:
    # read pdf
    reader = PyPDF2.PdfFileReader(pdf)
    # get the page obj
    page = reader.getPage(0)
    # roate the page
    page.rotateClockwise(90)
    # create a writer
    writer = PyPDF2.PdfFileWriter()
    # Add rotated page to writer
    writer.addPage(page)

    # Create a file in write mode and write the writer contents to file
    with open('tilt.pdf', 'wb') as output:
        writer.write(output)

# --Combine multiple pdf's--
# Read in the PFD's from cmdline and combine them into one

# inputs = sys.argv[1:]  # read in files from argv[1] to [end]


# Function to combine pdf's
def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')


# pdf_combiner(inputs)

# --Watermark each page in pdf file--
# template = PyPDF2.PdfFileReader(open('superduper.pdf', 'rb'))
# watermark = PyPDF2.PdfFileReader(open('water.pdf', 'rb'))
# output = PyPDF2.PdfFileWriter()
# This is the new way to do this:
template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

# for i in range(template.getNumPages()):
# New way to do this:
for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

with open('watermaked_output.pdf', 'wb') as outputFile:
    output.write(outputFile)