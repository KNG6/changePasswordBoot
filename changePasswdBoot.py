#!/usr/bin/python3
#Create by KNG6
import smtplib,datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint
from os import system
from base64 import b64decode
from time import sleep

_version="1.0"

email=["",""]#list of people email whom the password will be send.
userToChange="username"#the target username whom the password will be modified.
userMail=""#address mail who send the mail.
userPass=b64decode("").decode("utf-8")#juste password encrypted in b64 (just not have the password in clear (not very secure, but better than nothing)).

#for logs more visual(idk if it's make sense in english ?).
bad="[-] "
good="[+] "

def genPasswd(length):#generate password
	charList=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","&","#","!","@","?","_"]#list of caractere for the password
	genPassword=""
	for i in range(int(length)):
		charChoice=randint(0,len(charList)-1)
		genPassword=genPassword+str(charList[charChoice])
	return genPassword

def sendMail(target,subject,content):#function for send email, with the email of the target, the subject of the mail, and the content(classic email).
	serveur = smtplib.SMTP("smtp.gmail.com", 587)
	msg = MIMEMultipart()
	msg['From'] = userMail
	msg['To'] = toSendMail
	msg['Subject'] = subject
	message=content
	msg.attach(MIMEText(message))
	serveur.starttls()
	serveur.login(userMail, userPass)
	serveur.sendmail(userMail, target, msg.as_string())
	serveur.quit()

def changePasswd(user,newPasswd):#function for change password of the user, need "screen" to be download on the PC target.
	system("screen -dmS passwdCh")
	sleep(0.5)
	system("screen -x passwdCh -X stuff \"passwd "+user+"\\n\"")
	sleep(0.5)
	system("screen -x passwdCh -X stuff \""+newPasswd+"\\n\"")
	sleep(0.5)
	system("screen -x passwdCh -X stuff \""+newPasswd+"\\n\"")
	sleep(0.5)
	system("screen -x passwdCh -X stuff \"exit\\n\"")

print(good+"Generate password.")
newPassword=genPasswd(15)#if you want change the length of the password it's here.
print(good+"Changing generate password.")
changePasswd(userToChange,newPassword)
Time=str(datetime.datetime.now().time().hour)+":"+str(datetime.datetime.now().time().minute)+":"+str(datetime.datetime.now().time().second)
Date=str(datetime.datetime.now().date())
textToSend="L'ordinateur 'PC' à été allumé a "+Time+" le "+Date+"\nMot de passe: "+newPassword#the content of the email it's here.
for person in email:
	print(good+"Sending email to: "+person+".")
	sendMail(person,"Nouveau mot de passe pour PC",textToSend)
