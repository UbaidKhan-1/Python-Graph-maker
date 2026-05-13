import random
import math
import pygame as pg

pg.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 720, 1500
SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_color = "white"
clock = pg.time.Clock()

x_limit = 360
y_limit= SCREEN_HEIGHT/4
orig =[SCREEN_WIDTH/2, y_limit]
STEP= 50
dx = 0.5

text_size = 20
text_color = "black"
font = pg.font.Font(None, text_size)
font2 = pg.font.Font(None, 70)
font3 = pg.font.Font("Assets/DancingScript-Bold.ttf", 100)


x = -10
initial_x = x
goal = 10
# function specific values
points = []
points1 = []

#               ((((((((((((()))))))))))))

point_size = 5
point_color = "black"

graph_line_color = "black"
graph_line_thickness = 3
Plane_line_color = "purple"
scale_lines_color = "red"

projection = True			
display_y_coordinate = False
projection_lines_color = "red"


#                      (    functions    )

def f(x):
	y = (x**2)-(4*x)
	return y
	
def f1(x):
	y = x**2
	return y
		
#((((((((((((((((((((()))))))))))))))))))))))	
	
class PLANE:
	def __init__(self, origin, x_limit, y_limit):
		self.origin = origin
		self.x_limit = x_limit
		self.y_limit= y_limit
		
	def draw(self):
		pg.draw.circle(SCREEN, "black", (self.origin[0], self.origin[1]), 5)
		pg.draw.line(SCREEN, Plane_line_color, (self.origin[0]-self.x_limit, self.origin[1]), (self.origin[0]+self.x_limit, self.origin[1]), 3)
		pg.draw.line(SCREEN, Plane_line_color, (self.origin[0], self.origin[1]+self.y_limit), (self.origin[0],self.origin[1]-self.y_limit), 3)
		
		#Drawing scale lines and blitting text on y_axis
		for i in range(int((self.y_limit)/STEP)):
			#for positive
			x1 = self.origin[0] - 5
			x2 = self.origin[0] + 5
			y = self.origin[1] - i*STEP
			pg.draw.line(SCREEN, scale_lines_color, (x1,y), (x2,y), 3)
			if i> 0:
				text = font.render(str(i), True, text_color)
				text_rect = text.get_rect(center = (x1-text_size, y))
				SCREEN.blit(text, text_rect)
				
			#for negative
			y = self.origin[1] + i*STEP
			pg.draw.line(SCREEN, scale_lines_color, (x1,y), (x2,y), 3)
			if i>0:
				text = font.render(str(-i), True, text_color)
				text_rect = text.get_rect(center = (x1-text_size, y))
				SCREEN.blit(text, text_rect)
	
	
	#Drawing scale lines and blitting text on x_axis
		for i in range(int((self.x_limit*2)/STEP)):
			#for positive
			y1 = self.origin[1] - 5
			y2 = self.origin[1] + 5
			x = self.origin[0] + i*STEP
			pg.draw.line(SCREEN, scale_lines_color, (x,y1), (x,y2), 3)
			if i>0:
				text = font.render(str(i), True, text_color)
				text_rect = text.get_rect(center = (x, y1-text_size))
				SCREEN.blit(text, text_rect)
				
			#for negative
			x = self.origin[0] - i*STEP
			pg.draw.line(SCREEN, scale_lines_color, (x,y1), (x,y2), 3)
			if i > 0:
				text = font.render(str(-i), True, text_color)
				text_rect = text.get_rect(center = (x, y1-text_size))
				SCREEN.blit(text, text_rect)
	#(((((((((((((((((((((((((())))))))))))))))))))))))))
	
	
	def plot(self, points):
		x = 0
		y = 1
		for point in points:
				
			#projecting on x and y axis
					if projection == True:
						pg.draw.line(SCREEN, projection_lines_color, (self.origin[0]+point[x]*STEP, self.origin[1]-point[y]*STEP), (self.origin[0]+point[x]*STEP, self.origin[1]), graph_line_thickness)
						pg.draw.line(SCREEN, projection_lines_color, (self.origin[0]+point[x]*STEP, self.origin[1]-point[y]*STEP), (self.origin[0], self.origin[1]-point[y]*STEP), graph_line_thickness)
						
						#only ploting the points that lie within the graph
					if self.origin[1] - point[1]*STEP > self.origin[1] - self.y_limit and self.origin[1] - point[1]*STEP < self.origin[1] + self.y_limit:
						pg.draw.circle(SCREEN, point_color, (self.origin[0]+point[x]*STEP , self.origin[1]-point[y]*STEP), point_size)
						if display_y_coordinate:	
							text = font.render(str(point[y]),True, text_color)
							text_rect = text.get_rect(center = ((self.origin[0]+point[x]*STEP) -(text_size+5), self.origin[1]-point[y]*STEP))
							SCREEN.blit(text, text_rect)
						#drawing a line between each point, connecting the points together
						if (points.index(point)+1) < len(points):
								pg.draw.line(SCREEN, graph_line_color, (self.origin[0]+point[x]*STEP , self.origin[1]-point[y]*STEP ),(self.origin[0]+points[points.index(point)+1][x]*STEP , self.origin[1]-points[points.index(point)+1][y]*STEP), graph_line_thickness)
					if run_count == 0:
						pg.display.update()


cartesian_plane = PLANE(orig, x_limit, y_limit)

class Slider:
	def __init__(self):
		self.x = 0
		self.y = orig[1] + y_limit
		self.dx = 0
		self.sliderwidth = 150
		self.default_sliderx = self.x + SCREEN_WIDTH-10-self.sliderwidth
		self.sliderx = self.default_sliderx
		self.height = 50
		self.previousx = self.default_sliderx
		
	def make_slider(self):
		pg.draw.rect(SCREEN, "grey", (self.x + 10, self.y, SCREEN_WIDTH-20, self.height))
		pg.draw.rect(SCREEN, "dark grey", (self.sliderx, self.y+2, 150, self.height-5))
		
	def detect_sliding(self, x, y):
		if y > self.y and y < self.y + self.height:
			if x != self.previousx:
				if x < self.default_sliderx:
					self.sliderx = x
					self.dx = x - self.previousx
				else:
					self.sliderx = self.default_sliderx
					self.dx = x - self.previousx
				self.updateglobal()
				self.previousx = x
			else:
				pass
		else:
			pass
	
	def updateglobal(self):
		global STEP
		STEP += self.dx * 0.05
		
slider = Slider()

running = True
run_count = 0
while running:
	clock.tick(60)
	mx, my = pg.mouse.get_pos()
	events = pg.event.get()
	for event in events:
		if event.type == pg.QUIT:
			running = False
	
	SCREEN.fill(screen_color)
	cartesian_plane.draw()
	
	text = font2.render("("+"X = " +str(int(initial_x))+ " - " + str(int(goal)) + ")", True, "black")
	text2 = font3.render("f(x) = tan-¹(x)", True, "dark green")
	
	
	text_rect = text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT-(SCREEN_HEIGHT/8)))
	text2_rect = text2.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT-(SCREEN_HEIGHT/2)+150))
	
	
	SCREEN.blit(text, text_rect)
	SCREEN.blit(text2, text2_rect)
	
	# finding all points
	while True:
		if x <= goal:
		    try:
		        y1 = f(x)
		        y2 = f1(x)
		        
		        # Skip complex values explicitly
		        if isinstance(y1, complex):
		            x += dx
		            continue
		        points.append([x,y1])
		        #points1.append([x, y2])
		        x += dx
		    except:
		        x += dx
		    pg.display.update()
		    continue
		break
	
	
	
	#ploting points
	cartesian_plane.plot(points)
	cartesian_plane.plot(points1)
	slider.make_slider()
	slider.detect_sliding(mx, my)
	
	run_count += 1
	if run_count%(60*3) == 0:
		x = random.randint(-10, 0)
		initial_x = x
		run_count = 0
		points = []

	pg.display.update()