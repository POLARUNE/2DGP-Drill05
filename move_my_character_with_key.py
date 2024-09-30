from pico2d import *


open_canvas()
bg = load_image('TUK_GROUND.png')
character = load_image('adventurer_sprite_sheet_v1.1.png')


def handle_events():
    global running, dirx, diry

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx += 1
            elif event.key == SDLK_LEFT:
                dirx -= 1
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_LEFT:
                dirx += 1
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1

running = True
x = 800 // 2
y = 90

frame = 0
dirx = 0
diry = 0

while running:
    clear_canvas()
    bg.draw(400, 300)
    character.clip_draw(frame*32,192,32,32,x,y,150,150)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dirx * 10
    y += diry * 10
    delay(0.05)

close_canvas()

