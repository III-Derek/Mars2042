import math

WorkStats= {
    "satisfaction" = 50
    "ifSatisfied" = 1
    "productivity" = 0
    "actualProductivity" = 0
    "expectedSalary" = 0
}

class Worker:
    def __init__(self):
        
        self.satisf = WorkStats["satisfaction"]
        self.ifSatisfied=WorkStats["ifSatisfied"]
        self.prodcty=WorkStats["productivity"]
        self.actulProdcty=WorkStats["actualProductivity"]
        self.exptSal=WorkStats["expectedSalary"]

    def calculateExptSal(self):
        #depends on essential resources etc
        return 0

    def calculateSatisf(self,actulSal):
        #calculate using $f\left(x\right)=7\arctan\left(\log_{3}1.2x\right)$; x=actualSal/self.exptSal 
        #f(0.83)=0, f(1)=1.15, f(2)=4.71, f(3)=6.03, f(0.5)=-3.05, f(0.33)=-4.87, f(0)=-3.5pi
        if (actualSal / self.exptSal > 0) :
            self.satisf += 7 * math.atan(math.log(1.2 * actualSal / self.exptSal , a)) 
        if (actualSal / self.exptSal = 0) :
            self.satisf -= -3.5 * math.pi
        
        if (self.satisf > 100) : 
            self.satisf = 100
        if (self.satisf < 0) :
            self.satisf = 0

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
        
        

        
        

        

    

    

