from pypdf import PdfReader
import os

path = r"C:\Users\ACER\Desktop\space.pdf"

print(os.path.exists(path))

reader = PdfReader(path)

number_of_pages = len(reader.pages)

# print(number_of_pages)
# page = reader.pages[5]   # first page

# text = page.extract_text()
num, num1 = map(int, input("enter").split())
full_text = path

for page in reader.pages:
    full_text += page.extract_text()

print(full_text[num:num1])

