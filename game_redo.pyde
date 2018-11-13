from Ball import ball
from Obstacles import obstacles

def setup():
    global first_click, released, player, lines, level, mouse_origin
    size(1366, 768)
    first_click = True
    released = True
    player = ball()
    lines = obstacles()
    level = 1
    mouse_origin = PVector(0, 0)

def draw():
    background(127)
    lines.display_lines(1)
    if not released:
        strokeWeight(2)
        line(mouse_origin.x, mouse_origin.y, mouseX, mouseY)
    player.display_ball()
    strokeWeight(2)
    fill(255)
    rect(1291, 593, 50, 150)
    for i in range(150):
        
    player.hit_ball()
    lines.check_boundary_collision(player)
    lines.check_obstacle_collision(player, level)

def mouseDragged():
    global first_click, mouse_origin, released
    released = False
    if first_click:
        mouse_origin = PVector(mouseX, mouseY)
        first_click = False

def mouseReleased():
    global first_click, released
    first_click = True
    released = True
    mouse_end = PVector(mouseX, mouseY)
    velocity = PVector.sub(mouse_origin, mouse_end)
    player.velocity = velocity * 0.3
    if player.velocity.x > 75 or player.velocity.x < -75:
        player.velocity.x = abs(player.velocity.x) / player.velocity.x * 75
    if player.velocity.y > 75 or player.velocity.y < -75:
        player.velocity.y = abs(player.velocity.y) / player.velocity.y * 75
