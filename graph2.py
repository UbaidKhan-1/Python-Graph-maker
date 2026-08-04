import pygame
import random
import math
pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 720, 1500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# settings
canvascolor = "white"
plane_line_thickness = 3
graph_line_thickness = 3
graph_text_color = "dark green"
scale_text_color = "black"
plane_lines_color = "black"
scale_line_color = "red"
graph_text_size = 30
scale_text_size = 20
origin = [WIDTH//2, HEIGHT//4 + 100]
x_limit = WIDTH/2.2
y_limit = WIDTH/2
x_step = 50
y_step = 50
point_size = 3
dx = 0.5#use fractions with denominator 2 to avoid data misrepresentation in binary
plot_range = (-10, 10)
draw_line = True
project_on_xaxis = False
project_on_yaxis = False
show_coordinates = False
progressively_draw_graph = True

#list of tuples containing functions to be graphed and their colors
functions = [(lambda x: x**2 -1, "red"),
			(lambda x: x+1,  "purple")]
#___________________________________
	
# Experimental circle point function	
def getcirclepoints(radius, resolution):
	points = []
	for i in range(resolution+1):
		angle = i * (360/resolution)
		x = radius*math.sin(math.radians(angle))
		y = radius*math.cos	(math.radians(angle))
		point = (x, y)
		points.append(point)
	return points
#_____________________________

def draw_text(fnt, string,color,position, size):
	font = pygame.font.SysFont(fnt, size)
	text_surface = font.render(string, True, color)
	text_rect = text_surface.get_rect(center=position)
	SCREEN.blit(text_surface, text_rect)
	
#_______________________________


#((((((((((((((((((((((((((()))))))))))))))))))))))))))
class cartesian_plane:
	def __init__(self, origin, x_limit, y_limit, x_step, y_step):
		self.origin = origin
		self.x_limit = x_limit
		self.y_limit = y_limit
		self.x_step = x_step
		self.y_step = y_step
		self.runtime = 0
		
	def draw_plane(self):
		originx = self.origin[0]
		originy = self.origin[1]
		
#     drawing axis lines
		pygame.draw.line(SCREEN, plane_lines_color, (originx, originy-self.y_limit), (originx,originy+self.y_limit), plane_line_thickness)
		
		draw_text('Ariel', " +y ", graph_text_color, (originx, originy-self.y_limit-graph_text_size/2), graph_text_size)
		draw_text('Ariel', " -y ", graph_text_color, (originx, originy+self.y_limit+graph_text_size/2), graph_text_size)
		    
		pygame.draw.line(SCREEN, plane_lines_color, (originx-self.x_limit, originy), (originx+self.x_limit, originy), plane_line_thickness)
		
		draw_text('Ariel', "  +x ", graph_text_color, (originx+self.x_limit+graph_text_size/2, originy), graph_text_size)
		draw_text('Ariel', " -x", graph_text_color, (originx-self.x_limit-graph_text_size/2, originy), graph_text_size)
		#_____________________________
		
#drawing scale lines
         # for x-axis
		for i in range(round(self.x_limit/self.x_step)):
			#for positive
			pygame.draw.line(SCREEN, scale_line_color, (originx+i*self.x_step, originy-5), (originx+i*self.x_step, originy+5), plane_line_thickness)
			
			# for negative
			pygame.draw.line(SCREEN, scale_line_color, (originx-i*self.x_step, originy-5), (originx-i*self.x_step, originy+5), plane_line_thickness)
			
		#drawing scale text for x-axis
			if i!=0:
				draw_text('Ariel', str(-i), scale_text_color, (originx-i*self.x_step, originy-5-scale_text_size/2), scale_text_size)
				draw_text('Ariel', str(i), scale_text_color, (originx+i*self.x_step, originy-5-scale_text_size/2), scale_text_size)
			
		#for y-axis
		for i in range(int(self.y_limit/self.y_step)):
			#for positive
			pygame.draw.line(SCREEN, scale_line_color, (originx-5, originy-i*self.y_step), (originx+5, originy-i*self.y_step), plane_line_thickness)
			
			
			# for negative
			pygame.draw.line(SCREEN, scale_line_color, (originx-5, originy+i*self.y_step), (originx+5, originy+i*self.y_step), plane_line_thickness)
			
			# drawing scale text for y-axis
			if i!=0:
				draw_text('Ariel', str(i), scale_text_color, (originx+5+scale_text_size/2, originy-i*self.y_step), scale_text_size)
				draw_text('Ariel', str(-i), scale_text_color, (originx+5+scale_text_size/2, originy+i*self.y_step), scale_text_size)
#______________________________
	
		
	def plot(self, functions, rnge):
		for func, projection_color in functions:
			points = []
			x = rnge[0]
			goal = rnge[1]
			while x<=goal:
				try:
					y = func(x)
					points.append((x, func(x)))
					x+=dx
				except:
					x+=dx
				
			#plotting obtained points
			originx = self.origin[0]
			originy = self.origin[1]
			#graph boundaries
			left_bound=originx-self.x_limit
			right_bound=originx+self.x_limit
			top_bound=originy-self.y_limit
			bottom_bound=originy+self.y_limit
			for point in points:
					#coordinates
					x = originx + point[0]*self.x_step
					y = originy - point[1]*self.y_step
					
					if right_bound>=x>=left_bound and bottom_bound>=y>=top_bound:# prevents the points outside of graph area from being plotted
					
						if show_coordinates:
							if points.index(point)%(1/dx)==0:# shows coordinates (only for the points with whole number x coordinates
								draw_text('Ariel', "("+str(round(point[0],1))+", "+str(round(point[1],1))+")", scale_text_color, (x, y-10), scale_text_size)
					#________________________
					
					# projects on axis
						if project_on_yaxis:
							pygame.draw.line(SCREEN, projection_color, (x, y), (originx, y), graph_line_thickness)
						if project_on_xaxis:
							pygame.draw.line(SCREEN, projection_color, (x, y), (x, originy), graph_line_thickness)
					#_______________________
					

						
						if points.index(point)<len(points)-1:#prevents index out of range
							x2= originx + points[points.index(point)+1][0]*self.x_step
							y2= originy - points[points.index(point)+1][1]*self.y_step
								
							if draw_line and right_bound>=x2>=left_bound and bottom_bound>=y2>=top_bound: # prevents the line from overshooting past the last plotted point in the graph
								pygame.draw.line(SCREEN, projection_color, (x, y), (x2, y2), graph_line_thickness)
						
						pygame.draw.circle(SCREEN, projection_color, (x, y), point_size)# drawing the points after line so they are drawn pn top of line but they are two levels above in if-structure
														
					if not self.runtime:
						if progressively_draw_graph:
							pygame.display.update()
		self.runtime +=1



# SCALE SLIDER
class Slider:
	def __init__(self, plane):
		self.x = 0
		self.y = origin[1] + y_limit + graph_text_size
		self.dx = 0
		self.sliderwidth = 150
		self.default_sliderx = self.x + WIDTH-10-self.sliderwidth
		self.sliderx = self.default_sliderx
		self.height = 50
		self.plane = plane
		self.previousx = self.default_sliderx
		
	def make_slider(self):
		pygame.draw.rect(SCREEN, "grey", (self.x + 10, self.y, WIDTH-20, self.height))
		pygame.draw.rect(SCREEN, "dark grey", (self.sliderx, self.y+2, 150, self.height-5))
		
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
		self.plane.x_step += self.dx * (x_step/WIDTH)
		self.plane.y_step += self.dx* (y_step/WIDTH)
		
		
#((())))))(((((())))))(((((())))))(((((())))))(((((())))
		

def main():
	plane = cartesian_plane(origin, x_limit, y_limit, x_step, y_step)
	slider = Slider(plane)
			
	run = True
	while run:
		clock.tick(60)
		mx,my = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				break
				
		
		SCREEN.fill(canvascolor)
		
		slider.make_slider()
		slider.detect_sliding(mx, my)
		plane.draw_plane()
		plane.plot(functions, plot_range)
		pygame.display.update()
		
if __name__=="__main__":
	main()