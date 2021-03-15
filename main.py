from tkinter import *
import os
import math

clicks = 0
coordenates = []

INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8	
# ------------ INI ASSOCIACAO DE BOTAO A FUNCAO ------------ #
def setBresenhamCircle():
	# associar evento ao botao esquerdo do mouse
	canvas.bind('<Button-1>', draw_lineBC)
	# count clicks
	clicks = 0

def setBresenham():
	# associar evento ao botao esquerdo do mouse
	canvas.bind('<Button-1>', draw_lineB)
	# count clicks
	clicks = 0

def setDda():
	# associar evento ao botao esquerdo do mouse
	canvas.bind('<Button-1>', draw_lineD)
	# count clicks
	clicks = 0

def setTrans():
	# associar evento ao botao esquerdo do mouse
	canvas.bind('<Button-1>', translaConfig)
	# count clicks
	clicks = 0

def setEsc():
	# associar evento ao botao esquerdo do mouse
	canvas.bind('<Button-1>', escConfig)
	# count clicks
	clicks = 0

def setRotation():
	canvas.bind('<Button-1>', rotationYConfig)
	canvas.bind('<Button-3>', rotationXConfig)
	clicks = 0

def setMirror():
	canvas.bind('<Button-1>', mirrorXConfig)
	canvas.bind('<Button-2>', mirrorXYConfig)
	canvas.bind('<Button-3>', mirrorYConfig)
	clicks = 0

def showCoord():
	canvas.bind('<Button-1>', showCoordenate)
	clicks = 0

def setCohenSutherland():
	# associar evento ao botao esquerdo do mouse
	canvas.bind('<Button-1>', clip1)
	# count clicks
	clicks = 0

def setLiangBarsky():
	# associar evento ao botao esquerdo do mouse
	canvas.bind('<Button-1>', clip2)
	# count clicks
	clicks = 0

# ------------ FIM ASSOCIACAO DE BOTAO A FUNCAO ------------ #
# ------------ INICIO DA INICIALIZACAO E CHAMADA DE FUNCOES ------------ #
def showCoordenate(event):
	print('X: ' + str(event.x))
	print('Y: ' + str(event.y))

def translaConfig(event):
	x = event.x
	y = event.y
	transla(x, y)

def escConfig(event):
	x = event.x
	y = event.y
	escala(x, y)

def rotationYConfig(event):
	rotation('y')

def rotationXConfig(event):
	rotation('x')

def mirrorYConfig(event):
	mirror('y')

def mirrorXYConfig(event):
	mirror('xy')

def mirrorXConfig(event):
	mirror('x')

def draw_lineB(event):
	global clicks
	global coordenates
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
		coordenates.insert(len(coordenates),[x1, y1, x2, y2, 0])
		clicks = 0
		# chamada da funcao
		bres_gen(x1, y1, x2, y2)

def draw_lineBC(event):
	global clicks
	global coordenates
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
		coordenates.insert(len(coordenates),[x1, y1, x2, y2, 1])
		r = round(math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2)),0)
		clicks = 0
		# chamada da funcao
		circBresenhams(x1, y1, r)

def draw_lineD(event):
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
		coordenates.insert(len(coordenates),[x1, y1, x2, y2, 2])
		clicks = 0
		# chamada da funcao
		dda(x1, y1, x2, y2)

def clip1(event):
	global clicks
	global coordenates
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
		xtemp = 0
		ytemp = 0
		if(x1 < x2):
			xtemp = x1
			x1 = x2
			x2 = xtemp
		if(y1 < y2):
			ytemp = y1
			y1 = y2
			y2 = ytemp
		canvas.delete('all')
		for key in range(len(coordenates)):
			coordenate = coordenates[key]
			if(coordenate[4] != 1):
				cohenSutherland(coordenate, x1, y1, x2, y2)

def clip2(event):
	global clicks
	global coordenates
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
		xtemp = 0
		ytemp = 0
		if(x1 < x2):
			xtemp = x1
			x1 = x2
			x2 = xtemp
		if(y1 < y2):
			ytemp = y1
			y1 = y2
			y2 = ytemp
		canvas.delete('all')
		for key in range(len(coordenates)):
			coordenate = coordenates[key]
			if(coordenate[4] != 1):
				liangBarsky(coordenate, x1, y1, x2, y2)

# ------------ FIM DA INICIALIZACAO E CHAMADA DE FUNCOES ------------ #

# ------------ INICIO FUNCOES DO TRABALHO ------------ #

	"""[plotCircPoints]
	
	[coloca os pixeis da circuferencia]
	
	Arguments:
		xc {[int]} -- [x da origem]
		yc {[int]} -- [y da origem]
		x {[int]} -- [x de um ponto da borda]
		y {[int]} -- [y de um ponto da borda]
	"""
def plotCircPoints(xc, yc, x, y):
	canvas.create_line(xc+x, yc+y, xc+x+1, yc+y, fill='black', width=1)
	canvas.create_line(xc-x, yc+y, xc-x+1, yc+y, fill='black', width=1)
	canvas.create_line(xc+x, yc-y, xc+x+1, yc-y, fill='black', width=1)
	canvas.create_line(xc-x, yc-y, xc-x+1, yc-y, fill='black', width=1)
	canvas.create_line(xc+y, yc+x, xc+y+1, yc+x, fill='black', width=1)
	canvas.create_line(xc-y, yc+x, xc-y+1, yc+x, fill='black', width=1)
	canvas.create_line(xc+y, yc-x, xc+y+1, yc-x, fill='black', width=1)
	canvas.create_line(xc-y, yc-x, xc-y+1, yc-x, fill='black', width=1)

	"""[circBresenhams]
	
	[Gera uma circuferencia]
	
	Arguments:
		xc {[int]} -- [X da origem]
		yc {[int]} -- [Y da origem]
		r {[float]} -- [Raio da circuferencia]
	"""
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

	"""[bres_gen]
	
	[Usa do algoritimo de bresenhams para plotar uma reta]
	
	Arguments:
		x1 {[int]} -- [X Inicial]
		y1 {[int]} -- [Y Inicial]
		x2 {[int]} -- [X Final]
		y2 {[int]} -- [Y Final]
	"""
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

	"""[dda]
	
	[Usa do algoritimo DDA para plotar uma reta]
	
	Arguments:
		x1 {[int]} -- [X Inicial]
		y1 {[int]} -- [Y Inicial]
		x2 {[int]} -- [X Final]
		y2 {[int]} -- [Y Final]
	"""
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

	"""[transla]
	
	[Faz a translacao das figuras na tela para o ponto desejado]
	
	Arguments:
		x {[int]} -- [X do ponto clicado para tranlacao]
		y {[int]} -- [Y do ponto clicado para tranlacao]
	"""
def transla(x, y):
	global coordenates
	canvas.delete('all')
	for key in range(len(coordenates)):
		coordenate = coordenates[key]
		xo = x
		yo = y
		xd = coordenate[2] - coordenate[0]
		yd = coordenate[3] - coordenate[1]
		if(coordenate[4] == 0):
			bres_gen(xo, yo, xo + xd, yo + yd)
			coordenates[key][0] = xo
			coordenates[key][1] = yo
			coordenates[key][2] = xo + xd
			coordenates[key][3] = yo + yd
		elif(coordenate[4] == 1):
			r = round(math.sqrt(math.pow((xo + xd - xo), 2) + math.pow((yo + yd - yo), 2)),0)
			circBresenhams(xo, yo, r)
			coordenates[key][0] = xo
			coordenates[key][1] = yo
			coordenates[key][2] = xo + xd
			coordenates[key][3] = yo + yd
		elif(coordenate[4] == 2):
			dda(xo, yo, xo + xd, yo + yd)
			coordenates[key][0] = xo
			coordenates[key][1] = yo
			coordenates[key][2] = xo + xd
			coordenates[key][3] = yo + yd

"""[transla2]
	
	[Faz a translacao das figuras na tela para o ponto desejado]
	
	Arguments:
		x {[int]} -- [X do ponto clicado para tranlacao]
		y {[int]} -- [Y do ponto clicado para tranlacao]
	"""
def transla2(x, y):
	global coordenates
	tempCoo1 = [x, y]
	tempCoo2 = [x, y]
	canvas.delete('all')
	for key in range(len(coordenates)):
		coordenate = coordenates[key]
		if(tempCoo1[0] < coordenate[0]):
			tempCoo1[0] = 0 - tempCoo1[0]
		if(tempCoo1[1] < coordenate[1]):
			tempCoo1[1] = 0 - tempCoo1[1]
		if(tempCoo2[0] < coordenate[2]):
			tempCoo2[0] = 0 - tempCoo2[0]
		if(tempCoo2[1] < coordenate[3]):
			tempCoo2[1] = 0 - tempCoo2[1]
		if(coordenate[4] == 0):
			bres_gen(coordenate[0] + tempCoo1[0], coordenate[1] + tempCoo1[1], coordenate[2] + tempCoo2[0], coordenate[3] + tempCoo2[1])
			coordenates[key][0] += tempCoo1[0]
			coordenates[key][1] += tempCoo1[1]
			coordenates[key][2] += tempCoo2[0]
			coordenates[key][3] += tempCoo2[1]
		elif(coordenate[4] == 1):
			r = round(math.sqrt(math.pow((coordenate[2] + tempCoo2[0] - coordenate[0] + tempCoo1[0]), 2) + math.pow((coordenate[3] + tempCoo2[1] - coordenate[1] + tempCoo1[1]), 2)),0)
			circBresenhams(coordenate[0] + tempCoo1[0], coordenate[1] + tempCoo1[1], r)
			coordenates[key][0] += tempCoo1[0]
			coordenates[key][1] += tempCoo1[1]
			coordenates[key][2] += tempCoo2[0]
			coordenates[key][3] += tempCoo2[1]
		elif(coordenate[4] == 2):
			dda(coordenate[0] + tempCoo1[0], coordenate[1] + tempCoo1[1], coordenate[2] + tempCoo2[0], coordenate[3] + tempCoo2[1])
			coordenates[key][0] += tempCoo1[0]
			coordenates[key][1] += tempCoo1[1]
			coordenates[key][2] += tempCoo2[0]
			coordenates[key][3] += tempCoo2[1]


	"""[escala]
	
	[Escalona a imagem mantendo o ponto de origem fixo]
	
	Arguments:
		x {[int]} -- [X do ponto clicado para escalonamento]
		y {[int]} -- [Y do ponto clicado para escalonamento]
	"""
def escala(x,y):
	global coordenates
	canvas.delete('all')
	for key in range(len(coordenates)):
		coordenate = coordenates[key]
		if(x == 0):
			x = 1
		if(y == 0):
			y = 1
		divX = x / coordenate[2]
		divY = y / coordenate[3]
		if(coordenate[4] == 0):
			bres_gen(coordenate[0], coordenate[1], int(round(coordenate[2]*divX,0)), int(round(coordenate[3]*divY,0)))
			coordenates[key][2] = int(round(coordenate[2]*divX,0))
			coordenates[key][3] = int(round(coordenate[3]*divY,0))
		elif(coordenate[4] == 1):
			r = round(math.sqrt(math.pow((int(round(coordenate[2]*divX,0)) - coordenate[0]), 2) + math.pow((int(round(coordenate[3]*divY,0)) - coordenate[1]), 2)),0)
			circBresenhams(coordenate[0], coordenate[1], r)
			coordenates[key][2] = int(round(coordenate[2]*divX,0))
			coordenates[key][3] = int(round(coordenate[3]*divY,0))
		elif(coordenate[4] == 2):
			dda(coordenate[0], coordenate[1], int(round(coordenate[2]*divX,0)), int(round(coordenate[3]*divY,0)))
			coordenates[key][2] = int(round(coordenate[2]*divX,0))
			coordenates[key][3] = int(round(coordenate[3]*divY,0))

	"""[rotation]
	
	[rotaciona as figuras a partir do seu centro em relacao a x, y ou x e y]
	
	Arguments:
		typeR {[string]} -- [tipo de rotacao desejada (x, y ou xy)]
	"""
def rotation(typeR):
	global coordenates
	canvas.delete('all')
	for key in range(len(coordenates)):
		coordenate = coordenates[key]
		if(typeR == 'x'):
			x1 = coordenate[0]
			y1 = coordenate[3]
			x2 = coordenate[2]
			y2 = coordenate[1]
		if(typeR == 'y'):
			x1 = coordenate[2]
			y1 = coordenate[1]
			x2 = coordenate[0]
			y2 = coordenate[3]
		if(coordenate[4] == 0):
			bres_gen(x1, y1, x2, y2)
			coordenates[key][0] = x1
			coordenates[key][1] = y1
			coordenates[key][2] = x2
			coordenates[key][3] = y2
		elif(coordenate[4] == 1):
			r = round(math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2)),0)
			circBresenhams(x1, y1, r)
			coordenates[key][0] = x1
			coordenates[key][1] = y1
			coordenates[key][2] = x2
			coordenates[key][3] = y2
		elif(coordenate[4] == 2):
			dda(x1, y1, x2, y2)
			coordenates[key][0] = x1
			coordenates[key][1] = y1
			coordenates[key][2] = x2
			coordenates[key][3] = y2

	"""[mirror]
	
	[Faz o espelhamento das figuras a partir da sua origem em relacao a x, y ou x e y]
	
	Arguments:
		typeR {[string]} -- [tipo de rotacao desejada (x, y ou xy)]
	"""
def mirror(typeR):

	global coordenates
	canvas.delete('all')
	for key in range(len(coordenates)):
		coordenate = coordenates[key]
		if(typeR == 'x'):
			x1 = coordenate[0]	
			y1 = coordenate[1]
			x2 = x1 + (coordenate[0] - coordenate[2])
			y2 = coordenate[3]
		elif(typeR == 'y'):
			x1 = coordenate[0]
			y1 = coordenate[1]	
			x2 = coordenate[2]
			y2 = y1 + (coordenate[1] - coordenate[3])
		elif(typeR == 'xy'):
			x1 = coordenate[0]
			y1 = coordenate[1]	
			x2 = x1 + (coordenate[0] - coordenate[2])
			y2 = y1 + (coordenate[1] - coordenate[3])
		if(coordenate[4] == 0):
			bres_gen(x1, y1, x2, y2)
			coordenates[key][0] = x1
			coordenates[key][1] = y1
			coordenates[key][2] = x2
			coordenates[key][3] = y2
		elif(coordenate[4] == 1):
			r = round(math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2)),0)
			circBresenhams(x1, y1, r)
			coordenates[key][0] = x1
			coordenates[key][1] = y1
			coordenates[key][2] = x2
			coordenates[key][3] = y2
		elif(coordenate[4] == 2):
			dda(x1, y1, x2, y2)
			coordenates[key][0] = x1
			coordenates[key][1] = y1
			coordenates[key][2] = x2
			coordenates[key][3] = y2

	"""[region_code]
	
	[Determina se a o ponto esta dentro da janela]
	
	Arguments:
		x {[int]} -- [x do ponto a se testar]
		y {[int]} -- [y do ponto a se testar]
		xmax {[int]} -- [Maior x da janela]
		ymax {[int]} -- [Maior y da janela]
		xmin {[int]} -- [Menor x da janela]
		ymin {[int]} -- [Menor y da janela]
	
	Returns:
		[int] -- [Onde o ponto se encontra]
	"""
def region_code(x, y, xmax, ymax, xmin, ymin):
	code = INSIDE 
	if x < xmin:
		code |= LEFT 
	elif x > xmax:
		code |= RIGHT 
	if y < ymin:
		code |= BOTTOM 
	elif y > ymax:
		code |= TOP 
	return code

	"""[cohenSutherland]
	
	[Realiza o corte da figura usando o algoritimo de cohen Sutherland]
	
	Arguments:
		coordenate {[Array de int]} -- [Coordenadas com ponto inicial e final da reta]
		xmax {[int]} -- [Maior x da janela]
		ymax {[int]} -- [Maior y da janela]
		xmin {[int]} -- [Menor x da janela]
		ymin {[int]} -- [Menor y da janela]
	"""
def cohenSutherland(coordenate, xmax, ymax, xmin, ymin):
	x1 = coordenate[0]
	y1 = coordenate[1]
	x2 = coordenate[2]
	y2 = coordenate[3]
	c1 = region_code(x1, y1, xmax, ymax, xmin, ymin)
	c2 = region_code(x2, y2, xmax, ymax, xmin, ymin)
	aceita = False
	while True: 
		if c1 == 0 and c2 == 0: 
			aceita = True
			break
		elif (c1 & c2) != 0: 
			break
		else: 
			x = 1.0
			y = 1.0
			if c1 != 0: 
				cfora = c1 
			else: 
				cfora = c2 
			if cfora & TOP: 
				x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1) 
				y = ymax 
			elif cfora & BOTTOM: 
				x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1) 
				y = ymin 
			elif cfora & RIGHT: 
				y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1) 
				x = xmax 
			elif cfora & LEFT: 
				y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1) 
				x = xmin 
			if cfora == c1: 
				x1 = x 
				y1 = y 
				c1 = region_code(x1, y1, xmax, ymax, xmin, ymin)
			else: 
				x2 = x 
				y2 = y 
				c2 = region_code(x2, y2, xmax, ymax, xmin, ymin)
	if aceita:
		if(coordenate[4] == 0):
			bres_gen(round(x1), round(y1), round(x2), round(y2))
		elif(coordenate[4] == 2):
			dda(round(x1), round(y1), round(x2), round(y2))

def clipTest(p, q, u1, u2):
	result=True
	if(p < 0.0):
		r=q/p
		if(r>u2):
			result = False
		elif(r>u1):
			u1=r
	elif(p>0.0):
		r=q/p
		if(r<u1):
			result = False
		elif(r<u2):
			u2=r
	elif(q<0.0):
		result = False
	return [result, u1, u2]

def liangBarsky(coordenate, xmax, ymax, xmin, ymin):
	"""[liangBarsky]
	
	[Realiza o corte da figura usando o algoritimo de liang-Barsky]
	
	Arguments:
		coordenate {[Array de int]} -- [Coordenadas com ponto inicial e final da reta]
		xmax {[int]} -- [Maior x da janela]
		ymax {[int]} -- [Maior y da janela]
		xmin {[int]} -- [Menor x da janela]
		ymin {[int]} -- [Menor y da janela]
	"""
	x1 = coordenate[0]
	y1 = coordenate[1]
	x2 = coordenate[2]
	y2 = coordenate[3]
	u1=0.0
	u2=1.0
	dx = x2-x1
	dy = y2-y1
	result = clipTest(0-dx, x1-xmin, u1, u2)
	if(result[0]):
		u1 = result[1]
		u2 = result[2]
		result = clipTest(dx, xmax-x1, u1, u2)
		if(result[0]):
			u1 = result[1]
			u2 = result[2]
			result = clipTest(0-dy, y1-ymin, u1, u2)
			if(result[0]):
				u1 = result[1]
				u2 = result[2]
				result = clipTest(dy, ymax-y1, u1, u2)
				if(result[0]):
					u1 = result[1]
					u2 = result[2]
					if(u2 < 1.0):
						x2=x1+u2*dx
						y2=y1+u2*dy
					if(u1 > 0.0):
						x1=x1+u1*dx
						y1=y1+u1*dy

					if(coordenate[4] == 0):
						bres_gen(round(x1), round(y1), round(x2), round(y2))
					elif(coordenate[4] == 2):
						dda(round(x1), round(y1), round(x2), round(y2))


	"""[delete_lines]
	
	[Limpa a tela e reinicia o array de coordenadas]
	"""
def delete_lines():
	global coordenates
	coordenates = []
	# apaga todas as linhas desenhadas
	canvas.delete('all')

# ------------ FIM FUNCOES DO TRABALHO ------------ #
# ------------ INICIALIZACAO DO CANVAS ------------ #

win = Tk()
win.title('Computação Gráfica')
canvas = Canvas(win, width=1280, height=720, background='white')
canvas.grid(row=0, column=0)

menu = Menu(win)
mainMenu = Menu(menu, tearoff=0)
mainMenu.add_command(label='Bresenham', command=setBresenham)
mainMenu.add_command(label='Bresenham Circunferência', command=setBresenhamCircle)
mainMenu.add_command(label='Dda', command=setDda)
mainMenu.add_separator()
mainMenu.add_command(label='Translação', command=setTrans)
mainMenu.add_command(label='Escala', command=setEsc)
mainMenu.add_command(label='Rotação', command=setRotation)
mainMenu.add_command(label='Espelhamento', command=setMirror)
# mainMenu.add_command(label='coordenada do click', command=showCoord)
mainMenu.add_separator()
mainMenu.add_command(label='Cohen Sutherland', command=setCohenSutherland)
mainMenu.add_command(label='Liang-Barsky', command=setLiangBarsky)
mainMenu.add_separator()
mainMenu.add_command(label='Limpar Tela', command=delete_lines)
mainMenu.add_separator()
mainMenu.add_command(label='Fechar', command=win.quit)
menu.add_cascade(label='options', menu=mainMenu)

win.config(menu=menu)
win.mainloop()
# ------------ FIM DO PROGRAMA ------------ #