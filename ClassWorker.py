import math
import ClassEssentialResources


WorkStats= {
    "satisfaction" = 50
    "ifSatisfied" = 1
    "productivity" = 10
    "actualProductivity" = 0
    "expectedSalary" = 0
}

class Worker:
    def __init__(self,name,WorkStats):
        self.name=name
        self.satisf = WorkStats["satisfaction"]
        self.ifSatisfied=WorkStats["ifSatisfied"]
        self.prodcty=WorkStats["productivity"]
        self.actulProdcty=WorkStats["actualProductivity"]
        self.exptSal=WorkStats["expectedSalary"]

    def getName():
        print(self.name)
    
    def updateExptSal(self):
        #depends on prices of electricity, weter and food linearly
        k1 = 1 # to be determined
        k2 = 1
        k3 = 1
        self.exptSal =  k1 * ClassEssentialResources.ElectricityFields["price"] +
        k2 * ClassEssentialResources.WaterFields["price"] +
        k3 * ClassEssentialResources.FoodFields["price"] 
    
        return self.exptSal

    def updateSatisf(self,actulSal):
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
        
        return self.satisf 

    def updateProdcty(self):
        #...
        return self.prodcty

    def updateActulProdcty(self):
        if (ifSatisfied = 0) :
            self.prodcty = 0
        else:
            self.actulProdcty = self.prodcty * (self.satisf / 50)

        return self.actulProdcty
        

        
        

        

    

    

