import PyPDF2
import re, pyperclip

# creating a pdf file object
pdfFileObj = open('atradius.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
# print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
my_text = pageObj.extractText()
# print(my_text)

# closing the pdf file object
pdfFileObj.close()

# converting multiline string to one line
text = my_text.replace("\n", " ")
# print(text)

# searching and copying to clipboard
atr_data = re.search('Your Credit(.*) Yours faithfully', text).group(1)
pyperclip.copy('Your Credit' + atr_data)