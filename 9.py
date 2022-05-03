from tkinter import *
root = Tk()
 

c = Canvas(root, width=200, height=200, bg='white')
c.pack()
 

c.create_polygon((100, 20), (20, 100), 
                 (40, 100), (40, 130),
                 (160, 130), (160, 100), (180, 100),
                 fill='lightblue')
c.create_oval(160, 5, 190, 35, 
              fill='orange', outline='white') 

c.create_arc(120, 120, 200, 200, start=200, extent=-70, style=ARC, outline='green', width=3)
c.create_arc(100, 120, 180, 200, start=200, extent=-70, style=ARC, outline='green', width=3)
c.create_arc(80, 120, 160, 200, start=200, extent=-70, style=ARC, outline='green', width=3)
c.create_arc(60, 120, 140, 200, start=200, extent=-70, style=ARC, outline='green', width=3)
c.create_arc(40, 120, 120, 200, start=200, extent=-70, style=ARC, outline='green', width=3)
c.create_arc(20, 120, 100, 200, start=200, extent=-70, style=ARC, outline='green', width=3)
c.create_arc(0, 120, 80, 200, start=200, extent=-70, style=ARC, outline='green', width=3)
c.create_arc(140, 120, 220, 200, start=200, extent=-70, style=ARC, outline='green', width=3)
c.create_arc(160, 120, 240, 200, start=200, extent=-70, style=ARC, outline='green', width=3)

root.mainloop()
