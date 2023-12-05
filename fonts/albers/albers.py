from coldtype import *
from modularfont import * #INLINE

# https://www.moma.org/collection/works/2724

sq = Rect(200, 200)
fl = Rect(200, 15)

def qc():
    return P().oval(sq.scale(2)).intersection(P(sq).copy())

xs = (P({
        0: P().oval(sq),
        1: P(sq).layer(3).append(fl).stack(0),
        2: P(sq).layer(4).extend([fl, fl]).stack(0),
        3: P(qc().r90(-1), qc()).stack(0),
        4: P(qc().rotate(-90), fl, sq, qc()).stack(0),
        5: P(qc().rotate(-90), fl, fl, sq, sq, qc()).stack(0),
        6: qc(),
        7: P(sq, qc()).stack(0),
        8: P(sq).layer(2).extend([fl, qc()]).stack(0),
        9: P(sq).layer(3).extend([fl, fl, qc()]).stack(0),
    })
    .map(lambda p: p.pen().ro().unframe())
    .f(0)
    .data(vend=True))

@glyphfn(300)
def space(r):
    return P()

glyphs = (P(dict(
    a=P(P(xs[6].r90(1).align(xs[1], "N"), xs[7].scale(1,-1)), xs[8].r90(2)),
    b=P(xs[2], xs[4].flipx()),
    c=P(xs[4], xs[7].align(xs[4],"N")),
    d=P(xs[4], xs[2]),
    e=P(xs[4], xs[7].r90(2).align(xs[4],"N")),
    f=P(xs[9].flipy(), P(xs[6].align(xs[2], "N"), xs[7].align(xs[8], "N"))),
    g=P(xs[4], xs[9].flipx().align(xs[1], "N")),
    h=P(xs[2], xs[8].r90(2)),
    i=P(P(xs[1], xs[0].t(0, xs[1].h+20))),
    j=P(P(xs[9].flipx().align(xs[1], "N"), xs[0].t(0, xs[1].h+20))),
    k=P(xs[2], P(xs[6].flipx().align(xs[1], "N"), xs[7].r90(2))), 
    m=P(xs[1], xs[1], xs[8].r90(2)),
    n=P(xs[1], xs[8].r90(2)),
    o=P(xs[4]).layer(1, lambda p: p.flipx()),
    p=P(xs[2].align(xs[1], "N"), xs[4].flipx()),
    q=P(xs[4], xs[2].align(xs[1], "N")),
    r=P(xs[1], xs[7].align(xs[1], "N")),
    s=P(xs[3].align(xs[1], "N"), xs[6].r90(2)).layer(1, lambda p: p.r90(2)),
    t=P(xs[9].flipy(), xs[6].r90(1).align(xs[1],"N")),
    u=P(xs[8], xs[8].flipx()),
    v=P(xs[8].r90(2), xs[8].flipx()),
    w=P(xs[8], xs[1], xs[8].flipx()),
    x=P(xs[6].align(xs[1], "N"), xs[7].flipy()).layer(1, lambda p: p.flipx()),
    y=P(xs[8], xs[9].flipx().align(xs[1], "N")),
    ))
    .map(lambda p: p.spread(30)))

@renderable((1080, 230))
def shapes(r):
    return (P(
        P(
            xs_display:=xs.copy().spread(5).scale(0.25).align(r.inset(10), "N").f(bw(0, 0.25)),
            P().enumerate(xs_display, lambda x: StSt(str(x.i), Font.JBMono(), 30, wght=1).align(x.el.bounds(), "N")).f(0))))

def show_grid(p):
    return p + P(xs[1]).tag("guide").f(hsl(0.3, a=0.3))

@modularfont(globals(),
    "Albers",
    "Regular",
    default_lsb=20,
    default_rsb=20,
    filter=show_grid,
    bg=1)
def gufo(f):
    return gufo.glyphViewer(f)

@animation((1080, 270), tl=gufo.timeline)
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