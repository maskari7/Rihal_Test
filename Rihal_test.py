from PIL import Image 
import pytesseract 
from pdf2image import convert_from_path 
import re 
import os
import sys 

  
pdf_file = 'Rihal - Software Developer Test.pdf'

  
''' 
Part #1 : Converting PDF to images 
'''
  

pages = convert_from_path(pdf_file, 300) 
  
image_counter = 1
  

for page in pages: 

    filename = "page_"+str(image_counter)+".png"    
    page.save(filename, 'PNG')  
    image_counter = image_counter +1
  
''' 
Part #2 - Recognizing text from the images using OCR 
'''
    
page_limit = image_counter -1  
 
with open('OCR_Output.txt','w')as outfile:
    for i in range(2, page_limit + 1): 
        filename = "page_"+str(i)+".png"  
        text = str(((pytesseract.image_to_string(Image.open(filename)))))  
        text = text.replace('-\n', '')      
        outfile.write(text)
outfile.close()

''' 
Part #3 - Extractin text from the text file using REGEX 
'''
date =r'(\d{1,2}).(\d{1,2}).\d{2}(\d{2})?'
s_n = r'\d{3}\-\d{3}\-\d{3}-\d{3}'
city =r'from ([A-Z]\w*)'
age = r'\d(\.\d)? [A-Za-z]* old'
name =r'is ([A-Z]\w*)'
san="\\2/\\1/\\3"

new_date = re.sub(date, san, text, 0, re.MULTILINE)

print('Dates:')
for match in (re.finditer(date, new_date, re.MULTILINE)):
    
    print (match.group())
    
    
print('\nThe Serial Numbers:')
for num, match in enumerate(re.finditer(s_n, text, re.MULTILINE), start=1):
    
    print ("Serial Number {num}: {match}".format(num = num, match = match.group()))
    
    
print('\nCats Name:')
for match in (re.finditer(name, text, re.MULTILINE)):
    
    print (match.group(1))
    
    
print('\nCats Age:')
for  match in (re.finditer(age, text, re.MULTILINE)):
    
    print (match.group())
    
    
print('\nThe Cities:')    
for match in (re.finditer(city, text, re.MULTILINE)):
    
    print (match.group(1))
