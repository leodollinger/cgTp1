from tkinter import *

def draw_line(event):
	global clicks
	global x1, y1
	# se for o primeiro click, pegar primeira coordenada e adicionar 1 aos clicks
	if clicks == 0:
		x1 = event.x
		y1 = event.y
		clicks = 1
	# se for o segundo click, pegar segunda coordenada e zerar clicks
	else:
		x2 = event.x
		y2 = event.y
		clicks = 0
		# chamada da funcao
		bres_gen(x1, y1, x2, y2)

def bres_gen(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	if(dx >= 0):
		incrX = 1
	else:
		incrX = -1
		dx = -dx
	if(dy >= 0):
		incrY = 1
	else:
		incrY = -1
		dy = -dy
	x = x1
	y = y1
	canvas.create_line(round(x, 0), round(y, 0), round(x, 0)+1, round(y, 0))
	if(dy < dx):
		p = 2*dy - dx
		const1 = 2*dy
		const2 = 2*(dy-dx)
		for i in range(dx):
			x = x + incrX
			if(p < 0):
				p = p + const1
			else:
				y = y + incrY
				p = p + const2
			canvas.create_line(round(x, 0), round(y, 0), round(x, 0)+1, round(y, 0))
	else:
		p = 2*dx - dy
		const1 = 2*dx
		const2 = 2*(dx-dy)
		for i in range(dy):
			y = y + incrY
			if(p < 0):
				p = p + const1
			else:
				x = x + incrX
				p = p + const2
			canvas.create_line(round(x, 0), round(y, 0), round(x, 0)+1, round(y, 0))

def delete_lines(event):
	# apaga todas as linhas desenhadas
	canvas.delete('all')

# instanciando a classe de interface
win = Tk()
# set tela
win.title('bresenham')
canvas = Canvas(win, width=1080, height=720, background='white')
canvas.grid(row=0, column=0)
# associar evento ao botao esquerdo do mouse
canvas.bind('<Button-1>', draw_line)
# associar evento ao botao direito do mouse
canvas.bind('<Button-3>', delete_lines)
# count clicks
clicks = 0
# inicia app
win.mainloop()