import random
import smtplib
new = []
chores = ['folding_laundry', 'dishes_empty', 'dishes_load', 'inside_laundry', 'outside_Laundry', 'Bathroom', 'Dog_Food_and_Water', 'Dog_dodo', 'table', 'vacuum_living_room', 'vacuum_hallways', 'trash', 'kitchen_floor', 'counters']
EMAIL = ""
PASSWORD = ""
TO = ""
def sendMail(txt):
	smtpObj = smtplib.SMTP('smtp.cox.net', 587)
	smtpObj.login(EMAIL, PASSWORD)
	emailStr = "From: Chores\r\nSubject: Chores For today\r\n\r\n" + txt
	#print emailStr
	smtpObj.sendmail(EMAIL, TO, emailStr)
	smtpObj.quit()
def ran():
	txt = ''
	for i in chores:
		person = random.choice(new)
		n = random.randint(0,1)
		j =i + '-' + a
		print j
		txt += j +'\r\n '
	sendMail(txt)
	 
#__name__ == "__main__"
name = raw_input("Enter Kid Initials - No Spaces\n")
for c in name:
	new += c
ran()
	
