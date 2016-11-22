import ctypes
from subprocess import Popen
user32 = ctypes.windll.user32
w,h = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
x,y = 320,240
import os

#[p.wait() for p in [Popen("mplayer" + " -geometry {x}%:{y}% video/{f}".format(x=x, y=y, f=f)) for (x, y), f in list(zip([(x * i, y * j) for i in range(0, 1280 // 320) for j in range(0, 1024 // 240)], [os.path.abspath(f) for f in os.listdir('c:\\mplayer\\video\\')]))]]

'''''[p.wait() for p in [Popen("mplayer" + " -geometry {x}%:{y}% video/{f}".format(x=x,y=y,f=f))
                    for (x,y),f in list(zip(
        [(x * i, y * j) for i in range(0, w // x) for j in range(0, h // y)]
        , [os.path.abspath(f) for f in os.listdir('c:\\mplayer\\video\\')]))]]'''''

data = [(x*i,y*j) for i in range(0, w//x) for j in range(0, h//y)]
#vid = [f for f in os.listdir('c:\\mplayer\\video\\')]
vid = [os.path.abspath(f) for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.dll')]
data2 = list(zip(data,vid))
print(vid)
#excodes = [p.wait() for p in [Popen("mplayer" + " -geometry {x}:{y} c:\\mplayer\\video\\{f}".format(x=x,y=y,f=f)) for (x,y),f in data2]]

'''processes = [Popen("mplayer" + " -geometry {x}%:{y}%".format(x=x,y=y) + " video/2016_10_07_07.avi") for x,y in data]
exitcodes = [p.wait() for p in processes]
print([(x*i,y*j) for i in range(0, w1//x) for j in range(0, h1//y)])
print([f for f in os.listdir('c:\\mplayer\\video\\')])
##for x,y in data:
  ##  p = Popen("mplayer" + " -geometry {x}%:{y}%".format(x=x,y=y) + " video/2016_10_07_07.avi")
    ##p.wait()'''


