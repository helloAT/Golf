from Ball import ball

class obstacles:
    def check_boundary_collision(self, player):
        if player.location.x - 25 <= 0:
            player.location.x = 26
            player.velocity.x *= -1
        elif player.location.x + 25 >= 1366:
            player.location.x = width - 26
            player.velocity.x *= -1
            
        if player.location.y - 25 <= 0 :
            player.location.y = 26
            player.velocity.y *= -1
        elif player.location.y + 25 >= 768:
            player.location.y = height - 26
            player.velocity.y *= -1
    
    def display_lines(self, level):
        strokeWeight(5)
        global obstacle_list
        if level == 0:
            obstacle_list = []

        elif level == 1:
            obstacle_list = [[width * 1/6, 0, width * 1/6, height - 100], [width * 2/6, 100, width * 2/6, height], [width * 3/6, 0, width * 3/6, height - 100], [width * 4/6, 100, width * 4/6, height], [width * 5/6, 0, width * 5/6, height - 100]]
            fill(0)
            ellipse(width * 11/12, 100, 75, 75)
        
        #if level == 2:
        
        for i in obstacle_list:
            line(i[0], i[1], i[2], i[3])
    
    def check_obstacle_collision(self, player, level):
        buffer = abs(player.velocity.x * 0.6)
        if buffer < 5:
            buffer = 5
        for i in obstacle_list:
            if dist(i[0], i[1], i[2], i[3]) <= dist(player.location.x, player.location.y, i[0], i[1]) + dist(player.location.x, player.location.y, i[2], i[3]) < dist(i[0], i[1], i[2], i[3]) + buffer:
                player.velocity.x *= -1
                if player.velocity.x > 0:
                    player.location.x += 2
                else:
                    player.location.x -= 2
        
        if dist(player.location.x, player.location.y, width * 11/12, 100) <= 50:
            player.location = PVector(51, 51)
            level += 1
            player.velocity = PVector(0, 0)
