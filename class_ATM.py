
class ATM:

    def __init__(self, bank_name,money):

        self.withdrawals_list = []
        self.bank_name = bank_name
        self.money = money


      

    def withdraw(self,request):    
        
		self.request = request
		i=0
		balence=request
		print "Welcome to " + self.bank_name
		print "Current balance =" +str(self.money)

		while self.request>0:
			if self.request>self.money :
				print ("le montant n'existe pas en ATM")
				break
			else :
				
				liste=[100,50,10,5,4,3,2,1]
				if self.request>=liste[i] :
					d=self.request
					self.request-=liste[i]
					print "give " +str(d-self.request)
				else :	
					i+=1
		self.withdrawals_list.append(request)			
            

    def show_withdrawals(self):	
		for withdrawal in self.withdrawals_list:
			print (withdrawal)  


	
		

atm1 = ATM("Smart Bank",500)
atm2 = ATM("Baraka Bank",1000)
atm1.withdraw(277)
atm1.withdraw(300)
atm1.withdraw(400)
atm1.show_withdrawals()
print "======================================="	
atm2.withdraw(500)		
		