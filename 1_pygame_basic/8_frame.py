import pygame

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ#
#기본 초기화 (반드시 해야하는 것들)
pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#타이틀 설정
pygame.display.set_caption("CDH Game") #게임 이름

#FPS
clock = pygame.time.Clock()

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ#

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)



# 이벤트 루프
running = True #게임이 진행중인지 확인
while running:
    dt = clock.tick(60) #dt는 델타, 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): #어떤 이벤트가 발생하는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하는가?
            running = False #pygame 종료로 넘어감
    

    #3. 게임 캐릭터 위치 정의
    

    #4. 충돌 처리
    

    #5. 화면에 그리기
    

    pygame.display.update() #게임화면을 매프레임 다시 그리기
 

#잠시 대기
pygame.time.delay(1000) #1초 정도 대기 (1000ms)

#pygame 종료
pygame.quit()