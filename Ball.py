class ball:    
    def __init__(self):
        self.location = PVector(51, 51)
        self.velocity = PVector(0, 0)
    
    def display_ball(self):
        strokeWeight(0)
        fill(255)
        ellipse(self.location.x, self.location.y, 50, 50)
    
    def hit_ball(self):
        self.location.add(self.velocity)
        self.velocity.mult(0.94)
