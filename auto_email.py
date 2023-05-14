import pyautogui
import time
import openpyxl as ox

compose_image = 'compose.png'
subject_image = 'subject.png'
send_image = 'send.png'

pos_compose_image = pyautogui.locateOnScreen(compose_image, confidence = 0.90)

def send_email(pos_compose_image, email, text, subject):
    try:
        if pos_compose_image is not None:
            pyautogui.click(pos_compose_image)
            time.sleep(3)
            pyautogui.moveTo((10,10), duration = 0.5)
            pyautogui.write(email)
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(3)
            pos_subject_image = pyautogui.locateOnScreen(subject_image, confidence = 0.90)
            pyautogui.click(pos_subject_image)
            pyautogui.write(subject)
            time.sleep(3)
            x, y, width, height = pos_subject_image
            pyautogui.click(x + 20, y + 100)
            time.sleep(2)
            pyautogui.write(text)
            time.sleep(3)
            pos_send_image = pyautogui.locateOnScreen(send_image, confidence = 0.90)
            pyautogui.click(pos_send_image)
            time.sleep(2)
            
            

    except Exception as e:
        print(f'An error occured {e}')
    
wb = ox.load_workbook('emails_of_bankers.xlsx')
sheet = wb["Sheet"]
stop = False
iterator = 1
emails = []
while not stop:
    email_1 = sheet["B" + str(iterator)].value
    email_2 = sheet["C" + str(iterator)].value
    emails.append(email_1)
    emails.append(email_2)
    iterator += 1
    if email_1 is None and email_2 is None:
        stop = True
    
    
file1 = open("email_content.txt")
message = file1.read()
file2 = open("email_subject.txt")
subject = file2.read()
file1.close()
file2.close()

for email in emails:
    send_email(pos_compose_image, email, message, subject)
