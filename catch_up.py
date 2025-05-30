from pygame import *

#создай окно игры
window = display.set_mode((700,500))
display.set_caption('Dogonyalki') 
#задай фон сцены
background = transform.scale(image.load('background.png'),(700,500))
#создай 2 спрайта и размести их на сцене
sprite1 = transform.scale(image.load('sprite1.png'),(100,100))
sprite2 = transform.scale(image.load('sprite2.png'),(100,100))
clock = time.Clock()
FPS = 1000
clock.tick(FPS)
speed = 1
x1 = 350
y1 = 400
x2 = 350
y2 = 170
#обработай событие «клик по кнопке "Закрыть окно"»
game = True
while game:
    window.blit(background,(0,0))
    window.blit(sprite1,(x1,y1))
    window.blit(sprite2,(x2,y2))
    for i in event.get():
        if i.type == QUIT:
            game = False
    key_pressed = key.get_pressed()
    if key_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if key_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    if key_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if key_pressed[K_DOWN] and y1 < 395:
        y1 += speed
    if key_pressed[K_a] and x2 > 5:
        x2 -= speed
    if key_pressed[K_d] and x2 < 595:
        x2 += speed
    if key_pressed[K_w] and y2 > 5:
        y2 -= speed
    if key_pressed[K_s] and y2 < 395:
        y2 += speed
    display.update()
    clock.tick(FPS)

