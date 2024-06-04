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
        update: update the update_item with the corresponding update_num
        update_item: String and  any of {money, number_of_workers,
        credit_score, any itme in esse_res, any item in minging resouces}
        update_num: Float
        
        return: None
        '''
        if isinstance(update_item, float) == 0:
            raise TypeError('Invalid Update Number')



        esse_res_list = []
        for key, values in esse_resources: esse_res_list.append(key)
        mine_res_list = []
        for key, values in mining_resources: mine_res_list
        if update_item == 'Money':
            self.money = update_num
        elif update_item == 'Number of Workers':
            self.number_of_workers = update_num
        elif update_item in esse_res_list:
            self.esse_res[update_item] = update_num
        elif update_item in mine_res_list:
            self.mine_res[update_item] = update_num
        else:
            raise ValueError('Invalid Update Item')


        return None
    
    def input(self):
        '''
        input: Asks the users for two inputs, the item that user want to update,
        and the amount of the corresponding item that the user want to update. In 
        addition, we want to check whether the user input is one of the valid_items
        and whether user_num is a valid number 

        return: an array where the first is user_item of type String, and the second
        is user_num, of type Float
        '''
        # 
        valid_items = ['water', 'food', 'oxygen', 'electricity','silicon',
                       'iron', 'magnesium', 'aluminium', 'calcium', 'potassium']
        user_item = input("Please enter the item you wish to update: ")
        while user_item not in valid_items: 
            user_item = input("Please enter the item you wish to update: ")
        
        valid_nums = [' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        user_num = input("Please enter the amount of the item you want: ")
        user_num_separated = []
        for str in user_num:
            user_num_separated.append(str)
        
        user_num_check = []
        for str in user_num_separated:
            if str not in valid_nums:
                user_num_check.append(1)
        
        while sum(user_num_check) != 0:
            user_num = input("Please enter the amount of the item you want: ")
            user_num_check = []
            user_num_separated = []
            for str in user_num:
                user_num_separated.append(str)
            
            for str in user_num_separated:
                if str not in valid_nums:
                    user_num_check.append(1)
                
        
        
        
        return [user_item,user_num]
player1 = Player(chara_stats)
player1.money = 12
player1.esse_res['oxygen'] = 12
print(f'money of player 1: {player1.money}')
print(f'oxygen of player 1: {player1.esse_res["oxygen"]}')