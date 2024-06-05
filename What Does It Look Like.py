''' 
    DISCRIPTION
    릴레이도 포기하고 퀴즈만 남겨둘 예정
    따로 인원 설정도 없이 고정 한판
    이미지 리사이징, 텍스트 입력받기도 되었고
    띄우고 정답확인, regame? 만 하면 됨
    '''
import pygame
import math #for square root calculation
import time #for timer function
import random

#Screen size info (constants)
SCREEN_WIDTH = 900
SCREEN_HEIGHT = (SCREEN_WIDTH*0.65)

#processes
def MainLoop():
    running = True
    paint_running_time = 100
    InfoTextFont = pygame.font.Font(None, 30)
    guide = "<- -> select games     press ENTER to start !"
    screen.fill(bgcolor)
    g1 = pygame.image.load("D:\Learning\game discription\Slide1.PNG")
    g2 = pygame.image.load("D:\Learning\game discription\Slide2.PNG")
    g3 = pygame.image.load("D:\Learning\game discription\Slide3.PNG")

    gametype = 1
    textSurface = InfoTextFont.render(guide, True, (100, 100, 100))
    screen.blit(textSurface,(250, 450))
    while(running) : #wait for input value
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if gametype == 1:
                            Quiz()
                            running = False
                            break
                        elif gametype == 2:
                            screen.fill(bgcolor)
                            ShowText("**paint shortcuts**", (300, 30))
                            ShowText("q : quit", (300, 50))
                            ShowText("c : clear window", (300, 70))
                            ShowText("n / [ : size -", (300, 90))
                            ShowText("m / ] : size +", (300, 110))
                            ShowText("v/b : B-+", (300, 130))
                            ShowText("f/g : G-+", (300, 150))
                            ShowText("e/r : R-+", (300, 170))
                            ShowText("s/d : darker/brighter", (300, 190))
                            ShowText("Saved Image Location : the folder where .py located", (300, 300))
                            ShowText("filename is \"paintwindow_screenshot.png\"", (300, 320))
                            ShowText("Visit my Github : Eunhyuk0", (300, 400))
                            ShowText("Press ENTER to continue", (300, 500))
                            Wait = True
                            while(Wait):
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_RETURN:
                                            Wait = False
                                            break
                            screen.fill(bgcolor)
                        elif gametype == 3: #
                            PaintWindow(0, 0) #no time limit
                            running = False
                            break
                    if event.key == pygame.K_LEFT:
                        gametype -= 1
                        if gametype == 0:
                            gametype = 3
                    elif event.key == pygame.K_RIGHT:
                        gametype += 1
                        if gametype == 4:
                            gametype = 1
            if gametype == 1:
                screen.blit(g1, (150, 50))
            elif gametype == 2:
                screen.blit(g2, (150, 50))
            elif gametype == 3:
                screen.blit(g3, (150, 50))
            pygame.display.flip() #update screen

def Quiz():
    TFont = pygame.font.Font(None, 30)
    SFont = pygame.font.Font(None, 60)
    length = GetInput(0, 1, "Set Painting Length!")
    length = int(length[0])
    showtext = "Start Painting !  Press ENTER"
    textSurface = TFont.render(showtext, True, (100, 100, 100))
    subject = []
    screen.blit(textSurface, (250, 100))
    pygame.display.flip()

    Wait = True
    while(Wait):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Wait = False
                    break
    PaintWindow(length, 0)
    Title = GetInput(0, 1, "Entitle Your Painting !")
    subject = GetInput(0, 4, "Add wrong answer !")
    subject.append(Title[0])
    correctanswer = random.randint(0, 4)
    temp = subject[correctanswer]
    subject[correctanswer] = subject[4]
    subject[4] = temp  #subject list 의 랜덤 위치에 정답이 들어감
    guideimage = pygame.image.load("painting_0.png")
    guideimage = pygame.transform.scale(guideimage, (650, 422))
    screen.blit(guideimage, (100, 0))
    for i in range(5):
        ShowText(str(i)+" : "+subject[i], (150, 435+i*20)) #보기 제시
    pygame.display.flip()
    Wait = True
    input = ""

    while(Wait): #텍스트 입력 받기
        pygame.draw.rect(screen, bgcolor, pygame.Rect(800, 50, 30, 30)) #init text box
        q = "correct title ?"
        textSurface = TFont.render(q, True, (100, 100, 100))
        screen.blit(textSurface,(760,30))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(800, 50, 30, 30), 2)
        textSurface = TFont.render(input,True,(100, 100, 100))
        screen.blit(textSurface,(810, 55))
        pygame.display.flip() #update screen
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input = input[:-1]
                elif event.key == pygame.K_RETURN:
                    Wait = False
                    break
                else:
                    input += event.unicode

    if input == str(correctanswer):
        screen.fill(bgcolor)
        textSurface = SFont.render("Correct !", True, (100, 100, 100))
        screen.blit(textSurface,(400,200))  #정답
    else:
        screen.fill(bgcolor)
        textSurface = SFont.render("Title was \"%s\"."%subject[correctanswer], True, (100, 100, 100))
        screen.blit(textSurface,(200, 200)) #오답
    textSurface = TFont.render("Press ENTER to continue", True, (100, 100, 100))
    screen.blit(textSurface, (250, 500))
    pygame.display.flip()
    Wait = True
    while(Wait):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Wait = False
                    break
 
def TitleScreen():
    timer = 0
    scr = 0
    entirequit = 1
    title1 = pygame.image.load("D:\Learning\PythonGame_title_1.png")
    title2 = pygame.image.load("D:\Learning\PythonGame_title_2.png")
    screen.blit(title1, (0, 0))
    while(entirequit):
        timer += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                entirequit = 0 #enable quitting with [X]
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    MainLoop()
        if timer >= 100:
            if scr == 0:
                scr = 1
            else:
                scr = 0
            timer = 0
        if scr:
            screen.blit(title2, (0, 0))
        else:
            screen.blit(title1, (0, 0))
        pygame.display.flip() #update screen
    pygame.quit() #quit when the loop breaks

#functional functions
def Brush(type, color, PrevCursor, Cursor, size):
    if type == 0:
        drawcolor = color
    else:
        drawcolor = bgcolor

    pygame.draw.circle( screen, drawcolor, (Cursor[0], Cursor[1]), size)

    x_diff = Cursor[0] - PrevCursor[0] #현재와 이전 커서의 x좌표 차
    y_diff = Cursor[1] - PrevCursor[1] #현재와 이전 커서의 y좌표 차
    diff_distance = math.sqrt(x_diff**2 + y_diff**2) #커서의 거리 차
    complimentPoints = int(diff_distance / size*0.5) #최소한의 간격으로 거리 분할 -> 점 개수
    x_gap = x_diff / size*0.5 #이 간격으로 채움
    y_gap = y_diff / size*0.5 #이 간격으로 채움
    complimentCoord = (0, 0) #찍을 좌표

    for i in range(1, complimentPoints+1):
        complimentCoord = (PrevCursor[0] + x_gap*i, PrevCursor[1] + y_gap*i)
        pygame.draw.circle(screen, drawcolor, complimentCoord, size)
    
    #이전 위치와 현재 위치 간격이 클 때 사이에 1개 추가   
    if (Cursor[0] - PrevCursor[0] > size * 1.5) or (Cursor[1] - PrevCursor[1] > size * 1.5):
        MiddleCur = ((Cursor[0] - PrevCursor[0])/2, (Cursor[1] - PrevCursor[1])/2)
        pygame.draw.circle(screen, drawcolor, MiddleCur, size)

def GetInput(image,num,info): #입력한 이미지(surface) 를 띄우고 필요한 개수 입력받음
    InputTextFont = pygame.font.Font(None, 32)
    InfoTextFont = pygame.font.Font(None, 30)
    screen.fill(bgcolor)
    input_rect = pygame.Rect(150, 400, 600, 30)
    texts = []
    for i in range(num): #받을 개수만큼 추가
        texts.append("")

    i = 0
    while(i<num): #필요한 개수만큼 입력 받기
        screen.fill(bgcolor)
        if(image):
            screen.blit(image, (0, 0)) #only 900*585
        left = "%d / %d"%(i+1, num)
        textSurface = InfoTextFont.render(left, True, (100, 100, 100))
        screen.blit(textSurface,(100, 405))
        textSurface = InfoTextFont.render(info, True, (100, 100, 100))
        screen.blit(textSurface, (200, 300))
        pygame.draw.rect(screen, (0, 0, 0), input_rect, 2)
        textSurface = InputTextFont.render(texts[i],True,(100, 100, 100))
        screen.blit(textSurface,(160, 405))
        pygame.display.flip() #update screen
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    texts[i] = texts[i][:-1]
                elif event.key == pygame.K_RETURN:
                    i += 1
                else:
                    texts[i] += event.unicode
    screen.fill(bgcolor)
    return texts

def ShowText(text, pos):
    TFont = pygame.font.Font(None, 30)
    textSurface = TFont.render(text, True, (100, 100, 100))
    screen.blit(textSurface, pos)
    pygame.display.flip()

def PaintWindow(running_time, code): #paint something here
    tick = pygame.USEREVENT
    pygame.time.set_timer(tick,1000)
    timer = 0
    InfoTextFont = pygame.font.Font(None, 30)
    screen.fill((255, 255, 255))
    painting = True
    color = (0, 0, 0) #default : black
    tempcolor = (100, 100, 100) #default : grey
    temptup = (0, 0, 0) #temp variable for tuples
    R = 0
    G = 0
    B = 0
    bgcolor = (255, 255, 255) #color for clearing and eraser, default : white
    CursorColor = (100, 100, 100) #grey color for cursor
    BrushSize = 10 #brush size
    BrushStroking = 0 #using brush?
    x,y = (0, 0) #reset coordinates
    cr_x, cr_y = (0, 0) #current coordinates (for non-painting tasks)
    pr_x, pr_y = (x, y) #previous cursor coordinates
    BrushType = 0 #brush shape : 0==Brush, 1==eraser
    mousepressed = False #마우스가 눌린 '동안' 작동시키기 위함
    pygame.draw.rect(screen, (30, 30, 30), pygame.Rect(840,0, 10, 50))


    buttons = pygame.image.load("D:\Learning\menus.png")
    while(painting):
        paintKey = pygame.key.get_pressed()
        for event in pygame.event.get():
            if timer >= running_time and running_time != 0: #running_time 이 0이면 제한 X
                finalshot = screen
                pygame. image. save(finalshot,"painting_%d.png"%code)
                painting = False
                break
            if event.type == pygame.USEREVENT:
                timer += 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mousepressed == False:
                    pr_x, pr_y = pygame.mouse.get_pos()
                BrushStroking = 0
                mousepressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                mousepressed = False
            elif event.type == pygame.MOUSEMOTION and mousepressed == True and cr_x > 57:
                x,y = pygame.mouse.get_pos()
                BrushStroking = 1
                Brush(BrushType, color, (pr_x, pr_y), (x,y), BrushSize)
                pr_x, pr_y = x,y
            if cr_x <= 57 and mousepressed==True: #커서가 menu:color 에 있음
                pr_x,pr_y = cr_x, cr_y
                if BrushStroking:
                    pass
                elif cr_y <= 40: #black
                    R = 0
                    G = 0
                    B = 0
                elif cr_y <= 40 * 2: #red
                    R = 255
                    G = 0
                    B = 0
                elif cr_y <= 40 * 3: #blue
                    R = 0
                    G = 0
                    B = 255
                elif cr_y <= 40 * 4: #green
                    R = 0
                    G = 255
                    B = 0
                elif cr_y <= 40 * 5: #magenta
                    R = 255
                    G = 0
                    B = 255
                elif cr_y <= 40 * 6: #cyan
                    R = 0
                    G = 255
                    B = 255
                elif cr_y <= 40 * 7: #yellow
                    R = 255
                    G = 255
                    B = 0
                elif cr_y <= 320: #R+
                    if R<=235:
                        R += 20
                elif cr_y <= 354: #R-
                    if R>= 20:
                        R -= 20
                elif cr_y <= 387: #G+
                    if G<=235:
                        G += 20
                elif cr_y <= 421: #G-
                    if G>= 20:
                        G -= 20
                elif cr_y <= 454: #B+
                    if B<=235:
                        B += 20
                elif cr_y <= 488: #B-
                    if B>= 20:
                        B -= 20
                elif cr_y > 488 and cr_y < 535: #darker
                    R -= 15
                    G -= 15
                    B -= 15
                    if R < 0:
                        R = 0
                    if B < 0:
                        B = 0
                    if G < 0:
                        G = 0
                elif cr_y >= 535: #brighter
                    R += 15
                    G += 15
                    B += 15
                    if R > 255:
                        R = 255
                    if B > 255:
                        B = 255
                    if G > 255:
                        G = 255
            elif cr_x >= 841 and mousepressed==True: #커서가 menu:etc 에 있음
                if BrushStroking:
                    pass
                elif cr_y <= 60:
                    BrushType = 0
                    pygame.draw.rect(screen, (30, 30, 30), pygame.Rect(840,0, 10, 50))
                    pygame.draw.rect(screen, bgcolor, pygame.Rect(840,60, 10, 50))
                elif cr_y <= 100:
                    BrushType = 1
                    pygame.draw.rect(screen, (30, 30, 30), pygame.Rect(840,60, 10, 50))
                    pygame.draw.rect(screen, bgcolor, pygame.Rect(840,0, 10, 50))
                elif cr_y <= 170:
                    BrushSize += 3
                elif cr_y <= 210:
                    BrushSize -= 3
                    if BrushSize <= 0:
                        BrushSize = 1
                elif cr_y <= 270:
                    if BrushType:
                        screen.fill(bgcolor)
                    else:
                        screen.fill(color)
                elif cr_y >= 478 and cr_y<=532:
                    paintwindow_screenshot = screen
                    pygame. image. save(paintwindow_screenshot,"paintwindow_screenshot.png")
                    print("\nImage Saved!\n")
                elif cr_y >= 533:
                    finalshot = screen
                    pygame. image. save(finalshot,"painting_%d.png"%code)
                    painting = False
                    break
            if paintKey[pygame.K_q]:    
                finalshot = screen
                pygame. image. save(finalshot,"painting_%d.png"%code)     
                painting = False
                break
            if paintKey[pygame.K_c]:
                screen.fill(bgcolor) # clear screen
            if paintKey[pygame.K_LEFTBRACKET] or paintKey[pygame.K_n]:
                BrushSize -= 3
                if BrushSize <= 0:
                        BrushSize = 1
            if paintKey[pygame.K_RIGHTBRACKET] or paintKey[pygame.K_m]:
                BrushSize += 3
            if paintKey[pygame.K_r]: #R+
                if R<=235:
                    R += 20
            if paintKey[pygame.K_e]: #R-
                if R>=20:
                    R -= 20
            if paintKey[pygame.K_g]: #G+
                if G<=235:
                    G += 20
            if paintKey[pygame.K_f]: #G-
                if G>=20:
                    G -= 20
            if paintKey[pygame.K_b]: #B+
                if B<=235:
                    B += 20
            if paintKey[pygame.K_v]: #B-
                if B >=20:
                    B -= 20
            if paintKey[pygame.K_d]: #darker
                    R -= 15
                    G -= 15
                    B -= 15
                    if R < 0:
                        R = 0
                    if B < 0:
                        B = 0
                    if G < 0:
                        G = 0
            if paintKey[pygame.K_s]: #brighter
                    R += 15
                    G += 15
                    B += 15
                    if R > 255:
                        R = 255
                    if B > 255:
                        B = 255
                    if G > 255:
                        G = 255
        cr_x,cr_y = pygame.mouse.get_pos()
        color = (R, G, B)
        pygame.draw.rect(screen, color, pygame.Rect(845, 430, 45, 10)) #show current color
        #pygame.draw.rect(screen, tempcolor, pygame.Rect(867, 445, 22, 30)) #show temp color
        pygame.draw.circle(screen, color, (900, 350), BrushSize) #show current color and size
        time_print = running_time - timer
        textSurface = InfoTextFont.render(str(time_print), True, (100, 100, 100))
        if running_time != 0:
            screen.blit(textSurface,(845, 450))
        pygame.display.flip() #update screen
        #print(cr_x,cr_y)
        screen.blit(buttons, (0, 0)) #메뉴 이미지 표시

################# start running ####################

#Set-up 
from pygame.locals import *
pygame.init()

bgcolor = (255, 255, 255) #global variable
clock = pygame.time.Clock() #set FPS
FPS = 30 #global variable, default FPS
clock.tick(FPS)
pygame.display.set_caption('What Does It Look Like ?')
print("\n\nWhat Does It Look Like ?\n\nSimple Game + paint tool By Koh Eunhyuk\nvisit my gitHub : Eunhyuk0\n\nFine Release")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #global variable
screen.fill(bgcolor)
pygame.mouse.set_cursor(*pygame.cursors.diamond)
TitleScreen()