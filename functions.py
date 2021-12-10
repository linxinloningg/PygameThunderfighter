import sys
import pygame
import time
from trick import Trick
from alien import Alien
from bullet import Bullet
from sun import Sun
from chooser import Chooser

       
       
        ###移动的函数###
def check_keydown_events(event,ship):
    """ 相应按键按下"""
    if event.key == pygame.K_RIGHT:
        ship.ship_mv_rightflag = True 
    if event.key == pygame.K_LEFT:                              
        ship.ship_mv_leftflag = True
    if event.key == pygame.K_UP:                                              
        ship.ship_mv_upflag = True 
    if event.key == pygame.K_DOWN:
        ship.ship_mv_downflag = True 

def check_keyup_event(event,ship):
    """ 响应按键松开"""
    if event.key == pygame.K_RIGHT:
        ship.ship_mv_rightflag=False
    if event.key == pygame.K_LEFT:
        ship.ship_mv_leftflag=False
    if event.key == pygame.K_UP:
        ship.ship_mv_upflag=False
    if event.key == pygame.K_DOWN:
        ship.ship_mv_downflag=False
        ###移动的函数###

def check_keyspace(event,tricks,screen,stats):
    """ 相应空格按下"""
    if event.key  == pygame.K_SPACE:
        #改变显示状态标志，让大招动画显示
        if stats.trick >= 1:
            trick = Trick(screen)
            tricks.add(trick)
            stats.trick_flag = True
        
def check_l(event,stats):
    """ 相应l按下"""
    if event.key == pygame.K_l:
        stats.ship = "Ironman"      
        

### 点击检测       
def check_click(area,mouse_x,mouse_y):
    """在玩家单击选定区域时返回True"""
    """调用rect.collidepoint函数检查鼠标单击位置是否在区域的rect内"""
    #显示点击的区域坐标
    print("area.rect.x=:{},area.rect.y=:{}.".format(area.rect.x,area.rect.y))
    if area.rect.collidepoint(mouse_x,mouse_y):
        return True

    # 让光标是否可见
    # pygame.mouse.set_visible(True)

def check_clicksun(group,mouse_x,mouse_y):
    for member in group:
        #显示太阳的坐标
        print("member.rect.x=:{},member.rect.y=:{}.".format(member.rect.x,member.rect.y))
        if member.rect.collidepoint(mouse_x,mouse_y):
            return True
def check_clickitems(chooser,mouse_x,mouse_y):

    if chooser.card_cherrybomb_rect.collidepoint(mouse_x,mouse_y):
        return "Cherrybomb"

    elif chooser.card_snowpea_image_rect.collidepoint(mouse_x,mouse_y):
        return "SnowPea"

    elif chooser.card_threepeashooter_image_rect.collidepoint(mouse_x,mouse_y):
        return "Threepeashooter"
### 点击检测     


### 按键检测
def check_events(ai_settings,screen,stats,play_botton,ship,tricks,suns,chooser):
    for event in pygame.event.get():
        #退出
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.K_q:
            sys.exit()
            

        elif event.type == pygame.MOUSEBUTTONDOWN : 
            """ 无论点击屏幕什么地方，都会检测到一个MOUSEBUTTONDOWN事件，调用
                pygame.mouse.get_pos()会返回一个元祖，其中包含玩家点击鼠标时
                的x，y坐标
            """
            mouse_x,mouse_y = pygame.mouse.get_pos()
            #显示点击的坐标
            print("x=:{}，y=：{}".format(mouse_x,mouse_y))
            if check_click(play_botton,mouse_x,mouse_y):
                stats.game_active = True
                #stats.reset_stats()
                ship.center_ship()
                #game_start(stats,alien_settings,screen,aliens,alien_number,row_number,bullets)
            
            
            if check_clicksun(suns,mouse_x,mouse_y):
                stats.sun_number += 50
                #释放删除被点击的太阳
                for sun in suns.copy(): 
                    suns.remove(sun)

            ##检测按下选择板按键
            if check_clickitems(chooser,mouse_x,mouse_y) == "Cherrybomb":
                if stats.sun_number >= 150:
                    stats.sun_number -=150
                    stats.trick += 1

            if check_clickitems(chooser,mouse_x,mouse_y) == "SnowPea":
                if stats.sun_number >= 175:
                    stats.sun_number -=175 
                    stats.ship = "SnowPea"

            if check_clickitems(chooser,mouse_x,mouse_y) == "Threepeashooter":
                if stats.sun_number >= 300:
                    stats.sun_number -= 300
                    stats.ship = "Threepeashooter"

            
            

        #按键按下
        elif event.type==pygame.KEYDOWN:
            #移动
            check_keydown_events(event,ship)

            #按下空格 开火
            check_keyspace(event,tricks,screen,stats)

            #按下lin
            check_l(event,stats)

        #按键松开
        elif event.type==pygame.KEYUP:
            #移动
            check_keyup_event(event,ship)
### 按键检测           



 
                     
def delete_member(group):
         """ 删除离开屏幕的编组元素，释放内存"""     
         for member in group.copy():         
             if member.rect.bottom <= 0 :             
                 group.remove(member)


###外星人创建###

def get_number_alines_x(ai_settings,alien_width):
    """ 计算每行可容纳多少外星人"""
    #计算可用于摆放外星人的宽度 （每行边缘空出两个外星人左右）
    avaliable_space_x = ai_settings.width - 2*alien_width

    #设置外星人之间间隔宽度
    number_aliens_x = int(avaliable_space_x / (2*alien_width))

    return number_aliens_x


def get_number_aliens_y(ai_settings,ship_height,alien_height):
    """计算屏幕可容纳多少行"""
    avaliable_space_y=( ai_settings.height - (2*alien_height) - ship_height)

    number_aliens_y = int (avaliable_space_y / (3*alien_height) )

    return number_aliens_y
                   
def create_aliens(alien_settings,screen,aliens,alien_number,row_number,stats):
    """ 创建一个外星人并将其放入当前行"""

    """ 
        创建一个新的外星人，并通过设置x坐标将其加入到当前行。将每个外星人都往右
        推一个外星人的宽度。接下来，我们将外星人的宽度乘以2，得到每个外星人占据
        的空间（其中包括右边的空白区域），再据此计算当前外星人在当前行的位置。最
        后将每个新创建的外星人都添加到编组aliens中
        """
    #创建一个外星人并将其加入当前行
    alien = Alien(alien_settings,screen,"Zombie")

    if stats.level == 2:
    ##更换僵尸
        alien.load_image("BucketheadZombie")
    ##更换僵尸    
    elif stats.level == 3:
        alien.load_image("ConeheadZombie")
    elif stats.level == 4:
        alien.load_image("FlagZombie")
    elif stats.level == 5:
        alien.load_image("NewspaperZombie")
        
    

    #获取外星人图像的宽度
    alien_width = alien.rect.width
    ###通过设置显示图片的水平像素达到显示多个外星人效果

    #   从0开始增加（图片宽度像素+2*第几个图像）
    ###  外星人行的设置
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x

    #获取外星人图像的高度
    alien_height = alien.rect.height
    
    ###通过设置显示图片的垂直像素达到显示多个外星人的效果
   #   从0开始增加（图片高度像素+2*第几个图像）
    #### 外星人列的设置
    alien.y = alien_height + 2 * alien_height * row_number
    alien.rect.y = alien.y

    aliens.add(alien)

    ### 图像水平与垂直之间的间隔都为（2-1）个图像水平或垂直像素点


def create_fleet(ai_settings,alien_settings,screen,ship,aliens,stats):
    """ 创建外星人群"""
    """一波更比一波强，加快速度"""
    
    
    
    alien_settings.increase_speed()
    # 创建一个外星人用于计算
    alien = Alien(alien_settings,screen,"Zombie")

    # 每行可容纳多少外星人
    number_aliens_x = get_number_alines_x(ai_settings, alien.rect.width)
    print(number_aliens_x)

    # 屏幕可容纳多少行
    number_aliens_y = get_number_aliens_y(ai_settings, ship.rect.height, alien.rect.height)
    print(number_aliens_y)

    #创建多行外星人
    for row_number in range(number_aliens_y):
        #创建一行外星人
        for alien_number in range(number_aliens_x):
            create_aliens(alien_settings,screen,aliens,alien_number,row_number,stats)

###外星人创建

### 外星人移动
def change_direction(settings,group):
    """将整群外星人下移，并改变他们的方向"""
    for member in group.sprites():
        #alien.y += alien_settings.y_speed
        member.rect.y += settings.y_speed
    settings.fleet_direction *= -1

def check_edges(settings,group):
    """有外星人到达边缘时采取相应的措施"""
    for member in group.sprites():
        if member.check_edges():
            change_direction(settings,group)
            break
### 外星人移动

### 创建子弹
def creat_bullets(bullet_settings,bullets,screen,ship):
    #子弹定义
    #创建子弹并加入子弹编组
    bullet = Bullet(bullet_settings,screen,ship)

    bullets.add(bullet)
### 创建子弹

##创建大招
def creat_trick(tricks,screen):
    #大招定义
    #创建大招并加入大招编组
    trick = Trick(screen)
    
    tricks.add(trick)
##创建大招

## 创建阳光
def creat_suns(sun_settings, suns, screen):
    #阳光定义
    #创建阳光并加入阳光编组
    sun = Sun(sun_settings, screen)

    ##
    suns.add(sun)
## 创建阳光

###检测是否诞生了最高得分
def check_high_score(stats):
    """检测并更新最高分 """
    if stats.score > stats.high_score :
        stats.high_score = stats.score
###检测是否诞生了最高得分

### 检测子弹、大招与外星人的碰撞
def collision(First,Second,stats,alien_settings):
    """返回一个字典"""
    #检查是否有子弹击中外星人
    #如果是这样，就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(First,Second,True,True)

    """如果字典存在，遍历其中的所有值。每个值都是一个列表，包含被同一颗子弹击中的所有外星人
        对于每个列表，都将一个外星人的点数乘以其中包含的外星人数量，并将结果加入到当前得分中
    """
    if collisions :
        for aliens in collisions.values() :
            stats.score += alien_settings.point * len(aliens)
        check_high_score(stats)  
  
### 检测子弹、大招与外星人的碰撞



###检测游戏结束
def game_over(screen,ship,aliens):
    """ //检测外星人与飞船之间是否发生碰撞//检测飞船是否到达底部 """
    ### 外星人达到屏幕底端
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            return True
    ### 检测外星人与飞船之间是否发生碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        print("GAME OVER!")
        return True
###检测游戏结束


### 重生
def reborn(ai_settings,alien_settings,stats,screen,ship,aliens,bullets):
    #将ship_left减少1
    if stats.ships_left >0 :
        stats.ships_left -= 1
    else :
        stats.game_active = False

    #清空外星人列表和子弹列表
    aliens.empty()
    bullets.empty()

    #重新初始化外星人，创建一群新的外星人，并将飞船放到屏幕底部中央
    alien_settings.initialize_dynamic_settings()
    create_fleet(ai_settings,alien_settings,screen,ship,aliens,stats)
    ship.center_ship()

    #暂停
    time.sleep(0.5)
### 重生

#按钮显示
def play_botton(ai_settings,screen,stats,play_botton):
    if not stats.game_active :
        #屏幕初始化
        #screen.fill(ai_settings.bg_color)
        #绘制按钮
        play_botton.draw_botton()
        #让屏幕显示可见
        pygame.display.flip()
#按钮显示


#################################################################显示函数###########################################################
## 显示大招
def update_trick(tricks,screen,stats,aliens):
    ##刷新大招，并在大招释放之后释放内存
    ###删除大招
    def delet(tricks,stats):
        """ 删除大招"""
        for trick in tricks.copy():
            tricks.remove(trick)

    ###删除外星人,并增加得分
    def delet_fleet(aliens,stats):
        for alien in aliens.copy():
            stats.score += 50
            aliens.remove(alien)
    
    ### 显示大招 
    def blit(tricks,screen,stats,aliens):
        starttime=time.time()
        if stats.trick_flag :

            if len(tricks) >= 1:
            ##大招显示
                tricks.draw(screen)
                pygame.display.flip()
                time.sleep(1.0 - ((time.time() - starttime) % 1.0))
                delet_fleet(aliens,stats)
                stats.trick -= 1
                stats.trick_flag = False 
        

    blit(tricks,screen,stats,aliens)
    delet(tricks,stats)
### 显示大招

### 显示飞船
def update_ship(ai_settings,ship_settings,ship,stats): 
    if stats.ship == "SnowPea"  :
        ship.load_image("SnowPea")

    elif stats.ship == "Repeaterpea"  :
        ship.load_image("Repeaterpea")

    elif stats.ship == "Threepeashooter"  :
        ship.load_image("Threepeater")

    elif stats.ship == "Ironman" :
        ship.load_image("Ironman")
    #飞船显示
    ship.blitship()
    #刷新飞船显示
    ship.update_ship(ai_settings,ship_settings)
### 显示飞船

### 显示阳光
def update_sun(sun_settings,suns,screen):
    """ 检查是否有阳光位于屏幕边缘，并更新阳光位置"""
    """更新阳光位置"""
    """当阳光消失，创建新的阳光"""
    check_edges(sun_settings,suns)
    suns.update()
    if len(suns) == 0:
        creat_suns(sun_settings,suns,screen)

    ###阳光显示
    suns.draw(screen)

    ###删除飞出屏幕之外的阳光的内存
    delete_member(suns)
## 显示阳光

### 显示子弹
### 子弹向上移动，并创建新的子弹
def update_bullets(bullet_settings,bullets,screen,ship):
    

    if len(bullets) == 0:
        creat_bullets(bullet_settings,bullets,screen,ship)
    
    
    bullets.update()

    ###删除飞出屏幕之外的子弹
    delete_member(bullets)

    #子弹显示
    bullets.draw(screen)
### 子弹向上移动，并创建新的子弹
## 显示子弹

### 显示外星人
def update_aliens(ai_settings,alien_settings,screen,ship,aliens,stats):
    """ 检查是否有外星人位于屏幕边缘，并更新整群外星人的位置"""
    """更新外星人位置"""
    """当整群外星人都消灭殆尽，创建新的更强外星人"""
    
    check_edges(alien_settings,aliens)
    aliens.update()
    if len(aliens) == 0:
        create_fleet(ai_settings,alien_settings,screen,ship,aliens,stats)
    #外星人显示
    aliens.draw(screen)
### 显示外星人

### 显示选择面板、游戏信息
def update_imformation(chooser,scoreboard):
    ##显示选择面板
    chooser.blitchooser()
    chooser.blitchooser_items()

    #更新显示得分面板
    #渲染得分图像
    scoreboard.prep_scoreboard()
    scoreboard.draw_score()
    
    ##更新显示最高得分面板
    #渲染最高得分图像
    scoreboard.prep_scoreboard()
    scoreboard.draw_high_score()

    ##更新显示游戏等级
    #渲染游戏等级图像
    scoreboard.prep_level()
    scoreboard.draw_level()

    ##更新显示太阳得分
    #渲染太阳得分图像
    scoreboard.prep_sun()
    scoreboard.draw_sun()

    ##更新显示飞船生命
    #渲染飞船生命图像
    scoreboard.prep_ship_left()
    scoreboard.draw_ship_left()

    ##更新显示大招数量
    #渲染大招数量图像
    scoreboard.prep_trick()
    scoreboard.draw_trick()
### 显示选择面板、游戏信息

         
#################################################################显示函数###########################################################  


def update_screen(
    ai_settings,
    screen,
    ship,ship_settings,
    bullets,bullet_settings,
    tricks,
    alien_settings,aliens,
    scoreboard,
    suns,sun_settings,
    stats,
    chooser
    ):

    screen.blit(ai_settings.image,ai_settings.rect)

    ##刷新最高分数，游戏等级
    stats.check_high_score()
    stats.check_level()

    ##显示大招
    update_trick(tricks,screen,stats,aliens)

    ##刷新飞船显示
    update_ship(ai_settings,ship_settings,ship,stats)

    #更新阳光位置和显示
    update_sun(sun_settings,suns,screen)

    #刷新子弹显示，发射新子弹，并删除飞出屏幕的子弹
    update_bullets(bullet_settings,bullets,screen,ship)

    #更新外星人位置，并检测是否需要创建新的一群外星人
    update_aliens(ai_settings,alien_settings,screen,ship,aliens,stats)

    #更新游戏信息，刷新游戏信息显示
    update_imformation(chooser,scoreboard)
    

    #让最近绘制的屏幕显示
    pygame.display.flip()
