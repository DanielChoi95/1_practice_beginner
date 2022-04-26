import pygame
from random import *

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height))


#타이틀 설정
pygame.display.set_caption("찬양이 피하기") #게임 이름

#FPS
clock = pygame.time.Clock()

#배경 불러오기
background = pygame.image.load("C:\\Users\\user\\Desktop\\PythonWorkspace\\pygame_basic\\background.png")

#내 캐릭터(스프라이트 불러오기)
character = pygame.image.load("C:\\Users\\user\\Desktop\\PythonWorkspace\\pygame_basic\\character1.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로 크기의 절반 위치
character_y_pos = screen_height - character_height

#이동할 좌표
to_x = 0

#이동 속도
character_speed = 0.6
enemy_speed = 9

# 적 캐릭터
enemy = pygame.image.load("C:\\Users\\user\\Desktop\\PythonWorkspace\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size #이미지의 크기를 구해옴
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randint(0, screen_width - enemy_width)
enemy_y_pos = 0


# 이벤트 루프
running = True #게임이 진행중인지 확인
while running:
    dt = clock.tick(60) #dt는 델타, 게임화면의 초당 프레임 수를 설정

    for event in pygame.event.get(): #어떤 이벤트가 발생하는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하는가?
            running = False #pygame 종료로 넘어감

        if event.type == pygame.KEYDOWN: #어떠한 키가 눌러졌는가?
            if event.key == pygame.K_LEFT: #왼쪽 방향키가 눌러졌다면
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: #오른쪽 방향키
                to_x += character_speed

        if event.type == pygame.KEYUP: #방향키 떼면
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #누르고 있던게 왼쪽이나 오른쪽이었다면
                to_x = 0  #이동 정지
         
    character_x_pos += to_x * dt # *dt로 fps 변동에 따른 이동속도 보정

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = randint(0, screen_width - enemy_width)
    
    #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width


    #충돌 처리
    character_rect = character.get_rect() #캐릭터의 크기 변수 설정
    character_rect.left = character_x_pos #캐릭터의 실제 좌표를 캐릭터 이미지에 업데이트
    character_rect.top = character_y_pos 

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 체크

    if character_rect.colliderect(enemy_rect):
        print("뿌직")
        running = False

    #screen.fill((0, 0, 255))
    screen.blit(background, (0,0))    #배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #적 그리기





    pygame.display.update() #게임화면을 매프레임 다시 그리기
 

#잠시 대기
pygame.time.delay(1000) 

#pygame 종료
pygame.quit()