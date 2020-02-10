n_points = 500
moveSpeed = 0.4
moveScale = 800



def setup():
    global pos
    size(600, 360)
    background(0)
    noStroke()
    colors = [color(0,0,255), color(0,255,0), color(255,0,0)]
    pos = [{'x': random(width), 'y': random(height), 'c':colors[floor(random(len(colors)))]}
           for i in range(n_points)]


def draw():
    background(0)
    for i in range(len(pos)):
        x = pos[i]['x']
        y = pos[i]['y']
        c = pos[i]['c']
        angle = (noise(x / moveScale, y / moveScale) * TWO_PI) * moveScale
        x += cos(angle) * moveSpeed
        y += sin(angle) * moveSpeed
        fill(c)
        circle(x, y, 2)
        if((x > width) or (x < 0) or (y > height) or (y < 0) or (random(1) < 0.001)):
            x = random(width)
            y = random(height)
        pos[i]['x'] = x
        pos[i]['y'] = y
