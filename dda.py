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
		dda(x1, y1, x2, y2)

def dda(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	# se a variacao de x for maior que a variacao de y, a distancia considerada é a variacao de x
	if abs(dx) > abs(dy):
		step = abs(dx)
	# senao, a distancia considerada é a variacao de y
	else:
		step = abs(dy)
	# incremento de x e y
	x_inc = dx/step
	y_inc = dy/step
	# ponto a se setar
	x = x1
	y = y1
	# set primeiro pixel
	canvas.create_line(round(x, 0), round(y, 0), round(x, 0)+1, round(y, 0))
	# para todos os pontos do passo faca
	for k in range(step-1):
		# incrementar x e y
		x = x + x_inc
		y = y + y_inc
		# set pixel
		canvas.create_line(round(x, 0), round(y, 0), round(x, 0)+1, round(y, 0))

def delete_lines(event):
	# apaga todas as linhas desenhadas
	canvas.delete('all')

# instanciando a classe de interface
win = Tk()
# set tela
win.title('dda')
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