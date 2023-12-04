from coldtype import *

# https://www.moma.org/collection/works/2724

sq = P(Rect(100, 100))

def qc():
    return P().oval(sq.bounds().scale(2)).intersection(sq.copy())

xs = (sq
    .layer(
        lambda p: P().oval(p.bounds()),
        lambda p: p.layer(3).stack(0),
        lambda p: p.layer(4).stack(0),
        lambda _: P(qc().rotate(-90), qc()).stack(0),
        lambda p: P(qc().rotate(-90), p, qc()).stack(0),
        lambda p: P(qc().rotate(-90), p, p.copy(), qc()).stack(0),
        lambda _: qc(),
        lambda p: P(p, qc()).stack(0),
        lambda p: p.layer(2).append(qc()).stack(0),
        lambda p: p.layer(3).append(qc()).stack(0))
    .map(lambda p: p.pen().ro().unframe())
    .f(0)
    .data(vend=True))

glyphs = dict(
    a=P(P(xs[6].r90(1), xs[7].scale(1,-1)).stack(0), xs[8].r90(2)),
    b=P(xs[2], xs[4].flipx()),
    c=P(xs[4], xs[7].align(xs[4],"N")),
    d=P(xs[4], xs[2]),
    e=P(xs[4], xs[7].r90(2).align(xs[4],"N")),
    f=P(xs[9].flipy(), P(xs[6], xs[7]).stack(10).align(xs[9],"N")),
    g=P(xs[4], xs[9].flipx().t(0,-xs[0].h)),
    h=P(xs[2], xs[8].r90(2)),
    i=P(P(xs[0], xs[1]).stack(5)),
    j=P(P(xs[0], xs[9].flipx()).stack(5)).t(0,-xs[0].h),
    k=P(xs[2], P(xs[6].flipx(), xs[7].r90(2)).stack(0)), 
    m=P(xs[1], xs[1], xs[8].r90(2)),
    n=P(xs[1], xs[8].r90(2)),
    o=P(xs[4]).layer(1, lambda p: p.flipx()),
    p=P(xs[2].t(0,-xs[0].h), xs[4].flipx()),
    q=P(xs[4], xs[2].t(0,-xs[0].h)),
    r=P(xs[1], xs[7].align(xs[1],"N")),
    s=P(xs[3], xs[6].r90(2)).stack(0).layer(1, lambda p: p.r90(2)),
    t=P(xs[9].flipy(), xs[6].r90(1).align(xs[1],"N")),
    u=P(xs[8], xs[8].flipx()),
    v=P(xs[8].r90(2), xs[8].flipx()),
    w=P(xs[8], xs[1], xs[8].flipx()),
    x=P(xs[6], xs[7].flipy()).stack(0).layer(1, lambda p: p.flipx()),
    y=P(xs[8], xs[9].flipx().t(0,-xs[0].h)),
)

@renderable()
def shapes(r):
    return (P(
        P(
            xs_display:=xs.copy().spread(5).align(r, "N").f(bw(0, 0.25)),
            P().enumerate(xs_display, lambda x: StSt(str(x.i), Font.JBMono(), 50, wght=1).align(x.el.bounds(), "S")).f(0)),
        P().enumerate(glyphs, lambda x: x.el)
            .map(lambda p: p.spread(20))
            .fssw(-1,0,1)
            .spread(60)
            .scale(0.25, pt=(0,0))
            .t(-520, 100)))
