#画蟒蛇
from turtle import*        #引入turtle（海龟）绘图库
setup(600,500,200,200)        #设置窗口大小及位置
penup()        #抬起画笔
pencolor("red")        #设置画笔颜色
pensize(20)        #设置画笔大小为5个像素
goto(-230,0)        #去往窗口绝对坐标（x(-220),y(0))
pendown()        #放下画笔
right(45)        #海龟朝向当前海龟的左边50度方向
for x in range(4):        #for x in range循环运行
  circle(30,90)        #画一个直径为（海龟左侧）30，角度为（海龟顺时针）90度的弧线（-90为逆时针）
  circle(-30,90)        #画一个直径为（海龟右侧）30，角度为（海龟顺时针）90度的弧线
circle(30,90/2)
fd(30)        #海龟向前走30
circle(20,180)
fd(15)
done        #完成
