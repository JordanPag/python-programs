class Things:
    pass

class Inanimate(Things):
    pass

class Animate(Things):
    pass

class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    def breathe(self):
        print('breathing')
    def move(self):
        print('moving')
    def eat_food(self):
        print('eating food')

class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')

class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        self.eat_food()
    def find_food(self):
        self.move()
        print("I've found food!")
        self.eat_food()
    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()
    def __init__(self, spots):
        self.giraffe_spots = spots
    def left_foot_forward(self):
        print('Left foot forward')
    def right_foot_forward(self):
        print('Right foot forward')
    def left_foot_backward(self):
        print('Left foot back')
    def right_foot_backward(self):
        print('Right foot back')
    def dance(self):
        self.left_foot_forward()
        self.left_foot_backward()
        self.right_foot_forward()
        self.right_foot_backward()
        self.left_foot_backward()
        self.right_foot_backward()
        self.right_foot_forward()
        self.left_foot_forward()

reginald = Giraffes(200)
harold = Giraffes(15)
