'''
chara_stats:
    defines the initial character stats and updating it continuously
    based on player's performance
'''

esse_resources = {
    'water': 0,
    'food': 0,
    'electricity': 0,
    'oxygen':0,
}

mining_resources = {
    'silicon': 0,
    'iron': 0,
    'magnesium': 0,
    'aluminium': 0,
    'calcium': 0,
    'potassium': 0,
}

chara_stats = {
    'Money': 0,
    'Number of Workers': 0,
    'Credit Score': 0,
    'Essential Resources': esse_resources,
    'Mining Resources': mining_resources
}

class Player:
    '''
    This class updates the stats of the Player based on a set
     of initial conditions
    '''
    def __init__(self, chara_stats):
        self.money = chara_stats['Money']
        self.number_of_workers = chara_stats['Number of Workers']
        self.credit_score = chara_stats['Credit Score']
        self.esse_res = chara_stats['Essential Resources']
        self.mine_res = chara_stats['Mining Resources']




