import PyPDF2
import re, pyperclip

# creating a pdf file object
pdfFileObj = open('orbis.pdf', 'rb')

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
text = my_text.replace("\n", "")

# searching and copying to clipboard
more_data = re.search('MORE(.*) \$', text).group(1)
pyperclip.copy('MORE' + more_data + ' $')

# mtext = more_data.finditer(text)
# print(mtext)

# for m in mtext:
#     print(m)



# text = my_text

# try:
#     found = re.search('MORE credit (.*?) $', text).group(1)
# except AttributeError:
#     # AAA, ZZZ not found in the original string
#     found = 'kupa' # apply your error handling

# print(found)

# s = my_text
# result = re.search('MORE (.*) $', s)
# print(result.group(1))