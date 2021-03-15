from tkinter import *
import math

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
		r = round(math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2)),0)
		clicks = 0
		# chamada da funcao
		circBresenhams(x1, y1, r)

def plotCircPoints(xc, yc, x, y):
	canvas.create_line(xc+x, yc+y, xc+x+1, yc+y, fill='black', width=1)
	canvas.create_line(xc-x, yc+y, xc-x+1, yc+y, fill='black', width=1)
	canvas.create_line(xc+x, yc-y, xc+x+1, yc-y, fill='black', width=1)
	canvas.create_line(xc-x, yc-y, xc-x+1, yc-y, fill='black', width=1)
	canvas.create_line(xc+y, yc+x, xc+y+1, yc+x, fill='black', width=1)
	canvas.create_line(xc-y, yc+x, xc-y+1, yc+x, fill='black', width=1)
	canvas.create_line(xc+y, yc-x, xc+y+1, yc-x, fill='black', width=1)
	canvas.create_line(xc-y, yc-x, xc-y+1, yc-x, fill='black', width=1)


def circBresenhams(xc, yc, r):
	x = 0
	y = r
	p = 3-2*r
	plotCircPoints(xc, yc, x, y)
	while x < y:
		if p < 0:
			p = p+4*x+6
		else:
			p = p+4*(x-y)+10
			y -= 1
		x += 1
		plotCircPoints(xc, yc, x, y)

def delete_lines(event):
	# apaga todas as linhas desenhadas
	canvas.delete('all')

# instanciando a classe de interface
win = Tk()
win.title('bresenham circunferência')

# set tela
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