

def withdraw(request):
	i=0
	liste=[100,50,10,5,4,3,2,1]
	for lis in liste:
		if request>=lis :
			request-=lis
			return request
		else :	
			i+=1
		
		


def atm(money,request):
	balence=request
	print "Current balance =" +str(money)

	while request>0:
		if request>money :
			print ("le montant n'existe pas en ATM")
			break
		else :
			d=request
			request=withdraw(request)	
			print "give " +str(d-request)

	return money-balence		

print atm(500,455)			
		