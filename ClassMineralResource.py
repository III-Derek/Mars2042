MineralResourcesFields={
    "name" = ""
    "amount" = 0
    "price" = 0
    "generation" = 0
    "consumption" = 0
    }

class MineralResource:
    def __init__(self,EssentialResourcesFields):
        self.name = MineralResourcesFields["name"]
        self.amount = MineralResourcesFields["amount"]
        self.price = MineralResourcesFields["price"]
        self.generation = MineralResourcesFields["generation"]
        self.consumption  = MineralResourcesFields["consumption"]

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


SiliconFields={
    "name" = "silicon"
    "amount" = 0
    "price" = 0
    "generation" = 0
    "consumption" = 0
    }
silicon = MineralResource(SiliconFields)

IronFields={
    "name" = "iron"
    "amount" = 0
    "price" = 0
    "generation" = 0
    "consumption" = 0
    }
iron = MineralResource(IronFields)

MagnesiumFields={
    "name" = "magnesium"
    "amount" = 0
    "price" = 0
    "generation" = 0
    "consumption" = 0
    }
magnesium = MineralResource(MagnesiumFields)

AluminiumFields={
    "name" = "aluminium"
    "amount" = 0
    "price" = 0
    "generation" = 0
    "consumption" = 0
    }
aluminium = MineralResource(AluminiumFields)

CalciumFields={
    "name" = "calcium"
    "amount" = 0
    "price" = 0
    "generation" = 0
    "consumption" = 0
    }
calcium = MineralResource(CalciumFields)

PotassiumFields={
    "name" = "potassium"
    "amount" = 0
    "price" = 0
    "generation" = 0
    "consumption" = 0
    }
potassium = MineralResource(PotassiumFields)
