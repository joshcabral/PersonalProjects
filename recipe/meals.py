import pandas as pd
import smtplib
import random

days = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wendsday", 4:"Thursday", 5:"Friday", 6:"Saturday"}

print("starting")
df = pd.read_excel("recipes.xlsx")

recipes = {}
## create list
## onFriday should b 5 if it cannot b eaten on friday
for index, row in df.iterrows():
	recipes[row['dish']] = [row['dish'], row['type'], row['onFriday'], row['time'], row['ingredients']]
print('past0')
food = []
ingredients = []
for i in range(4):
	dish, info  = random.choice(list(recipes.items()))
	#if len(food) !=0:
	'''
		while food[-1][1] != info[1] or i%7 == int(info[2]):
			dish, info  = random.choice(list(recipes.items()))
	'''
	food.append(info)
	items = info[-1].split(", ")

	ingredients += items
	del recipes[dish]
	
print('past1')
ingredients = list(set(ingredients))
d = pd.read_excel("food.xlsx")
d['item'] = d['item'].astype('str') 
d['type'] = d['type'].astype('str') 
items = []
for i in ingredients:
	items.append([d.loc[d.item == i,'type'].to_string()[5:],i])
#items.sort(key=lambda x: x[0])
## Dividing items up 
## add fish, spices, 
fruits = [x[1] for x in items if (x[0] == 'fruit')]
veggie = [x[1] for x in items if (x[0] == 'vegetable')]
frozen = [x[1] for x in items if (x[0] == 'frozen') ]
meats = [x[1] for x in items if (x[0] == 'meat')]
breads = [x[1] for x in items if (x[0] == 'bread') ]
other = [x[1] for x in items if (x[0] == 'other')]
cheese = [x[1] for x in items if (x[0] == 'cheese')]


## Send the email process
smtpObj = smtplib.SMTP('smtp.cox.net', 587)
print(smtpObj.ehlo())
print(smtpObj.starttls())

smtpObj.login('', '')
emailString = "Subject: Dinner\n"
emailString += "Dear Josh,\n\n"
for i in range(4):
	emailString += days[i%7]+ ": "+food[i][0]+ ", Cook Time:  "+str(food[i][3]) +'\n'+'\n'
emailString +="Your shopping list:\n" 
emailString +="Fruits: "+', '.join(fruits) +'\n'
emailString +="Vegetables: "+', '.join(veggie)+'\n'
emailString +="Frozen Foods: "+', '.join(frozen)+'\n'
emailString +="Meats: "+', '.join(meats)+'\n'
emailString +="Cheese: "+', '.join(cheese)+'\n'
emailString +="Others: "+', '.join(other)+'\n'
print(emailString)
smtpObj.sendmail('', '', emailString)

smtpObj.quit()
