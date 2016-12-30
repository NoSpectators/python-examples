class Bobblehead(object):
	def __init__(self, bobbles): #creates instance of the class
		self.bobbles = bobbles

	def number_of_bobbles(self): #prints number of bobbles
		print 'number of bobbles =', self.bobbles

class Karthik(Bobblehead):
    def __init__(self, bobbles):
        self.bobbles = bobbles
    def print_unique_to_Karthik(self):
        print 'this works only in Karthik class'
    
numberBobs = Bobblehead(3) #set instance of Bobblehead to numberBobs
numberBobs.number_of_bobbles() #from class numberBobs get function number_of_bobbles

numberBobs2 = Bobblehead(4) #create another instance of Bobblehead, set to numberBobs2
numberBobs2.number_of_bobbles() #from class numberBobs get function_number_of_bobbles

numberBob3 = Karthik(5)
numberBob3.number_of_bobbles()
numberBob3.print_unique_to_Karthik()

numberBob4 = Bobblehead(9)
numberBobs.print_unique_to_Karthik()