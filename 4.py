from tkinter import * 
root=Tk() 
root.title('Window') 
root.geometry('500x240')   
defop(): txt.delete(1.0,END) 
a=ent.get() 
f=open('my_file.txt') 
while True: 
	t=f.readline()    
if not t: 
	break 
txt.insert(END, t) 
f.close()   
defsv(): 
	a=ent.get() 
	z=open('my_file.txt','w') 
	b=txt.get(1.0,END) 
	z.write(b) 
	z.close()   
	rootmenu=Menu(root) 
	rootmenu.add_command(label='Открыть',command=op) 
	rootmenu.add_command(label='Сохранить',command=sv)
	root.config(menu=rootmenu)   
	filemenu=Menu(rootmenu,tearoff=0)   
	ent=Entry()   
	txt=Text()     
	ent.pack() 
	txt.pack() 
root.mainloop()
