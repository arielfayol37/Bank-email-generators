
import re, openpyxl, os
from bank_email_formats_finder import find_bank_domain
import time
    
##Generating possible local part of people's emails using their first and last names
def gen_emails(people_string, extension, format ='f1'):
    people_list = people_string.split("; ")
    error = 0
    # Initialize empty list to hold email addresses
    emails = []
    names = []

    # Iterate through the list of people
    for person in people_list:
      # Check if person is a board member
        if "Board" in person:
            continue
      # Use regular expression to extract first and last names
        match = re.search(r'([\s\w-]*), ([\s\w-]*)', person)
        
        try:
            match1, match2 = match.group(1).strip(), match.group(2).strip()
            names.append(match1 + ' '+ match2)
            if format == 'f1':
                
                first_name = ''.join(match2.split())
                last_name = ''.join(match1.split())
              # Generate email address and append to list
                email = f"{first_name}.{last_name}@{extension}"
                emails.append(email)
            elif format == 'f2':
                first_initial = match2[0]
                last_name = ''.join(match1.split())
              # Generate email address and append to list
                email = f"{first_initial}{last_name}@{extension}"
                emails.append(email)                
        except:
            error+=1
    
    return (names, emails, error)

filename = 'bank_names_and_executives.xlsx' #Excel file containing a list of banks, their capital, and executive members
wb = openpyxl.load_workbook(filename)
sheet = wb['Screening'] #this is the sheet with the information we need
new_wb = openpyxl.Workbook()
filename2 = 'emails_of_bankers.xlsx' #excel file where we will save our newly generated emails
sheet2 = new_wb['Sheet']
num_cells = 6065 
cell_2_num = 2
total_errors1 = 0
total_errors2 = 0
counter = 0
for i in range(9, num_cells):
    if (counter+1)%300==0:
        time.sleep(1000)
    counter += 1
    print(counter)
    bank_name = sheet['A' + str(i)].value
    bank_capital = sheet['D' + str(i)].value 
    extension,search_url = find_bank_domain(bank_name)
    if extension is not None:
        people_names = sheet["I" + str(i)].value 
        names1, emails1, error1 = gen_emails(people_names,  f'{extension}', 'f1')
        names2,emails2, error2 = gen_emails(people_names,  f'{extension}', 'f2')
        total_errors1 += error1
        total_errors2 += error2
        for name,email1,email2 in zip(names1,emails1, emails2):
            sheet2["A"+str(cell_2_num)].value = name
            sheet2["B"+str(cell_2_num)].value = email1
            sheet2["C"+str(cell_2_num)].value = email2
            sheet2['D'+str(cell_2_num)].value = bank_name
            sheet2['E'+str(cell_2_num)].value = bank_capital
            sheet2['F'+str(cell_2_num)].value = search_url
            
            cell_2_num += 1
        
    elif extension == -1:
        print(counter)
        
        break
    new_wb.save(filename2)
print(total_errors1)
print(total_errors2)

    
