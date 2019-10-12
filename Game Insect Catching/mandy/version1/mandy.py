import pyglet
import random

window = pyglet.window.Window(1250,750)
pyglet.resource.path = ['/tmp/guest-9d86yl/mandy/resources']
pyglet.resource.reindex()

label_game = pyglet.text.Label('Beeeeeee Happy!',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
score_label = pyglet.text.Label(text="Score: ", x=15, y=720)
level_label = pyglet.text.Label(text="Time: ",
                                x=1200, y=720, anchor_x='center')

background = pyglet.resource.image('garden7.jpg')
bee1 = pyglet.resource.image.load_animation('bee3.gif')
bee2 = pyglet.resource.image('bee4.gif')
bad_bee1 = pyglet.resource.image('bee7.gif')
bad_bee2 = pyglet.resource.image('bee13.gif')

small_bee1 = pyglet.resource.image('bee9.gif')
bee3 = pyglet.resource.image('bee12.gif')

@window.event
def on_draw():
    window.clear()
    level_label.draw()
    label_game.draw()
    score_label.draw()
    background.blit(0, 0)
    bee1.blit(500,200)
    #bad_bee1.blit(20,20)



pyglet.app.run() #call the game
