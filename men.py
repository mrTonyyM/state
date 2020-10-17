import random as rn

class Man():
    #средний человек с рейтингом 50
    #чем выше рейтинг тем быстрей вертикальная социальная мобильность
    def __init__(self):
        self.rating = rn.randint(1,100)


class Environment():
    #среда проверяет рейтинг человека и двигает в нужную сферу

    def socialMove(self, Man):
        if Man.rating <= 50:
            pass
        elif 50 < Man.rating <= 90:
            pass
        else:
            pass