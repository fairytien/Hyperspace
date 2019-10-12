import pyglet
from random import randint
from pyglet.window import key
window = pyglet.window.Window(1280, 960)
label = pyglet.text.Label("Hello World",
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=580,
                          anchor_x='center', anchor_y='top')
batch = pyglet.graphics.Batch()
floor = pyglet.image.load('Pictures/floor.png')
cloud = pyglet.image.load('Pictures/cloud.png')
sprite = [
        pyglet.sprite.Sprite(img=cloud, x=1280, y= 900, batch=batch),
        pyglet.sprite.Sprite(img=cloud, x=1480, y= 780, batch=batch),
        pyglet.sprite.Sprite(img=cloud, x=1680, y= 900, batch=batch),
        pyglet.sprite.Sprite(img=cloud, x=1880, y= 780, batch=batch),
        pyglet.sprite.Sprite(img=cloud, x=2080, y= 900, batch=batch),
        pyglet.sprite.Sprite(img=cloud, x=2280, y= 780, batch=batch)
]
floor = pyglet.sprite.Sprite(img=floor, x=0, y= -200)
character1 = pyglet.image.load_animation('Pictures/nhanvat.gif')
character =pyglet.sprite.Sprite(img=character1, x=0, y= 50)
@window.event
def on_draw():
    window.clear()
    batch.draw()
    floor.draw()
    character.draw()
@window.event
def update(dt):
    for i in sprite:
        i.x -= 10
        if i.x < 0:
            i.x = 1280
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.RIGHT:
        character.x += 10
    if symbol == key.LEFT:
        character.x -= 10

pyglet.clock.schedule_interval(update, 1/30)
pyglet.app.run()
