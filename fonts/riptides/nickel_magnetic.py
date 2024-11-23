from coldtype import *
from coldtype.raster import *
from coldtype.warping import warp

from coldtype import *
from modularfont import * #INLINE


def mag(l, rejects=[]):
    r = Rect(1920, 1080)

    letter = (StSt(l, "NickelGothicV3Variable", 1300, wdth=1, wght=1)
        .f(1)
        .align(r)
        .scale(0.75, 1)
        .ro())
    
    letter_reversed = letter.copy().xor(P(r)).f(0)
    
    warped = (letter.copy()
        .ch(warp(1, xs=500, ys=500, mult=30, base=ord(l)))
        .fssw(1, 0, 70, 0)
        .ch(phototype(r, 25, 140, 23))
        .ch(potrace(r)).f(1)
        .fssw(1, 0, 70)
        .ch(phototype(r, 15, 120, 20))
        .ch(potrace(r)).f(1)
        )
    
    #return warped
    
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
            .layer(2)
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
            .ch(shake(1, 6, ord(l)))
            .ch(phototype(r.inset(0, -200), 3, 48, 9, fill=1))
            .ch(potrace(r.inset(0, -200), turdsize=50)).f(1)
        )
        .scale(0.75)[0]
        .removeOverlap()
        #.filterContours(lambda i, c: i not in rejects)
        )

spr = 20
sps = 20

@glyphfn(200)
def space(): return P()

@glyphfn("auto", spr, sps, cover_lower=1)
def A():
    return mag("A", [14, 16, 9])

@glyphfn("auto", spr, sps, cover_lower=1)
def B(): return mag("B", [12, 13, 14, 15, 16, 22, 23, 24, 25])

@glyphfn("auto", spr, sps, cover_lower=1)
def C(): return mag("C", [])

@glyphfn("auto", spr, sps, cover_lower=1)
def D(): return mag("D", [])

@modularfont(globals(),
    "Nickel Magnetic",
    "Regular",
    preview_size=(1920, None),
    default_lsb=sps,
    default_rsb=sps,
    #filter=show_grid,
    bg=1)
def gufo(f):
    return gufo.glyphViewer(f)

#@animation((1080, 270), tl=gufo.timeline)
def spacecenter(f):
    #return gufo.spacecenter(f.a.r, "auto", idx=f.i)

    try:
        glyphs = P([gf.glyph_with_frame(gufo) for gf in gufo.glyph_fns])
        return (glyphs.spread(10)
            .scale(0.2, pt=(0,0))
            .f(0)
            .centerPoint(f.a.r, (f.i, "C")))
    except:
        return None

#@renderable((1080, 290))
def smoke(r):
    try:
        return StSt("SMOKE\nPROOF", gufo.fontmake_font(), 120, ss01=1).align(r, ty=1).f(0)
    except FontNotFoundException:
        print("FONT NOT FOUND")
        return None

def release(_):
    [gufo.buildGlyph(gf) for gf in gufo.glyph_fns]

    from textwrap import indent

    ss01 = []
    for gf in gufo.glyph_fns:
        if "_ss01" in gf.glyph_name:
            plain = gf.glyph_name.split("_")[0]
            ss01.append(f"sub {plain} by {gf.glyph_name};")
    
    ss01 = indent("\n".join(ss01), "    ")

    features = f"""languagesystem DFLT dflt;
languagesystem latn dflt;

feature ss01 {{
{ss01}
}} ss01;"""

    gufo.fontmake(version="a1", features=features)