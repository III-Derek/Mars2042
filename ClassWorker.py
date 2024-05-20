import math

class Worker:
    def __init__(self):
        
        self.satisf=50
        self.ifSatisfied=1
        self.prodcty=0
        self.actulProdcty=0
        self.exptSal=0

    def calculateExptSal(self):
        #depends on essential resources etc
        return 0

    def calculateSatisf(self,actulSal):
        self.satisf += 2.5 * math.log(1.5 * actualSal / self.exptSal)
        if (self.satisf > 100) :
            self.satisf = 100
        if (self.satisf < 0) :
            self.satisf = 100

        if (self.satisf < 20) or (self.satisf = 20):
            ifSatisfied = 0

    def calculateProdcty(self):
        #...
        return 0

    def calculateActulProdcty(self):
        if (ifSatisfied = 0) :
            self.prodcty = 0
        else:
            self.actulProdcty = self.prodcty * (self.satisf / 50)
        
        

        
        

        

    

    

