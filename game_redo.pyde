from Ball import ball
from Obstacles import obstacles
from Menu import menu

def setup():
    global first_click, released, player, lines, level, mouse_origin, strength
    size(1366, 768)
    first_click = True
    released = True
    player = ball()
    lines = obstacles()
    level = 0
    mouse_origin = PVector(0, 0)
    strength = 0

def draw():
    global strength
    background(0, 255, 0)
    lines.display_lines(level)
    if not released:
        strokeWeight(2)
        line(mouse_origin.x, mouse_origin.y, mouseX, mouseY)
    player.display_ball()
    strokeWeight(2)
    fill(255)
    rect(1281, 583, 60, 160)
    for i in range(int(strength * 140 / 75)):
        if i > 70:
            i -= 70
            stroke(255, 255 - (i * 255 / 140), 0)
            i += 70
        else:
            stroke(i * 255 / 140 + 150, 255, 0)
        line(1291, 733 - i, 1331, 733 - i)
    stroke(0)
    player.hit_ball()
    lines.check_boundary_collision(player)
    lines.check_obstacle_collision(player, level)
    if level == 0:
        menu()


def mouseDragged():
    global first_click, mouse_origin, released, strength
    released = False
    if first_click:
        mouse_origin = PVector(mouseX, mouseY)
        first_click = False
    strength = dist(mouse_origin.x, mouse_origin.y, mouseX, mouseY) * 0.3
    if strength > 75:
        strength = 75

def mouseReleased():
    global first_click, released, strength
    first_click = True
    released = True
    mouse_end = PVector(mouseX, mouseY)
    velocity = PVector.sub(mouse_origin, mouse_end)
    player.velocity = velocity * 0.3
    if player.velocity.x > 75 or player.velocity.x < -75:
        player.velocity.x = abs(player.velocity.x) / player.velocity.x * 75
    if player.velocity.y > 75 or player.velocity.y < -75:
        player.velocity.y = abs(player.velocity.y) / player.velocity.y * 75
    strength = 0

def mousePressed():
    global level
    if level == 0 and 610 <= mouseX <= 759 and 347 <= mouseY <= 421:
        level += 1
