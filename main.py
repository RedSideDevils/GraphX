import pygame as pg
import math

class Matrix:
    def __init__(self):
        pg.init()
        pg.font.init()
        self.RES = self.WIDTH, self.HEIGHT = 800, 800  #Resolution of Window
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.x0 = self.WIDTH // 2                      #Function X0 point
        self.y0 = self.HEIGHT // 2                     #Function Y0 Point
        self.cordinates = []                           #Cordinate Points Array
        self.Unit = 25                                 #Scale of Function
        self.x = -(self.x0 / self.Unit)                #Function X starting Point
        self.FPS = 360                                 #FPS limiter (120 is default)
        self.DrawSpeed = 0.1                           #Function Draw Speed (default 0.1)
        self.myfont = pg.font.Font("Roboto-Bold.ttf", 12)

    def f(self, x):
        return (x ** 3) + 2

    def DrawText(self, scr, text, x, y):
        textsurface = self.myfont.render(text, False, (255, 0, 0))
        scr.blit(textsurface, (x, y))

    def draw(self):
        if self.x <= (self.WIDTH / self.Unit):
            y = self.f(self.x)
            self.cordinates.append([self.x * self.Unit + self.x0, self.y0 - y * self.Unit])
            self.x += self.DrawSpeed

        for i in range(len(self.cordinates) - 1):
            pg.draw.line(self.screen, (255, 255, 255), self.cordinates[i], self.cordinates[i+1], 3)

    def run(self):
        for i in range(0, self.WIDTH, self.Unit):
            for j in range(0, self.HEIGHT, self.Unit):
                pg.draw.rect(self.screen, (64, 128, 255), (i, j, self.Unit, self.Unit), 2)

        pg.draw.line(self.screen, (0, 255, 0), [0, self.y0], [self.WIDTH, self.y0], 3)
        pg.draw.line(self.screen, (0, 255, 0), [self.x0, 0], [self.x0, self.HEIGHT], 3)
        pg.draw.circle(self.screen, (255, 0, 0), [self.x0, self.y0], 8)

        if (self.Unit >= 25):
            x_draw = 0
            while x_draw <= self.WIDTH:
                self.DrawText(self.screen, str(x_draw), x_draw, self.y0 + 5)
                pg.draw.circle(self.screen, (255, 255, 224), [x_draw, self.y0], 3)
                x_draw += self.Unit

            y_draw = 0
            while y_draw <= self.HEIGHT:
                self.DrawText(self.screen, str(y_draw), self.x0 + 10, y_draw)
                pg.draw.circle(self.screen, (255, 255, 224), [self.x0, y_draw], 3)
                y_draw += self.Unit

        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.flip()
            self.clock.tick(self.FPS)

app = Matrix()
app.run()