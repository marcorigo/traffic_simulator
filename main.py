from tkinter import Tk, Canvas
from threading import Timer
from map import Map

WIDTH = 500
HEIGHT = 500

tk = Tk()
tk.title('Traffic Simulation')
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="lightgreen")

road_map =   [['0', '0'],
        ['0', '0']]

map = Map(canvas, road_map)
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