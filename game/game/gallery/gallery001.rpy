init python:
    g = Gallery()

    g.button("a1")
    g.condition("persistent.a1")
    g.image("gallery/pic/Page1/1.png")

    g.button("a2")
    g.condition("persistent.a2")
    g.image("gallery/pic/Page1/2.png")

    g.button("a3")
    g.condition("persistent.a3")
    g.image("gallery/pic/Page1/3.png")

    g.button("a4")
    g.condition("persistent.a4")
    g.image("gallery/pic/Page1/4.png")

    g.button("a5")
    g.condition("persistent.a5")
    g.image("gallery/pic/Page1/5.png")

    g.button("a6")
    g.condition("persistent.a6")
    g.image("gallery/pic/Page1/6.png")

screen gallery_001():

    tag menu
    imagemap:
        ground "gallery/pic/Button/idle.png"
        idle "gallery/pic/Button/idle.png"
        hover "gallery/pic/Button/hover.png"
        selected_idle "gallery/pic/Button/hover.png"
        selected_hover "gallery/pic/Button/hover.png"

        alpha True

        hotspot (461, 943, 95, 95) action NullAction()
        hotspot (562, 943, 95, 95) action ShowMenu("gallery_001")
        hotspot (663, 943, 95, 95) action ShowMenu("gallery_002")
        hotspot (764, 943, 95, 95) action ShowMenu("gallery_003")
        hotspot (865, 943, 95, 95) action ShowMenu("gallery_004")
        hotspot (967, 943, 95, 95) action ShowMenu("gallery_005")
        hotspot (1068, 943, 95, 95) action ShowMenu("gallery_006")
        hotspot (1169, 943, 95, 95) action ShowMenu("gallery_007")
        hotspot (1270, 943, 95, 95) action ShowMenu("gallery_008")
        hotspot (1371, 943, 95, 95) action ShowMenu("gallery_002")

        hotspot (1597, 16, 292, 126) action Return()

    grid 3 2:
        spacing 120
        yalign 0.50
        xalign 0.50

        add g.make_button("a1","gallery/pic/cover/1_1.png", locked = "gallery/pic/cover/locked.png")
        add g.make_button("a2","gallery/pic/cover/1_2.png", locked = "gallery/pic/cover/locked.png")
        add g.make_button("a3","gallery/pic/cover/1_3.png", locked = "gallery/pic/cover/locked.png")

        add g.make_button("a4","gallery/pic/cover/1_4.png", locked = "gallery/pic/cover/locked.png")
        add g.make_button("a5","gallery/pic/cover/1_5.png", locked = "gallery/pic/cover/locked.png")
        add g.make_button("a6","gallery/pic/cover/1_6.png", locked = "gallery/pic/cover/locked.png")
