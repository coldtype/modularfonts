from coldtype import *
from coldtype.raster import *
from coldtype.warping import warp

letters = "ALENRIMSBCDEFGHIJKLMNOPQRSTUVWXYZ"

@animation((1920, 1080), tl=len(letters), bg=0.3)
def riptide(f):
    letter = (StSt(letters[f.i], "NickelGothicV3Variable", 1300, wdth=1, wght=1)
        .f(1)
        .align(f.a.r)
        .scale(0.75, 1)
        .ro())
    
    #return letter
    
    letter_reversed = letter.copy().xor(P(f.a.r)).f(0)
    
    warped = (letter.copy()
        .ch(warp(1, xs=500, ys=500, mult=30, base=f.i))
        .fssw(1, 0, 70, 0)
        .ch(phototype(f.a.r, 25, 140, 23))
        .ch(potrace(f.a.r)).f(1)
        .fssw(1, 0, 70)
        .ch(phototype(f.a.r, 15, 120, 20))
        .ch(potrace(f.a.r)).f(1)
        )
    
    #return letter.f(0.2) + warped
    
    return (P(
        #letter.copy().f(0),
        #warped.copy().f(hsl(0.18, 0.7, 0.65)).f(0),
        # warped.explode()[1]
        #     .layer(7)
        #     .map(lambda i, p: p
        #         .outline(20+i*20, drawInner=0)
        #         .ro()
        #         .fssw(-1, 1, 2)),
        warped#.explode()
            .layer(4)
            .map(lambda i, p: p
                #.outline(20+i*20, drawInner=0)
                #.ro()
                .layer(
                    lambda a: a.fssw(-1, 1, 0+i*50),
                    lambda a: a.fssw(-1, 0, (0+i*50)-6),
                    lambda a: a.f(0),
                    #lambda a: letter.copy().f(0),
                    #lambda a: letter_reversed.copy(),
                )
                #.ch(phototype(f.a.r, 5, 43, 5, fill=1))
                #.ch(potrace(f.a.r, turdsize=2500)).f(1)
                #.intersection(letter.copy())
                #.difference(warped.copy())
                #.ch(phototype(f.a.r, 5, 83, 5))
                #.ch(potrace(f.a.r, opticurve=0))
                #.f(1)
                )
            .reverse()
            .append(warped.copy().fssw(-1, 1, 3))
            .ch(shake(1, 6, f.i))
            .ch(phototype(f.a.r.inset(0, -200), 3, 48, 9, fill=1))
            .ch(potrace(f.a.r.inset(0, -200), turdsize=50)).f(1)
    )).scale(0.75).align(f.a.r)