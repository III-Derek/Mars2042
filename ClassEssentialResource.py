EssentialResourcesFields={
    "name" = ""
    "amount" = 0
    "price" = 0
    "generation" = 0
    "consumption" = 0
    }

class EssentialResource:
    def __init__(self,EssentialResourcesFields):
        self.name = EssentialResourcesFields["name"]
        self.amount = EssentialResourcesFields["amount"]
        self.price = EssentialResourcesFields["price"]
        self.generation = EssentialResourcesFields["generation"]
        self.consumption  = EssentialResourcesFields["consumption"]

    def update(self, update_item, update_num):
        '''
        update_item: String and  any of {name, amount,
        price, generation, consumption}
        update_num: Float
        '''

        if update_item == "amount":
            self.amount = update_num
        elif update_item == "price":
            self.amount = update_num
        elif update_item == "generation":
            self.amount = update_num
        elif update_item == "consumption":
            self.amount = update_num
        else:
            raise ValueError('invalid value')

EletricityFields={
    "name" = "electricity"
    "amount" = 10
    "price" = 0
    "generation" = 0
    "consumption" = 0
    }
electricity = EssentialResource(EletricityFields)

WaterFields={
    "name" = "water"
    "amount" = 10
    "price" = 0
    "generation" = 0
    "consumption" = 0
    }
water = EssentialResource(WaterFields)

FoodFields={
    "name" = "food"
    "amount" = 10
    "price" = 0
    "generation" = 0
    "consumption" = 0
    }
food = EssentialResource(FoodFields)

OxygenFields={
    "name" = "food"
    "amount" = 10
    "price" = 0
    "generation" = 0
    "consumption" = 0
    }
oxygen = EssentialResource(OxygenFields)

