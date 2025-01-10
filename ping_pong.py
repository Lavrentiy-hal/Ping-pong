from pygame import *
class GameSprite():
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_W] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_S] and self.rect.y < 450:
            self.rect.y += self.speed
    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
back = (200, 255, 255)
win_with = 600
win_height = 500
window = display.set_mode((win_with, win_height))
window.fill(back)
player1 = Player('png-klev-club-utft-p-zemlya-dlya-igri-png-21.png', 30, 100, 5)
player2 = Player('png-klev-club-utft-p-zemlya-dlya-igri-png-21.png', 450, 100, 5)
clock = time.Clock()
FPS = 60
game = True
while game:
    for e in event.get():
        if e.type ==QUIT:
            game = False

    player1.draw(window)
    player2.draw(window)
    player1.update_l()
    player2.update_r()
    display.update()
    clock.tick(FPS)

