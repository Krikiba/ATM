

def withdraw(request):
	i=0
	liste=[100,50,10,5,4,3,2,1]
	while len(liste):
		if request>=liste[i] :
			request-=liste[i]
			return request
		else :	
			i+=1
		
		


def atm(money,request):
	print "Current balance =" +str(money)
	while request>0:
		if request>money :
			print ("le montant n'existe pas en ATM")
			break
		else :
			d=request
			request=withdraw(request)	
			print "give " +str(d-request)

atm(500,499)			
		