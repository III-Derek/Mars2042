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
        '''

        :param chara_stats: must be a dictionary
        '''
        self.money = chara_stats['Money']
        self.number_of_workers = chara_stats['Number of Workers']
        self.credit_score = chara_stats['Credit Score']
        self.esse_res = chara_stats['Essential Resources']
        self.mine_res = chara_stats['Mining Resources']

    def update(self, update_item, update_num):
        '''
        update_item: String and  any of {money, number_of_workers,
        credit_score, any itme in esse_res, any item in minging resouces}
        update_num: Float
        updates the
        :return: None
        '''
        if isinstance(update_item, float) == 0:
            raise TypeError('not a number')



        esse_res_list = []
        for key, values in esse_resources: esse_res_list.append(key)
        mine_res_list = []
        for key, values in mining_resources: mine_res_list
        if update_item == 'money':
            self.money = update_num
        elif update_item == 'number_of_workers':
            self.number_of_workers = update_num
        elif any(esse_res_list):
            self.esse_res[update_item] = update_num
        elif any(mine_res_list):
            self.mine_res[update_item] = update_num
        else:
            raise ValueError('invalid value')


        return None

player1 = Player(chara_stats)
player1.money = 12
player1.esse_res['oxygen'] = 12
print(f'money of player 1: {player1.money}')
print(f'oxygen of player 1: {player1.esse_res["oxygen"]}')