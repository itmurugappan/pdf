from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("input.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

# Set password here
writer.encrypt("yourpassword")

# Save the protected file
with open("output_protected.pdf", "wb") as f:
    writer.write(f)
