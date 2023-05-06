import time
from turtle import Turtle, done, Screen
from plyer import notification

game_status = True


class Line(Turtle):

    def __init__(self, x, y, side, number):
        super().__init__()
        self.side = side
        self.number = number
        self.hideturtle()
        self.color("white")
        self.speed(10000)
        self.shape("square")
        self.shapesize(1, 10)
        self.penup()
        self.goto(x, y)
        self.setheading(side)
        self.color("black")
        # self.write(f"im {self.number}", align='center', font=('Arial', 25, 'bold'))
        self.color("white")
        self.showturtle()


line_1 = Line(200, 0, 90, 1)
line_2 = Line(100, 50, 90, 2)
line_3 = Line(0, 0, 0, 3)
line_4 = Line(-100, 90, 0, 4)
line_5 = Line(-200, 0, 90, 5)
line_6 = Line(-300, -90, 0, 6)
line_7 = Line(200, 100, 90, 7)
line_8 = Line(100, 150, 90, 8)
line_9 = Line(0, 190, 0, 9)
line_10 = Line(-100, 190, 0, 10)
line_11 = Line(-200, 90, 0, 11)
line_12 = Line(-300, 300, 0, 12)
line_13 = Line(-300, 90, 90, 11)

lst_l = [line_1, line_2, line_3, line_4, line_5, line_6, line_7,
         line_8, line_9, line_10, line_11, line_12, line_13]


class Enemy(Turtle):
    def __init__(self, x, y, shape, color):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.showturtle()
        self.speed(10)


def check_queen():
    xe_n = queen.xcor() - player.xcor()
    ye_n = queen.ycor() - player.ycor()
    xe = int(abs(xe_n))
    ye = int(abs(ye_n))
    if xe < 15 and ye < 15:
        win()
        print(f"столкновение с принцессой : x {xe}, y {ye}")


def check():
    for line in lst_l:
        xm_na = line.xcor() - player.xcor()
        ym_na = line.ycor() - player.ycor()
        xm = int(abs(xm_na))
        ym = int(abs(ym_na))
        # print(f"по x {xm}, по y {ym}")
        if line.side == 0:
            if xm < 105 and ym < 15:
                print("side 0")
                restart_p()
                print(f"столкновение со стеной по x {xm}, по y {ym}")
                break

        elif line.side == 90:
            if ym < 105 and xm < 15:
                print("side 90")
                restart_p()
                print(f"столкновение со стеной по x {xm}, по y {ym}")
                break
        print("конец итерации")
    print("КОНЕЦ ЦИКЛА")


class Player(Turtle):

    def __init__(self, color, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(11111)
        self.goto(x, y)
        self.color(color)
        self.shape("turtle")
        self.speed(20)
        self.showturtle()

    def restart(self):
        self.goto(start_posx_player, start_posy_player)

    def to_right(self):
        self.setheading(0)
        self.forward(speed)
        check()
        check_queen()

    def to_left(self):
        self.setheading(180)
        self.forward(speed)
        check()
        check_queen()

    def move_up(self):
        self.setheading(90)
        self.forward(speed)
        check()
        check_queen()

    def move_down(self):
        self.setheading(270)
        self.forward(speed)
        check()
        check_queen()


scr = Screen()

start_posx_player = 0
start_posy_player = -200

player = Player("blue", start_posx_player, start_posy_player)

speed = 15

queen = Turtle()
queen.hideturtle()
queen.penup()
queen.color("purple")
queen.goto(-240, 50)
queen.shape("turtle")
queen.showturtle()

enemy_1 = Enemy(-166, -58, "turtle", "black")


def win():
    notification.notify(
        title='Уведомление',
        message='Вы победили!',
        app_icon='notifications2.ico')
    for i in lst_l:
        i.hideturtle()
    enemy_1.hideturtle()

    def circle_w():
        draw = queen.clone()
        draw.goto(-20, -100)
        for _ in range(20):
            draw.forward(40)
            draw.left(20)
            draw.stamp()

    circle_w()

    def stars():
        class Star(Turtle):
            def __init__(self, x, y):
                super().__init__()
                self.speed(50)
                self.hideturtle()
                self.color("yellow")
                self.penup()
                self.goto(x, y)
                self.pendown()

        size = 10
        angle = 120

        def star_draw(self):
            self.fillcolor("yellow")
            self.begin_fill()
            self.right(12)
            for _ in range(5):
                self.forward(size)
                self.right(angle)
                self.forward(size)
                self.right(72 - angle)
            self.end_fill()

        star_1 = Star(-40, -10)
        star_draw(star_1)
        star_2 = Star(0, -10)
        star_draw(star_2)
        star_3 = Star(+40, -10)
        star_draw(star_3)

    def txt():
        player.goto(-30, 0)
        player.write("Win", align='center', font=('Arial', 18, 'bold'))
        player.goto(2, 15)
        player.setheading(0)
        queen.goto(35, 15)
        queen.setheading(180)

    txt()

    stars()
    # scr.listen(False)
    time.sleep(3)


def restart_p():
    player.restart()


def main():
    scr.title('Final project')
    scr.bgcolor("light blue")

    # 0, 90
    def check_enemy():
        xe_n = enemy_1.xcor() - player.xcor()
        ye_n = enemy_1.ycor() - player.ycor()
        xe = int(abs(xe_n))
        ye = int(abs(ye_n))
        if xe < 13 and ye < 10:
            restart_p()
            print(f"столкновение с противником : x {xe}, y {ye}")

    def move_enemy1():
        while enemy_1.xcor() < 51:
            enemy_1.forward(1)
            check_enemy()
        enemy_1.setheading(enemy_1.towards(-166, -58))
        while enemy_1.xcor() > -166:
            enemy_1.forward(1)
            check_enemy()
        enemy_1.setheading(enemy_1.towards(51, -58))

    scr.listen()
    scr.onkey(player.to_right, "Right")
    scr.onkey(player.to_left, "Left")
    scr.onkey(player.move_up, "Up")
    scr.onkey(player.move_down, "Down")

    while game_status is True:
        move_enemy1()


main()

done()
