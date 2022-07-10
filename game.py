import pygame
import random
import cv2
import numpy as np
import os

camera=cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
x = 130
y = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pygame.init()
pygame.display.set_caption("SNAKE GAME")
icon=pygame.image.load(r"C:\Users\bertug\PycharmProjects\Snake_Game\Images\logo.png")
pygame.display.set_icon(icon)
ekran_en=500
ekran_boy=400

skorDosyasi=open(r"C:\Users\bertug\PycharmProjects\Snake_Game\skorlar.txt","a+")

pencere=pygame.display.set_mode((ekran_en,ekran_boy))

zaman=pygame.time.Clock()
block_size=10

black=(0,0,0)
chocalate=(210,105,30)
white=(255,255,255)
green=(0,128,0)
red=(255,0,0)
blue=(0,0,255)
aqua=(0,255,255)
yellow=(255,255,0)
purple=(255,0,255)
orange=(255,165,0)
lime=(0,255,0)
gold=(255,215,0)
salmon=(250,128,114)
deepPink=(255,0,127)
brown=(204,102,0)

class otherGameSettings():
    def logo(self):
        logo=pygame.image.load(r"C:\Users\bertug\PycharmProjects\Snake_Game\Images\snake.jpg")
        rect=logo.get_rect()
        rect.x,rect.y=(150,10)
        pencere.blit(logo,rect)

    def pause(self):
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            pencere.fill((0, 0, 0))
            txt = texts()
            txt.write("PAUSE", deepPink, 150, 100, 80)
            txt.write("SPACE TO CONTINUE OR Q TO EXIT", red, 25, 250, 35)
            pygame.display.update()
            zaman.tick(5)

class texts():
    def write(self,message,color,x,y,size):
        self.message=message
        self.color=color
        self.x=x
        self.y=y
        self.size=size
        font=pygame.font.SysFont(None,size)
        text=font.render(message,True,color)
        pencere.blit(text,[x,y])

class snake():
    def snake(self,block_size,snakelist,snakeColor):
        self.snakeColor=snakeColor
        for XnY in snakelist:
            pygame.draw.rect(pencere,snakeColor,[XnY[0], XnY[1], block_size, block_size])

class Game_Intro():
    ogs=otherGameSettings()
    ogs.logo()
    def Intro(self):
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        intro = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            txt=texts()
            txt.write("Yılan yön tuşları kullanılarak hareket ettirilir.",orange,40,290,30)
            txt.write("HER SEVİYE ARTIŞIN DA YILANIN HIZI DA ARTAR",aqua,40,320,25)
            txt.write("Oyuna başlamak için 'Space' tuşuna,",purple,90,350,25)
            txt.write("Çıkış yapmak için 'Q' tuşuna basın.",purple,90,380,25)
            pygame.display.update()
            zaman.tick(5)

class gameLoop():
    def game(self):
        self.u = False
        self.l = False
        self.d = False
        self.r = False
        pygame.mixer_music.load(r"C:\Users\bertug\PycharmProjects\Snake_Game\Music\snakeSound.mp3")
        pygame.mixer_music.play(0)
        level = 1
        gameExit = False
        gameOver = False
        skor = 0
        yilanX = ekran_en / 2
        yilanY = ekran_boy / 2
        FPS = 10
        snakelist = []
        snake_length = 1

        bg=pygame.image.load(r"C:\Users\bertug\PycharmProjects\Snake_Game\Images\bg.jpg")

        randyemX = round(random.randrange(0, ekran_en - block_size) / 10.0) * 10.0
        randyemY = round(random.randrange(0, ekran_boy - block_size) / 10.0) * 10.0
        yilanX_Yon = 0
        yilanY_Yon = 0
        txt = texts()
        ogs=otherGameSettings()

        while not gameExit:
            while gameOver == True:
                pencere.fill((0, 0, 0))
                snakeLogo=pygame.image.load(r"C:\Users\bertug\PycharmProjects\Snake_Game\Images\snake.jpg")
                txt.write("GAME OVER!",red,100,25,70)
                pencere.blit(snakeLogo,(145,90))
                txt.write("PRESS SPACE TO PLAY AGAIN OR Q TO QUIT",white,30,350,30)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            gameExit = True
                            gameOver = False
                        elif event.key == pygame.K_SPACE:
                            game=gameLoop()
                            game.game()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        ogs.pause()
            if yilanX >= ekran_en or yilanX <= 0 or yilanY >= ekran_boy or yilanY < 0:
                gameOver = True
#------------------------------------ Color Detection ----------------------------------------:
            ret, frame = camera.read()
            frame = cv2.flip(frame, 1)

            # -------------------------- Up Rectangle -------------------------------------:
            x_up, y_up, w_up, h_up = (240, 10, 150, 150)
            rect_up = frame[y_up:y_up + h_up, x_up:x_up + w_up]
            hsv_frame_up = cv2.cvtColor(rect_up, cv2.COLOR_BGR2HSV)
            blue_up = cv2.inRange(hsv_frame_up, (100, 150, 0), (140, 255, 255))
            kernal = np.ones((5, 5), "uint8")
            blue_mask = cv2.dilate(blue_up, kernal)
            res_blue = cv2.bitwise_and(rect_up, rect_up,
                                       mask=blue_mask)
            contours, hierarchy = cv2.findContours(blue_mask,
                                                   cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)
            for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if (area > 300):
                    x, y, w, h = cv2.boundingRect(contour)
                    blue_up = cv2.rectangle(blue_up, (x, y),
                                            (x + w, y + h),
                                            (0, 0, 255), 2)
                    cv2.putText(frame, "Blue Up Colour", (200, 250),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1.0, (255, 0, 0), 2)
                    self.u = True
                else:
                    self.u = False

            # ----------------------------- Left Rectangle -----------------------------------------:
            x_left, y_left, w_left, h_left = (10, 170, 150, 150)
            rect_left = frame[y_left:y_left + h_left, x_left:x_left + w_left]
            hsv_frame_left = cv2.cvtColor(rect_left, cv2.COLOR_BGR2HSV)
            blue_left = cv2.inRange(hsv_frame_left, (100, 150, 0), (140, 255, 255))
            kernal = np.ones((5, 5), "uint8")
            blue_mask = cv2.dilate(blue_left, kernal)
            res_blue = cv2.bitwise_and(rect_left, rect_left, blue_left)
            contours, hierarchy = cv2.findContours(blue_mask,
                                                   cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)
            for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if (area > 300):
                    x, y, w, h = cv2.boundingRect(contour)
                    blue_left = cv2.rectangle(blue_left, (x, y),
                                              (x + w, y + h),
                                              (0, 0, 255), 2)
                    cv2.putText(frame, "Blue Left Colour", (200, 250),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1.0, (255, 0, 0), 2)
                    self.l = True
                else:
                    self.l = False

            # ----------------------------- Down Rectangle --------------------------------------:
            x_down, y_down, w_down, h_down = (240, 310, 150, 150)
            rect_down = frame[y_down:y_down + h_down, x_down:x_down + w_down]
            hsv_frame_down = cv2.cvtColor(rect_down, cv2.COLOR_BGR2HSV)
            blue_down = cv2.inRange(hsv_frame_down, (100, 150, 0), (140, 255, 255))
            kernal = np.ones((5, 5), "uint8")
            blue_mask = cv2.dilate(blue_down, kernal)
            res_blue = cv2.bitwise_and(rect_down, rect_down, blue_down)
            contours, hierarchy = cv2.findContours(blue_mask,
                                                   cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)
            for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if (area > 300):
                    x, y, w, h = cv2.boundingRect(contour)
                    blue_down = cv2.rectangle(blue_down, (x, y),
                                              (x + w, y + h),
                                              (0, 0, 255), 2)
                    cv2.putText(frame, "Blue Down Colour", (200, 250),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1.0, (255, 0, 0), 2)
                    self.d = True
                else:
                    self.d = False

            # ----------------------------- Right Rectangle --------------------------------------:
            x_right, y_right, w_right, h_right = (480, 170, 150, 150)
            rect_right = frame[y_right:y_right + h_right, x_right:x_right + w_right]
            hsv_frame_right = cv2.cvtColor(rect_right, cv2.COLOR_BGR2HSV)
            blue_right = cv2.inRange(hsv_frame_right, (100, 150, 0), (140, 255, 255))
            kernal = np.ones((5, 5), "uint8")
            blue_mask = cv2.dilate(blue_right, kernal)
            res_blue = cv2.bitwise_and(rect_right, rect_right, blue_right)
            contours, hierarchy = cv2.findContours(blue_mask,
                                                   cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)
            for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if (area > 300):
                    x, y, w, h = cv2.boundingRect(contour)
                    blue_right = cv2.rectangle(blue_right, (x, y),
                                               (x + w, y + h),
                                               (0, 0, 255), 2)
                    cv2.putText(frame, "Blue Right Colour", (200, 250),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1.0, (255, 0, 0), 2)
                    self.r = True
                else:
                    self.r = False

            if self.l:
                yilanX_Yon = -block_size
                yilanY_Yon = 0
            elif self.r:
                yilanX_Yon = block_size
                yilanY_Yon = 0
            elif self.u:
                yilanY_Yon = -block_size
                yilanX_Yon = 0
            elif self.d:
                yilanY_Yon = block_size
                yilanX_Yon = 0

            yilanX += yilanX_Yon
            yilanY += yilanY_Yon

            pencere.fill((0, 0, 0))
            pencere.blit(bg, (0, 0))
            pygame.draw.rect(pencere, (255, 0, 0), [randyemX, randyemY, block_size, block_size])

            snakehead = []
            snakehead.append(yilanX)
            snakehead.append(yilanY)
            snakelist.append(snakehead)

            if len(snakelist) > snake_length:
                del snakelist[0]

            for eachSegment in snakelist[:-1]:
                if eachSegment == snakehead:
                    gameOver = True

            pygame.display.update()
            if yilanX == randyemX and yilanY == randyemY:
                skor = skor + 10
                snake_length += 4
                if skor % 50 == 0:
                    level += 1
                if skor >= 50:
                    FPS = 20
                if skor >= 100:
                    FPS = 25
                if skor >= 150:
                    FPS = 30
                if skor >= 200:
                    FPS = 35
                if skor >= 250:
                    FPS = 40
                if skor>=300:
                    FPS=50
                    pygame.display.update()
                randyemX = round(random.randrange(0, ekran_en - block_size) / 10.0) * 10.0
                randyemY = round(random.randrange(0, ekran_boy - block_size) / 10.0) * 10.0

            snk = snake()
            snakeColor=blue
            if level==2:
               snakeColor=purple
            if level==3:
                snakeColor=deepPink
            if level == 4:
                snakeColor = gold
            if level>4:
                snakeColor=white

            snk.snake(block_size, snakelist, snakeColor)

            pygame.draw.rect(pencere, black, (yilanX, yilanY, 3, 3))
            pygame.draw.rect(pencere,black,(yilanX+5,yilanY,3,3))
            txt.write("Score: ",black,0,0,35)
            txt.write(str(skor),black,80,2,35)
            txt.write("Level: ",black,400,0,35)
            txt.write(str(level),black,475,0,35)
            pygame.display.update()
            zaman.tick(FPS)

            if gameOver==True:
                pygame.mixer_music.pause()

            cv2.rectangle(frame, (x_right, y_right), (x_right + w_right, y_right + h_right), (0, 255, 0), 3)
            cv2.rectangle(frame, (x_down, y_down), (x_down + w_down, y_down + h_down), (0, 255, 0), 3)
            cv2.rectangle(frame, (x_left, y_left), (x_left + w_left, y_left + h_left), (0, 255, 0), 3)
            cv2.rectangle(frame, (x_up, y_up), (x_up + w_up, y_up + h_up), (0, 255, 0), 3)
            cv2.imshow("Frame", frame)
            #cv2.imshow("Blue Up Frame", blue_up)
            #cv2.imshow("Blue Left Frame", blue_left)
            #cv2.imshow("Blue Down Frame", blue_down)
            #cv2.imshow("Blue Right Frame", blue_right)
            print("Durum Up = ", self.u, "\n")
            print("Durum Left", self.l, "\n")
            print("Durum Down", self.d, "\n")
            print("Durum Right", self.r, "\n")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        camera.release()
        cv2.destroyAllWindows()
        skorDosyasi.write("Skor: " + str(skor) + "\n")
        skorDosyasi.close()
        pygame.quit()
        quit()

intro=Game_Intro()
intro.Intro()
game=gameLoop()
game.game()