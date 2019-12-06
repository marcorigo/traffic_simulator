from tkinter import Tk, Canvas
from threading import Timer
from map import Map
from render import RenderEngine

WIDTH = 500
HEIGHT = 500

tk = Tk()
tk.title('Traffic Simulation')
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="lightgreen")

renderEngine = RenderEngine(canvas, WIDTH, HEIGHT)

road_map    =  [['|', '='],
                ['#', '='],
                ['|', '#']]

map = Map(renderEngine, road_map, 100)
map.createRoads(road_map)
map.addVeichle()

#Timer(0, map.update).start()

def update():
    map.update()
    tk.after(2, update)

update()

#tk.after(2, map.update)

canvas.focus_set()
canvas.pack()


if __name__ == "__main__":
    tk.mainloop()