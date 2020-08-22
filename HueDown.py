from phue import Bridge

f = open("HueConf.txt", "r")
lines = f.readlines()

IP = lines[0].replace('\n','').replace('b','')
bri_value = round(int(lines[1])*254/100)

def init():
    b = Bridge(IP)
    b.connect()
    lights = b.lights
    for l in lights:
        if l.on:
            if l.brightness < bri_value:
                l.on = False
            else:
                l.brightness -= bri_value

init()