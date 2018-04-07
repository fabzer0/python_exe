import turtle
my_turtle = turtle.Turtle()
my_win = turtle.Screen()


def pentagon(my_turtle, line_len):
	if line_len > 0:
		my_turtle.left(60)
		my_turtle.forward(line_len)
		my_turtle.right(80)
		my_turtle.forward(line_len)
		my_turtle.right(60)
		my_turtle.forward(line_len)
		my_turtle.right(80)
		my_turtle.forward(line_len)
		my_turtle.right(80)
		my_turtle.forward(line_len)
		my_turtle.right(120)
		pentagon(my_turtle, line_len-5)
		


pentagon(my_turtle, 100)
my_win.exitonclick()

