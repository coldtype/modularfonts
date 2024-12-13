from coldtype import *
from coldtype.raster import *

rc = random_series(seed=2)

@animation((1920, 1080), bg=0, tl=60)
def scratch(f):
    return (StSt("BIG\nSALE\nNOW!!!", "/Users/robstenson/Coldtype/modularfonts/fonts/riptides/fontmakes/NickelMagnetic_Regular_a1.otf", 400, tu=0, leading="8%") #f.e("seio", rng=(-700, 0)), leading="8%")
        .align(f.a.r)
        #.reverse()
        .mapv(lambda i, p: p.f(hsl(rc[i], 0.80, 0.60)))
        .fssw(-1, 1, 3)
        #.ch(phototype(f.a.r, 1.5, 100, 40))
        )
