import pyglet
from pyglet import window
import random

pyglet.resource.path = ['/tmp/guest-pidbbe/Desktop/Game Insect Catching/Tien_s/resources']
pyglet.resource.reindex()

window = pyglet.window.Window(1280,720, "Bee game",resizable=True,style = window.Window.WINDOW_STYLE_DIALOG)
window.set_minimum_size(900,550) # giao dien min

label_game = pyglet.text.Label('Beeeeeee Happy!',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
score_label = pyglet.text.Label(text="Score: ", x=15, y=720)
level_label = pyglet.text.Label(text="Time: ",
                                x=1200, y=720, anchor_x='center')

background = pyglet.resource.image('garden7.jpg')


#bubble_image = pyglet.image.load_animation('white_bubble.png')
#bubbleSprite = pyglet.sprite.Sprite(bubble_image)

#class PhysicalObject(pyglet.sprite.Sprite):
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.velocity_x, self.velocity_y = 0.0, 0.0
#    def update(self, dt):
#        self.x += self.velocity_x * dt
#        self.y += self.velocity_y * dt

bee1 = pyglet.image.load_animation('bee.gif')
bee2 = pyglet.image.load_animation('bee2.gif')
bee3 = pyglet.image.load_animation('bad_bee1.gif')
bee4 = pyglet.image.load_animation('fly.gif')

resects = [
bee1Sprite = pyglet.sprite.Sprite(bee1, x = random.randint(-1000, -10), y = random.randint(5, 700), batch = batch)
bee2Sprite = pyglet.sprite.Sprite(bee2, x = random.randint(-1000, -10), y = random.randint(5, 700), batch = batch)
bee3Sprite = pyglet.sprite.Sprite(bee3, x = random.randint(-1000, -10), y = random.randint(5, 700), batch = batch)
bee1Sprite = pyglet.sprite.Sprite(bee1, x = random.randint(-1000, -10), y = random.randint(5, 700), batch = batch)
]

bees = []
def create_bees(num_bees):
    global bee_position
    bee_position = []
    for i in range(num_bees):
        bee_x = random.randint(-10000, 50)
        bee_y = random.randint(100, 620)
        bee_position.append([bee_x, bee_y])
        bee_image = pyglet.image.load_animation('/tmp/guest-pidbbe/Desktop/Game Insect Catching/Tien_s/resources/bee3.gif')
        new_bee = pyglet.sprite.Sprite(img=bee_image, x=bee_x, y=bee_y)
        bees.append(new_bee)
    return bees

create_bees(100)

@window.event
def on_draw():
    window.clear()
    background.blit(0, 0)
    level_label.draw()
    label_game.draw()
    score_label.draw()
    for bee in bees:
        bee.draw()

def update(dt):
    for bee in bees:
        bee.x += random.randint(0, 20)
        bee.y += random.randint(-5, 5)

#def update(dt):
#    for bee in bees:
#        bee.x += dt * 100
#        bee.y += dt * 10

# Call update 60 times a second
pyglet.clock.schedule_interval(update, 1/60.)

from pyglet.window import mouse

@window.event
def on_mouse_motion(x, y, dx, dy):
    pass

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        pass

@window.event
def on_mouse_enter(x, y):
    pass

@window.event
def on_mouse_leave(x, y):
    pass

mouse_cursor_image = pyglet.resource.image('net.png')
cursor = pyglet.window.ImageMouseCursor(mouse_cursor_image, 16, 8)
window.set_mouse_cursor(cursor)

pyglet.app.run() #call the game
