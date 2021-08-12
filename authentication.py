import pickle

sender="nightfury4653@gmail.com"
password = "Ambition@gmail18"

authentication = [sender,password]

with open("authentication.pickle",'wb') as f:
	pickle.dump(authentication,f)