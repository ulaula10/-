x = 10
z = 1
def setup():
    size(1000,1000)
def draw():
    global x,z
    background(255,217,0)
    ellipse(x,x,100,70)
    if x==1000:
        
        x= 0
    ellipse(500,500,  z,z)
    if z>100:
        
        z=0
    
        
        
        
        
        
        
        
        
        
        
        
        
    x = x + 5          
    z = z + 5
    
    
