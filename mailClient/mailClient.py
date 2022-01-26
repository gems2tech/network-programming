import smtplib
from cryptography.fernet import Fernet
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart



with open ('/pathToFilekey/'+'filekey.key','rb') as filekey:
    key = filekey.read() 


with open('password.txt','rb') as enc_file:
    encrypted = enc_file.read()


f = Fernet(key)
decrypted = f.decrypt(encrypted)

password = decrypted.decode("utf-8")


msg = MIMEMultipart()
msg['From'] = 'myName'
msg['To'] = 'jzu19821@boofx.com' #10 min mail 
msg['Subject'] = 'Just A Test'

with open ('message.txt','r') as m:
    message = m.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'feld.jpg' # attachment file name 
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()

server = smtplib.SMTP('smtp.live.com', 25)
server.ehlo()
server.starttls()
server.login('example@hotmail.com', password)
server.sendmail('example@hotmail.com','jzu19821@boofx.com',text) #10 min mail
server.quit()
print("Mail sending successful")
