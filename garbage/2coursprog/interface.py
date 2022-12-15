from data import ABC
from multiprocessing import Process
path='F:\python\project\котировки.txt'
ab=ABC()
global trainmod,traidmod,runGame
traidmod=trainmod=''
runGame=True
def interface(money):

    # from data import ABC
    import pygame
    import data
    pygame.init()
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    display_width = 500
    display_height = 600
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((display_width,display_height))

    traidmod = trainmod = ''
    button1=pygame.draw.rect(screen, (255, 255, 255), (20, 35, 450, 50))
    f1=pygame.font.SysFont('arial', 30)
    text1=f1.render('ввести название модуля тренировки',True,BLUE)
    screen.blit(text1,(30,40))

    button2=pygame.draw.rect(screen, (255, 255, 255), (20, 105, 450, 50))
    f2=pygame.font.SysFont('arial', 30)
    text2=f2.render('ввести название модуля торговли',True,BLUE)
    screen.blit(text2,(30,110))
    # pygame.draw.line(screen,BLACK,[20,35],[470,85],2)

    pygame.display.flip()
    f = pygame.font.SysFont('arial', 30)
    pygame.display.set_caption("интерфейс")
    flag=0
    runGame = True
    s1=s2=''
    while runGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runGame = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 20 and pygame.mouse.get_pos()[0] <= 470 and pygame.mouse.get_pos()[1] >= 35 and pygame.mouse.get_pos()[1] <= 85 and flag==0:
                    button1 = pygame.draw.rect(screen, (255, 255, 255), (20, 35, 450, 50))
                    button2 = pygame.draw.rect(screen, (255, 255, 255), (20, 105, 450, 50))
                    pygame.draw.line(screen,BLACK,[25,75],[465,75],2)
                    pygame.display.flip()
                    flag=1
                    s1=''
                if pygame.mouse.get_pos()[0] >= 20 and pygame.mouse.get_pos()[0] <= 470 and pygame.mouse.get_pos()[1] >= 105 and pygame.mouse.get_pos()[1] <= 155 and flag==0 and trainmod:
                    button1 = pygame.draw.rect(screen, (255, 255, 255), (20, 35, 450, 50))
                    button2 = pygame.draw.rect(screen, (255, 255, 255), (20, 105, 450, 50))
                    pygame.draw.line(screen,BLACK,[25,145],[465,145],2)
                    pygame.display.flip()
                    flag=2
                    s2=''
                if pygame.mouse.get_pos()[0] >= 20 and pygame.mouse.get_pos()[0] <= 470 and pygame.mouse.get_pos()[1] >= 35 and pygame.mouse.get_pos()[1] <= 85 and flag == 5:
                    button1 = pygame.draw.rect(screen, (255, 255, 255), (20, 35, 450, 50))
                    pygame.draw.line(screen, BLACK, [25, 75], [465, 75], 2)
                    pygame.display.flip()
                    flag=6
                    s3=''

            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE and (flag==1 or flag==2 or flag==3):
                    screen.fill(BLACK)
                    button1 = pygame.draw.rect(screen, (255, 255, 255), (20, 35, 450, 50))
                    f1 = pygame.font.SysFont('arial', 30)
                    text1 = f1.render('ввести название модуля тренировки', True, BLUE)
                    screen.blit(text1, (30, 40))
                    button2 = pygame.draw.rect(screen, (255, 255, 255), (20, 105, 450, 50))
                    f2 = pygame.font.SysFont('arial', 30)
                    text2 = f2.render('ввести название модуля торговли', True, BLUE)
                    screen.blit(text2, (30, 110))
                    pygame.display.flip()
                    s1=s2=''
                    flag=0
                elif event.key==pygame.K_ESCAPE and flag==6:
                    flag=5
                elif event.key==pygame.K_RETURN:
                    if flag==1:
                        try:
                            print('---')
                            f=open(s1)
                            f.close()
                            print('Opened')
                            trainmod=s1.split('.')[0]
                            if trainmod:
                                # p2=Process()
                                ab.reading(path)
                                ab.training(trainmod)
                                print('--=-=-')





                        except FileNotFoundError:
                            screen.fill(BLACK)
                            button=pygame.draw.rect(screen,WHITE,(100,200,300,100))
                            f1 = pygame.font.SysFont('arial', 35)
                            text=f1.render('такого файла нет',True,RED)
                            screen.blit(text,(130,225))
                            flag=3
                            pygame.display.flip()
                    elif flag==2:
                        try:
                            print('--')
                            f=open(s2)
                            f.close()
                            print('Opened')
                            traidmod=s2.split('.')[0]
                            if traidmod:
                                if traidmod:
                                    flag = 5
                                    qwer=ab.traiding(traidmod,money)
                                    print('сейчас история портфолио в интерфейсе')
                                    print(ab.totalvaluess)

                                    # ab.portfoliohistory()
                                    # ab.printing('+МосЭнерго')



                        except FileNotFoundError:
                            screen.fill(BLACK)
                            button=pygame.draw.rect(screen,WHITE,(100,200,300,100))
                            f1 = pygame.font.SysFont('arial', 35)
                            text=f1.render('такого файла нет',True,RED)
                            screen.blit(text, (130, 225))
                            flag=3
                            pygame.display.flip()

                    elif flag==6:
                        if s3!= 'портфель':
                            ab.printing(s3)
                        else:
                            ab.portfoliohistory()

                elif flag==1 :
                    # print(event.scancode, event.key, event.unicode)
                    if event.key==pygame.K_BACKSPACE:
                        s1=s1[:-1]
                    else:
                        s1+=event.unicode
                    button1 = pygame.draw.rect(screen, (255, 255, 255), (20, 35, 450, 50))
                    button2 = pygame.draw.rect(screen, (255, 255, 255), (20, 105, 450, 50))
                    pygame.draw.line(screen, BLACK, [25, 75], [465, 75], 2)
                    text1=f1.render(s1,True,BLUE)
                    screen.blit(text1,(30,40))
                    pygame.display.flip()

                elif flag==2:
                    if event.key==pygame.K_BACKSPACE:
                        s2=s2[:-1]
                    else:
                        s2+=event.unicode
                    button1 = pygame.draw.rect(screen, (255, 255, 255), (20, 35, 450, 50))
                    button2 = pygame.draw.rect(screen, (255, 255, 255), (20, 105, 450, 50))
                    pygame.draw.line(screen, BLACK, [25,145],[465,145],2)
                    text2 = f1.render(s2, True, BLUE)
                    screen.blit(text2, (30, 110))
                    pygame.display.flip()

                elif flag==6:
                    if event.key==pygame.K_BACKSPACE:
                        s3=s3[:-1]
                    else:
                        s3+=event.unicode
                    button1 = pygame.draw.rect(screen, (255, 255, 255), (20, 35, 450, 50))
                    pygame.draw.line(screen, BLACK, [25, 75], [465, 75], 2)
                    text1=f1.render(s3,True,BLUE)
                    screen.blit(text1,(30,40))
                    pygame.display.flip()

            elif flag==5:
                screen.fill(BLACK)
                button1 = pygame.draw.rect(screen, (255, 255, 255), (20, 35, 450, 50))
                f1 = pygame.font.SysFont('arial', 30)
                text1 = f1.render('ввести название компании', True, BLUE)
                screen.blit(text1, (30, 40))
                pygame.display.flip()

def check(q):
    if q==1:
        if trainmod:
            return trainmod
    elif q==2:
        if trainmod and traidmod:
            return traidmod
def checkrun():
    if runGame==False:
        return 0