
r = 255
g =140
b= 0
def setup():
    
   size(1000,1000)
def draw():
    global r,g,b
    fill(r,g,b)
    ellipse(500,500,300,300)

    if r >170 and g >170 and b >170:
        r = 23
        g = 24
        b = 50
      
    r = r + 1
    g = g + 1
    b = b + 1
