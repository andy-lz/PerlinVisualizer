add_library('sound')

n_points = 1000
point_radius = 6
base_moveSpeed = 0.2
base_moveScale = 1200



def setup():
    global pos
    global overlay
    size(1200,  700, P2D)
    smooth(2)
    pixelDensity(2)
    frameRate(30)
    background("#162a25")
    noStroke()
    colors = [color(floor(random(256)), floor(random(256)),floor(random(256))) 
              for i in range(int(n_points/10))]
    pos = [{'x': random(width), 
            'y': random(height), 
            'c':colors[floor(random(len(colors)))], 
            'r': random(point_radius)}
           for i in range(n_points)]

    mic_in = AudioIn(this, 0)
    mic_in.start()
    global amp_in
    amp_in = Amplitude(this)
    amp_in.input(mic_in)


def draw():
    amp = min(amp_in.analyze()*5,1.)
    for i in range(len(pos)):
        # print(pos[i])
        x = pos[i]['x']
        y = pos[i]['y']
        c = pos[i]['c']
        r = pos[i]['r']
        # print(red(c), green(c), blue(c))
        # c = color(max(red(c) - amp, 0), green(c), min(blue(c) + amp, 255))
        dx = mouseX - x
        dy = mouseY - y
        d = sqrt(dx**2 + dy**2)
        # theta = acos(dx/d)
        moveSpeed = base_moveSpeed * r * (1 + amp*5) + (50 / (d + 1))
        moveScale = base_moveScale # random(200, 400)
        angle = (noise(x / moveScale, y / moveScale) * TWO_PI) * pow(moveScale, 0.25)
        x += cos(angle) * moveSpeed
        y += sin(angle) * moveSpeed
        fill(min(red(c) + 20*moveSpeed, 255), green(c), min(blue(c) + 64 * (1-moveSpeed/3), 255))
        circle(x, y, r)
        # stroke(c)
        # strokeWeight(r)
        # line(pos[i]['x'], pos[i]['y'],  x, y)
        if((x > width) or (x < 0) or (y > height) or (y < 0) or (random(1) < 0.001)):
            x = random(width)
            y = random(height)
        pos[i]['x'] = x
        pos[i]['y'] = y
        # tint(255,0,0, 10)
        # image(overlay,0,0)
        # tint(min(amp,255),0,0)
 
       
def mousePressed():
    setup()
    noiseSeed(int(random(12800000)))
    # background(random(1000))
    # noLoop()
    

def mouseReleased():
    # loop()
    # circle(width/2, height/2, 10)
    pass
