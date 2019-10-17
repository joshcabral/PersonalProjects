import random
import smtplib
import time
#smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
def filter(a,b):
    return True


#ending = '@g.hmc.edu'
'''
def sendEmail(a,b):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()

    to = emails[a] + ending
    message = """From: 
    To: {0} <{1}>
    Subject: Secret Santa Pairing
    Hello {0}, 
    This year you are paired with {2}. Please check the speadsheet for gift ideas. Merry Christmas!

    """.format(a, to, b)
    x = smtpObj.sendmail('', to, message)# "Subject: Hello\n\nHere is you're secret santa pairing. " + a + " you have " + b)
    print(x)
    print("Done!")
    print(message)
    print(to)
    smtpObj.quit()
#sendEmail("Josh", "Taylor")

'''
def createPairs():
    random.shuffle(recievers)
    random.shuffle(givers)
    #print(recievers)
    #print(givers)
    #print(recievers1)
    random.shuffle(recievers)
    i = 0
    pairs = {}
    l = len(givers) -1
    while recievers:

        currentReciever = recievers.pop()
        #print(i)
        currentGiver = givers[i]
        #print("Rec" + currentReciever )
        #print("giv" +  currentGiver)
        if filter(currentGiver, currentReciever):
            pairs[currentGiver] = currentReciever
            i += 1
        else:
            if i == l:
                pairs = {}
                i = 0
                recievers = names.copy()
            else:
                recievers.append(currentReciever)
            
        random.shuffle(recievers)
        #print(pairs)
        #time.sleep(.5)
    return pairs

def main():
    pairs = createPairs()
    #print(pairs)
    #d1 = {}
    #d2 = {}
    #i = 0 
    for key, value in pairs.items():
        print("Giver: " + key + ", Receiver: " + value + "\n")

    '''
    #f= open("taylor.txt","w+")
    #f.write(str(d1))
    #f.close()

    #f= open("josh.txt","w+")
    #f.write(str(d2))
    #f.close()
        #print(key +' : ' + value)

        #sendEmail("", value)

#print(createPairs()) 
main()


