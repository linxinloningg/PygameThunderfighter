import pygame.font

class Botton():
    def __init__(self,ai_settings,screen,msg):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #设置按钮的尺寸和其他属性  
        self.width =200
        self.height = 200 

        #开始菜单设置
        self.image = pygame.image.load('resource\Background\MainMenu.bmp')
        
        
        
        self.rect = pygame.Rect(0,0,1100,500)
        

        self.botton_color = (0,0,0)
        self.text_color = (120,120,120)
        self.font = pygame.font.SysFont(None,100)

        #创建按钮的rect对象，并使其居中

        #填充一个矩形：
        #self.rect = pygame.Rect(0,0,self.width,self.height)
        #设置矩形的中心：
        #self.rect.center = self.screen_rect.center

        #按钮的标签只需创建一次

        #每当创建按钮实例时调用函数prep_msg()渲染显示的按钮
        self.prep_msg(msg)
        
    def prep_msg(self,msg):
        """将msg渲染为图像，并使其放入按钮上并居中"""
        #调用font.render（）将存储在msg中的文本转换为图像，然后将该图像存储在msg__images中
        #方法font.render()还接受一个布尔实参，该实参指定开启还是关闭反锯齿功能（反锯齿）
        #反锯齿让文本的边缘更平滑。余下的两个实参分别是文本颜色和背景色
        self.msg_image = self.font.render(msg,False,self.text_color,self.botton_color)
        
        self.msg_image_rect = self.msg_image.get_rect()
        
        self.msg_image_rect.center = self.rect.center

    def draw_botton(self):
        """
        调用screen.fill()来绘制表示按钮的矩形，
        再调用screen.blit(),并向它传递一副图像以及与该图像相关联的rect对象，
        从而在屏幕上绘制文本图像）
        """
        #绘制一个用颜色填充的按钮，再绘制文本
        self.screen.blit(self.image,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)

        
