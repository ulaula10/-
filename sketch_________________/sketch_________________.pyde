x = 10
def setup():
    size(1000,1000)
def draw():
    global x
   # strokeWeight(random(1,200))
    #stroke(random(0,255), random(0,255), random(0,255))
  #  point(random(1000), random(1000))
    background(255,217,0)
    rect(x,x,50,50)
    
    
    x = x + 1
    
