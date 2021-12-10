import pygame.font

class Scoreboard():
    """显示信息的类"""

    def __init__(self,ai_settings,screen,stats):
        """ 初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #显示得分面板信息时使用的字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,24)

        #初始化得分图像
        self.prep_scoreboard()

        #初始化最高得分图像
        self.prep_high_scoreboard()

        #初始化等级图像
        self.prep_level()

        #初始化太阳数
        self.prep_sun()

        #初始化大招数量
        self.prep_trick()


    def prep_scoreboard(self):
        """将得分渲染成图像"""
        #调用font.render（）将存储在msg中的文本转换为图像，然后将该图像存储
        # 方法font.render()还接受一个布尔实参，该实参指定
        # 开启还是关闭反锯齿功能（反锯齿）
        #反锯齿让文本的边缘更平滑。余下的两个实参分别是文本颜色和背景色

        #使用字符串格式化命令，它让python将数值转换为字符串时并在其中加入逗号
        #输入1，000，000而不是1000000
        score = "SCORE : "+"{:,}".format((self.stats.score))

        self.score_image = self.font.render(score,False,self.text_color,self.ai_settings.bg_color)

        self.score_rect = self.score_image.get_rect()

        self.score_rect.right = self.screen_rect.right 

        self.score_rect.top   = self.screen_rect.top    


    def prep_high_scoreboard(self):
        """将得分渲染成图像"""
        #调用font.render（）将存储在msg中的文本转换为图像，然后将该图像存储
        # 方法font.render()还接受一个布尔实参，该实参指定
        # 开启还是关闭反锯齿功能（反锯齿）
        #反锯齿让文本的边缘更平滑。余下的两个实参分别是文本颜色和背景色

        #使用字符串格式化命令，它让python将数值转换为字符串时并在其中加入逗号
        #输入1，000，000而不是1000000
        high_score ="HIGH_SCORE : "+"{:,}".format((self.stats.high_score))

        self.high_score_image = self.font.render(high_score,False,self.text_color,self.ai_settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()

        self.high_score_rect.center = self.screen_rect.center

        self.high_score_rect.top   = self.screen_rect.top

    def prep_level(self):
        """渲染等级图像"""
        level = "LEVEL : "+"{:,}".format((self.stats.level))

        self.level_image = self.font.render(level,False,self.text_color,self.ai_settings.bg_color)

        self.level_rect = self.level_image.get_rect()

        self.level_rect.right = self.screen_rect.right 

        self.level_rect.top   = self.screen_rect.top + 25  

    def prep_sun(self):
        """渲染太阳数量"""

        sun = " "+ str(self.stats.sun_number) + " "

        self.sun_image = self.font.render(sun,False,self.text_color,self.ai_settings.bg_color)

        self.sun_rect = self.score_image.get_rect()

        self.sun_rect.left = self.screen_rect.left + 27

        self.sun_rect.top   = self.screen_rect.top + 64 

    def prep_ship_left(self):
        """渲染飞船生命图像"""
        left = "LEFT : "+"{:,}".format((self.stats.ships_left))

        self.left_image = self.font.render(left,False,self.text_color,self.ai_settings.bg_color)

        self.left_rect = self.left_image.get_rect()

        self.left_rect.right = self.screen_rect.right 

        self.left_rect.top   = self.screen_rect.top   + 50


    def prep_trick(self):
        """ 渲染大招数"""
        trick = "TRICK : "+"{:,}".format((self.stats.trick))

        self.trick_image = self.font.render(trick,False,self.text_color,self.ai_settings.bg_color)

        self.trick_rect = self.trick_image.get_rect()

        self.trick_rect.right = self.screen_rect.right 

        self.trick_rect.top   = self.screen_rect.top   + 75


    def draw_score(self):
        """ 调用screen.blit(),并向它传递一副图像以及与该图像相关联的rect对象，
        从而在屏幕上绘制文本图像 """
        self.screen.blit(self.score_image,self.score_rect)

    def draw_high_score(self):
        """ 调用screen.blit(),并向它传递一副图像以及与该图像相关联的rect对象，
        从而在屏幕上绘制文本图像 """
        self.screen.blit(self.high_score_image,self.high_score_rect)
    
    def draw_level(self):
        """ """
        self.screen.blit(self.level_image,self.level_rect)

    def draw_sun(self):
        """ """
        self.screen.blit(self.sun_image,self.sun_rect)

    def draw_ship_left(self):
        """ """
        self.screen.blit(self.left_image,self.left_rect)

    def draw_trick(self):
        """ """
        self.screen.blit(self.trick_image,self.trick_rect)


    
