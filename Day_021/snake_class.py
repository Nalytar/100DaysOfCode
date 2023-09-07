from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
# Should use more constants to for further tweaking of code


class Snake:
    def __init__(self):
        self.snake_body_parts = []
        for position in STARTING_POSITION:
            self.create_snake(position)

        self.snake_head = self.snake_body_parts[0]

    def create_snake(self, position):
        self.add_body_part(position)

    def add_body_part(self, position):
        self.snake_body_parts.append(Turtle("square"))
        self.snake_body_parts[-1].penup()
        self.snake_body_parts[-1].goto(position)
        self.snake_body_parts[-1].color("white")

    def extends(self):
        self.add_body_part(self.snake_body_parts[-1].position())

    def move(self):
        for part_number in range(len(self.snake_body_parts) - 1, 0, -1):
            new_x_part = self.snake_body_parts[part_number - 1].xcor()
            new_y_part = self.snake_body_parts[part_number - 1].ycor()
            self.snake_body_parts[part_number].goto(new_x_part, new_y_part)
        self.snake_body_parts[0].forward(DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def check_wall_collision(self):
        if self.snake_head.xcor() > 360 or self.snake_head.xcor() < -360 or self.snake_head.ycor() > 300 or self.snake_head.ycor() < -320:
            return True
        return False

    def hits_own_body(self):
        for part in self.snake_body_parts[1::]:
            if self.snake_head.distance(part) < 10:
                return True
        return False
