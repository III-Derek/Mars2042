import math
import ClassEssentialResources

class Worker:
    def __init__(self,name):
        """
        name: str. 
        fields info see below
        """
        self.name=name  
        self.population = 0 #int>=0
        self.satisf = 50 #float, between 0 and 100
        self.ifSatisfied= 1 #bool, becomes 0 if satisf<20
        self.prodcty= 0 #float
        self.actulProdcty= 0 #float
        self.exptSal= 0 #float

    def getName():
        #print name of the worker.
        print(self.name)
    
    def updateExptSal(self):
        #update and return expected salary.
        #expected salary depends on prices of electricity, water and food linearly.
        k1 = 1 # to be determined
        k2 = 1
        k3 = 1
        self.exptSal =  k1 * ClassEssentialResources.ElectricityFields["price"] +
        k2 * ClassEssentialResources.WaterFields["price"] +
        k3 * ClassEssentialResources.FoodFields["price"] 
    
        return self.exptSal

    def updateSatisf(self):
        #update and return satisfaction based on ratio of actual salary and expected salary.
        #formula: current satisfaction + $f\left(x\right)=7\arctan\left(\log_{3}1.2x\right)$; x=actualSal/self.exptSal 
        #f(0.83)=0, f(1)=1.15, f(2)=4.71, f(3)=6.03, f(0.5)=-3.05, f(0.33)=-4.87, f(0)=-3.5pi
        
        if (actualSal / self.exptSal > 0) :
            self.satisf += 7 * math.atan(math.log(1.2 * actualSal / self.exptSal , a)) 
        if (actualSal / self.exptSal = 0) :
            self.satisf -= -3.5 * math.pi
        
        if (self.satisf > 100) : 
            self.satisf = 100
        if (self.satisf < 0) :
            self.satisf = 0

        if (self.satisf < 20) :
            ifSatisfied = 0
        
        return self.satisf 

    def updateProdcty(self):
        #...
        return self.prodcty

    def updateActulProdcty(self):
        #update and return actual productivity.
        #formula: self.prodcty * (self.satisf / 50) if ifSatisfied=1; else 0.
        
        if (ifSatisfied = 0) :
            self.prodcty = 0
            print(WORKERS ON STRIKE!)
        else:
            self.actulProdcty = self.prodcty * (self.satisf / 50)

        return self.actulProdcty
        

        
        

        

    

    

