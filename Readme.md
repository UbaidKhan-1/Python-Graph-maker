📈 Python Graph Maker (Pygame)

A real-time 2D graph plotting application built using Python and Pygame.
It renders a customizable Cartesian plane and plots mathematical functions dynamically, with support for multiple functions, scaling, projections, and progressive rendering.


---

🚀 Features

📊 Draws a fully labeled Cartesian coordinate system

📈 Plots multiple mathematical functions simultaneously

🎨 Custom colors for each function

⚡ Progressive graph rendering (animation-style plotting)

📏 Adjustable scale using an interactive slider

📍 Optional coordinate display on points

📉 Axis projection lines (x-axis / y-axis projections)

🔢 Safe numerical stepping to reduce floating-point errors

🧠 Supports any Python lambda-based function input



---

🧮 Example Functions

You can define functions like this:

functions = [
    (lambda x: x**2 - 1, "red"),
    (lambda x: x + 1, "purple")
]

Each function is a tuple:

(function, color)


---

🖥️ Preview

The program displays:

![Graph Preview](assets/graph.png)

---

⚙️ Configuration Options

You can customize the graph behavior using these variables:

canvascolor = "white"
plane_line_thickness = 3
graph_line_thickness = 1
graph_text_color = "dark green"
scale_text_color = "black"
plane_lines_color = "black"
scale_line_color = "red"

📌 Graph Settings

origin = [WIDTH//2, HEIGHT//4 + 100]
x_limit = WIDTH/2.2
y_limit = WIDTH/2
x_step = 50
y_step = 50
dx = 0.5
plot_range = (-10, 10)


---

🎛️ Optional Features

You can toggle features by changing these flags:

draw_line = True
project_on_xaxis = False
project_on_yaxis = False
show_coordinates = False
progressively_draw_graph = True


---

📦 Requirements

Install dependencies:

pip install pygame


---

▶️ How to Run

Clone the repository:

git clone https://github.com/UbaidKhan-1/Python-Graph-maker.git

cd Python-Graph-maker

Run the program:
python graph2.py or 
python graph1.py (for older version)


---

How It Works

1. Cartesian Plane

The cartesian_plane class:

Draws X/Y axes

Adds scale ticks and labels

Converts mathematical coordinates → screen pixels



---

2. Function Plotting

Each function is sampled over a range

Points are calculated using:

y = func(x)

Points are converted into screen coordinates

Lines are drawn between successive points



---

3. Slider System

The Slider class:

Detects mouse movement

Adjusts x_step and y_step

Dynamically changes graph scale in real-time



---

⚠️ Notes

dx = 0.5 is used to reduce floating-point precision issues.

Some functions may cause errors (e.g., division by zero), these are safely skipped.

Large ranges or small dx may reduce performance.



---

🔧 Future Improvements

Zoom in/out with mouse wheel

Grid background

Better UI slider

Function input from user (text input)

Support for parametric functions

Save graph as image



---

Author:-

Built by Ubaid Khan


---

📜 License

This project is open-source and free to use for learning purposes.
