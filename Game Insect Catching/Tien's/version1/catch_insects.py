import pyglet

window = pyglet.window.Window(1280, 720)
pyglet.resource.path = ['/tmp/guest-v0480i/Desktop/nvntien/game/resources']
pyglet.resource.reindex()
image = image = pyglet.resource.image('white_bubble.png')
sprite = pyglet.sprite.Sprite(image)

@window.event
def on_draw():
    window.clear()
    sprite.draw()

def update(dt):
    # Move 100 pixels per second
    sprite.x += dt * 100

# Call update 60 times a second
pyglet.clock.schedule_interval(update, 1/60.)

pyglet.app.run()


def displaying_background():

def run_game():
    # the entrance of game (botton: play, quit, the best score => the player click the botton PLAY)
        # create botton ....
        # add some funny music
        # working with mouse: click QUIT => off
        # working with mouse: click PLAY => RUN GAME
    # function shows the background (the score in the top of left, the time (60s) in the top of right, the net controls by player)
        # change new background
        # set the score => start : 0 point
        # set the time =>  60s countdown
        # appearance the net, and move the net by mouse => working with mouse
        # change music theme
    # while (60s countdown):
        # function drops the bees random (about 150-200 bees in 60 seconds)
        # Each click of player:
            # create a balloon (hold in 1-2s)
            # function check the distance between bee and net (the distance < 1.5cm from the heart of net => CATCH)
            # if catch:
                # if the bee:
                    # add short sound => ting tongg (funny)
                    # score ++

                # else the bad_bee or bommmm or ......:
                    # add short sound => troll
                    # score --
    # result
        # output score
run_game()
