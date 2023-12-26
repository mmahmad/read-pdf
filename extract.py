import PyPDF2
import re


# Open the PDF file
with open('radiology_procedure_codes.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
   
    # Number of pages in the PDF
    num_pages = len(reader.pages)

    final_codes = []

    # Read each page
    for page in range(num_pages):
        page_obj = reader.pages[page]
        text = page_obj.extract_text()

        # Regular expression to match procedure codes
        pattern = r'^\d+'

        # Find all occurrences of the pattern
        procedure_codes = re.findall(pattern, text, re.MULTILINE)

        # Add the codes to the final list
        final_codes.extend(procedure_codes)

    # Remove duplicates
    remove_duplicates = set(final_codes)

    # Print the codes
    print(remove_duplicates)
    
    # Print the number of codes
    print(len(remove_duplicates))