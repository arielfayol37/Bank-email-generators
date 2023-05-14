import re, openpyxl as ox

wb = ox.load_workbook('emails_bankers.xlsx')
regex = re.compile(r'(.{1,65}@.{1,65}?)\.(com|gov|org|bank).*')
sheet = wb["Sheet"]

def replace(string):
    regex_result = regex.search(string)
    try:
        return regex_result.groups()[0] + '.' + regex_result.groups()[1]
    except:
        return None

for i in range(2,1388):
    string1 = sheet['B'+str(i)].value
    string2 = sheet['C'+str(i)].value
    a = replace(str(string1))
    if a is not None:
        sheet['B'+str(i)].value = a
    b = replace(str(string2))
    if b is not None:
        sheet['C'+str(i)].value = b

wb.save('emails_gen.xlsx')
