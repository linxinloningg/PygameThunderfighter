class GameStats():
    """追踪游戏的统计信息"""
    def __init__(self,ship_settings):
        """初始化统计信息"""
        # 游戏刚启动时处于活动状态
        self.game_active =False
        self.ship_settings = ship_settings

        #最高得分
        self.high_score = 0


        ### 每当玩家开始新游戏的时候，需要重置一些统计信息，创建reset_stats进行重置
        ### 每当创建gamestats实例时也调用函数进行某些信息的重置
        self.reset_stats()
        
        


    def reset_stats(self):
        """初始化在游戏期间可能变化的统计信息"""
        #飞船生命
        self.ships_left = self.ship_settings.limit
        #得分
        self.score = 0
        #太阳数量
        self.sun_number = 50
        #等级
        self.level = 1
        #缓存的大招
        self.trick = 1
        self.trick_flag = True
        #初始化的飞船
        self.ship = "Peashooter"

    def check_high_score(self):
        """检测并更新最高分 """
        if self.score > self.high_score :
            self.high_score = self.score

    def check_level(self):

        """ 更换游戏等级"""
        if self.score >= 5000 and self.score <15000:
            self.level = 2
        elif self.score >= 15000 and self.score <30000:
            self.level = 3
        elif self.score >= 30000 and self.score <50000:
            self.level = 4
        elif self.score >= 50000 and self.score <750000:
            self.level = 5

