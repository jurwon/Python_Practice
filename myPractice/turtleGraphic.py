import turtle
import random

#함수 선언
def screenLeftClick(x,y):
  global r,g,b
  turtle.pencolor((r,g,b))
  turtle.pendown()
  turtle.goto(x,y)

def screenRightClick(x,y):
  turtle.penup()
  turtle.goto(x,y)

def screenMidClick(x,y):
  global r,g,b
  tSize = random.randrange(1,10)
  turtle.shapesize(tSize)
  r = random.random()
  g = random.random()
  b = random.random()


#변수 선언
pSize= 10
r,g,b = 0.0, 0.0, 0.0


# main
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

#윈도창 마우스 이벤트
#1:마우스 왼쪽버튼, 2:마우스 가운데 버튼, 3:마우스 오른쪽버튼
turtle.onscreenclick(screenLeftClick,1)
turtle.onscreenclick(screenMidClick,2)
turtle.onscreenclick(screenRightClick,3)

turtle.done()