# Bank-email-generators
Generating possible emails of bank executives given a spreadsheet of 6000banks and key executives. Then automatically sending them emails for a survey.
The excel file 'bank_names.xlsx' contains the names of about 6000 banks with some key executives names.
The main aim is to generate possible emails with that information and automatically send out surveys. 

In order to do so, we need the domain name of each bank, which is exactly what 'bank_email_format_finder.py.' It uses different search engines search urls\
then parses the html page to find the first email on the page, which is likely one of the emails of the bank.

Then, the main program uses the function from the previous program to generate the emails, using the excel file of bank names and executive names. It
then saves the generated emails in another excel file called "emails_of_bankers.xlsx"
