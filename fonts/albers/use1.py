from coldtype import *
from coldtype.blender import *

rsx = random_series(-4, 4, 1)
rsh = random_series(0, 1, 2)

@b3d_runnable(playback=B3DPlayback.KeepPlaying)
def setup2(bpw:BpyWorld):
    (bpw.delete_previous(materials=False)
        .timeline(Timeline(220), resetFrame=0
            , output=setup2.output_folder / "a4_")
        .rigidbody(2.5, 360))

    (BpyObj.Cube("Backdrop")
        .material("backdrop_mat")
        .rigidbody("passive", friction=0, bounce=1)
        .dimensions(12, 12, 1))
    
    frames = [
        BpyObj.Cube("FrameTop").dimensions(12, 1, z:=1.5).locate(0, y=5),
        BpyObj.Cube("FrameBottom").dimensions(12, 1, z).locate(0, y=-5),
        BpyObj.Cube("FrameLeft").dimensions(1, 9, z).locate(x=-5),
        BpyObj.Cube("FrameRight").dimensions(1, 9, z).locate(x=5)
    ]

    for idx, frame in enumerate(frames):
        if idx < 4:
            frame.material("frame_mat").rigidbody("passive")
        else:
            (frame.material("frame_mat").rigidbody("active", True)
                .insert_keyframe(0, "location", [5, 0, 0])
                .insert_keyframe(90, "location", [3, 0, 0])
                .insert_keyframe(100, "location", [5, 0, 0])
                #.make_keyframes_linear("location")
                )
                
    
    # (BpyGroup.Curves(StSt("i", "Albers.*a1", 2).pen().explode()[0]
    #     .layer(4)
    #     .stack(1)
    #     .mapv(lambda i, p: p.t(rsx[i], 0))
    #     #.î(0, lambda p: p.t(0, 2))
    #     .centerZero()
    #     , collection="/Glyphs2")
    #     .map(lambda idx, bp: bp
    #         .extrude(0.01)
    #         .locate(z=20+idx*5)
    #         .convertToMesh()
    #         .rigidbody("active", bounce=0.5, friction=0)
    #         .material("circle_material")))

    (BpyObj.UVSphere("Ball")
        .rigidbody("active", animated=False, friction=0, bounce=0.75)
        .scale(s:=0.25, s, s)
        .locate(x=-0.24, y=0.5, z=25)
        .shade_smooth()
        .material("ball_mat"))
    
    (BpyGroup.Curves(StSt("abcdefg\nhijkmnop\nqrstuvx", "Albers.*a1", 2, leading=0.5)
        .mapv(lambda p: p.explode())
        .collapse()
        .centerZero()
        , collection="/Glyphs")
        .map(lambda idx, bp: bp
            #.parent("Empty1")
            .extrude(0.01+0.05)
            .locate(z=0.51+0.05)
            .bevel(0.01)
            .convertToMesh()
            .rigidbody("active", bounce=0.5, friction=0)
            #.material("glyph_material")
            .material(f"glyph_mat_{idx}", lambda m: m
                #.f(hsl(rsh[idx], 0.5, 0.3))
                .f(bw(0.9))
                .specular(0)
                .roughness(1)
            )))