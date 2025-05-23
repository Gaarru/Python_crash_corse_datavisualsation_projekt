from random import choice

class RandomWalk():
    def __init__(self, num_points=500):
        self.numpoints = num_points
        self.x_values = [0]
        self.y_values = [0]
        
        
    def fill_walk(self):
        while len(self.x_values) < self.numpoints:
            x_direction = choice([1, -1])
            x_distence = choice([0, 1, 2, 3, 4,])
            x_step = x_direction * x_distence
            
            y_direction = choice([1, -1])
            y_distence = choice([0, 1, 2, 3, 4,])
            y_step = y_direction * y_distence
            
            if x_step == 0 and y_step == 0:
                continue
            
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)