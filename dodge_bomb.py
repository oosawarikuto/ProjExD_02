import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900
delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0),
}

"""
def zahyou_check(x,y):
    z=True
    if x>WIDTH:
        z=False
    elif y>HEIGHT:
        z=False
    elif x<0:
        z=False
    elif y<0:
        z=False
    return z
"""
def check_bound(rect: pg.rect):
    yoko,tate=True,True
    if rect.left<0 or WIDTH<rect.right:
        yoko=False
    if rect.top<0 or HEIGHT<rect.bottom:
        tate=False
    return yoko,tate
def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img2=pg.transform.flip(kk_img,True,False)
    kk_jisho={(-5,0):pg.transform.rotozoom(kk_img, 0, 2.0),(-5,-5):pg.transform.rotozoom(kk_img, -45, 2.0),(0,-5):pg.transform.rotozoom(kk_img2, 90, 2.0),(5,-5):pg.transform.rotozoom(kk_img2, 45, 2.0),(5,0):pg.transform.rotozoom(kk_img2, 0, 2.0),
              (5,5):pg.transform.rotozoom(kk_img2, -45, 2.0),(0,5):pg.transform.rotozoom(kk_img2, -90, 2.0),(-5,5):pg.transform.rotozoom(kk_img, -315, 2.0),(0,0):pg.transform.rotozoom(kk_img, 0, 2.0)}
    kk_img=pg.transform.rotozoom(kk_img, 0, 2.0)

    # こうかとんSurface（kk_img）からこうかとんRect（kk_rct）を抽出する
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    bd_img = pg.Surface((20, 20))  # 練習１
    bd_img.set_colorkey((0, 0, 0))  # 黒い部分を透明にする
    pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10)
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    # 爆弾Surface（bd_img）から爆弾Rect（bd_rct）を抽出する
    bd_rct = bd_img.get_rect()
    # 爆弾Rectの中心座標を乱数する
    bd_rct.center = x, y 
    vx, vy = +5, +5  # 練習２
    
    bd_imgs=[] #追加課題2
    for r in range(1,11):
        bd_img=pg.Surface((20*r,20*r))
        bd_img.set_colorkey((0, 0, 0))
        pg.draw.circle(bd_img,(255,0,0),(10*r,10*r),10*r)
        bd_imgs.append(bd_img)
    

    clock = pg.time.Clock()

    tmr = 0 

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        if kk_rct.colliderect(bd_rct):  # 練習５
            print("ゲームオーバー")
            return   # ゲームオーバー 
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]  # 合計移動量
        for k, mv in delta.items():
            if key_lst[k]: 
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rct.move_ip(sum_mv)
        if check_bound(kk_rct)!=(True,True):
            kk_rct.move_ip(-sum_mv[0],-sum_mv[1])
        screen.blit(bg_img, [0, 0])
        kk_img=kk_jisho[(sum_mv[0],sum_mv[1])]
                                    
        screen.blit(kk_img, kk_rct)
        print(kk_rct)
        bd_rct.move_ip(vx, vy)  # 練習２
        yoko, tate = check_bound(bd_rct)
        if not yoko:  # 横方向に画面外だったら
            vx *= -1
        if not tate:  # 縦方向に範囲外だったら
            vy *= -1
        bd_img=bd_imgs[min(tmr//500,9)]
        bd_rct.width, bd_rct.height= bd_img.get_rect().width, bd_img.get_rect().height
        screen.blit(bd_img,bd_rct)
        pg.display.update()
        tmr += 1
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()